#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pytropic` package."""


import tempfile
import unittest
import os
from pytropic import pytropic


class TestPytropic(unittest.TestCase):
    """Tests for `pytropic` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_sliding(self):
        assert list(pytropic.sliding("test", 2)) == ["te", "es", "st"]

    def test_read(self):
        m = pytropic.Model(2)
        cwd = os.path.dirname(os.path.realpath(__file__))
        p = os.path.join(cwd, "data", "google_books_2.tsv")
        with open(p) as f:
            m.read(f)
        assert m.entropy("fish") > 0

    def test_read_corpus(self):
        en = pytropic.Model(2, name="English sample")
        fr = pytropic.Model(2, name="French sample")
        cwd = os.path.dirname(os.path.realpath(__file__))
        en_path = os.path.join(cwd, "data", "bible-english-sample.txt")
        fr_path = os.path.join(cwd, "data", "bible-french-sample.txt")
        with open(en_path) as f:
            en.train(f)
        with open(fr_path) as f:
            fr.train(f)
        assert en.entropy("fish") < fr.entropy("fish")
        assert en.entropy("poisson") > fr.entropy("poisson")

    def test_read_write_json(self):
        fr = pytropic.Model(2, name="French sample")
        cwd = os.path.dirname(os.path.realpath(__file__))
        fr_path = os.path.join(cwd, "data", "bible-french-sample.txt")
        with open(fr_path) as f:
            fr.train(f)
        fr2 = pytropic.Model(2, name="Read French sample")
        tf = tempfile.mkstemp(text=True)[1]
        with open(tf, "w") as f:
            fr.dump_json(f)
        with open(tf) as f:
            fr2.read_json(f)
        assert fr.entropy("poisson") == fr2.entropy("poisson")

    def test_read_json(self):
        fr = pytropic.Model(2, name="French sample")
        cwd = os.path.dirname(os.path.realpath(__file__))
        fr_path = os.path.join(cwd, "data", "bible-french-sample.json")
        with open(fr_path) as f:
            fr.read_json(f)
        assert fr.entropy("poisson") < fr.entropy("fish")
