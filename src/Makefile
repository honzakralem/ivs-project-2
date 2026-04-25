.PHONY: test profile clean generate
TESTFILES=src/infixtopost_test.py src/mathlib_test.py

test: 
	pytest $(TESTFILES) && echo "All tests have passed!" || echo "Tests did not pass!"

generate:
	mkdir -p inputs
	python src/generate.py 10 > inputs/input10.txt
	python src/generate.py 1000 > inputs/input1000.txt
	python src/generate.py 1000000 > inputs/input1e6.txt

profile:
	python src/profiling.py < inputs/input10.txt
	mv stats.prof profiling/profiler10.prof

	python src/profiling.py < inputs/input1000.txt
	mv stats.prof profiling/profiler1000.prof

	python src/profiling.py < inputs/input1e6.txt
	mv stats.prof profiling/profiler1e6.prof

clean:
	rm -r __pycache__; rm -r .pytest_cache inputs 
	rm -f profiling/*

rmdox:
	rm -rf doc/html doc/latex