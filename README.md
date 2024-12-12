

brew install pipenv


In Three simple steps to create current directory :


export the variable as

    'export PIPENV_VENV_IN_PROJECT=1'

Create a empty folder and file Pipfile

    mkdir .venv

    touch Pipfile

Then execute

    pipenv shell

activate venv

    source .venv/bin/activate




To execute hello

    bazel run //:hello

or 

    pipenv run python hello.py


To install all requirments and update requirements



bazel run //:requirements.update



running cli 


bazel run //:cli -- sum 2 3   
bazel run //:cli -- hello murli  
bazel run //:cli -- bye murli  
