# M1-2022-git

## Introduction
This repository is a fork from the previous repository.
The bugs in the converter have been fixed and now we want to publish our work as a publicly available python package.

## Getting started
You should be working from **your own repository** that is a fork of M1-2022-git-workflow.
In order to run this project, you will have to follow these steps.
1. Clone this project
2. move into the project folder
``` shell
cd M1-2022-git-workflow
```
3. Set up a virtual environment
 * Create the virtual environment
 ```shell
 python -m venv myvenv
 ```
 * Activate venv
 ```shell
 . venv/bin/activate
 ```
4. Install pytest
```shell
pip install -U pytest
```
5. Execute main script
```shell
python main.py
```

## Instructions
### Merge feature branch into dev
Now that the converter has no more bugs, we want to merge our branch feature into the dev branch.
We will do a pull request (on your own repo). On GitHub, go to the "Pull requests tab" and click "New pull request".
Select *base* and *compare*. Remember : we want to merge *decimal-binary-converter* into *dev*. 
Then, *Create the pull request*. Add some description of the work you have done and publish the Pull Request.

**Note** : We could have just merge *decimal-binary-converter* into *dev* from the command line. However, when working on a real project, you probably won't have the rights to do so. Remember : dev is a public branch. So all the work going down there should be carefully reviewed and tested.


### Publish your work
We now have an awesome binary/decimal two ways converter ! It's time to publish it so the rest of the world can enjoy it !
We will publish it on PyPI (Python Package Index) which is a public repository of softwares for Python.
1. First, you have to create an account on [Pypi.org](https://pypi.org/)
2. Then, in your repository, you will find a [.github directory](/.github)
3. Inside this directory, you will find .yml files that defines workflows (using GitHub actions)
4. Open the yml files and take time to understand them. Do not hesitate to ask the teacher about them

#### Hands on !
5. We want to create a workflow that will, on publish, test our code and if tests succeed, then publish our package on PyPI
6. In GitHub, click on the *Actions* tab, then click on *new workflow*
7. Choose among the suggestions the template that best suits your use-case and click *Configure*
8. You may find some useful informations in the [Python documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
9. When creating a release on GitHub, do not forget to create a tag corresponding to that release

#### Pull request
10. Once the workflow is setup and tested (you have published your package using it) you can open a pull request to the [original repository](https://github.com/rgt-yncrea/M1-2022-git-workflow)
