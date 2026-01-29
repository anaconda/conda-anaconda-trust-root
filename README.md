# conda-anaconda-trust-root

Anaconda's initial trust root metadata for conda package signature verification.

## What is conda-anaconda-trust-root?

The `conda-anaconda-trust-root` package installs the initial trust root metadata files that [conda-content-trust](https://github.com/conda/conda-content-trust) uses for verifying package signatures. This trust root establishes the chain of trust for package metadata verification based on [The Update Framework (TUF)](https://theupdateframework.io/).

## How It Works

1. **Installation**: When this package is installed, it places `1.root.json` (and any subsequent root versions) into `$CONDA_PREFIX/etc/conda/`.

2. **Discovery**: When conda-content-trust performs signature verification, it looks for root metadata files in `$CONDA_PREFIX/etc/conda/` (the `av_data_dir`).

3. **Required**: Without this package (or another trust root provider), signature verification in conda-content-trust is disabled since no trust root is available.

4. **Updates**: Root metadata can be updated via normal TUF root rotation. This package can be updated via conda to distribute new root versions.

## Installation

This package is typically installed as a dependency or alongside conda-content-trust:

```bash
conda install conda-anaconda-trust-root
```

## Installed Files

After installation, the following files are placed in `$CONDA_PREFIX/etc/conda/`:

| File | Description |
|------|-------------|
| `1.root.json` | Initial root metadata (version 1) |

## Trust Root Structure

The trust root metadata follows the TUF specification and includes:

- **signatures**: Cryptographic signatures from root key holders
- **signed.delegations**: Key delegation information for root and key_mgr roles
- **signed.version**: Version number for root rotation
- **signed.expiration**: Metadata expiration timestamp
- **signed.metadata_spec_version**: TUF metadata specification version

## Security

The trust root metadata is cryptographically signed by multiple root key holders. Any changes to this package require:

1. Valid signatures from the threshold number of root key holders
2. Proper TUF root rotation if keys are being changed

## Testing

```bash
# Clone the repository
git clone https://github.com/anaconda/conda-anaconda-trust-root.git
cd conda-anaconda-trust-root

# Create development environment
conda create --name=catr-dev python=3.10
conda activate catr-dev
pip install -e .

# Run tests
pip install pytest pytest-cov
pytest --cov=conda_anaconda_trust_root
```

## History

Conda signature verification was developed by Anaconda to address supply chain security concerns in the Python/conda ecosystem.

### Timeline

- **2009**: [The Update Framework (TUF)](https://theupdateframework.io/) was originally developed as a solution to address widespread vulnerabilities in package managers.

- **May 2021**: Anaconda [announced conda signature verification](https://www.anaconda.com/blog/conda-signature-verification), releasing the initial implementation based on TUF. The feature was designed to preserve conda install integrity by verifying package artifacts and metadata against a chain of trust.

- **December 2021**: Anaconda [announced expanded community collaboration](https://www.anaconda.com/blog/paving-the-way-for-community-innovation-with-security-features-for-signed-packages), working with the Mamba and conda-forge teams to adopt trust and verification features. A mamba-compatible implementation was released.

- **March 2026**: The signature verification functionality was migrated from conda core to the [conda-content-trust](https://github.com/conda/conda-content-trust) plugin, with the trust root metadata distributed via this package (`conda-anaconda-trust-root`).

### Benefits

Conda signature verification defends against:

- Man-in-the-middle attacks
- Compromised mirrors or CDNs
- TLS misconfiguration
- Tampering with packages after they leave Anaconda's secure build network

## Related Projects

- [conda](https://github.com/conda/conda) - The package management system
- [conda-content-trust](https://github.com/conda/conda-content-trust) - Signing and verification tools for conda
- [The Update Framework (TUF)](https://theupdateframework.io/) - The security framework this is based on

## License

TBD
