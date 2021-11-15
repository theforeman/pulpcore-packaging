FROM docker.io/centos/python-38-centos7:latest

USER 0

RUN yum install -y epel-release &&  \
    yum install -y which postgresql-devel gcc python3 python3-devel python3-pip git git-annex rpm-build rpmdevtools crudini && \
    yum install -y gcc make cmake bzip2-devel expat-devel file-devel glib2-devel libcurl-devel cairo-devel.x86_64 cairo-gobject-devel.x86_64 libmodulemd2-devel ninja-build libxml2-devel pygobject3-devel.x86_64 rh-python38-python-devel python36-gobject rpm-devel openssl-devel sqlite-devel xz-devel zchunk-devel zlib-devel swig libxslt-devel libxml2-devel && \
    yum clean all

COPY _generate_deps.sh /app/_generate_deps.sh
COPY requirements.txt /app/requirements.txt

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash", "/app/_generate_deps.sh"]
