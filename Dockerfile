FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./root
RUN pip install --proxy http://172.25.255.98:8080 -r ./root/requirements.txt
COPY ./ ./root
EXPOSE 8000
WORKDIR /root
COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
