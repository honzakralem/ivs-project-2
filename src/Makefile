.PHONY: test clean
TESTFILES=src/infixtopost_test.py src/mathlib_test.py

test: 
	pytest $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"

clean:
	rm -r __pycache__; rm -r .pytest_cache

