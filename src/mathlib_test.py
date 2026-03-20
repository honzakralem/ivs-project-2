#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file mathlib_test.py
# @brief Math library Tests for IVS calculator 2026
# @date 12.3.2026
# @author: Ha Pham <xphamha00> Kristian Duzek <xduzekk00>
#
# Implemenation of tests for calculator library
############################################################################

from mathlib import *
import pytest 

##
#@test Tests addition function
#
def test_add():
    assert add(0,0) == 0
    assert add(0,5) == 5
    assert add(-1,-1) == -2
    assert add(-4, 2) == -2
    assert add(0.1,0.2) == pytest.approx(0.3)
    assert add(-0.1, 0.2) == pytest.approx(0.1)
    assert add(532169, 2350789) == 2882958

##
#@test Tests division function
#
def test_div():
    with pytest.raises(ZeroDivisionError):
        div(1,0)
    assert div(0,1) == 0
    assert div(1, 0.2) == 5
    assert div(5,-1) == -5
    assert div(-5,1) == -5
    assert div(-30, -5) == 6
    assert div(50,50) == 1
    assert div(50,-50) == -1

##
#@test Tests subtraction function
#
def test_sub():
    assert sub(0,0) == 0
    assert sub(-5,0) == -5
    assert sub(-10,-5) == -5
    assert sub(-10, 5) == -15
    assert sub(4,-2) == 6
    assert sub(8,4) == 4
    assert sub(0,3) == -3
    assert sub(-1000000000000000000000000,1) == -1000000000000000000000001
    assert sub(-1000000000000000000000000,-1000000000000000000000000) == 0

##
#@test Tests multiplication function
#
def test_mul():
    assert mul(2,2) == 4
    assert mul(0,0) == 0
    assert mul(0,1) == 0
    assert mul(1,0) == 0
    assert mul(10000000000000000000,0) == 0
    assert mul(10000000000000000000,1) == 10000000000000000000
    assert mul(-1, -10) == 10
    assert mul(20, -10) == -200
    assert mul(0.1, 0.1) == pytest.approx(0.01)
    assert mul(-0.2, 0.4) == pytest.approx(-0.08)