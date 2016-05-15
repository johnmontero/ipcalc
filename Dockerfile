FROM centos:latest
MAINTAINER jmonteroc@gmail.pe

ENV PYTHONUNBUFFERED 1

RUN yum -y update && yum clean all
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-devel python-setuptools python-pip python-lxml && yum clean all
RUN pip install --upgrade pip
RUN yum -y install gcc gcc-c++ && yum clean all
RUN yum -y reinstall glibc-common  && yum clean all

RUN yum -y install wget  && yum clean all
#RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64
#RUN chmod +x /usr/local/bin/dumb-init

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install --editable .

ENTRYPOINT ["ipcalc"]
