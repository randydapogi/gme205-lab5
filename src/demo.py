import json
import sys
from shapely import Polygon, LineString
from shapely.geometry import shape

from spatial import Parcel, Building, Road

with open('data/spatial_features.json', 'r') as file:
    data = json.load(file)
    
    
features = []
for d in data:
    data_type = d.pop('type')
    geometry = shape(d.pop('geometry'))
    
    if data_type == "Parcel":
        feature = Parcel(geometry=geometry, **d)
        features.append(feature)
    elif data_type == "Building":
        feature = Building(geometry=geometry, **d)
        features.append(feature)
    elif data_type == "Road":
        feature = Road(geometry=geometry, **d)
        features.append(feature)
        
        
if len(features) == 0:
    print("No object found.")
    sys.exit()
    
    
for f in features:
    print(type(f).__name__, f.effective_area())
