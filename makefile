.PHONY: venv rmenv clean all test doc

#CONFIGURATION
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3
TESTFILES=src/infixtopost_test.py src/mathlib_test.py
PATHTODOXYFILE=src/Doxyfile
PATHTODOCDIR=src/doc
TOBECLEANED= .pytest_cache

#Creates virtual environment and downloads all dependencies
all: 
	@$(PYTHON) src/setup.py

#Creates doxygen documentation into PATHTODOCDIR
doc:
	@doxygen $(PATHTODOXYFILE)

#Removes doxygen documentation from PATHTODOCDIR
rmdox:
	@rm -rf $(PATHTODOCDIR)/html $(PATHTODOCDIR)/latex

#Launches the calculator	
run:
	@$(PYTHON) src/gui.py

#Removes virtual environment
rmenv:
	@rm -rf $(VENVNAME)

#Runs tests for TESTFILES
test: 
	@pytest $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"

#Prints out "manual" for makefile
help:
	@echo "make all/ make -- Creates virtual environment and installs all dependencies"
	@echo "make test -- Runs all tests"
	@echo "make doc -- Creates doxygen documentation into $(PATHTODOCDIR)"
	@echo "make rmdox -- Removes generated doxygen files"
	@echo "make run -- Runs the calculator application"
	@echo "make rmenv -- Deletes the virtual environment directory" 
	@echo "make clean -- Cleans temporary files and files not meant to be handed over"

#Removes temporary files and files not meant to be handed
clean:
	@rm -rf $(TOBECLEANED)
