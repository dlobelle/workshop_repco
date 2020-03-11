# Project description
Estimation of the location of microplastic sinking from the surface of the ocean in the Mediterranean for 4 months in year 2007. This tests the seasonality of plastic sinking 

# Running the project
In the command line type: python for_repco_workshop.py 
The figure will be produced in the results/

# Version of language
python 3.7.1 

# Packages loaded in main script: 

import numpy as np
import matplotlib.pyplot as plt
import pickle 
from numpy import *
import scipy.linalg
import pandas as pd 
import netCDF4 as nc4
import xarray as xr
from scipy.stats.stats import pearsonr
 

# Test

Version 0.1.0

Testing cookiecutter during reproducibility workshop


## Project organization

```
.
├── .gitignore
├── CITATION.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── bin                <- Compiled and external code, ignored by git (PG)
│   └── external       <- Any external source code, ignored by git (RO)
├── config             <- Configuration files (HW)
├── data               <- All project data, ignored by git
│   ├── processed      <- The final, canonical data sets for modeling. (PG)
│   ├── raw            <- The original, immutable data dump. (RO)
│   └── temp           <- Intermediate data that has been transformed. (PG)
├── docs               <- Documentation notebook for users (HW)
│   ├── manuscript     <- Manuscript source, e.g., LaTeX, Markdown, etc. (HW)
│   └── reports        <- Other project reports and notebooks (e.g. Jupyter, .Rmd) (HW)
├── results
│   ├── figures        <- Figures for the manuscript or reports (PG)
│   └── output         <- Other output for the manuscript or reports (PG)
└── src                <- Source code for this project (HW)

```


## License

This project is licensed under the terms of the [MIT License](/LICENSE.md)

## Citation

Please [cite this project as described here](/CITATION.md).
