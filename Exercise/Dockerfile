FROM python:3.7.5-slim
LABLE author="DeepSquare"
RUN pip install Flask requests
COPY ./server.py /server.py
ENV PORT 80
CMD ["python", "-u", "server.py"]
