.PHONY: venv rmenv clean
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3

venv:
	$(PYTHON) -m venv $(VENVNAME) 
	$(VENVNAME)/bin/pip install -r $(REQUIREMENTSPATH)	

rmenv:
	rm -rf $(VENVNAME)

clean:
	rm -rf .pytest_cache
