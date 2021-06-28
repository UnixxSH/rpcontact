#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Project: rpcontact
# Description: provides database connection model
# Author: UnixSH
# app/database.py
###

## Modules
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

## Open a database connection
def createConnection(databaseName):
    ## SQLITE driver
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)
    ## Return error if database connection failed
    if not connection.open():
        QMessageBox.warning(
            None,
            "RPcontact"
            f"Database error: {connection.lastError().text()}"
        )
        return False
    ## Call for create contacts table if connection successfull
    _createContactsTable()
    return True

## Create contacts table if not exists
def _createContactsTable():
    createTableQuery = QSqlQuery()
    ## SQL query
    return createTableQuery.exec(
        """
        create table if not exists contacts (
            id integer primary key autoincrement unique not null,
            name varchar(40) not null,
            job varchar(50),
            email varchar(40) not null,
        )
        """
    )