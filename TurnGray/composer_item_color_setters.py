from PyQt5.QtGui import QColor
from qgis.core import (
    QgsLayoutItemLabel,
    QgsLayoutItemLegend,
    QgsLayoutItemMap,
    QgsLayoutItemPicture,
    QgsLayoutItemScaleBar,
    QgsLayoutItemShape,
    QgsSimpleFillSymbolLayer)
    #, QgsLayoutItemTable, QgsLayoutItemFrame


def set_label_color(item, foreground_color=None, background_color=None):
    if foreground_color is not None:
        item.setFontColor(foreground_color)
        item.setFrameStrokeColor(foreground_color)
    if background_color is not None:
        item.setbackground_color(background_color)


def set_legend_color(item, foreground_color=None, background_color=None):
    if foreground_color is not None:
        item.setFontColor(foreground_color)
        item.setFrameStrokeColor(foreground_color)
    if background_color is not None:
        item.setbackground_color(background_color)


def set_map_color(item, foreground_color=None, background_color=None):
    if foreground_color is not None:
        item.setFrameStrokeColor(foreground_color)
        for grid in item.grids().asList():
            grid.setAnnotationFontColor(foreground_color)
            grid.setFramePenColor(foreground_color)
            grid.setFrameFillColor2(foreground_color)
            grid.setGridLineColor(foreground_color)
    if background_color is not None:
        item.setbackground_color(background_color)
        for grid in item.grids().asList():
            grid.setFrameFillColor1(background_color)


def set_picture_color(item, foreground_color=None, background_color=None):
    if foreground_color is not None:
        item.setFrameStrokeColor(foreground_color)
        item.setSvgStrokeColor(foreground_color)
    if background_color is not None:
        item.setbackground_color(background_color)
        item.setSvgFillColor(background_color)


def set_scale_bar_color(item, foreground_color=None, background_color=None):
    if foreground_color is not None:
        item.setFontColor(foreground_color)
        item.setLineColor(foreground_color)
        item.setFillColor(foreground_color)
        item.setFrameStrokeColor(foreground_color)
    if background_color is not None:
        item.setbackground_color(background_color)
        item.setFillColor2(background_color)


def set_shape_color(item, foreground_color=None, background_color=None):
    # TODO: check if exists!
    try:
        symbol = item.symbol().symbolLayers()[0]
    except:
        return
    if not isinstance(symbol, QgsSimpleFillSymbolLayer):
        return
    if foreground_color is not None:
        symbol.setStrokeColor(foreground_color)
    if background_color is not None:
        symbol.setFillColor(background_color)


# todo: fix for qgis 3
def set_table_color(item, foreground_color=None, background_color=None):
    if not isinstance(item.multiFrame(), QgsComposerTableV2):
        return
    if foreground_color is not None:
        item.multiFrame().setGridColor(foreground_color)
        item.multiFrame().setHeaderFontColor(foreground_color)
        item.multiFrame().setContentFontColor(foreground_color)
    if background_color is not None:
        item.multiFrame().setbackground_color(background_color)


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

def set_layout_item_color(item, foreground_color=None, background_color=None):
    if foreground_color is None and background_color is None:
        return

    class_name = type(item).__name__
    #print(class_name)

    if isinstance(item, QgsLayoutItemLabel):
        set_label_color(item, foreground_color, background_color)
    elif isinstance(item, QgsLayoutItemLegend):
        set_legend_color(item, foreground_color, background_color)
    elif isinstance(item, QgsLayoutItemMap):
        set_map_color(item, foreground_color, background_color)
    elif isinstance(item, QgsLayoutItemPicture):
        set_picture_color(item, foreground_color, background_color)
    elif isinstance(item, QgsLayoutItemScaleBar):
        set_scale_bar_color(item, foreground_color, background_color)
    elif isinstance(item, QgsLayoutItemShape):
        set_shape_color(item, foreground_color, background_color)
    else:
        print(f'Could not change attributes of class: {class_name}')

    '''
    if isinstance(item, QgsLayoutItemFrame):
        setAttributeTableColor(item, foreground_color, background_color)
    '''
