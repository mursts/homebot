FROM arm32v7/python:3.7.2-stretch
WORKDIR /bot
COPY ./ ./
RUN apt-get install openssl ca-certificates && pip install -r requirements.txt 
ENTRYPOINT ["python", "run.py"]
