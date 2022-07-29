# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TurnGray
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
import os.path

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QDialogButtonBox

import qgis
from qgis.core import QgsMessageLog, QgsProject

from .turn_gray_dialog import TurnGrayDialog
from .composer_item_color_setters import setlayoutItemColor


class TurnGray:

    def __init__(self, iface):
        print('10')
        self.iface = iface
        print('20')
        self.plugin_dir = os.path.dirname(__file__)
        self.name = 'TurnGray'
        self.actions = []
        self.do_log = False # set to True for debugging

    def log(self, message, tab=None):
        if tab is None:
            tab = self.name
        if self.do_log:
            QgsMessageLog.logMessage(str(message), 'turn gray', QgsMessageLog.INFO)
            #progress.setText('  '+str(message))


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        self.menu = '&Turn Gray'
        self.toolbar = self.iface.addToolBar(self.name)
        self.toolbar.setObjectName(self.name)


        icon_path = os.path.join(self.plugin_dir, 'img', 'icon.png')
        self.add_action(
            icon_path,
            text='Change color of composer items',
            callback=self.run,
            parent=self.iface.mainWindow(),
            status_tip=self.name)

        self.dlg = TurnGrayDialog()

        # connections:
        self.dlg.comboBox_composer.currentIndexChanged.connect(self.updateInterface)
        self.dlg.checkBox_foreground.toggled.connect(self.updateInterface)
        self.dlg.checkBox_background.toggled.connect(self.updateInterface)
        #self.dlg.mColorButtonForeground.setAllowAlpha(True)
        #self.dlg.mColorButtonBackground.setAllowAlpha(True)
        self.updateInterface()


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                '&Turn Gray',
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def updateInterface(self):
        self.dlg.mColorButtonForeground.setEnabled(self.dlg.checkBox_foreground.isChecked())
        self.dlg.mColorButtonBackground.setEnabled(self.dlg.checkBox_background.isChecked())
        if self.dlg.comboBox_composer.currentIndex() > 0 and (self.dlg.checkBox_foreground.isChecked() or self.dlg.checkBox_background.isChecked()):
            self.dlg.button_box.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.dlg.button_box.button(QDialogButtonBox.Ok).setEnabled(False)


    def run(self):
        # add composer names to dialog
        layouts = QgsProject.instance().layoutManager().layouts()
        self.dlg.comboBox_composer.clear()
        self.dlg.comboBox_composer.addItem('')
        for layout in layouts:
            self.dlg.comboBox_composer.addItem(layout.name())
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            self.log(layouts)

            if self.dlg.comboBox_composer.currentText() == '':
                self.log('no composer selected')
                return

            lo = None
            for layout in layouts:
                self.log('layout name: {}"'.format(layout.name()))
                self.log('combobox item: {}"'.format(self.dlg.comboBox_composer.currentText()))
                if layout.name() == self.dlg.comboBox_composer.currentText():
                    lo = layout
                    break
            if lo is None:
                self.log('layout "{}" does not exist'.format(self.dlg.comboBox_composer.currentText()))
                return

            if self.dlg.checkBox_foreground.isChecked():
                newForegroundColor = self.dlg.mColorButtonForeground.color()
                self.log(newForegroundColor.getRgb())
            else:
                newForegroundColor = None

            if self.dlg.checkBox_background.isChecked():
                newBackgroundColor = self.dlg.mColorButtonBackground.color()
                self.log(newBackgroundColor.getRgb())
            else:
                newBackgroundColor = None

            for item in lo.items():
                setlayoutItemColor(item, newForegroundColor, newBackgroundColor)

            # refresh
            lo.refresh()
