# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TurnGrayDialog
                                 A QGIS plugin
 Turn black items in composer into gray (or any other color).
                             -------------------
        begin                : 2017-02-26
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Raymond Nijssen / Terglobo
        email                : r.nijssen@terglobo.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import QtGui, QtWidgets, uic


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'turn_gray_dialog_base.ui'))


class TurnGrayDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(TurnGrayDialog, self).__init__(parent)
        self.setupUi(self)
