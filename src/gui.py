#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file gui.py
# @brief GUI for INTERCALCULATOR
# @date 3.4.2026
# @author Michal Holesa <xholesm00> Adrian Stanik <xstania00>
#
# Graphical user interface implementation
############################################################################

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QGridLayout, QTextEdit, 
                             QPushButton, QMessageBox, QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor

from infixtopost import InfixToPostFix, eval_postfix

#TODO GUI