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
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

## Define main window
class Window(QMainWindow):
    ## Show main window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RPcontact")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        ## Call for window setup
        self.setupUI()
    ## Window items setup
    def setupUI(self):
        # Create table view widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)