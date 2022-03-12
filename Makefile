.PHONY: all test clean

check-pep257:
	@prospector --with-tool pep257

create-requirements:
	@pip-compile ./requirements/base.in

freeze:
	@pip freeze

format:
	@blue .
	@isort .

install-requirements:
	@pip install -r ./requirements/base.in

lint:
	@blue . --check
	@isort . --check

update-requirements:
	@rm ./requirements/base.txt
	@pip-compile ./requirements/base.in
