.PHONY: install

install:
	pip install -r requirements.txt

setup: install
	python3 aws_config.py

run:
	python3 main.py
	
