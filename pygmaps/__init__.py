"""
The MIT License

Copyright (c) 2009 Huy Nguyen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from xml.dom.minidom import Document

class GMap(object):
    """
    Creates a KML file for Google Maps or Google Earth
    Usage: 
        
        m = GMap()
        m.add_placemark(lon=39, lat=39, title="Sample Placemark", desc="A longer description for the placemark. It can include <b>HTML</b>")
        print m.renderKML()
    """
    
    def __init__(self):
        self.doc = Document()
        self.kml = self.doc.createElement("kml")
        self.kml.setAttribute("http://www.opengis.net/kml/2.2")
        self.doc.appendChild(self.kml)
            
    def add_placemark(self, lon, lat, alt=2, title="Default", desc="",  show=1):
        # create <Placemark>
        placemark = self.doc.createElement("Placemark")
        self.kml.appendChild(placemark)
        
        
        # create <name> 
        name = self.doc.createElement("name")
        placemark.appendChild(name)
        name.appendChild( self.doc.createTextNode(title) )
        
        # create <visibility> 
        visibility = self.doc.createElement("visibility")
        placemark.appendChild(visibility)
        visibility.appendChild( self.doc.createTextNode("1") )
        
        # create <description>
        description = self.doc.createElement("description")
        placemark.appendChild(description)
        description.appendChild( self.doc.createCDATASection(desc) )

        # create <Point>
        point = self.doc.createElement("Point")
        placemark.appendChild(point)

        # create <coordinates>
        coordinates = self.doc.createElement("coordinates")
        point.appendChild(coordinates)
        coordinates.appendChild( self.doc.createTextNode( "%s,%s,%s" % ( lon , lat, alt)))

    def renderKML(self):
        return self.doc.toxml()
