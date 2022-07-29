# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TurnGray
                                 A QGIS plugin
 Turn black items in composer into gray (or any other color).
                             -------------------
        begin                : 2017-02-26
        copyright            : (C) 2017 by Raymond Nijssen / Terglobo
        email                : r.nijssen@terglobo.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from .turn_gray import TurnGray




def classFactory(iface):
    return TurnGray(iface)
