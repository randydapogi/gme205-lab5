# GmE 205 – Laboratory Exercise 5

## Overview

GmE 205 Lab Exercise 5

---

## Environment Setup

- Python 3.x

---

## How to Run

1. Activate the virtual environment
2. run `python src/run_lab5.py`

---

## Outputs

- output/summary.json

---

## Reflection

1. Where does polymorphism appear in your system?

- It appears in the spatial.py file when i set a different effective_area instance method for Parcel, Building and Road class.

2. How does polymorphism remove conditional logic from analysis.py?

- The run_lab5.py only needs to call the effective_area method of the feature and depending on the class, a different calculation for area will be executed. This effectively removes the if condition for calling different effective_area calculations in run_lab5.py.

3. Which OOP pillar allows multiple spatial classes to share a method name?

- Inheritance

4. Why is it better for objects to compute their own area rather than a condition to decide how?

- This moves the area compute logic to the object class. This way the logic that is related to the object stays in the object class.

5. If you add a new class tomorrow (River), what changes are required in spatial.py?

- Nothing will change in the existing SpatialObject class. I will just have to create a new class River in spatial.py and make it inherit from SpatialObject. I then need to define a effective_area methon in River that calculates the area of the river.

---
