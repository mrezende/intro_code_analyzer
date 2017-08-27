#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `code_analyzer` class."""

import pytest


from intro_code_analyzer import code_analyzer


@pytest.fixture
def function_call_code():
    return "print('hello world')"


def test_number_of_calls(function_call_code):

    code_analyzer = CodeAnalyzer()
    assert code_analyzer.number_of_calls() == 1
    
