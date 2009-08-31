# pygmap - Generate Google Map Annotations in Python

This is a small module that helps you annoutate Google Maps through a pythonic interface. Use it to generated a KML file which can then be fed to http://maps.google.com for display.

## Example Usage

    from pygmap import GMap
    m = GMap()
    m.add_placemark(lon="-122.0827778", 
                    lat="37.3861111", 
                    title="Mountain View, CA", 
                    desc="this is a <b>placemark</b> over Moutain View, CA. This field can contain HTML formatting!")
    print m.renderKML()

