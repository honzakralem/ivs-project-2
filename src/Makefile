.PHONY: test clean

test:
	pytest mathlib_test.py && pytest infixtopost_test.py && echo "Test success" || echo "Test fail"

clean:
	rm -r __pycache__; rm -r .pytest_cache

