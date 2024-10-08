FROM debian:bookworm
RUN apt-get --yes update; \
    apt-get --yes install --no-install-recommends \
        ca-certificates curl python3 python-is-python3; \
    apt-get --yes clean; \
    rm -rf /var/lib/apt/lists/*; \
    curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local" sh; \
    uv tool install tox --with tox-uv
WORKDIR /echec

