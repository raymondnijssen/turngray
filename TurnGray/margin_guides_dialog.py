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
from PyQt5.QtWidgets import QDialogButtonBox

from qgis.core import (
    QgsLayoutMeasurement,
    QgsLayoutGuide
)

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'margin_guides_dialog.ui'))


class MarginGuidesDialog(QtWidgets.QDialog, FORM_CLASS):

    def __init__(self, parent=None):
        super(MarginGuidesDialog, self).__init__(parent)
        self.setupUi(self)

        # connections:
        #self.comboBox_composer.currentIndexChanged.connect(self.updateInterface)
        #self.checkBox_foreground.toggled.connect(self.updateInterface)
        #self.checkBox_background.toggled.connect(self.updateInterface)


    def updateInterface(self):
        pass
        '''
        self.mColorButtonForeground.setEnabled(self.checkBox_foreground.isChecked())
        self.mColorButtonBackground.setEnabled(self.checkBox_background.isChecked())
        if self.comboBox_composer.currentIndex() > 0 and (self.checkBox_foreground.isChecked() or self.checkBox_background.isChecked()):
            self.button_box.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        '''

    def add_margin_guides(self, designer):
        layout = designer.masterLayout()
        first_page = layout.pageCollection().pages()[0] # TODO: needs index check
        distance = self.doubleSpinBox_margin.value()
        # top
        loc = QgsLayoutMeasurement(distance, 0)
        new_guide = QgsLayoutGuide(1, loc, first_page) # horizontal
        layout.guides().addGuide(new_guide)
        # left
        new_guide = QgsLayoutGuide(2, loc, first_page) # vertical
        layout.guides().addGuide(new_guide)
        # bottom
        height = first_page.pageSize().height()
        loc = QgsLayoutMeasurement(height - distance, 0)
        new_guide = QgsLayoutGuide(1, loc, first_page) # horizontal
        layout.guides().addGuide(new_guide)
        # right
        width = first_page.pageSize().width()
        loc = QgsLayoutMeasurement(width - distance, 0)
        new_guide = QgsLayoutGuide(2, loc, first_page) # vertical
        layout.guides().addGuide(new_guide)
