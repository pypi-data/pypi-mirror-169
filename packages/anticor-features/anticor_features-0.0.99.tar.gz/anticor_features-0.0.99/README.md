# README #

### Tutorials ###

Anti-correlated genes as a method of feature selection

### What is this repository for? ###

* Unsupervised feature selection for single cell omics (or anything else!) that passes the null dataset test

### How do I get set up? ###

`python3 -m pip install anticor_features`

You can also install using the setup.py script in the distribution like so:
`python3 setup.py install`


### How do I run use this package? ###

#### Using Scanpy or AnnData as an interface? ####

```
from XXX import XXX


```
This yields a pandas data frame that will give you the collected summary statistics, and let you filter based on the features annotated as "selected" in that column
```
>>> print(anti_cor_res.head())

```


A list of the gProfiler accepted species codes is listed here: https://biit.cs.ut.ee/gprofiler/page/organism-list

### License ###
This package is available via the AGPLv3 license.

### Who do I talk to? ###

* Repo owner/admin: scottyler89+bitbucket@gmail.com