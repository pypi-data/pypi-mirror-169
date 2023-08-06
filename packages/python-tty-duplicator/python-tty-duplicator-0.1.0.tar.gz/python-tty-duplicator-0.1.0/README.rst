=====================
python-tty-duplicator
=====================

.. image:: https://img.shields.io/pypi/v/python-tty-duplicator.svg
    :target: https://pypi.org/project/python-tty-duplicator
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/python-tty-duplicator.svg
    :target: https://pypi.org/project/python-tty-duplicator
    :alt: Python versions

.. image:: https://ci.appveyor.com/api/projects/status/github/Salamandar/python-tty-duplicator?branch=master
    :target: https://ci.appveyor.com/project/Salamandar/python-tty-duplicator/branch/master
    :alt: See Build Status on AppVeyor

Utility that duplicates a serial port tty.

The main reason for using this tool is to log what is going through the tty.

Why create a "dummy" tty just to log ?
Well, a tty can only be read by ONE process. If two processes read the tty, each will read partial data from the tty.
Also, you can't read the data going *into* the tty this way.

So this utility reads / writes to the real TTY, bridges it to a dummy tty, and logs everything going via the dummy tty.

Requirements
------------

* Python >=3.6
* socat

Installation
------------

You can install "python-tty-duplicator" via pip from `PyPI`_::

    $ pip install python-tty-duplicator

Usage
-----

    from tty_duplicator import TTYDuplicator

    duplicator = TTYDuplicator("/dev/ttyUSB0", "serial_data.log")
    print(duplicator.fake_tty)

    duplicator.start()

    # Now you can interact with the "fake tty" and everything will be logged!
    # e.g use picocom, tio, or pyserial

    # Optional: will be called when python exits gracefully
    duplicator.stop()


License
-------

Distributed under the terms of the `MIT`_ license, "python-tty-duplicator" is free and open source software

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
