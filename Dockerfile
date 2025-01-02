FROM python:3-slim
ENV PATH=/root/.local/bin:$PATH
RUN pip install uv; \
	uv tool install tox --with tox-uv
ENTRYPOINT ["uv"]
WORKDIR /echec

