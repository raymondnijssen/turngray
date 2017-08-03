from PyQt4.QtGui import QColor
from qgis.core import QgsComposerLabel, QgsComposerLegend, QgsComposerMap, QgsComposerPicture, QgsComposerScaleBar, \
    QgsComposerShape, QgsComposerTableV2, QgsComposerFrame, QgsSimpleFillSymbolLayerV2

#qgisVersion = qgis.utils.QGis.QGIS_VERSION_INT

# fixes not updated composer widget
# https://lists.osgeo.org/pipermail/qgis-developer/2017-February/047241.html
def sillyWidgetFix(item):
    old_id = item.id()
    item.setId('a')
    item.setId(old_id)

def setQgsComposerLabelColor(composerLabel, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print(composerLabel.fontColor().getRgb())
        composerLabel.setFontColor(foregroundColor)
        #print(composerLabel.frameOutlineColor().getRgb())
        composerLabel.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print(composerLabel.backgroundColor().getRgb())
        composerLabel.setBackgroundColor(backgroundColor)


def setQgsComposerLegendColor(composerLegend, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print(composerLegend.fontColor().getRgb())
        composerLegend.setFontColor(foregroundColor)
        #print(composerLegend.frameOutlineColor().getRgb())
        composerLegend.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print(composerLegend.backgroundColor().getRgb())
        composerLegend.setBackgroundColor(backgroundColor)


def setQgsComposerMapColor(composerMap, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print(composerMap.frameOutlineColor().getRgb())
        composerMap.setFrameOutlineColor(foregroundColor)
        for grid in composerMap.grids().asList():
            grid.setAnnotationFontColor(foregroundColor)
            grid.setFramePenColor(foregroundColor)
            grid.setFrameFillColor2(foregroundColor)
            grid.setGridLineColor(foregroundColor)
    if backgroundColor is not None:
        composerMap.setBackgroundColor(backgroundColor)
        for grid in composerMap.grids().asList():
            grid.setFrameFillColor1(backgroundColor)
            


def setQgsComposerPictureColor(composerMap, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print(composerMap.frameOutlineColor().getRgb())
        composerMap.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print(composerMap.backgroundColor().getRgb())
        composerMap.setBackgroundColor(backgroundColor)


def setQgsComposerScaleBarColor(composerScaleBar, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print(composerScaleBar.fontColor().getRgb())
        composerScaleBar.setFontColor(foregroundColor)
        #print(composerScaleBar.frameOutlineColor().getRgb())
        composerScaleBar.setFrameOutlineColor(foregroundColor)        
        composerScaleBar.setBrush(foregroundColor)
        composerScaleBar.setPen(foregroundColor)
        
        # this will only work from QGIS 3. work in progress
        if False:#qgisVersion >= 29900:
            #print(composerScaleBar.fillColor().getRgb())
            composerScaleBar.setFillColor(foregroundColor)
    if backgroundColor is not None:
        #print(composerScaleBar.backgroundColor().getRgb())
        composerScaleBar.setBackgroundColor(backgroundColor)
        composerScaleBar.setBrush2(backgroundColor)
        if False:#qgisVersion >= 29900:
            #print(composerScaleBar.fillColor2().getRgb())
            composerScaleBar.setFillColor2(backgroundColor)


def setQgsComposerShapeColor(composerShape, foregroundColor=None, backgroundColor=None):
    # TODO: check if exists!
    try:
        symbol = composerShape.shapeStyleSymbol().symbolLayers()[0]
    except:
        return
    if not isinstance(symbol, QgsSimpleFillSymbolLayerV2):
        return
    if foregroundColor is not None:
        symbol.setBorderColor(foregroundColor)
    if backgroundColor is not None:
        symbol.setFillColor(backgroundColor)


def setQgsComposerAttributeTableColor(composerFrame, foregroundColor=None, backgroundColor=None):
    if not isinstance(composerFrame.multiFrame(), QgsComposerTableV2):
        return
    if foregroundColor is not None:
        composerFrame.multiFrame().setGridColor(foregroundColor)
        composerFrame.multiFrame().setHeaderFontColor(foregroundColor)
        composerFrame.multiFrame().setContentFontColor(foregroundColor)
    if backgroundColor is not None:
        composerFrame.multiFrame().setBackgroundColor(backgroundColor)



'''
todo:
    QgsComposerArrow
    # QgsComposerAttributeTable
    QgsComposerFrame
    # QgsComposerLabel
    # QgsComposerLegend
    # QgsComposerMap
    # QgsComposerMapGrid
    # QgsComposerPicture
    # QgsComposerScaleBar
    # QgsComposerShape
    QgsComposerTable
'''    

def setQgsComposerItemColor(composerItem, foregroundColor=None, backgroundColor=None):
    if foregroundColor is None and backgroundColor is None:
        return
    classname = type(composerItem).__name__
    ##print(classname)
    if isinstance(composerItem, QgsComposerLabel):
        setQgsComposerLabelColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerLegend):
        setQgsComposerLegendColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerMap):
        setQgsComposerMapColor(composerItem, foregroundColor, backgroundColor)
        #sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerPicture):
        setQgsComposerPictureColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerScaleBar):
        setQgsComposerScaleBarColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerShape):
        setQgsComposerShapeColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    if isinstance(composerItem, QgsComposerFrame):
        setQgsComposerAttributeTableColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    '''
    if isinstance(composerItem, QgsComposerArrow):
        setQgsComposerAttributeTableColor(composerItem, foregroundColor, backgroundColor)
        sillyWidgetFix(composerItem)
    '''


