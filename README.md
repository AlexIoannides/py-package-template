# Python Package Template Project

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](https://pypi.org/project/py-package-template/)

This repository contains a skeleton Python package project that can be used as a template for developing **any** type of Package that is destined for upload to PyPI, or just for local install using Pip. It includes the following components:

- a minimal `setup.py` file;
- testing with PyTest; and,
- documentation (HTML and PDF) generated using Sphinx with auto-documentation setup; and,
- an entry-point that allows the package to execute functions directly from the command line (e.g. to start a server, interact with a user, etc.).

A description of how to work with (and modify) each of these components, is provided in more detail in the sections of this README that follow-on below.

This is obviously a opinionated view of how a Python package project ought to be structured, that is based largely on my own experiences (and common requirements). Where I have needed guidance on this subject, I have leant heavily on the advice given by the [Python Packaging Authority (PyPA)](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and used the excellent [Requests](https://github.com/requests/requests) and [Flask](https://github.com/pallets/flask) projects as references for 'best practices'.

## Project Dependencies

We use [pipenv](https://docs.pipenv.org) for managing project dependencies and Python environments (i.e. virtual environments). This is **not** to be confused with managing installation dependencies for the package under developement - i.e. those that need to be defined in `setup.py`. All of the direct packages dependencies required to run the code (e.g. NumPy for tensors), as well as all the packages used during development (e.g. flake8 for code linting and IPython for interactive console sessions), are described in the `Pipfile`. Their precise downstream dependencies are described in `Pipfile.lock`.

### Installing Pipenv

To get started with Pipenv, first of all download it - assuming that there is a global version of Python available on your system and on the PATH, then this can be achieved by running the following command,

```bash
pip3 install pipenv
```

For more information, including advanced configuration options, see the [official pipenv documentation](https://docs.pipenv.org).

### Installing this Projects' Dependencies

Make sure that you're in the project's root directory (the same one in which `Pipfile` resides), and then run,

```bash
pipenv install --dev
```

This will install all of the direct project dependencies as well as the development dependencies (the latter a consequence of the `--dev` flag).

### Running Python and IPython from the Project's Virtual Environment

In order to continue development in a Python environment that precisely mimics the one the project was initially developed with, use Pipenv from the command line as follows,

```bash
pipenv run python3
```

The `python3` command could just as well be `ipython3`.

## Running Unit Tests

All test have been written using the [PyTest](https://docs.pytest.org/en/latest/) package. Tests are kept in the `tests` folder and can be run from the command line by - e.g. by evoking,

```bash
pipenv run pytest
```

## Linting Code

We have chosen [flake8](http://flake8.pycqa.org/en/latest/) for style guide enforcement. This can be invoked from the command line by running,

```bash
pipenv run flake8 py_pkg
```

## Static Type Checking

We have used the Python type annotation framework, together with the [MyPy package](http://mypy-lang.org), to perform static type checks on the codebase. Analogous to any linter or unit testing framework, MyPy can be run from the command line as follows,

```bash
pipenv run python -m mypy py_pkg/*.py
```

MyPy options for this project are kept in the `mypy.ini` file that MyPy will look for by default. For more information on the fulls set of options, see the [mypy documentation](https://mypy.readthedocs.io/en/stable/config_file.html).

## Documentation

The documentation in the `docs` folder has have been built using [Sphinx](http://www.sphinx-doc.org). We have used the default 'quickstart' automatic configuration, which is triggered by executing,

```bash
pipenv run sphinx-quickstart
```

The output is based primarily on the Docstrings in the source code, using the `autodoc` extension within Sphinx (specified during the 'quickstart'). The documentation can be built by running the following command,

```bash
pipenv run sphinx-build -b html docs/source docs/build_html
```

A third party theme from [Read the Docs](https://readthedocs.org) has also been used, by installing the `sphinx_rtd_theme` as a development dependency and modifying `docs/source/config.py` as follows:

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

### Creating a PDF Version Using LaTeX

So long as a LaTex distribution is present on your system (e.g. MikTeX for Mac OS X), then it is possible to create a PDF version of the documentation, as well. Start by building the prerequisite LaTex version from the ReStructured Text originals,

```bash
pipenv run sphinx-build -b latex docs/source docs/build_latex
```

Then, navigate to `docs/build_latex` and run,

```bash
make
```

Both LaTeX and PDF versions can then be found in `docs/build_latex`.

## Building Deployable Distributions

The easiest and most pragmatic way to deploy this package is to build a Python [wheel](https://wheel.readthedocs.io/en/stable/) and to then to install it in a fresh virtual environment on the target system. The exact build configuration is determined by the parameters in `setup.py`. Note, that this requires that all package dependencies also be specified in `setup.py`, regardless of their entry in `Pipfile`. For more information on Python packaging refer to the [Python Packaging User Guide](https://packaging.python.org) and the accompanying [sample project](https://github.com/pypa/sampleproject). To create the Python wheel run,

```bash
pipenv run python setup.py bdist_wheel
```

This will create `build`, `py_package_template.egg-info` and `dist` directories - the wheel can be found in the latter. This needs to be copied to the target system (which we are assuming has Python and Pipenv available as a minimum), where it can be installed into a new virtual environment, together with all downstream dependencies, using,

```bash
pipenv install path/to/your-package.whl
```
