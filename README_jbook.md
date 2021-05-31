## Using the Jupyter Book version of the [template generator](https://github.com/roadfoodr/6.419x_report_template)

#### 1) Install Jupyter Book

See the [docs](https://jupyterbook.org/intro.html#install-jupyter-book) for installation. 

This script has been tested with the following package versions:

```
> python --version
Python 3.7.9                                                                                  
                                                                                              
> jupyter-book --version
Jupyter Book: 0.10.0
MyST-NB: 0.11.1
Sphinx Book Theme: 0.0.39
MyST-Parser: 0.13.3
Jupyter-Cache: 0.4.2
NbClient: 0.5.3
```

**Note:** [On Windows in particular](https://jupyterbook.org/advanced/windows.html), [there may be conflicts](https://github.com/executablebooks/jupyter-book/issues/906) with `python >= 3.8`.  You may need to create a separate env that uses an earlier version of Python.

#### 2) Install configuration files

In a subdirectory, copy the full tree of configuration files under [`/report`](https://github.com/roadfoodr/6.419x_report_template/tree/main/report) of this repo.  These are also supplied as a [single zip file](https://github.com/roadfoodr/6.419x_report_template/blob/main/templates/report_config.zip) under [`/templates`](https://github.com/roadfoodr/6.419x_report_template/tree/main/templates).

- Edit `_config.yml`: `Title` and `Author` at top, values under `myst_substitutions` at bottom.
- Edit `_toc.yml` with the name of your notebook (no `.ipynb` extension).
- If there are errors at build time, you may need to edit `requirements.txt` to add needed packages.

#### 3) Install the Jupyter Book-formatted notebook 

Build a notebook from the [template script](https://github.com/roadfoodr/6.419x_report_template/blob/main/build_HW_report_template.py) (edit the top of the script to set `TEMPLATE_STYLE = 'jbook'`), or copy a pre-built `*_jbook.ipynb` notebook from [`/templates`](https://github.com/roadfoodr/6.419x_report_template/tree/main/templates).  Place this notebook in the top level of the subdirectory you created in step 2.

#### 4) Edit the notebook

Edit and run code cells normally to produce your report, but with enhanced Jupyter Book features available.  See a list of these [especially useful features](#especially-useful-features) below.

#### 5) Build the book

To create the rendered version of the Jupyter Book, from the top level of the subdirectory (from step 2) where the notebook is located:  
`jupyter-book build .\<report_notebook_name>.ipynb`

HTML page will be created under `_build`.  To convert to PDF, use your system/printer driver "Print to..." features.

**Note:** the formatting for the "printed" PDF is intentionally different from the browser css.  You can preview this within the browser, without actually printing, as described [here](https://developer.chrome.com/docs/devtools/css/print-preview/).

It should also be possible to [build directly to PDF](https://jupyterbook.org/advanced/pdf.html) via `pyppeteer` or LaTeX, but I haven't succeeded with this in Windows.

### Especially useful features

1. By adding particular [cell tags](https://jupyterbook.org/content/metadata.html#adding-tags-using-notebook-interfaces), You can selectively [remove code cells](https://jupyterbook.org/interactive/hiding.html#removing-code-cell-content) to display only the output (e.g. plots), or suppress intermediate code cells entirely from the rendered HTML.
1. You can specify that particular cells (e.g. code annotations) will [display in sidebars or margins](https://jupyterbook.org/content/layout.html#sidebar-content).
1. You can [insert code outputs into page content](https://jupyterbook.org/content/code-outputs.html?highlight=glue#insert-code-outputs-into-page-content).  Thus, you can reference results from code in a narrative markdown cell, and when you redo or update code that yields different results, the value within the markdown cell will update automatically.
1. [Bibiliographic citations](https://jupyterbook.org/tutorials/references.html#create-a-bibtex-file) are a snap.  Edit `references.bib` in the report configuration subdirectory and [add a citation](https://jupyterbook.org/tutorials/references.html#add-a-citation) within your markdown.
   - To render the bibliography, [place the following](https://jupyterbook.org/content/citations.html?highlight=docname%20docnames#local-bibliographies) in a markdown cell at the end of your notebook:
   ```
       ```{bibliography}
       :filter: docname in docnames
       ```  
   ```
   - **Tip:** You can find pre-formatted bibtex listings that you can cut and paste into your `references.bib` file.  Here is [one search engine](http://bibtexsearch.com) for these listings.
