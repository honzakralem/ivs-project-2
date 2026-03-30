#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file mathlib.py
# @brief Math library for IVS calculator 2026
# @date 12.3.2026
# @author: Ha Pham <xphamha00> Kristian Duzek <xduzekk00>
#
# Implemenation of calculator functions
############################################################################

import math

##
#@brief Adds two numbers
#@return Sum of two numbers provided
#@param a addend
#@param b addend
#
def add(a,b):
    return a+b

##
#@brief Subtracts two numbers
#@return Subtraction of two numbers provided
#@param a minuend
#@param b subtrahend
#
def sub(a,b):
    return a-b

##
#@brief Multiplies two numbers
#@return Multiplication of two numbers provided
#@param a multiplicant
#@param b multiplier
#
def mul(a,b):
    return a*b

##
#@brief Divides two numbers
#@return Division of two numbers provided
#@param a numerator
#@param b denominator
#@exception ZeroDivisionError in case b == 0
#
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b
    
##
#@brief Calculates power
#@return Power of the base to the exponent
#@param a base
#@param b exponent
#
def pow(a,b):
    return math.pow(a,b)

##
# @brief      Calculates the root of a number
# @param      a the base of the root
# @param      b the base of the root
# @exception  ValueError if the base is negative
# @return     Root of base
def sqt(a,b):
    pass

##
# @brief      Calculates factorial of a non-negative integer
# @param      n the input number (non-negative integer)
# @exception  ValueError if n is negative
# @exception  TypeError if n is not an integer
# @return     Factorial of n
def fac(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return math.factorial(n)