# Python Package Template Project

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](https://pypi.org/project/py-package-template/)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](https://travis-ci.org/AlexIoannides/py-package-template)

The py-template-project package allows users to download the contents of this [GiHub repository](https://github.com/AlexIoannides/py-package-template),  containing a skeleton Python package project to be used as a template for kick-starting development of **any** type of Package; destined for upload to PyPI, or just for local install using Pip. The downloaded package includes the following components to aid rapid development without having to spend time cloning existing set-ups from other projects:

- a minimal `setup.py` file;
- testing with PyTest;
- documentation (HTML and PDF) generated using Sphinx with auto-documentation setup; 
- an entry-point that allows the package to execute functions directly from the command line - e.g. to start a server, interact with a user, download a GitHub repository, etc.; and,
- automated testing and deployment using Travis CI.

A description of how to work with (and modify) each of these components, is provided in more detail in the sections that follow-on below, as well as in the documentation and within the example code bundled with the package.

This is obviously a opinionated view of how a Python package project ought to be structured, based largely on my own experiences and requirements. Where I have needed guidance on this subject, I have leant heavily on the advice given by the [Python Packaging Authority (PyPA)](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and used the excellent [Requests](https://github.com/requests/requests) and [Flask](https://github.com/pallets/flask) projects as references for 'best practices'.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip3 install py-template-project
```

## Downloading a Python Package Template Project

To down load the latest version of the Python Package Template project located in [this GiHub repository](https://github.com/AlexIoannides/py-package-template), execute the following command from the command line:

```bash
py-package-template install
```

This will be downloaded to the current directory and will contain the following directory structure:

```bash
py-package-tempate/
 |-- docs/
 |-- |-- build_html/
 |-- |-- build_latex/
 |-- |-- source/
 |-- py-pkg/
 |-- |-- __init__.py
 |-- |-- __version__.py
 |-- |-- curves.py
 |-- |-- entry_points.py
 |-- tests/
 |-- |-- test_data/
 |-- |   |-- supply_demand_data.json
 |-- |   __init__.py
 |-- |   conftest.py
 |-- |   test_curves.py
 |-- .env
 |-- .gitignore
 |-- Pipfile
 |-- Pipfile.lock
 |-- README.md
 |-- setup.py
```

## The Python Package Template Project

We now describe the various components of the template project and the workflows associated with it. The template package project contains two modules to get things started:

- `curves.py`
- `entry_points.py`

The `curves.py` module contains sample code for modelling economic supply and demand curves and makes for a useful demonstration of how Python type annotation and interface definition via abstract base classes, can make code easier to read, document and reason about (I am a big fan). The test suite for this module is contained in the `tests` folder and demonstrates how to get up-and-running with PyTest.

The `entry_points.py` module is referenced in the `setup.py` file via the `entry_points` definitions:

```python
entry_points={
    'console_scripts': ['py-package-template=py_pkg.entry_points:main'],
}
```

It enables the declared entry point - `py_pkg.entry_points.main` -  to be invoked when `py-package-template` is called from the command line. This is what enables the template project to be downloaded programmatically (check the code for the full details). This could easily be extended to start a server (e.g. using Flask), or run any other type of script.

### Project Dependencies

We use [pipenv](https://docs.pipenv.org) for managing project dependencies and Python environments (i.e. virtual environments). These dependencies are **not** to be confused with the package installation dependencies for the package under developement - i.e. those that need to be defined in the `install_requires` section of `setup.py`. All of the direct packages dependencies required to run the project's code (e.g. NumPy for tensors), as well as all the packages used during development (e.g. flake8 for code linting and IPython for interactive console sessions), are described in the `Pipfile`. Their precise downstream dependencies are crystallised in `Pipfile.lock`, which is used to guarentee repeatable (i.e. deterministic) builds.

#### Installing Pipenv

To get started with Pipenv, first of all download it - assuming that there is a 'global' version of Python available on your system and on the PATH, then this can be achieved by running the following command,

```bash
pip3 install pipenv
```

For more information, including advanced configuration options, see the [official pipenv documentation](https://docs.pipenv.org).

#### Installing this Projects' Dependencies

Make sure that you're in the project's root directory (the same one in which `Pipfile` resides), and then run,

```bash
pipenv install --dev
```

This will install all of the direct project dependencies as well as the development dependencies (the latter a consequence of the `--dev` flag). To add and remove dependencies as required for your new project, use `pipenv install` and `pipenv uninstall` as required, using the `--dev` flag for development-only dependencies.

#### Running Python and IPython from the Project's Virtual Environment

In order to open a Python REPL using within an environment that precisely mimics the one the project is being developed with, use Pipenv from the command line as follows,

```bash
pipenv run python3
```

The `python3` command could just as well be `ipython3`.

#### Automatic Loading of Environment Variables

Pipenv will automatically pick-up and load any environment variables declared in the `.env` file, located in the package's root directory. For example, adding,

```bash
SPARK_HOME=applications/spark-2.3.1/bin
```

Will enable access to this variable within any Python program, via a call to `os.environ['SPARK_HOME']`. Note, that if any security credentials are placed here, then this file **must** be removed from source control - i.e. add `.env` to the `.gitignore` file to prevent potential security risks.

#### Pipenv Shells

Prepending `pipenv` to every command you want to run within the context of your Pipenv-managed virtual environment, can get (very) tedious. This can be avoided by entering into a Pipenv-managed shell,

```bash
pipenv shell
```

Which is equivalent to 'activating' the virtual environment. Any command will now be executed within the virtual environment. Use `exit` to leave the shell session.

### Running Unit Tests

All test have been written using the [PyTest](https://docs.pytest.org/en/latest/) package. Tests are kept in the `tests` folder and can be run from the command line by - e.g. by invoking,

```bash
pipenv run pytest
```

The test suite is structured as an independent Python package as follows:

```bash
tests/
 |-- test_data/
 |   |-- supply_demand_data.json
 |   __init__.py
 |   conftest.py
 |   test_curves.py
```

The `conftest.py` module is used by PyTest - in this particular instance for loading test data and building objects that will then be used by potentially many other tests. These are referred to as 'fixtures' in PyTest - more details can be found [here](https://docs.pytest.org/en/latest/fixture.html).

### Linting Code

I prefer to use [flake8](http://flake8.pycqa.org/en/latest/) for style guide enforcement. This can be invoked from the command line by running,

```bash
pipenv run flake8 py_pkg
```

Flake8 could easily be swapped-out for another tool by using Pipenv as described above.

### Static Type Checking

We have used the Python type annotation framework, together with the [MyPy package](http://mypy-lang.org), to perform static type checks on the codebase. Analogous to any linter or unit testing framework, MyPy can be run from the command line as follows,

```bash
pipenv run python -m mypy py_pkg/*.py
```

MyPy options for this project can be defined in the `mypy.ini` file that MyPy will look for by default. For more information on the full set of options, see the [mypy documentation](https://mypy.readthedocs.io/en/stable/config_file.html).

Examples of type annotation and type checking for library development can be found in the `py_pkg.curves.py` module. This should also be cross-referenced with the improvement to readability (and usability) that this has on package documentation.

### Documentation

The documentation in the `docs` folder has been built using [Sphinx](http://www.sphinx-doc.org). We have used the default 'quickstart' automatic configuration, which was originally triggered by executing,

```bash
pipenv run sphinx-quickstart
```

The output is based primarily on the Docstrings in the source code, using the `autodoc` extension within Sphinx (specified during the 'quickstart'). The contents for the entry point into the docs (`index.html`), is defined in the `index.rst` file, which itself imports the `modules.rst` file that lists all of the modules to document. The documentation can be built by running the following command,

```bash
pipenv run sphinx-build -b html docs/source docs/build_html
```

The resulting HTML documentation can be accessed by opening `docs/build_html/index.html` in a web browser.

My preferred third party theme from [Read the Docs](https://readthedocs.org) has also been used, by installing the `sphinx_rtd_theme` as a development dependency and modifying `docs/source/config.py` as follows:

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

#### Creating a PDF Version Using LaTeX

So long as a LaTex distribution is present on your system (e.g. MikTeX for Mac OS X), then it is possible to create a PDF version of the documentation, as well. Start by building the prerequisite LaTex version from the ReStructured Text originals,

```bash
pipenv run sphinx-build -b latex docs/source docs/build_latex
```

Then, navigate to `docs/build_latex` and run,

```bash
make
```

Both LaTeX and PDF versions can then be found in `docs/build_latex`.

### Building Deployable Distributions

The recommended (and most pragmatic) way of deploy this package is to build a Python [wheel](https://wheel.readthedocs.io/en/stable/) and to then to install it in a fresh virtual environment on the target system. The exact build configuration is determined by the parameters in `setup.py`. Note, that this requires that all package dependencies also be specified in the `install_requires` declaration in `setup.py`, **regardless** of their entry in `Pipfile`. For more information on Python packaging refer to the [Python Packaging User Guide](https://packaging.python.org) and the accompanying [sample project](https://github.com/pypa/sampleproject). To create the Python wheel run,

```bash
pipenv run python setup.py bdist_wheel
```

This will create `build`, `py_package_template.egg-info` and `dist` directories - the wheel can be found in the latter. This needs to be copied to the target system (which we are assuming has Python and Pipenv available as a minimum), where it can be installed into a new virtual environment, together with all downstream dependencies, using,

```bash
pipenv install path/to/your-package.whl
```

### Automated Testing and Deployment using Travis CI

We have chosen Travis for Continuous Integration (CI) as it integrates very easily with Python and GitHub (where I have granted it access to my public repositories). The configuration details are kept in the `.travis.yaml` file in the root directory:

```yaml
ncsudo: required

language: python

python:
  - 3.7-dev

install:
  - pip install pipenv
  - pipenv install --dev

script:
  - pipenv run pytest

deploy:
  provider: pypi
  user: alexioannides
  password:
    secure: my-encrypted-pypi-password
  on:
    tags: true
  distributions: bdist_wheel
```

Briefly, this instructs the Travis build server to:

1. download, build and install Python 3.7;
2. install Pipenv
3. use Pipenv and `Pipfile.lock` to install **all** dependencies (dev dependencies are necessary for running PyTest);
4. run all unit tests using PyTest;
5. if the tests were run successfully and if we have pushed a new tag (i.e. a release) to the master branch then:
    - build a Python wheel; and,
    - push it to PyPI.org using my PyPI account credentials.

Note that we provide Travis with an encrypted password, that was made using the Travis command line tool (downloaded using HomeBrew on OS X). For more details on this and PyPI deployment more generally see the [Travis CI documentation](https://docs.travis-ci.com/user/deployment/pypi/#stq=&stp=0).
