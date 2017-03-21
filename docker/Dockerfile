FROM kmccormick/base

MAINTAINER Kevin McCormick <https://github.com/kmccormick>

ENV GIT_REPO=https://github.com/kmccormick/rmm.git \
    DUID=23487

RUN apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        git \
        python3 \
        python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && pip3 install -U \
        pip \
        setuptools \
    && useradd --uid $DUID --user-group --create-home --home-dir /code --skel /dev/null docker

WORKDIR /code
EXPOSE 8000
ADD start.sh /
CMD ["/start.sh"]
