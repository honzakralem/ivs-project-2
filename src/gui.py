#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file gui.py
# @brief GUI for IVS calculator 2026
# @date 3.4.2026
# @author:Michal Holesa <xholesm00> Adrian Stanik <xstania00>
#
# Graphical user interface implementation
############################################################################

import sys
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QGridLayout, QLineEdit, 
                             QPushButton, QMessageBox, QAction)
from PyQt5.QtCore import Qt

# Import infix to post logic from infixtopost.py
from infixtopost import InfixToPostFix, eval_postfix

#TODO GUI