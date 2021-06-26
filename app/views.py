#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Project: rpcontact
# Description: provides views to manage contacts in table
# Author: UnixSH
# app/views.py
###

## Modules
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

## Define main window
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)