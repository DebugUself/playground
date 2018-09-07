#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.tools import *
import NAME


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN1")


def test_basic():
    print("I RAN!", end='')