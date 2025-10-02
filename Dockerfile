#leonardo David Salazar Mora#
#Froylan Alonso Perez Alanis#
#Automatizacion de infraestructura digital ll#

FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
