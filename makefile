.PHONY: venv rmenv clean all test doc help run rmdox profile

#CONFIGURATION
VENVNAME=env
REQUIREMENTSPATH=src/requirements.txt
PYTHON=python3
TESTFILES=src/infixtopost_test.py src/mathlib_test.py
PATHTODOXYFILE=src/Doxyfile
PATHTODOCDIR=src/doc
INPUTDIR=inputs
PROFILEDIR=profiling
TOBECLEANED=.pytest_cache src/.pytest_cache __pycache__ src/__pycache__ inputs

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


#Runs profiler with generated inputs, creates outputs
profile:
	@mkdir -p $(PROFILEDIR)
	@mkdir -p $(INPUTDIR)

	@$(PYTHON) src/generate.py 10 > $(INPUTDIR)/input10.txt
	@$(PYTHON) src/generate.py 1000 > $(INPUTDIR)/input1000.txt
	@$(PYTHON) src/generate.py 1000000 > $(INPUTDIR)/input1000000.txt

	@$(PYTHON) src/profiling.py < $(INPUTDIR)/input10.txt
	@mv stats.prof $(PROFILEDIR)/profile_10.prof

	@$(PYTHON) src/profiling.py < $(INPUTDIR)/input1000.txt
	@mv stats.prof $(PROFILEDIR)/profile_1000.prof

	@$(PYTHON) src/profiling.py < $(INPUTDIR)/input1000000.txt
	@mv stats.prof $(PROFILEDIR)/profile_1000000.prof

	@echo "Profiling completed."

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
	@echo "make generate -- Generates profiling input files"
	@echo "make profile -- Generates inputs and runs profiling"
	@echo "make clean -- Cleans temporary files and files not meant to be handed over"

#Removes temporary files and files not meant to be handed
clean:
	@rm -rf $(TOBECLEANED)
	@rm -f $(PROFILEDIR)/*
