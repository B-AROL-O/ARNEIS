# HOWTO Configure arneis.readthedocs.io

<https://arneis.readthedocs.io/>

## Step-by-step instructions

### Create a feature branch

Logged as gmacario@gmpowerhorse

```bash
cd ~/github/B-AROL-O/ARNEIS/
git checkout main
git pull --all --prune
```

Create a feature branch

```bash
git checkout -b feat/issue-29-readthedocs
```

### Create initial Sphinx configuration

Follow instructions at <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>

Create initial Sphinx configuration

```bash
cd docs
python3 -m venv .venv
source .venv/bin/activate
pip3 install sphinx
sphinx-quickstart
```

Fill in the required information:

```text
(.venv) gmacario@gmpowerhorse:~/github/B-AROL-O/ARNEIS/docs (feat/issue-29-readthedocs)$ sphinx-quickstart 
Welcome to the Sphinx 4.4.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: 

The project name will occur in several places in the built documentation.
> Project name: ARNEIS
> Author name(s): The B-AROL-O Team
> Project release []: 

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]:  

Creating file /home/gmacario/github/B-AROL-O/ARNEIS/docs/conf.py.
Creating file /home/gmacario/github/B-AROL-O/ARNEIS/docs/index.rst.
Creating file /home/gmacario/github/B-AROL-O/ARNEIS/docs/Makefile.
Creating file /home/gmacario/github/B-AROL-O/ARNEIS/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /home/gmacario/github/B-AROL-O/ARNEIS/docs/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

(.venv) gmacario@gmpowerhorse:~/github/B-AROL-O/ARNEIS/docs (feat/issue-29-readthedocs)*$
```

### Locally build the static HTML site

Run the following command:

```bash
make html
```

Result:

```text
(.venv) gmacario@gmpowerhorse:~/github/B-AROL-O/ARNEIS/docs (feat/issue-29-readthedocs)*$ make html
Running Sphinx v4.4.0
making output directory... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: [new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index                  
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index                   
generating indices... genindex done
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded.

The HTML pages are in _build/html.
(.venv) gmacario@gmpowerhorse:~/github/B-AROL-O/ARNEIS/docs (feat/issue-29-readthedocs)*$
```

#### Test the generated website

Run a webserver to verify the generated site from another host in the network:

```bash
cd ~/github/B-AROL-O/ARNEIS/docs/
python3 -m http.server --directory _build/html/
```

then open <http://localhost:8000/> from your browser

### Adding support for Markdown

Reference: <https://www.sphinx-doc.org/en/master/usage/markdown.html>

```bash
cd ~/github/B-AROL-O/ARNEIS/docs
pip3 install --upgrade myst-parser
```

Add _myst_parser_ to the [list of configured extensions](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions)

```python
extensions = [
    'myst_parser'
]
```

TODO

Test: Open <https://arneis.readthedocs.io/>

TODO

<!-- EOF -->
