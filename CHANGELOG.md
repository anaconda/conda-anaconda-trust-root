# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-30

### Added

- Initial publication of `conda-anaconda-trust-root`.
- Ship `1.root.json` as TUF root metadata v1 for conda signature verification bootstrap.
- Install metadata to `$PREFIX/etc/conda/1.root.json` for discovery by conda-content-trust (`av_data_dir`).
- Documented compatibility: use **conda-content-trust 0.3.0 or later** for signature verification that loads this trust root (conda plugin and migrated verification path).
- Conda recipe: `conda-content-trust >=0.3.0` run requirement so conda installs pull a compatible verifier.
- Python package `conda_anaconda_trust_root` with `__version__` from hatch-vcs.

[1.0.0]: https://github.com/anaconda/conda-anaconda-trust-root/releases/tag/v1.0.0
