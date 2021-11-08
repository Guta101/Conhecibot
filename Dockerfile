FROM python:3.7.11
MAINTAINER Gustavo Tartaglia
COPY . /rasa_bot
WORKDIR /rasa_bot
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python -m spacy download pt_core_news_lg
ENTRYPOINT rasa run --model models --enable-api --cors "*" --debug
EXPOSE 5005