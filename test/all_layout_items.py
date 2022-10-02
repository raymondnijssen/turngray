print(u'--- layoutItemLabel ----')
p = QgsProject.instance()
lom = p.layoutManager()
lo = lom.layoutByName('one_item')
print(lo)

for lo_item in lo.items():
    print(lo_item)
    
    if isinstance(lo_item, QgsLayoutFrame):
        print('frame')
        for d in dir(lo_item):
            pass
            #print(f'  {d}')
            
        lo_item.setBackgroundEnabled(True)
        lo_item.setBackgroundColor(QColor('yellow'))
        lo_item.setFrameStrokeColor(QColor('red'))
            
        mf = lo_item.multiFrame()
        print(mf)
        if isinstance(mf, QgsLayoutTable):
            print('yes')
        for d in dir(mf):
            pass
            #print(f'  {d}')
        mf.setGridColor(QColor('red'))
        mf.setHeaderFontColor(QColor('red'))
        mf.setContentFontColor(QColor('red'))
        mf.setBackgroundColor(QColor('yellow'))

    print('--')
