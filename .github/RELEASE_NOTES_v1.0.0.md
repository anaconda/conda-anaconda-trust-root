## conda-anaconda-trust-root 1.0.0

First stable release of the Anaconda initial trust root metadata package for conda package signature verification.

### Added

- Initial publication of `conda-anaconda-trust-root`.
- Ship `1.root.json` as TUF root metadata v1 for conda signature verification bootstrap.
- Install metadata to `$PREFIX/etc/conda/1.root.json` for discovery by conda-content-trust (`av_data_dir`).
- Python package `conda_anaconda_trust_root` with `__version__` from hatch-vcs.
- Licensed under BSD 3-Clause.

### Compatibility

Use **conda-content-trust 0.3.0 or later** for signature verification that loads this trust root from `av_data_dir` (conda plugin and migrated verification stack).

### Links

- [CHANGELOG](https://github.com/anaconda/conda-anaconda-trust-root/blob/main/CHANGELOG.md)
- [LICENSE](https://github.com/anaconda/conda-anaconda-trust-root/blob/main/LICENSE)
