FROM python:3-slim
ENV PATH=/root/.local/bin:$PATH
RUN pip install --root-user-action 'ignore' uv; \
	uv tool install tox --with tox-uv
ENTRYPOINT ["uv"]
WORKDIR /echec

