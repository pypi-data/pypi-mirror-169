"""Overlap (Finnish: limitys) assesses sentences from constrained and overlapping vocabularies."""
import argparse
import datetime as dti
import json
import logging
import pathlib
import sys
from typing import Dict, Tuple, Union

import yaml
from gensim import downloader as model_api
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex

from limitys import ENCODING, log, stop

PathLike = Union[str, pathlib.Path]
Documents = Dict[str, Dict[str, str]]
Verification = Tuple[bool, str]

MODELS = {
    'news': 'word2vec-google-news-300',
    'wiki': 'fasttext-wiki-news-subwords-300',
}
DEFAULT_MODEL = MODELS['news']
DEFAULT_DOCUMENTS_NAME = 'documents.yml'


def load_documents(path: PathLike = DEFAULT_DOCUMENTS_NAME) -> Documents:
    """Load the keyed documents from the file per convention and format (from suffix)."""
    source = pathlib.Path(path)
    log.debug(f'- documents suffix is {source.suffix}')

    if source.suffix.lower() in ('.yaml', '.yml'):
        log.debug('- reading documents as yaml')
        with open(source, 'rt', encoding=ENCODING) as handle:
            return yaml.safe_load(handle)  # type: ignore

    if source.suffix.lower() in ('.json',):
        log.debug('- reading documents as json')
        with open(source, 'rt', encoding=ENCODING) as handle:
            return json.load(handle)  # type: ignore

    return {}


def similarity(options: argparse.Namespace) -> int:
    """Drive the verification."""
    documents = pathlib.Path(options.documents)
    language = options.language
    language_code = stop.language_code_of(language)
    quiet = options.quiet
    if quiet:
        logging.getLogger().setLevel(logging.ERROR)

    start_time = dti.datetime.now(tz=dti.timezone.utc)
    log.info(f'starting similarity analysis of {language} (code {language_code}) documents in ({documents})')
    log.info(f'output channel is {"STDOUT" if options.out_path is sys.stdout else options.out_path}')
    docs = load_documents(documents)
    log.info(f'- loaded {len(docs)} documents from ({documents})')

    if not docs:
        log.error('no documents to analyze')
        return 1

    sentences = {k: stop.cleanse(docs[k], stop.EN) for k in docs}

    dictionary = Dictionary(list(sentences.values()))
    bags_of_words = {k: dictionary.doc2bow(sentences[k]) for k in sentences}

    tfidf = TfidfModel(list(bags_of_words.values()))
    tfidfs = {k: tfidf[bags_of_words[k]] for k in bags_of_words}

    model = model_api.load(MODELS['wiki'])

    termsim_index = WordEmbeddingSimilarityIndex(model)
    termsim_matrix = SparseTermSimilarityMatrix(termsim_index, dictionary, tfidf)

    pbm, row_heads = [], []
    col_heads = [key for key in tfidfs]
    for row, (i, bag) in enumerate(tfidfs.items()):
        pbm.append([])
        row_heads.append(i)
        for col, (j, bah) in enumerate(tfidfs.items()):
            similarity = termsim_matrix.inner_product(bag, bah, normalized=(True, True))
            pbm[row].append(similarity if col > row else None)
            log.debug(f'{i=}, {j=}')
            log.debug(docs[i])
            log.debug(docs[j])
            log.debug('similarity = %.4f' % similarity)
            log.debug('# ' + '- ' * 42)

    matrix_rep = ['# Matrix:', '']
    matrix_rep.append(f'{" ".join(cell.rjust(12) for cell in col_heads[1:])}{" "*12}')
    matrix_rep.append(f'{" ".join(("-"*11).rjust(12) for _ in row_heads[1:])}{" "*12}')
    for rank, row in enumerate(pbm[:-1]):
        upp_tri_mat_row = ' '.join(str('' if cell is None else round(cell, 3)).rjust(12) for cell in row[1:])
        matrix_rep.append(f'{upp_tri_mat_row} | {row_heads[rank] :12s}')
    if options.out_path is sys.stdout:
        log.info('- writing similarity upper triangle matrix to STDOUT')
        print('\n'.join(matrix_rep))
    else:
        out = pathlib.Path(options.out_path)
        log.info(f'- writing similarity upper triangle matrix to {out}')
        with open(out, 'wt', encoding=ENCODING) as handle:
            handle.write('\n'.join(matrix_rep) + '\n')

    end_time = dti.datetime.now(tz=dti.timezone.utc)
    log.info(f'similarity analysis complete after {(end_time - start_time).total_seconds()} seconds')
    return 0
