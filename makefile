.PHONY: venv rmenv clean
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3
TESTFILES=src/infixtopost_test.py src/mathlib_test.py

venv:
	$(PYTHON) -m venv $(VENVNAME) 
	$(VENVNAME)/bin/pip install -r $(REQUIREMENTSPATH)	

rmenv:
	rm -rf $(VENVNAME)

test: 
	pytest $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"
	
clean:
	rm -rf .pytest_cache
