# Copyright (C) 2024 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
"""Anaconda's initial trust root metadata for conda package signature verification.

This package installs the initial trust root metadata files to
$CONDA_PREFIX/etc/conda/ where conda-content-trust can find them for
signature verification bootstrapping.

The installed files:
- 1.root.json: The initial root metadata (version 1)

These files can be updated via conda package updates, allowing Anaconda to
distribute trust root rotations independently of conda-content-trust releases.
"""

from __future__ import annotations

try:
    from ._version import __version__
except ImportError:
    # _version.py is only created after running `pip install`
    try:
        from setuptools_scm import get_version

        __version__ = get_version(root="..", relative_to=__file__)
    except (ImportError, OSError, LookupError):
        # ImportError: setuptools_scm isn't installed
        # OSError: git isn't installed
        # LookupError: setuptools_scm unable to detect version
        __version__ = "0.0.0.dev0+placeholder"
