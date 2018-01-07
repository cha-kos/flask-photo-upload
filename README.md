# Photo Upload

A simple photo upload form built using Flask.

## Travis CI Build Status  
[![Build Status](https://travis-ci.org/chrishakos/flask-photo-upload.svg?branch=master)](https://travis-ci.org/chrishakos/flask-photo-upload)


### Running Locally

In order to run this app locally, first clone or download the repository and navigate to the root directory of the project from your command line.

Create your virtualenv by running the command
`virtualenv env`

Activate your virtualenv with the command
`source env/bin/activate`

Download package dependencies by with the command
`pip install -r requirements.txt`

Start up local server with the command
`gunicorn app:app`
