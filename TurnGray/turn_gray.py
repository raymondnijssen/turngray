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
from functools import partial

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

import qgis
from qgis.core import QgsMessageLog, QgsProject

from .turn_gray_dialog import TurnGrayDialog
from .margin_guides_dialog import MarginGuidesDialog
from .composer_item_color_setters import set_layout_item_color




class TurnGray:

    def __init__(self, iface):
        print('10')
        self.iface = iface
        print('20')
        self.plugin_dir = os.path.dirname(__file__)
        self.name = 'TurnGray'
        self.actions = []
        self.do_log = False # set to True for debugging

        self.testlo = 1

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


        icon_path = os.path.join(self.plugin_dir, 'img', 'icon.svg')
        self.add_action(
            icon_path,
            text='Change color of all composer items',
            callback=self.run,
            parent=self.iface.mainWindow(),
            status_tip=self.name)

        self.dlg = TurnGrayDialog()
        self.margin_guides_dlg = MarginGuidesDialog()

        # connections
        self.iface.layoutDesignerOpened.connect(self.designer_opened)
        self.iface.layoutDesignerClosed.connect(self.designer_closed)


    def unload(self):
        # disconnections
        self.iface.layoutDesignerOpened.disconnect(self.designer_opened)
        self.iface.layoutDesignerClosed.disconnect(self.designer_closed)

        # remove actions
        for action in self.actions:
            self.iface.removePluginMenu(
                '&Turn Gray',
                action)
            self.iface.removeToolBarIcon(action)

        # remove the toolbar
        del self.toolbar


    def designer_opened(self, designer):
        print('opened')

        tb = designer.actionsToolbar()

        icon = QIcon(os.path.join(self.plugin_dir, 'img', 'icon.svg'))
        action = QAction(icon, 'Change color of all composer items', parent=designer)
        #action.triggered.connect(partial(self.dlg.show, designer))
        action.triggered.connect(partial(self.run, designer))
        tb.addAction(action)

        margin_icon = QIcon(os.path.join(self.plugin_dir, 'img', 'icon_margin_guides.svg'))
        margin_action = QAction(margin_icon, 'Set margin guides', parent=designer)
        margin_action.triggered.connect(partial(self.run_margin_guides, designer))
        tb.addAction(margin_action)

        print('opened finished')


    def designer_closed(self):
        pass
        print('closed')


    def run(self, designer):
        print('--- run turn_gray---')
        #print(designer)
        self.testlo = designer
        if designer:
            pass
            ##rint(designer.layout())
            #print(designer.masterLayout())
            #print(designer.masterLayout().name())
        #print('---')

        # add composer names to dialog
        layouts = QgsProject.instance().layoutManager().layouts()
        self.dlg.comboBox_composer.clear()
        self.dlg.comboBox_composer.addItem('')
        for layout in layouts:
            self.dlg.comboBox_composer.addItem(layout.name())

        if designer:
            layout_index = self.dlg.comboBox_composer.findText(designer.masterLayout().name())
            self.dlg.comboBox_composer.setCurrentIndex(layout_index)
            self.dlg.comboBox_composer.setEnabled(False)
        else:
            self.dlg.comboBox_composer.setEnabled(True)

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
                new_foreground_color = self.dlg.mColorButtonForeground.color()
                self.log(new_foreground_color.getRgb())
            else:
                new_foreground_color = None

            if self.dlg.checkBox_background.isChecked():
                new_background_color = self.dlg.mColorButtonBackground.color()
                self.log(new_background_color.getRgb())
            else:
                new_background_color = None

            for item in lo.items():
                set_layout_item_color(item, new_foreground_color, new_background_color)

            # refresh
            lo.refresh()


    def run_margin_guides(self, designer):
        self.margin_guides_dlg.show()
        result = self.margin_guides_dlg.exec_()
        if result:
            print('--- run margin_guides ---')
            self.margin_guides_dlg.add_margin_guides(designer)
