# Python Proxy Switcher

A simple HTTP - Python proxy switcher (PPS).

## Setup

To be able to execute PPS, we'll need to setup our local environment by installing some of the dependencies this project needs.

You'll need to install [pipenv](https://pipenv-es.readthedocs.io/es/stable/), you can get it trough pip or direct installation with your OS app manager.

- Pip installation

  -     pip install pipenv

- APP Manager

  -     sudo apt install software-properties-common python-software-properties
    sudo add-apt-repository ppa:pypa/ppa
    sudo apt update
    sudo apt install pipenv

  pipenv install

After installing the dependencies, we will need to install the packages we are going to use.

    python3 -m pipenv install

This will install the packages registered in the Pipfile.

After we have installed the required packages, we need toactivate the shell to interact with the virtualenv we just created.

    pipenv shell
    python3 --version

This will spawn a new shell subprocess, which can be deactivated by using `exit`.
