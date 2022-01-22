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

Run a simple http server to make the generated pages available on the network:

```bash
cd ~/github/B-AROL-O/ARNEIS/docs/
python3 -m http.server --directory _build/html/
```

then open <http://localhost:8000/> from your browser. You should see the home page of the generated website:

![2022-01-22-0744-initial-docsite.png](../images/2022-01-22-0744-initial-docsite.png)

All the http requests will also be logged on the terminal where you launched the http server:

```text
(.venv) gmacario@gmpowerhorse:~/github/B-AROL-O/ARNEIS/docs (feat/docsite-add-links)*$ python3 -m http.server --directory _build/html/
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [22/Jan/2022 07:48:24] "GET / HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:24] "GET /_static/pygments.css HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:24] "GET /_static/css/theme.css HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:24] "GET /_static/documentation_options.js HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:24] "GET /_static/js/theme.js HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:25] "GET /_static/css/fonts/lato-normal.woff2?bd03a2cc277bbbc338d464e679fe9942 HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:25] "GET /_static/css/fonts/fontawesome-webfont.woff2?af7ae505a9eed503f8b8e6982036873e HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:25] "GET /_static/css/fonts/lato-bold.woff2?cccb897485813c7c256901dbca54ecf2 HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:25] "GET /_static/css/fonts/Roboto-Slab-Bold.woff2?9984f4a9bda09be08e83f2506954adbe HTTP/1.1" 304 -
127.0.0.1 - - [22/Jan/2022 07:48:32] "GET /genindex.html HTTP/1.1" 200 -
127.0.0.1 - - [22/Jan/2022 07:48:36] "GET /index.html HTTP/1.1" 200 -
```


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
