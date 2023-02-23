FROM python:3
WORKDIR /user/src/app
COPY requirments.txt ./
RUN pip install -r requirments.txt 