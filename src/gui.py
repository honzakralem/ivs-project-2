#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# @file gui.py
# @brief GUI for INTERCALCULATOR
# @date 3.4.2026
# @author Michal Holesa <xholesm00> Adrian Stanik <xstania00>
#
# Graphical user interface implementation using PyQt5.
############################################################################

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QGridLayout, QTextEdit, 
                             QPushButton, QMessageBox, QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor

from infixtopost import InfixToPostFix, eval_postfix


##
#@brief Main window class for the INTERCALCULATOR application.
# Inherits from QMainWindow to provide a standard application window frame.
#
class CalculatorGUI(QMainWindow):

    ##
    #@brief Initializes the main calculator window, setting its title and size.
    #@return None
    #@param self instance reference
    #
    def __init__(self):
        super().__init__()
        self.setWindowTitle("INTERCALCULATOR")
        self.setFixedSize(600, 750)
        self.initUI()

    ##
    #@brief Constructs the user interface.
    #@return None
    #@param self instance reference
    #
    def initUI(self):
        menubar = self.menuBar()

        help_action = QAction('Guide', self)
        menubar.addAction(help_action)

        info_action = QAction('About', self)
        menubar.addAction(info_action)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.display = QTextEdit()
        self.display.setFixedHeight(100)
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Arial", 28))
        self.display.setLineWrapMode(QTextEdit.NoWrap)
        
        self.display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.display.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.display.setAlignment(Qt.AlignRight)
        
        self.layout.addWidget(self.display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorGUI()
    window.show()
    sys.exit(app.exec_())