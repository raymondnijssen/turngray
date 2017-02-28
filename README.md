# turngray
QGIS plugin for changing color of map composer items

Changing dialog
---------------

The dialog contains QgsColorButtonV2 widgets, which do not work on many
QGIS instances the way they are produced by (my) QtDesigner. A solution 
for this is described here:

<https://lists.osgeo.org/pipermail/qgis-developer/2016-August/044138.html>

Every time when saving `turn_gray_dialog_base.ui` the text `qgscolorbuttonv2.h`
should be replaced by `qgis.gui`.

