'''
QgsLayoutGuideCollection
QgsLayoutGuide
QgsLayoutMeasurement
'''

lo = QgsProject.instance().layoutManager().layoutByName('map 2')

print(lo)

bgcolor = QColor('ff0000')

for item in lo.items():
    print(item)
    
    if isinstance(item, QgsLayoutFrame):
        print('yes')
        print(item.type())

guides = lo.guides()
print(guides)

first_page = lo.pageCollection().pages()[0]
print(first_page)
loc = QgsLayoutMeasurement(12, 0)
new_guide = QgsLayoutGuide(1, loc, first_page)

lo.guides().addGuide(new_guide)