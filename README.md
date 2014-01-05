# N1YWB Equidistant Azimuthal Map Toolkit #

Copyright 2014 by Jeffrey M. Laughlin

This free toolkit provides an easy way to get started with equidistant
azimuthal maps using the free Quantum GIS application. 

It includes the following features:

* A complete QGIS project
* World basemap from http://www.naturalearthdata.com/
* Polar graticule with 5,000km & 30deg major and 2,500km & 15deg minor ticks
* Polar graticule generation script
* Lat/lon graticule
* Saved style files for base map, polar, and lat/lon graticules
* Print composer template optimized for US Letter sized paper

## How to use project ##

Just open it in QGIS 2. It should already be in pretty good shape for most world map use
cases, e.g. plotting DX QSOs.

## How to change map center ##

To center the map on your QTH, you need to edit the custom CRS.

Go to the Settings menu and select "Custom CRS"

    +proj=aeqd +lat_0=44.197227 +lon_0=-72.486237 +x_0=0 +y_0=0 +a=6371000 +b=6371000 +units=m +no_defs

Change the `lat` and `lon` parameters to your QTH lat & lon and click OK.

## How to customize the graticule ##

Refer to the style rules in the graticule layer properties. 

To change the major/minor spacing, copy the `create_polar_graticule.py` script
to your qgis scripts directory.

Linux script directory:

    /home/jeff/.qgis2/processing/scripts

Windows scripts directory:

    C:\Program Files\QGIS Dufour\apps\qgis\python\plugins\processing\script\scripts

Go to the Processing menu and display the toolbox if it's not already visible.

Go to `Scripts --> User scripts`

Double click `create polar graticule`

Most of the settings are pretty self explanitory. Units are in meters or
degrees. 

`label offset` deserves a bit of explanation; it sets how far away the
degree labels appear from the outermost major range ring. The default value is
fine for world maps. For smaller maps you may need to decrease the value. If
you can come up with a scale independent way to space the labels from the outer
ring, drop me a line.

Be sure to save the graticule and graticule labels to permanent files, not
temporary files, if you want to see them again the next time you run qgis.

Apply the saved style files to the new graticule layers.

## License ##

The basemap from Natural Earth Data is in the public domain.

The polar graticule generation script is released under the AGPL 3.0.

All other files and data, unless noted otherwise, are released under the
Creative Commons Attribution-ShareAlike 4.0 International Public License.

## Thanks ##

Thanks to Andrew Webster for providing assistance and inspiration. For tips on
making maps of amateur radio QSOs, please visit his blog:
http://alloutput.com/amateur-radio/using-gis-for-radio-maps

