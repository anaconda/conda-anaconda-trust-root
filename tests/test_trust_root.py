# Copyright (C) 2024 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
"""Tests for the trust root data files."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Path to the data file in the source tree
DATA_DIR = Path(__file__).parent.parent / "conda_anaconda_trust_root" / "data"
TESTDATA = Path(__file__).parent / "testdata"


@pytest.fixture
def trust_root():
    """Load the trust root from the data file."""
    with (DATA_DIR / "1.root.json").open() as f:
        return json.load(f)


# Trust root data file tests


def test_file_exists():
    """Test that the data file exists."""
    assert (DATA_DIR / "1.root.json").exists()


def test_is_valid_json():
    """Test that the data file is valid JSON."""
    with (DATA_DIR / "1.root.json").open() as f:
        data = json.load(f)
    assert isinstance(data, dict)


def test_has_signatures(trust_root):
    """Test that the trust root has signatures."""
    assert "signatures" in trust_root
    assert len(trust_root["signatures"]) >= 1


def test_has_signed_section(trust_root):
    """Test that the trust root has a signed section."""
    assert "signed" in trust_root


def test_signed_has_delegations(trust_root):
    """Test that the signed section has delegations."""
    signed = trust_root["signed"]
    assert "delegations" in signed


def test_delegations_has_key_mgr(trust_root):
    """Test that delegations include key_mgr."""
    delegations = trust_root["signed"]["delegations"]
    assert "key_mgr" in delegations
    assert "pubkeys" in delegations["key_mgr"]
    assert "threshold" in delegations["key_mgr"]
    assert delegations["key_mgr"]["threshold"] >= 1


def test_delegations_has_root(trust_root):
    """Test that delegations include root."""
    delegations = trust_root["signed"]["delegations"]
    assert "root" in delegations
    assert "pubkeys" in delegations["root"]
    assert "threshold" in delegations["root"]
    assert delegations["root"]["threshold"] >= 1


def test_signed_has_version(trust_root):
    """Test that the signed section has a version."""
    signed = trust_root["signed"]
    assert "version" in signed
    assert isinstance(signed["version"], int)
    assert signed["version"] >= 1


def test_signed_has_type(trust_root):
    """Test that the signed section has type 'root'."""
    signed = trust_root["signed"]
    assert "type" in signed
    assert signed["type"] == "root"


def test_signed_has_metadata_spec_version(trust_root):
    """Test that the signed section has a metadata spec version."""
    signed = trust_root["signed"]
    assert "metadata_spec_version" in signed


def test_signed_has_expiration(trust_root):
    """Test that the signed section has an expiration."""
    signed = trust_root["signed"]
    assert "expiration" in signed


def test_signed_has_timestamp(trust_root):
    """Test that the signed section has a timestamp."""
    signed = trust_root["signed"]
    assert "timestamp" in signed


def test_pubkeys_are_valid_hex(trust_root):
    """Test that all public keys are valid 64-character hex strings."""
    delegations = trust_root["signed"]["delegations"]

    for role_name, role_data in delegations.items():
        for pubkey in role_data["pubkeys"]:
            assert len(pubkey) == 64, f"Key in {role_name} is not 64 chars"
            assert all(c in "0123456789abcdef" for c in pubkey), (
                f"Key in {role_name} is not valid hex"
            )


def test_signatures_are_valid_hex(trust_root):
    """Test that all signatures are valid hex strings."""
    for key_id, sig_data in trust_root["signatures"].items():
        assert len(key_id) == 64, "Signature key ID is not 64 chars"
        assert "signature" in sig_data
        sig = sig_data["signature"]
        assert len(sig) == 128, "Signature is not 128 chars (64 bytes)"
        assert all(c in "0123456789abcdef" for c in sig), "Signature is not valid hex"


# Trust root validation tests


def test_matches_testdata():
    """Test that the data file matches the test data file."""
    testdata_path = TESTDATA / "1.root.json"
    if testdata_path.exists():
        with testdata_path.open() as f:
            testdata_root = json.load(f)
        with (DATA_DIR / "1.root.json").open() as f:
            data_root = json.load(f)
        assert data_root == testdata_root
