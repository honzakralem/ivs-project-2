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
                             QPushButton, QMessageBox, QAction, QShortcut)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor, QKeySequence

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
        help_action.triggered.connect(self.show_help)
        menubar.addAction(help_action)

        info_action = QAction('About', self)
        info_action.triggered.connect(self.show_info)
        menubar.addAction(info_action)

        controls_action = QAction('Controls', self)
        controls_action.triggered.connect(self.show_controls)
        menubar.addAction(controls_action)

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
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.layout.addLayout(self.grid)

        buttons = {
            'C': (0, 0), 'DEL': (0, 1), '(': (0, 2), ')': (0, 3), 'sqrt': (0, 4),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3), 'ln': (1, 4),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3), 'fac': (2, 4),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3), '^': (3, 4),
            '0': (4, 0), '.': (4, 1), '=': (4, 2), '+': (4, 3), '%': (4, 4),
        }

        for btn_text, pos in buttons.items():
            btn = QPushButton(btn_text)
            btn.setFixedSize(105, 95)
            btn.setFont(QFont("Arial", 22))
            
            if btn_text in ['C', 'DEL']:
                btn.setProperty("btnClass", "control")
            elif btn_text in ['+', '-', '*', '/', '%', '^', 'sqrt', 'ln', 'fac', '=', '(', ')']:
                btn.setProperty("btnClass", "operator")
            else:
                btn.setProperty("btnClass", "number")

            btn.clicked.connect(lambda checked, t=btn_text: self.on_button_click(t))

            self.grid.addWidget(btn, pos[0], pos[1])

        self.setStyleSheet("""
            QMainWindow, QWidget { background-color: #f2f2f2; color: #111; }
                           
            QPushButton { border-radius: 8px; border: 2px solid #ccc; }
            QPushButton[btnClass="number"] { background-color: #ffffff; }
            QPushButton[btnClass="number"]:pressed { background-color: #e0e0e0; }
                           
            QPushButton[btnClass="operator"] { background-color: #d6eaf8; }
            QPushButton[btnClass="operator"]:pressed { background-color: #aed6f1; }
                           
            QPushButton[btnClass="control"] { background-color: #fadbd8; }
            QPushButton[btnClass="control"]:pressed { background-color: #f5b7b1; }
                           
            QTextEdit { background-color: #fff; border: 3px solid #ccc; border-radius: 8px; padding: 10px; }
            QScrollBar:horizontal { height: 12px; background-color: #f0f0f0; }
        """)

        self.setup_shortcuts()

    ##
    #@brief Binds keyboard keys to calculator functions.
    #@return None
    #@param self instance reference
    #
    def setup_shortcuts(self):
        for key in '0123456789.+-*/%^()':
            shortcut = QShortcut(QKeySequence(key), self)
            shortcut.activated.connect(lambda k=key: self.on_button_click(k))
        
        special_keys = {
            Qt.Key_Comma: '.',
            Qt.Key_Exclam: 'fac',
            Qt.Key_S: 'sqrt',
            Qt.Key_L: 'ln',
            Qt.Key_Enter: '=',
            Qt.Key_Return: '=',
            Qt.Key_Backspace: 'DEL',
            Qt.Key_Escape: 'C',
            Qt.Key_Delete: 'C'
        }
        
        for key, action in special_keys.items():
            shortcut = QShortcut(QKeySequence(key), self)
            shortcut.activated.connect(lambda a=action: self.on_button_click(a))

    ##
    #@brief Updates the display text and ensures the cursor remains at the end.
    #@return None
    #@param self instance reference
    #@param text The string to output to the calculator display
    #
    def update_display(self, text):
        self.display.setText(text)
        self.display.setAlignment(Qt.AlignRight)
    
        cursor = self.display.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.display.setTextCursor(cursor)

    ##
    #@brief Displays a pop-up dialog box with instructions on how to use the calculator.
    #@return None
    #@param self instance reference
    #
    def show_help(self):
        text = (
            "Simple guide:\n\n"
            "- Enter the mathematical expression conventionally (infix).\n"
            "- Single-operand operations (fac, ln): Enter the number first, then the operator. (e.g., '5 fac')\n"
            "- Root operation (sqrt): Behaves like a binary operator, enter in the format 'base sqrt degree'.\n"
            "- 'C' clears the entire display, 'DEL' deletes the last character.\n"
            "- After pressing '=', the expression is evaluated."
        )
        QMessageBox.information(self, "Guide", text)

    ##
    #@brief Displays a pop-up dialog box containing application version and author information.
    #@return None
    #@param self instance reference
    #
    def show_info(self):
        text = (
            "INTERCALCULATOR\n\n"
            "Version: 1.0.0\n"
            "\n"
            "Authors:\n"
            "• Ha Pham <xphamha00>\n"
            "• Kristian Duzek <xduzekk00>\n"
            "• Michal Holesa <xholesm00>\n"
            "• Adrian Stanik <xstania00>\n"
            )
        QMessageBox.information(self, "About", text)

    ##
    #@brief Displays a pop-up dialog box listing the keyboard shortcuts.
    #@return None
    #@param self instance reference
    #
    def show_controls(self):
        text = (
            "Keyboard Shortcuts:\n\n"
            "• 0-9, +, -, *, /, %, ^, (, ) : Standard input\n"
            "• . or , (Comma) : Decimal point\n"
            "• ! (Exclamation) : Factorial (fac)\n"
            "• S : Square root (sqrt)\n"
            "• L : Natural logarithm (ln)\n"
            "• Enter or Return : Evaluate (=)\n"
            "• Backspace : Delete last character (DEL)\n"
            "• Escape or Delete : Clear entire display (C)\n"
        )
        QMessageBox.information(self, "Controls", text)

    ##
    #@brief Handles button click events, updating the display or triggering evaluation.
    #@return None
    #@param self instance reference
    #@param text The label of the button that was clicked
    #
    def on_button_click(self, text):
        curr = self.display.toPlainText()

        if text == 'C':
            self.display.clear()
        
        elif text == 'DEL':
            stripped = curr.rstrip()
            if stripped.endswith('sqrt'):
                self.update_display(stripped[:-4].rstrip())
            elif stripped.endswith('fac'):
                self.update_display(stripped[:-3].rstrip())
            elif stripped.endswith('ln'):
                self.update_display(stripped[:-2].rstrip())
            else:
                self.update_display(stripped[:-1].rstrip())
        
        elif text == '=':
            if not curr.strip():
                return
            
            try:
                eval_string = curr.replace('sqrt', 'sqt')
                postfix = InfixToPostFix(eval_string)
                res = eval_postfix(postfix)
                
                if res == int(res):
                    res = int(res)
                else:
                    res = round(res, 10)
                    
                self.update_display(str(res))
            
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Invalid expression:\n{e}")
                self.display.clear()
        
        else:
            ops = ['+', '-', '*', '/', '%', '^', 'sqrt', 'ln', 'fac', '(', ')']
            
            if text in ops:
                if curr and not curr.endswith(' '):
                    self.update_display(curr + f" {text} ")
                else:
                    self.update_display(curr + f"{text} ")
            else:
                self.update_display(curr + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorGUI()
    window.show()
    sys.exit(app.exec_())