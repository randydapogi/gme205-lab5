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
    
    
total_area = sum(f.effective_area() for f in features)

area_per_class = {}
for item in features:
    category = type(item).__name__
    area = item.effective_area()
    
    area_per_class[category] = area_per_class.get(category, 0) + area

summary = {
    "parameters": {
        "spatial_features_file": "data/spatial_features.json"
    },
    "result": {
        "total_features": len(features),
        "total_area": total_area,
        "area_per_class": area_per_class
    }
}

with open('output/summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)