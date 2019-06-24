# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7.3-alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=try-django Version=0.0.1
EXPOSE 8000

COPY ./apps/requirements.txt /requirements.txt

WORKDIR /app
ADD . /app

RUN apk add --no-cache gcc libc-dev unixodbc-dev

# Using pip:
RUN python3 -m pip install -r /requirements.txt
CMD ["python3", "-m", "try-django"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "try-django"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m try-django"
