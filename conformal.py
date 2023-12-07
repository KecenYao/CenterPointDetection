import numpy as np


"""
    split the nuImages test dataset into 
        - calibration dataset
        - testing dataset
"""

"""
    (Traing+validation) -> (train, val, test: 6:1:3)
    train -> model
    test (3) -> 1:2 (conformal_cal, conformal_test)

    Solution: local test data /mnt/NAS/data/ruixuan/data/nuImages/vehicle_data/annotations/test.json
"""

"""
    inference on calibration dataset: -> provide path using demo.py 
    python src/demo.py ctdet --demo /home/eacv/kevinyao/CenterNet/images/n008-2018-09-18-14-18-33-0400__CAM_FRONT__1537294833612404.jpg --load_model /home/eacv/kevinyao/CenterNet/models/ctdet_vehicle_hourglass/model_best.pth --debug 2 --arch hourglass
"""

"""
    inference output: debugger.py, /src/lib/detectors/ctdet.py
    GT input: /mnt/NAS/data/ruixuan/data/nuImages/vehicle_data/anootations
"""


"""
    upscale heatmap back to 1400*900. use linear interpolation

"""


