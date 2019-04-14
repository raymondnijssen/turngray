from PyQt5.QtGui import QColor
from qgis.core import QgsLayoutItemLabel, QgsLayoutItemLegend, QgsLayoutItemMap, QgsLayoutItemPicture, QgsLayoutItemScaleBar, \
    QgsLayoutItemShape, QgsSimpleFillSymbolLayer#, QgsLayoutItemTable, QgsLayoutItemFrame

#qgisVersion = qgis.utils.QGis.QGIS_VERSION_INT

# fixes not updated composer widget
# https://lists.osgeo.org/pipermail/qgis-developer/2017-February/047241.html
def sillyWidgetFix(item):
    old_id = item.id()
    item.setId('a')
    item.setId(old_id)

def setLabelColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        item.setFontColor(foregroundColor)
        item.setFrameStrokeColor(foregroundColor)
    if backgroundColor is not None:
        item.setBackgroundColor(backgroundColor)


def setLegendColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        item.setFontColor(foregroundColor)
        item.setFrameStrokeColor(foregroundColor)
    if backgroundColor is not None:
        item.setBackgroundColor(backgroundColor)


def setMapColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        item.setFrameStrokeColor(foregroundColor)
        for grid in item.grids().asList():
            grid.setAnnotationFontColor(foregroundColor)
            grid.setFramePenColor(foregroundColor)
            grid.setFrameFillColor2(foregroundColor)
            grid.setGridLineColor(foregroundColor)
    if backgroundColor is not None:
        item.setBackgroundColor(backgroundColor)
        for grid in item.grids().asList():
            grid.setFrameFillColor1(backgroundColor)


def setPictureColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        item.setFrameStrokeColor(foregroundColor)
        item.setSvgStrokeColor(foregroundColor)
    if backgroundColor is not None:
        item.setBackgroundColor(backgroundColor)
        item.setSvgFillColor(backgroundColor)


def setScaleBarColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        item.setFontColor(foregroundColor)
        item.setLineColor(foregroundColor)
        item.setFillColor(foregroundColor)
        item.setFrameStrokeColor(foregroundColor)
    if backgroundColor is not None:
        item.setBackgroundColor(backgroundColor)
        item.setFillColor2(backgroundColor)


def setShapeColor(item, foregroundColor=None, backgroundColor=None):
    # TODO: check if exists!
    try:
        symbol = item.symbol().symbolLayers()[0]
    except:
        return
    if not isinstance(symbol, QgsSimpleFillSymbolLayer):
        return
    if foregroundColor is not None:
        symbol.setStrokeColor(foregroundColor)
    if backgroundColor is not None:
        symbol.setFillColor(backgroundColor)

# todo: fix for qgis 3
def setTableColor(item, foregroundColor=None, backgroundColor=None):
    if not isinstance(item.multiFrame(), QgsComposerTableV2):
        return
    if foregroundColor is not None:
        item.multiFrame().setGridColor(foregroundColor)
        item.multiFrame().setHeaderFontColor(foregroundColor)
        item.multiFrame().setContentFontColor(foregroundColor)
    if backgroundColor is not None:
        item.multiFrame().setBackgroundColor(backgroundColor)



'''
todo:
    QgsLayoutItemArrow
    QgsLayoutItemAttributeTable
    # QgsLayoutItemLabel
    # QgsLayoutItemLegend
    # QgsLayoutItemMap
    # QgsLayoutItemPicture
    # QgsLayoutItemScaleBar
    # QgsLayoutItemShape
    QgsLayoutItemTable
'''

def setlayoutItemColor(item, foregroundColor=None, backgroundColor=None):
    if foregroundColor is None and backgroundColor is None:
        return
    classname = type(item).__name__
    print(classname)
    if isinstance(item, QgsLayoutItemLabel):
        setLabelColor(item, foregroundColor, backgroundColor)
    if isinstance(item, QgsLayoutItemLegend):
        setLegendColor(item, foregroundColor, backgroundColor)
    if isinstance(item, QgsLayoutItemMap):
        setMapColor(item, foregroundColor, backgroundColor)
    if isinstance(item, QgsLayoutItemPicture):
        setPictureColor(item, foregroundColor, backgroundColor)
    if isinstance(item, QgsLayoutItemScaleBar):
        setScaleBarColor(item, foregroundColor, backgroundColor)
    if isinstance(item, QgsLayoutItemShape):
        setShapeColor(item, foregroundColor, backgroundColor)
    '''
    if isinstance(item, QgsLayoutItemFrame):
        setAttributeTableColor(item, foregroundColor, backgroundColor)
    '''
