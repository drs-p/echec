.PHONY: all clean image test dist

all: dist

clean:
	-rm -rf src/echec.egg-info tests/__pycache__ .tox

image:
	docker build --tag uv .

test: image
	docker create --tty --name "uv" uv tool run tox run
	docker cp . uv:/home/uv
	docker start --attach uv
	docker rm uv

dist: image
	docker create --tty --name "uv" uv build
	docker cp . uv:/home/uv
	docker start --attach uv
	mkdir -p dist
	docker cp uv:dist/. dist
	docker rm uv
