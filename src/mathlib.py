#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file mathlib.py
# @brief Math library for IVS calculator 2026
# @date 12.3.2026
# @author: Ha Pham <xphamha00> Kristian Duzek <xduzekk00>
#
# Implemenation of tests for calculator library
############################################################################
import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b
def pow(a):
    return math.pow(a)
def sqt(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)