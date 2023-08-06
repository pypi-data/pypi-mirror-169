import sys
import numpy as np

sys.path.insert(0, "/home/joshua/Documents/MADpy/src/pymadng")
from main import MAD

with MAD("/home/joshua/Documents/MADpy/examples", log=True) as mad:
    print("Hello")
    mad["a"] = np.asarray([1, 2, 3, 4, 5])
    mad.sendall()
    mad.a
