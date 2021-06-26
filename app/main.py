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

## Show main window
def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())