from PyQt4.QtGui import QColor

#qgisVersion = qgis.utils.QGis.QGIS_VERSION_INT

def setQgsComposerLabelColor(composerLabel, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print composerLabel.fontColor().getRgb()
        composerLabel.setFontColor(foregroundColor)
        #print composerLabel.frameOutlineColor().getRgb()
        composerLabel.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print composerLabel.backgroundColor().getRgb()
        composerLabel.setBackgroundColor(backgroundColor)


def setQgsComposerLegendColor(composerLegend, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print composerLegend.fontColor().getRgb()
        composerLegend.setFontColor(foregroundColor)
        #print composerLegend.frameOutlineColor().getRgb()
        composerLegend.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print composerLegend.backgroundColor().getRgb()
        composerLegend.setBackgroundColor(backgroundColor)


def setQgsComposerMapColor(composerMap, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print composerMap.frameOutlineColor().getRgb()
        composerMap.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print composerMap.backgroundColor().getRgb()
        composerMap.setBackgroundColor(backgroundColor)


def setQgsComposerPictureColor(composerMap, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print composerMap.frameOutlineColor().getRgb()
        composerMap.setFrameOutlineColor(foregroundColor)
    if backgroundColor is not None:
        #print composerMap.backgroundColor().getRgb()
        composerMap.setBackgroundColor(backgroundColor)


def setQgsComposerScaleBarColor(composerScaleBar, foregroundColor=None, backgroundColor=None):
    if foregroundColor is not None:
        #print composerScaleBar.fontColor().getRgb()
        composerScaleBar.setFontColor(foregroundColor)
        #print composerScaleBar.frameOutlineColor().getRgb()
        composerScaleBar.setFrameOutlineColor(foregroundColor)
        # this will only work from QGIS 3
        if False:#qgisVersion >= 29900:
            #print composerScaleBar.fillColor().getRgb()
            composerScaleBar.setFillColor(foregroundColor)
    if backgroundColor is not None:
        print composerScaleBar.backgroundColor().getRgb()
        composerScaleBar.setBackgroundColor(backgroundColor)
        if False:#qgisVersion >= 29900:
            #print composerScaleBar.fillColor2().getRgb()
            composerScaleBar.setFillColor2(backgroundColor)


def setQgsComposerShapeColor(composerShape, foregroundColor=None, backgroundColor=None):
    # TODO: check if exists!
    symbol = composerShape.shapeStyleSymbol().symbolLayers()[0]
    if not type(symbol).__name__ == u'QgsSimpleFillSymbolLayerV2':
        return
    if foregroundColor is not None:
        #print symbol.borderColor().getRgb()
        symbol.setBorderColor(foregroundColor)
    if backgroundColor is not None:
        #print symbol.fillColor().getRgb()
        symbol.setFillColor(backgroundColor)

'''
classes:
    QgsComposerArrow
    QgsComposerAttributeTable
    QgsComposerFrame
    # QgsComposerLabel
    # QgsComposerLegend
    # QgsComposerMap
    QgsComposerMapGrid
    QgsComposerPicture
    # QgsComposerScaleBar
    # QgsComposerShape
    QgsComposerTable
'''    

def setQgsComposerItemColor(composerItem, foregroundColor=None, backgroundColor=None):
    if foregroundColor is None and backgroundColor is None:
        return
    classname = type(composerItem).__name__
    print classname
    if classname == u'QgsComposerLabel':
        setQgsComposerLabelColor(composerItem, foregroundColor, backgroundColor)
    if classname == u'QgsComposerLegend':
        setQgsComposerLegendColor(composerItem, foregroundColor, backgroundColor)
    if classname == u'QgsComposerMap':
        setQgsComposerMapColor(composerItem, foregroundColor, backgroundColor)
    if classname == u'QgsComposerPicture':
        setQgsComposerPictureColor(composerItem, foregroundColor, backgroundColor)
    if classname == u'QgsComposerScaleBar':
        setQgsComposerScaleBarColor(composerItem, foregroundColor, backgroundColor)
    if classname == u'QgsComposerShape':
        setQgsComposerShapeColor(composerItem, foregroundColor, backgroundColor)



