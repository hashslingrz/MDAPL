book = book
build_folder = $(book)/_build
html_build_folder = $(build_folder)/html
latex_build_folder = $(build_folder)/latex

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
	jb build $(book)

build_latex:
	jb build $(book) --builder latex
	python scripts/tex_postprocess.py
	echo "NOTICE: The tex file needs to be compiled!"

publish_html:
	ghp-import -npf $(html_build_folder)
