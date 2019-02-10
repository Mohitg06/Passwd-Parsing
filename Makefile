build:
	python parsing.py /etc/passwd /etc/group


test:
	python -m pytest tests/