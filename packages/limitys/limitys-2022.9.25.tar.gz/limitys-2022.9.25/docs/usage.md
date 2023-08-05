# Usage

## Help Screen

```console
❯ limitys
usage: limitys [-h] [--language LANGUAGE] [--documents DOCUMENTS] [--out-path OUT_PATH] [--quiet] [--verbose] [documents_pos]

Overlap (Finnish: limitys) assesses sentences from constrained and overlapping vocabularies.

positional arguments:
  documents_pos         file with format in (json, yaml) providing the keyed documents. Optional
                        (default: documents.yml)

options:
  -h, --help            show this help message and exit
  --language LANGUAGE, -l LANGUAGE
                        language in (english, french, german, spanish) of the documents. Optional
                        (default: english)
  --documents DOCUMENTS, -d DOCUMENTS
                        file providing the keyed documents. Optional
                        (default: positional documents value)
  --out-path OUT_PATH, -o OUT_PATH
                        output file path for matrix (default: STDOUT)
  --quiet, -q           work as quiet as possible - progress bar only if all well (default: False)
  --verbose, -v         work logging more information along the way (default: False)
```

## Example

Given six documents per the YAML file `documents.yml`:
```yaml
---
wonderful: >
  Mr. Wonderful became president after winning the cooking selection.
  Though he lost the support of some volleyball friends, Wonderful is friends with President Magic
selection: >
  President Wonderful says Magic had no cooking interference is the selection outcome.
  He says it was a witchhunt by cooking parties.
  He claimed President Magic is a friend who had nothing to do with the selection
magic: >
  Post selections, Nelson Magic became President of Prussia.
  President Magic had served as the Sous Chef earlier in his cooking career
soup: >
  Soup is a primarily liquid food, generally served warm or hot (but may be cool or cold),
  that is made by combining ingredients of meat or vegetables with stock, juice, water, or another liquid.
noodles: >
  Noodles are a staple food in many cultures.
  They are made from unleavened dough which is stretched, extruded, or rolled flat and cut into one of a variety of shapes.
dosa: >
  Dosa is a type of pancake from the Indian subcontinent, made from a fermented batter.
  It is somewhat similar to a crepe in appearance. Its main ingredients are rice and black gram.
```

The call:

```console
❯ limitys -l english -d documents.yml -q -o matrix.txt
100%|███████████████████████████| 83/83 [00:03<00:00, 25.57it/s]
```

Yields the following matrix in the result file `matrix.txt`:

```
# Matrix:

   selection        magic         soup      noodles         dosa
 -----------  -----------  -----------  -----------  -----------
       0.236         0.15        0.012        0.017        0.037 | wonderful
                     0.13          0.0        0.019          0.0 | selection
                                 0.035        0.018        0.038 | magic
                                              0.091        0.062 | soup
                                                           0.109 | noodles
```
