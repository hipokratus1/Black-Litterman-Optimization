FROM python:3

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/messari/messari-python-api.git

COPY . .

CMD [ "python", "-u", "./portfolio.py" ]