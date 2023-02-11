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

After installing the dependencies, we will need to install the packages we are going to use.

    python3 -m pipenv install

This will install the packages registered in the Pipfile.

After we have installed the required packages, we need toactivate the shell to interact with the virtualenv we just created.

    pipenv shell
    python3 --version

This will spawn a new shell subprocess, which can be deactivated by using `exit`.

## How to use PPS

Now that you have everything set-up, you can checkout `request_proxy_jumping.py` where you'll find a short example of the way PPS is used. In here we interact with environment variables defined in a `.env` file. You'll see an example of it on `.env.example`.

To execute this file you'll just need to run:

    python3 request_proxy_jumping.py

## Good to know

This switcher will use a list of available proxies that you provide, including the ports where this IP's respond for your desired protocol. Please take in consideration the type of request you want to perform.
