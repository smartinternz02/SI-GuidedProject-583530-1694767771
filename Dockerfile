
FROM python

RUN mkdir -p /Aruna

COPY . /Aruna 

RUN python3 -m pip install -r /Aruna/requirements.txt

EXPOSE 5000

CMD ["python", "app1.py"]