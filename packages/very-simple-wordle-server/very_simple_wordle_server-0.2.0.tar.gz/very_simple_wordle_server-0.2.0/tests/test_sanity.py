"""
Some basic sanity checks.
"""

import pytest


# Small import test first...
def test_import():
    """Test that the package can be imported."""
    with pytest.raises(NameError):
        very_simple_wordle_server
    import very_simple_wordle_server
    very_simple_wordle_server


# ...then properly import package and run the rest of the sanity tests
import very_simple_wordle_server


def test_has_author():
    """Test that the package has an author."""
    very_simple_wordle_server.__author__


def test_has_email():
    """Test that an email address is associated with the package."""
    very_simple_wordle_server.__email__


def test_has_version():
    """Test that the package has a version."""
    very_simple_wordle_server.__version__
