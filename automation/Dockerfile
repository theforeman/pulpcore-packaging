FROM centos:7

RUN yum install -y epel-release && \
  yum install -y which postgresql-devel gcc python3 python3-devel python3-pip git git-annex rpm-build rpmdevtools crudini && \
  yum install -y gcc make cmake bzip2-devel expat-devel file-devel glib2-devel libcurl-devel libmodulemd2-devel ninja-build libxml2-devel python36-devel python36-gobject rpm-devel openssl-devel sqlite-devel xz-devel zchunk-devel zlib-devel swig && \
  yum clean all

COPY _generate_deps.sh /app/_generate_deps.sh
COPY requirements.txt /app/requirements.txt

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash", "/app/_generate_deps.sh"]
