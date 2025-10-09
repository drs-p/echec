FROM python:3-slim
ENV PATH=/root/.local/bin:$PATH
RUN apt-get update && apt-get -y install build-essential libgmp-dev libmpfr-dev libmpc-dev; \
    pip install --root-user-action 'ignore' uv; \
	uv tool install tox --with tox-uv
ENTRYPOINT ["uv"]
WORKDIR /echec

