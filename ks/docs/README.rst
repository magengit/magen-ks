Key Service Sphinx Documentation Instructions
=============================================

1. Original commands to generate this directory using ``sphinx-quickstart``,
   including creating ``.keep`` files for git commit.
   - Note the important of ``-q`` to keep ``sphinx-quickstart`` from asking its interactive questions even though command line options have been specified.

.. code:: bash

    bash$ cd magen-ks/ks
    bash$ sphinx-quickstart -q \
	    --project="Magen Key Service" \
	    --author=RP \
	    -v 1.3 \
	    --epub \
	    --ext-autodoc \
	    --ext-doctest \
	    --ext-todo \
	    --ext-coverage \
	    --ext-mathjax \
	    --ext-ifconfig \
	    --ext-viewcode \
	    --makefile \
	    --batchfile \
	    --templatedir=_ \
	    ./docs
    bash$ touch docs/_static/.keep docs/_template/.keep

Additionally, created this README

2. ``make doc_api`` step is intended to be done repeatedly, but only when module list changes. it is included in ``make doc`` target. ``make doc_api`` has to be implemented inside a component as it's very specific to the component structure. Other targets can be inherited from `magen-helper <https://github.com/magengit/magen-helper>`_ repo.
   
.. code:: bash

    bash$ cd magen-ks/ks
        bash$ make doc_api

3. ``make doc`` step is done repeatedly whenever html documentation should be generated.

.. code:: bash

    bash$ cd magen-ks/ks
        bash$ make doc
