FROM python:3.7-stretch

WORKDIR /tmp

ARG RMR_VER=1.9.1
RUN wget -nv --content-disposition https://packagecloud.io/o-ran-sc/staging/packages/debian/stretch/rmr_${RMR_VER}_amd64.deb/download.deb
RUN dpkg -i rmr_${RMR_VER}_amd64.deb

RUN pip install rmr request

ADD rmracumosadapter.py /tmp

CMD ["python", "rmracumosadapter.py"]




