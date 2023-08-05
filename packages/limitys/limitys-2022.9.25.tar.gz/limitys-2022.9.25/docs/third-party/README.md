# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([8da08f2a ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:8da08f2ac78fbac5545bc05d86933e3610eec5da55c54a9eb3ccb83e891390e0")).
<!--[[[end]]] (checksum: 8dcb5c23c3e507f3541a2f2770701d1c)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                               | License                 | Author                      | Description (from packaging data)                                       |
|:-------------------------------------------|:------------------------------------------------------|:------------------------|:----------------------------|:------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)              | [6.0](https://pypi.org/project/PyYAML/6.0/)           | MIT License             | Kirill Simonov              | YAML parser and emitter for Python                                      |
| [gensim](http://radimrehurek.com/gensim)   | [4.2.0](https://pypi.org/project/gensim/4.2.0/)       | LGPL-2.1-only           | Radim Rehurek               | Python framework for fast Vector Space Modelling                        |
| [nltk](https://www.nltk.org/)              | [3.7](https://pypi.org/project/nltk/3.7/)             | Apache Software License | NLTK Team                   | Natural Language Toolkit                                                |
| [numpy](https://www.numpy.org)             | [1.23.3](https://pypi.org/project/numpy/1.23.3/)      | BSD License             | Travis E. Oliphant et al.   | NumPy is the fundamental package for array computing with Python.       |
| [pandas](https://pandas.pydata.org)        | [1.5.0](https://pypi.org/project/pandas/1.5.0/)       | BSD License             | The Pandas Development Team | Powerful data structures for data analysis, time series, and statistics |
| [scikit-learn](http://scikit-learn.org)    | [1.1.2](https://pypi.org/project/scikit-learn/1.1.2/) | BSD License             | UNKNOWN                     | A set of python modules for machine learning and data mining            |
| [typer](https://github.com/tiangolo/typer) | [0.6.1](https://pypi.org/project/typer/0.6.1/)        | MIT License             | Sebastián Ramírez           | Typer, build great CLIs. Easy to code. Based on Python type hints.      |
<!--[[[end]]] (checksum: 619e77e21e280f71f494b92d95bec61f)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
gensim==4.2.0
  - numpy [required: >=1.17.0, installed: 1.23.3]
  - scipy [required: >=0.18.1, installed: 1.9.1]
    - numpy [required: >=1.18.5,<1.26.0, installed: 1.23.3]
  - smart-open [required: >=1.8.1, installed: 6.2.0]
nltk==3.7
  - click [required: Any, installed: 8.1.3]
  - joblib [required: Any, installed: 1.2.0]
  - regex [required: >=2021.8.3, installed: 2022.9.13]
  - tqdm [required: Any, installed: 4.64.1]
pandas==1.5.0
  - numpy [required: >=1.21.0, installed: 1.23.3]
  - python-dateutil [required: >=2.8.1, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2020.1, installed: 2022.2.1]
PyYAML==6.0
scikit-learn==1.1.2
  - joblib [required: >=1.0.0, installed: 1.2.0]
  - numpy [required: >=1.17.3, installed: 1.23.3]
  - scipy [required: >=1.3.2, installed: 1.9.1]
    - numpy [required: >=1.18.5,<1.26.0, installed: 1.23.3]
  - threadpoolctl [required: >=2.0.0, installed: 3.1.0]
typer==0.6.1
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: db89c2606ea727a50b00ba7e62968ed3)-->
