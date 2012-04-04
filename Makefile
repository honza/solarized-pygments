all:
	make js
js:
	pygmentize -f html -O full -O style=solarized -o _build/javascript.html reference/javascript.js

clean:
	rm -rf _build
