


# DIML

This dataset contains synchronized RGB-D frames from both Kinect v2 and Zed stereo camera. For the outdoor scene, we first generate disparity maps using an accurate stereo matching method and convert them using calibration parameters. A per-pixel confidence map of disparity is also provided. Our scenes are captured at various places, e.g., offices, rooms, dormitory, exhibition center, street, road etc., from Yonsei University and Ewha University.

---

### Prepare Dataset

The dataset can be downloaded from [here](https://dimlrgbd.github.io/).
We randomly select 200K dataset from both indoor and outdoor scene. 

---

### File Structure
```
.
|-- Indoor
    |-- Store
    |-- Kitchen
    |-- Church
    |-- Corridor
    |-- Library
    |-- ...
|--Outdoor
    |-- Buliding
    |-- Street
    |-- Field
    |-- Overpass
    |-- Driverway
    |-- Construction
    |-- ...
```


### Citation
```
@article{DIML,
  author       = {Jaehoon Cho and
                  Dongbo Min and
                  Youngjung Kim and
                  Kwanghoon Sohn},
  title        = {DIML/CVL RGB-D Dataset: 2M RGB-D Images of Natural Indoor and Outdoor Scenes},
  journal      = {CoRR},
  volume       = {abs/2110.11590},
  year         = {2021}
}
```