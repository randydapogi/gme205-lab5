import math

from shapely.geometry import Point as ShapelyPoint
from shapely.geometry.base import BaseGeometry


def rad_area_to_meter_area(rad_area: float, rad_lat: float):
    # 1 deg lat ~ 111.32km, 1 deg lon ~ 111.32km * cos(lat)
    meters_per_degree_lat: float = 111320.0
    meters_per_degree_lon: float = 111320.0 * math.cos(math.radians(rad_lat))
    
    return rad_area * meters_per_degree_lat * meters_per_degree_lon
    

class SpatialObject:
    def __init__(self, geometry: BaseGeometry):
        self.geometry = geometry

    def bbox(self):
        return self.geometry.bounds

    def intersects(self, other) -> bool:
        return self.geometry.intersects(other.geometry)
    
    def effective_area(self): 
        """ Return the spatial area representation of the object. Subclasses must implement this behavior. """ 
        raise NotImplementedError


class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes
        
    def effective_area(self):
        lat = self.geometry.centroid.y
        area_m2 = rad_area_to_meter_area(self.geometry.area, lat)
        return area_m2
    
    def as_dict(self):
        return {
            "parcel_id": self.parcel_id,
            "attributes": self.attributes,
            "bbox": self.bbox(),
            "area": self.effective_area()
        }
        
        
class Building(SpatialObject): 
    def __init__(self, building_id, geometry, floors: int, usage: str):
        super().__init__(geometry)
        self.building_id = building_id
        self.floors = floors
        self.usage = usage
        
    def effective_area(self):
        lat = self.geometry.centroid.y
        area_m2 = rad_area_to_meter_area(self.geometry.area, lat)
        return area_m2 * self.floors
    
    def as_dict(self):
        return {
            "building_id": self.building_id,
            "floors": self.floors,
            "usage": self.usage,
            "bbox": self.bbox(),
            # "area": self.effective_area()
        } 
    

class Road(SpatialObject): 
    def __init__(self, road_id, geometry, name: str, width: int):
        super().__init__(geometry)
        self.road_id = road_id
        self.name = name
        self.width = width
        
    def effective_area(self): 
        lat = self.geometry.centroid.y
        width_in_degrees = self.width / 111320
        area_m2 = rad_area_to_meter_area(self.geometry.buffer(width_in_degrees).area, lat)
        return area_m2
    
    def as_dict(self):
        return {
            "road_id": self.road_id,
            "name": self.name,
            "width": self.width,
            "bbox": self.bbox(),
            "area": self.effective_area()
        } 