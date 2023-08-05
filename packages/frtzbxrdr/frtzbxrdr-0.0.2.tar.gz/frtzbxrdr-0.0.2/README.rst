

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=========
frtzbxrdr
=========


    Check your fritzbox to see who comes and goes in your WiFi network



Installation
============

.. code-block:: bash
    
    $ pip install frtzboxrdr

Usage in code
=============

.. code-block:: python

    from frtzboxrdr import Monitor

    m = Monitor(user, password)
    m.on_device_connected(lambda mac: print(f" Device {mac} connected!"))
    m.on_device_disconnected(lambda mac: print(f" Device {mac} disconnected!"))
    m.run_forever(5)


Usage as cli
============

.. code-block:: bash
    
    $ frtzboxrdr <user> <password>


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
