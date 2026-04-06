.PHONY: venv rmenv clean all test doc

VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3
TESTFILES=src/infixtopost_test.py src/mathlib_test.py
PATHTODOXYFILE=src/Doxyfile
PATHTODOCDIR=src/doc

#Creates virtual environment and downloads all dependencies
all: 
	$(PYTHON) src/setup.py

#Creates doxygen documentation into PATHTODOCDIR
doc:
	doxygen $(PATHTODOXYFILE)

#Removes doxygen documentation from PATHTODOCDIR
rmdox:
	rm -rf $(PATHTODOCDIR)/html $(PATHTODOCDIR)/latex

#Removes virtual environment
rmenv:
	rm -rf $(VENVNAME)

#Runs tests for TESTFILES
test: 
	pytest $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"

#Removes temporary files and files not meant to be handed
clean:
	rm -rf .pytest_cache
