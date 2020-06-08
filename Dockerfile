FROM python:3.7-slim
COPY requirements.txt top_app.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD ./api /app/api
EXPOSE 5000
ENV FLASK_APP="top_app.py"
CMD ["flask", "run", "--host", "0.0.0.0"]
