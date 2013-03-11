.. 

django_hospital
======================

Quickstart
----------

To bootstrap the project::

    virtualenv django_hospital
    source django_hospital/bin/activate
    cd path/to/django_hospital/repository
    pip install -r requirements.pip
    pip install -e .
    cp django_hospital/settings/local.py.example django_hospital/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
