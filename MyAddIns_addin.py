# -*- coding: utf-8 -*-
import arcpy
import pythonaddins
import pyperclip

class ButtonClass1(object):
    """Implementation for MyAddIns_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    # Implementation of OnClick method of Button's class
    def onClick(self):

        with arcpy.da.SearchCursor('', ['CROSS_NBR', 'ROAD_NAME']) as cursor:
            for row in cursor:
                x = row[0]
                y = row[1]
                roadxng = str(x) + ', ' + str(y)
                rdxing = roadxng.upper()
                pyperclip.copy(str(rdxing.strip())) 