brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

eclear:
	pip uninstall hexlet-code 

einstall:
	make build
	make publish
	make package-install

lint:
	poetry run flake8 brain_games