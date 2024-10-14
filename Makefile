.PHONY: all clean container test dist

all: dist

clean:
	-rm -rf src/echec.egg-info tests/__pycache__ .tox

container:
	docker build --tag echec .

test: container
	docker run --rm -it --mount type=bind,source=.,target=/echec echec uvx tox run

dist: container
	docker run --rm -it --mount type=bind,source=.,target=/echec echec uv build

