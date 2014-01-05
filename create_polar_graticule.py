#!/usr/bin/env python

"""
Generate a polar graticule for an equidistant azimuthal map.

Copyright 2014 by Jeffrey Michael Laughlin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import math
from qgis.core import *
from PyQt4.QtCore import *
import traceback

from processing.core.VectorWriter import VectorWriter

##major_degree_spacing=number 30
##minor_degree_spacing=number 15
##major_ring_spacing=number 5000000
##minor_ring_spacing=number 2500000
##major_rings=number 4
##centerx=number 0.0
##centery=number 0.0
##label_offset=number 1000000
##buffer_segments=number 25
##graticule=output vector
##gratlables=output vector
##crsId=string USER:100001

# When called from the python console with default args, qgis fails to convert
# default values from strings.
major_degree_spacing=int(major_degree_spacing)
minor_degree_spacing=int(minor_degree_spacing)
major_ring_spacing=int(major_ring_spacing)
minor_ring_spacing=int(minor_ring_spacing)
major_rings=int(major_rings)
centerx=float(centerx)
centery=float(centery)
label_offset=int(label_offset)
buffer_segments=int(buffer_segments)

def mkfeature(geom, attrs):
    f = QgsFeature()
    f.setGeometry(geom)
    f.setAttributes(attrs)
    return f

def mkpoint(start, distance, bearing):
    rads = math.radians(bearing)
    x, y = distance * math.sin(rads), distance * math.cos(rads)
    return QgsPoint(start.x() + x, start.y() + y)

crs = QgsCoordinateReferenceSystem(crsId)
start = QgsPoint(centerx,centery)
maxdist = major_ring_spacing * major_rings

shapetype = QGis.WKBLineString
fields = [
    QgsField('precedence', QVariant.String),
    QgsField('theta', QVariant.Int),
    QgsField('distance', QVariant.Int),
    QgsField('label', QVariant.String),
]
writer = VectorWriter(graticule, None, fields, shapetype, crs)

shapetype = QGis.WKBPoint
fields = [
    QgsField('label', QVariant.String),
]
point_writer = VectorWriter(gratlables, None, fields, shapetype, crs)

majorticks = set(range(0, 360, major_degree_spacing))
minorticks = set(range(0, 360, minor_degree_spacing))
ticks = sorted(majorticks | minorticks)
print ticks

for theta in ticks:
    precedence = 'major' if theta in majorticks else 'minor'
    point = mkpoint(start, maxdist, theta)
    line = QgsGeometry.fromPolyline([start, point])
    print line
    writer.addFeature(mkfeature(line, [precedence, theta, -1, str(theta)]))
    point = mkpoint(start, maxdist + label_offset, theta)
    point = QgsGeometry.fromPoint(point)
    point_writer.addFeature(mkfeature(point, [str(theta)]))

majorticks = set(range(major_ring_spacing, maxdist+1, major_ring_spacing))
minorticks = set(range(minor_ring_spacing, maxdist, minor_ring_spacing))

for distance in sorted(majorticks | minorticks):
    precedence = 'major' if distance in majorticks else 'minor'
    buf = QgsGeometry.fromPoint(start).buffer(distance, buffer_segments)
    writer.addFeature(mkfeature(buf, [precedence, -1, distance, '%d'%(distance / 1e3)]))

del writer
del point_writer

