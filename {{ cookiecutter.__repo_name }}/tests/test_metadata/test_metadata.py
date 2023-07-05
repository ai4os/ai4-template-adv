"""Testing module for api metadata. This is a test file designed to use
pytest and prepared for some basic assertions and to add your own tests.

You can add new tests following the next structure:
```py
def test_{description for the test}(metadata):
    assert {statement with metadata that returns true or false}
```

The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `metadata` the value generated by
your function defined at `api.get_metadata`.
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_authors(metadata):
    """Tests that metadata provides authors information."""
    assert "authors" in metadata
    assert metadata["authors"] == ["{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>"]


def test_description(metadata):
    """Tests that metadata provides description information."""
    assert "description" in metadata
    assert metadata["description"] == "{{ cookiecutter.description }}"


def test_license(metadata):
    """Tests that metadata provides license information."""
    assert "license" in metadata
    assert metadata["license"] == "{{ cookiecutter.open_source_license }}"


def test_version(metadata):
    """Tests that metadata provides version information."""
    assert "version" in metadata
    assert isinstance(metadata["version"], str)
    assert all(v.isnumeric() for v in metadata["version"].split("."))
    assert len(metadata["version"].split(".")) == 3


def test_checkpoints(metadata):
    """Tests that metadata provides checkpoints information."""
    assert "checkpoints" in metadata
    assert metadata["checkpoints"] == []  # TODO: Add your test checkpoints


def test_datasets(metadata):
    """Tests that metadata provides datasets information."""
    assert "datasets" in metadata
    assert metadata["datasets"] == []  # TODO: Add your test checkpoints
