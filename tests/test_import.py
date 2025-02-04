# test the point cloud classes
import importlib

import pytest


class TestImport:
    def test_install(self):
        quickshift = importlib.import_module("quickshift")
        assert quickshift is not None
