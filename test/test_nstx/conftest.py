"""
pytest fixtures.
"""

import pytest
import fdp

@pytest.fixture(scope="module")
def setup_nstx():
    return fdp.nstx()

@pytest.fixture(scope="module")
def setup_shot(setup_nstx):
    nstx = setup_nstx
    return nstx.s141000

@pytest.fixture(scope="module")
def setup_bes(setup_shot):
    shot = setup_shot
    return shot.bes