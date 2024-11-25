FROM python:3-slim
RUN useradd -m uv
USER uv
ENV PATH=/home/uv/.local/bin:$PATH
RUN pip install uv; \
	uv tool install tox --with tox-uv
ENTRYPOINT ["uv"]
WORKDIR /home/uv/echec

