.PHONY: venv rmenv clean all test doc help run rmdox stddev pack

#DETECT OS
ifeq ($(OS),Windows_NT)
    SEP := $(strip \ )
    RM := del /f /q
    RMDIR := rd /s /q
    MV := move
    MKDIR := mkdir
    PYTHON := python
else
    SEP := /
    RM := rm -f
    RMDIR := rm -rf
    MV := mv
    MKDIR := mkdir -p
    PYTHON := python3
endif

#CONFIGURATION
VENVNAME=env
REQUIREMENTSPATH=src$(SEP)requirements.txt
TESTFILES=src$(SEP)infixtopost_test.py src$(SEP)mathlib_test.py
PATHTODOXYFILE=src$(SEP)Doxyfile
PATHTODOCDIR=src$(SEP)doc
INPUTDIR=inputs
PROFILEDIR=profiling
ZIPNAME=xphamha00_xduzekk00_xholesm00_xstania00.zip
FILETOBEZIPPED=src mockup plan profiling makefile README.md stddev LICENSE VERSION install.sh ubuntu_dependencies.txt src$(SEP)requirements.txt 
SETUPSCRIPT=src$(SEP)setup.py
RUNSCRIPT=src$(SEP)gui.py
PROFILINGSCRIPT=profiling.py
TESTFRAMEWORK=pytest

#Creates virtual environment and downloads all dependencies
all: 
	@$(PYTHON) $(SETUPSCRIPT)

#Creates doxygen documentation into PATHTODOCDIR
doc:
	@doxygen $(PATHTODOXYFILE)

#Removes doxygen documentation from PATHTODOCDIR
rmdox:
	-@$(RMDIR) $(PATHTODOCDIR)$(SEP)html 
	-@$(RMDIR) $(PATHTODOCDIR)$(SEP)latex

#Launches the calculator	
run:
	@$(PYTHON) $(RUNSCRIPT)

#Removes virtual environment
rmenv:
	-@$(RMDIR) $(VENVNAME)

#Runs profiler with generated inputs, creates outputs
stddev:
	-@$(RMDIR) $(INPUTDIR)
	-@$(MKDIR) $(INPUTDIR)
	-@$(RMDIR) $(PROFILEDIR)
	-@$(MKDIR) $(PROFILEDIR)

	@$(PYTHON) src$(SEP)generate.py 10 > $(INPUTDIR)$(SEP)input10.txt
	@$(PYTHON) src$(SEP)generate.py 1000 > $(INPUTDIR)$(SEP)input1000.txt
	@$(PYTHON) src$(SEP)generate.py 1000000 > $(INPUTDIR)$(SEP)input1000000.txt

	@$(PYTHON) src$(SEP)$(PROFILINGSCRIPT) < $(INPUTDIR)$(SEP)input10.txt
	@$(MV) stats.prof $(PROFILEDIR)$(SEP)profile_10.prof

	@$(PYTHON) src$(SEP)$(PROFILINGSCRIPT) < $(INPUTDIR)$(SEP)input1000.txt
	@$(MV) stats.prof $(PROFILEDIR)$(SEP)profile_1000.prof

	@$(PYTHON) src$(SEP)$(PROFILINGSCRIPT) < $(INPUTDIR)$(SEP)input1000000.txt
	@$(MV) stats.prof $(PROFILEDIR)$(SEP)profile_1000000.prof

	@echo "Profiling completed."

#Runs tests for TESTFILES
test: 
	@$(TESTFRAMEWORK) $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"

#Prints out "manual" for makefile
help:
	@echo "make all / make -- Creates virtual environment and installs all dependencies"
	@echo "make test -- Runs all tests"
	@echo "make doc -- Creates doxygen documentation into $(PATHTODOCDIR)"
	@echo "make rmdox -- Removes generated doxygen files"
	@echo "make run -- Runs the calculator application"
	@echo "make rmenv -- Deletes the virtual environment directory"
	@echo "make generate -- Generates profiling input files"
	@echo "make stddev -- Generates inputs and runs profiling"
	@echo "make clean -- Cleans temporary files and files not meant to be handed over"
	@echo "make pack -- Packs the projects into a zip archive"

# Archives project - clean before
pack: clean 
	@zip $(ZIPNAME) $(FILETOBEZIPPED)

#Removes temporary files and files not meant to be handed
clean: rmdox rmenv
	-@$(RMDIR) .pytest_cache
	-@$(RMDIR) src$(SEP).pytest_cache
	-@$(RMDIR) __pycache__
	-@$(RMDIR) src$(SEP)__pycache__
	-@$(RMDIR) $(INPUTDIR)
	-@$(RMDIR) $(INPUTDIR)
	-@$(RMDIR) $(PROFILEDIR)

