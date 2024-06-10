![ci build results](https://github.com/JuliusWiedemann/PythonCIExample/actions/workflows/python-ci.yml/badge.svg)
![pylint-score](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/pylint-score.json)
![mypy-warnings](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/mypy_warnings.json)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/coverage.json)
[![license](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

# 🏗️ Python Continuous Integration - Example 

This repo shows a basic example of CI/CD in python with github actions
Navigate to the branch [example-failed-unittest](https://github.com/JuliusWiedemann/PythonCIExample/tree/example-failed-unittest) or [example-failed-pylint](https://github.com/JuliusWiedemann/PythonCIExample/tree/example-failed-pylint) to view what a failed build will look like.

## Features
- Static code analysis with pylint
- Type checking with mypy
- Testing with python unittest module
- Code coverage with coverage module

## Usage
- Download the source code and use it as a template for your new python project
- You need to follow [this](https://github.com/marketplace/actions/dynamic-badges) configuration to use the dynamic badges. Alternative: Just remove the "Create Badge" step from the yml file to disable the feature

## Output
![](images/ci-report.png)

---

Python Lecture for DHBW - Computer Science

🧑 Julius Wiedemann
