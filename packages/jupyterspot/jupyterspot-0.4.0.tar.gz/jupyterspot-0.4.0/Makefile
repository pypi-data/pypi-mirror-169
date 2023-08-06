VERSION ?= 0.3.0

# mamba create -n jspot-ext python=3.9 -y
install:
 	mamba install -c conda-forge jupyterlab==3.0 nodejs
	pip install -e .
	jupyter labextension develop . --overwrite

bump:
	hatch version $(VERSION)
	# also edit package.json

publish:
	python -m build
	twine upload dist/*

	jlpm build
	npm publish --access public