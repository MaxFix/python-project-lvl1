build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install dist/mindgame-0.1.0-py3-none-any.whl
make lint:
	poetry run flake8 brain_games
