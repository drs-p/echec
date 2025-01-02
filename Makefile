.PHONY: all clean image test dist

all: dist

clean:
	-rm -rf src/echec.egg-info tests/__pycache__ .tox

image:
	docker build --tag uv .

test: image
	docker run --rm -it --mount type=bind,source=.,target=/echec uv tool run tox --workdir /tmp/echec/tox run

dist: image
	docker run --rm -it --mount type=bind,source=.,target=/echec uv build
