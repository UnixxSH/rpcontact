#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Project: rpcontact
# Description: provides application
# Author: UnixSH
# app/main.py
###

## Modules
import sys
from PyQt5.QtWidgets import QApplication
from .views import Window
from .database import createConnection

## Show main window
def main():
    ## Create application
    app = QApplication(sys.argv)
    ## Initilize database connection
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    ## Create window
    win = Window()
    win.show()
    ## Run event loop
    sys.exit(app.exec())