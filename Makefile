ISORT_ARGS := --combine-star --combine-as --order-by-type --thirdparty scrapy --multi-line 3 --trailing-comma --force-grid-wrap 0 --use-parentheses --line-width 88

SRC_DIRS := ./resources
TST_DIRS := ./tests

check:
	python3 -m isort --check --diff $(ISORT_ARGS) $(SRC_DIRS)
	python3 -m black --check $(SRC_DIRS)
	flake8 $(SRC_DIRS)

format:
	python3 -m isort --apply $(ISORT_ARGS) $(SRC_DIRS)
	python3 -m black $(SRC_DIRS)

tags:
	ctags -R -f tags $(SRC_DIRS) $(TST_DIRS)

test:
	coverage run --source $(SRC_DIRS) -m pytest

cov:
	coverage report -m
