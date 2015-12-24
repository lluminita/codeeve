# codeeve

[![Requirements
Status](https://requires.io/github/luminitacristinalazarescu/codeeve/requirements.svg?branch=master)](https://requires.io/github/luminitacristinalazarescu/codeeve/requirements/?branch=master)

**Description**

CodeEve is a project designed during and for the Django Mentoring initiative, where one can upload a project is working on and also can find projects to contribute to. Is also aimed to be a tool for organizing events for the initiative.

**Installation**
* fork the repo
* run:
```
pip install -r requirements/dev.txt
```
* for development we will be using sqlite3 for the database, which is already
  set up in the settings.py file. In order to create it on you local just run
```
python manage.py migrate
```
* make sure you install python3

**Contributing**
* fork repo
* clone locally the fork
* add this repo as upstream (git add upstream git@github.com:lluminita/codeeve.git)
* work on a branch
* make pull request (PR) against master branch of git@github.com:lluminita/codeeve.git

