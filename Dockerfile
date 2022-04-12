FROM python:latest
RUN git clone https://github.com/IAmS4n/panoramix.git
RUN cd ./panoramix;pip install .
ENTRYPOINT ["panoramix"]
