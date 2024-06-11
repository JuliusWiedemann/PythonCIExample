![ci build results](https://github.com/JuliusWiedemann/PythonCIExample/actions/workflows/python-ci.yml/badge.svg)
![pylint-score](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/pylint-score.json)
![mypy-warnings](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/mypy_warnings.json)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/coverage.json)
[![license](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

# 🏗️ Python Continuous Integration - Example 

This repository shows a basic example of CI/CD in python with [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](#). It can be used as a template to set up a new [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) project.

Navigate to the branch [example-failed-unittest](https://github.com/JuliusWiedemann/PythonCIExample/tree/example-failed-unittest) or [example-failed-pylint](https://github.com/JuliusWiedemann/PythonCIExample/tree/example-failed-pylint) to view what a failed build will look like.

## Features
- Static code analysis with [pylint](https://www.pylint.org/).
- Type checking with [mypy](https://www.mypy-lang.org/).
- Testing with python [unittest](https://docs.python.org/3/library/unittest.html) module.
- Code coverage with [coverage](https://pypi.org/project/coverage/) module.

## Usage
- Download the source code and use it as a template for your new python project.
- You need to follow [this](https://github.com/marketplace/actions/dynamic-badges) configuration to use the dynamic badges. Alternative: Just remove the "Create Badge" step from the yml file to disable the feature.

## Output
- This template uses [GitHub Actions](https://docs.github.com/en/actions) to run all the tools. It will generate dynamic badges with the [dynamic-badges](https://github.com/marketplace/actions/dynamic-badges) action.
- Alternatively you can just look at the console output: [GitHub Actions Output](https://github.com/JuliusWiedemann/PythonCIExample/actions).

An example build can look like this:
![](images/ci-report.png)

---

Python Lecture for DHBW - Computer Science

🧑 Julius Wiedemann
