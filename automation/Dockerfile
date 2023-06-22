FROM quay.io/centos/centos:stream8

USER 0

RUN dnf install -y epel-release python39-rpm-macros python39-devel &&  \
    dnf config-manager --set-enabled powertools && \
    dnf module reset ruby && \
    dnf module -y enable ruby:2.7 && \
    dnf module -y install ruby:2.7 && \
    dnf config-manager --add-repo https://downloads.kitenet.net/git-annex/linux/current/rpms/git-annex.repo && \
    dnf install -y ruby-devel which postgresql-devel gcc python3 python3-devel python3-pip git git-annex-standalone rpm-build rpmdevtools crudini && \
    dnf install -y gcc make cmake bzip2-devel expat-devel file-devel glib2-devel libcurl-devel cairo-devel.x86_64 cairo-gobject-devel.x86_64 libmodulemd-devel ninja-build libxml2-devel pygobject3-devel rpm-devel openssl-devel sqlite-devel xz-devel zchunk-devel zlib-devel swig libxslt-devel libxml2-devel  glibc-langpack-en; sed -i 's/^LANG=.*/LANG="en_US.utf8"/' /etc/locale.conf && \
    dnf clean all

RUN alternatives --set python3 /usr/bin/python3.9

COPY _generate_deps.sh /app/_generate_deps.sh
COPY requirements.txt /app/requirements.txt

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash", "/app/_generate_deps.sh"]