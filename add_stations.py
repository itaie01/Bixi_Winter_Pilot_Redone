from qgis.core import QgsFeature, QgsField, QgsFields, QgsVectorLayer, QgsProject, QgsPointXY, QgsCoordinateReferenceSystem

lat_lon_pairs = []
with open('/Users/itai-epstein/Documents/Development/bixi_winter_pilot/150_most_pop_station_coords.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        x = line.strip()[1:len(line)-1].split(',')
        lat_lon_pairs.append((float(x[0]), float(x[1])))

# Define the desired coordinate reference system (CRS) with geographic (lat/long) coordinates
desired_crs = QgsCoordinateReferenceSystem('EPSG:4326')  # WGS 84

# Create a memory layer for points
point_layer = QgsVectorLayer('Point?crs=' + desired_crs.authid(), 'PointLayer', 'memory')

# Define fields for the layer
fields = QgsFields()
fields.append(QgsField('Latitude', QVariant.Double))
fields.append(QgsField('Longitude', QVariant.Double))
point_layer.dataProvider().addAttributes(fields)
point_layer.updateFields()

# Set the coordinate system for the layer
point_layer.setCrs(desired_crs)

# Create points and add them to the layer
features = []
for lat, lon in lat_lon_pairs:
    point = QgsPointXY(lon, lat)
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPointXY(point))
    feature.setAttributes([lat, lon])
    features.append(feature)

point_layer.dataProvider().addFeatures(features)

# Add the layer to the map
QgsProject.instance().addMapLayer(point_layer)

# Refresh the map canvas
iface.mapCanvas().refresh()
