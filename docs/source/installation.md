Installing FLAMES
=======================

Setting the environment
-----------------------

The FLAMES package is written in Python and requires a few dependencies to be installed. The easiest way to install these dependencies is to use the conda package manager. If you do not have conda installed, we recommend installing the [anaconda](https://www.anaconda.com/download) distribution. Once conda is installed, you can create a new environment with the required dependencies using the following command:

```bash
conda env create --file environment.yml
```

Requirements
------------

0. Python >= 3.10
1. pymatgen >= 2022.0.0
2. numpy >= 1.2
3. scipy >= 1.6.3
4. simplejson
5. ase
6. gemmi

```{admonition} Activate the conda environment
:class: attention

   Don't forget to activate the conda environment before installing or running FLAMES. To do so, run the following command:

    conda activate flames

```

Installation
------------

### Option 1: Using pip

The easiest way to install ``FLAMES`` is using ``pip``. To do so, run the following command:

```bash
pip install flames
```

### Option 2: Manually importing the module

It is possible to just download the package and manually import ``flames`` it using the ``sys`` module, as exemplified below:

```python
# importing module
import sys

# appending a path
sys.path.append('{PATH_TO_FLAMES}/flames')

import flames
```

Just remember to change the ``{PATH_TO_FLAMES}`` to the directory where you download the FLAMES package.

### Option 3: Installing from source

To install **flames** from source, first clone [the repository](https://github.com/lipelopesoliveira/flames):

```bash
git clone https://github.com/lipelopesoliveira/flames.git
cd flames
```

Then run

```bash
pip install -e .
```
