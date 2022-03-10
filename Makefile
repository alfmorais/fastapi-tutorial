.PHONY: all test clean

create-requirements:
	@pip-compile ./requirements/base.in

install-requirements:
	@pip install -r ./requirements/base.in

update-requirements:
	@rm ./requirements/base.txt
	@pip-compile ./requirements/base.in
