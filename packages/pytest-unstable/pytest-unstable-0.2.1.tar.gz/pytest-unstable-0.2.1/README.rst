===============
pytest-unstable
===============

.. image:: https://img.shields.io/pypi/v/pytest-unstable.svg
    :target: https://pypi.org/project/pytest-unstable
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-unstable.svg
    :target: https://pypi.org/project/pytest-unstable
    :alt: Python versions

.. image:: https://ci.appveyor.com/api/projects/status/github/Salamandar/pytest-unstable?branch=master
    :target: https://ci.appveyor.com/project/Salamandar/pytest-unstable/branch/master
    :alt: See Build Status on AppVeyor


Provides a test mark `@pytest.mark.unstable`.

If tests marked as unstable fail, Pytest will still return 0. Failures will still be present in the reports.

Requirements
------------

* Python >=3.6
* `Pytest`_

Installation
------------

You can install "pytest-unstable" via pip from `PyPI`_::

    $ pip install pytest-unstable

Usage
-----

* Mark tests as unstable `@pytest.mark.unstable`
* If those tests fail (and no other test), pytest will return 0
* Go read the reports to see the failures!

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-unstable" is free and open source software

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
