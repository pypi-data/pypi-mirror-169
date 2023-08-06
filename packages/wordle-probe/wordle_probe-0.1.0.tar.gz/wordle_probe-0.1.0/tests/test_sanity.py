"""
Some basic sanity checks.
"""

import pytest


# Small import test first...
def test_import():
    """Test that the package can be imported."""
    with pytest.raises(NameError):
        wordle_probe
    import wordle_probe
    wordle_probe


# ...then properly import package and run the rest of the sanity tests
import wordle_probe


def test_has_author():
    """Test that the package has an author."""
    wordle_probe.__author__


def test_has_email():
    """Test that an email address is associated with the package."""
    wordle_probe.__email__


def test_has_version():
    """Test that the package has a version."""
    wordle_probe.__version__
