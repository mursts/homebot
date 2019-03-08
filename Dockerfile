FROM python:3.7.2-alpine
WORKDIR /bot
COPY ./ ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]