html: preprocess build_html publish_html

dbg_html: preprocess python_reqs preprocess build_html

latex: preprocess build_latex

python_reqs:
	pip3 install -e scripts/
	pip3 install -r scripts/requirements.txt

preprocess:
	python3 scripts/migrate_resources.py
	python3 scripts/preprocess.py

build_html:
	jb build book

build_latex:
	jb build book --builder latex

publish_html:
	ghp-import -npf book/_build/html
