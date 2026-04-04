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
                             QPushButton, QMessageBox, QAction, QLabel)
from PyQt5.QtCore import Qt

# Import infix to post logic from infixtopost.py
from infixtopost import InfixToPostFix, eval_postfix

## template for testing PyInstaller
class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('IVS Calculator 2026 - Test')
        self.resize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        test_label = QLabel("test")
        test_label.setAlignment(Qt.AlignCenter)
        test_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(test_label)

def main():
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
##
#TODO GUI