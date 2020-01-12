# BUILD IMAGE

FROM arm32v6/python:3.6-alpine
COPY dth22toinflux.py /home/dth22/
COPY requirements.txt /home/dth22/
COPY run.sh /home/dth22/

RUN apk --no-cache add git build-base
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
	cd Adafruit_Python_DHT && \
	python3 setup.py install

WORKDIR /home/dth22

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "./run.sh"]
