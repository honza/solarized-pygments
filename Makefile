all:
	make js
	make python
js:
	pygmentize -f html -O full -O style=solarized -o _build/javascript.html reference/javascript.js
python:
	pygmentize -f html -O full -O style=solarized -o _build/python.html reference/python.py

clean:
	rm -rf _build
