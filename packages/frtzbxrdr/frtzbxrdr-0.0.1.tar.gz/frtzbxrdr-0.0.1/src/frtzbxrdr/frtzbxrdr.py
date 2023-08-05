"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = frtzbxrdr.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys

from frtzbxrdr import __version__
from frtzbxrdr import Monitor

__author__ = "Daniel Ewert"
__copyright__ = "Daniel Ewert"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from frtzbxrdr.skeleton import fib`,
# when using this Python module as a library.


def monitor(user, password):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    m = Monitor(user, password)
    m.on_device_connected(lambda mac: _logger.info(f" Device {mac} connected!"))
    m.on_device_disconnected(lambda mac: _logger.info(f" Device {mac} disconnected!"))
    m.run_forever(5)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="frtzbxrdr {ver}".format(ver=__version__),
    )
    parser.add_argument(dest="user", help="fritzbox user name",
                        type=str, metavar="USER")
    parser.add_argument(dest="password", help="fritzbox password",
                        type=str, metavar="PASSWORD")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="output debug info",
        action="store_const",
        const=logging.DEBUG,
        default=logging.INFO
    )

    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)

    setup_logging(args.loglevel)
    _logger.info("Starting monitoring...")
    monitor(args.user, args.password)


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
