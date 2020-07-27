FROM python:3.8-buster

RUN apt update && apt install -y sudo mecab libmecab-dev mecab-ipadic-utf8
RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y

RUN python -m pip install python-dotenv tweepy mecab-python

RUN cp /etc/mecabrc /usr/local/etc

ADD src /src
WORKDIR /src
ENTRYPOINT [ "python", "main.py" ]
