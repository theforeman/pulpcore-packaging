FROM quay.io/centos/centos:stream9

RUN dnf install 'dnf-command(config-manager)' -y && \
    dnf config-manager --set-enabled crb && \
    dnf install -y gobject-introspection-devel cairo-gobject-devel cairo-devel gcc make cmake python3.11-devel python3.11-wheel python3.11-pip && \
    dnf clean all

COPY generate_package_list.sh /app/generate_package_list.sh
COPY requirements.txt /app/requirements.txt

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash", "/app/generate_package_list.sh"]
