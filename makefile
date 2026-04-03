.PHONY: venv
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3

venv:
	$(PYTHON) -m venv $(VENVNAME) 
	$(VENVNAME)/bin/pip install -r $(REQUIREMENTSPATH)