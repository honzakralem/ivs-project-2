.PHONY: venv
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt

venv:
	python -m venv $(VENVNAME) 
	$(VENVNAME)/bin/pip install -r $(REQUIREMENTSPATH)