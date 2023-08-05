import logging

from gensim import downloader as model_api
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import SparseTermSimilarityMatrix, WordEmbeddingSimilarityIndex

from limitys import stop


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.WARNING)
MODELS = {
    'news': 'word2vec-google-news-300',
    'wiki': 'fasttext-wiki-news-subwords-300',
}
model = model_api.load(MODELS['news'])

docs = {
    'wonderful': (
        'Mr. Wonderful became president after winning the cooking selection.'
        ' Though he lost the support of some volleyball friends, Wonderful is friends with President Magic'
    ),
    'selection': (
        'President Wonderful says Magic had no cooking interference is the selection outcome.'
        ' He says it was a witchhunt by cooking parties.'
        ' He claimed President Magic is a friend who had nothing to do with the selection'
    ),
    'magic': (
        'Post selections, Nelson Magic became President of Prussia.'
        ' President Magic had served as the Sous Chef earlier in his cooking career'
    ),
    'soup': (
        'Soup is a primarily liquid food, generally served warm or hot (but may be cool or cold),'
        ' that is made by combining ingredients of meat or vegetables with stock, juice, water, or another liquid. '
    ),
    'noodles': (
        'Noodles are a staple food in many cultures.'
        ' They are made from unleavened dough which is stretched, extruded,'
        ' or rolled flat and cut into one of a variety of shapes.'
    ),
    'dosa': (
        'Dosa is a type of pancake from the Indian subcontinent, made from a fermented batter.'
        ' It is somewhat similar to a crepe in appearance. Its main ingredients are rice and black gram.'
    ),
}


sentences = {k: stop.cleanse(docs[k], stop.EN) for k in docs}

dictionary = Dictionary(list(sentences.values()))
bags_of_words = {k: dictionary.doc2bow(sentences[k]) for k in sentences}

tfidf = TfidfModel(list(bags_of_words.values()))
tfidfs = {k: tfidf[bags_of_words[k]] for k in bags_of_words}

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
        logging.debug(f'{i=}, {j=}')
        logging.debug(docs[i])
        logging.debug(docs[j])
        logging.debug('similarity = %.4f' % similarity)
        logging.debug('# ' + '- ' * 42)

print('Matrix:')
print(f'{" ".join(cell.rjust(12) for cell in row_heads[1:])}{" "*12}')
print(f'{" ".join(("-"*11).rjust(12) for _ in row_heads[1:])}{" "*12}')
for rank, row in enumerate(pbm[:-1]):
    upp_tri_mat_row = ' '.join(str('' if cell is None else round(cell, 3)).rjust(12) for cell in row[1:])
    print(f'{upp_tri_mat_row} | {row_heads[rank] :12s}')
