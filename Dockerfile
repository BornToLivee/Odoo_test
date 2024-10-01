FROM python:3.12
LABEL authors="clash"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "odoo/odoo-bin", "-c", "./config/odoo.conf"]
