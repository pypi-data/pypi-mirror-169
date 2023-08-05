# Installation

Preferred way to install is as usual (for testing or in isolation):

```console
❯ pipx install limitys
```

For production use (well, ahem, ...) or within a virtual python env:

```console
❯ pip install limitys
```
**Note**: Installing `scipy`or (as in this case) `scikit-learn` is sometimes surprisingly difficult. 
In case you target an arm64 system based on the M1 chip with a package management per homebrew and the normal
`pip install` fails for a python 3.10 based virtual environment because of openblas is not found by scikit-learn
and you did do `brew install openblas`before, the following workaround seems to help (as of 2022-SEP-25): 

```console
❯ export PKG_CONFIG_PATH="/opt/homebrew/opt/openblas/lib/pkgconfig"
❯ pip install limitys
```
