"""
TODO:
1) Add more support to iNAV.
2) Add the possibility to register a callback functions when a msg is transmitted.
3) Improve the arming confirmation.
4) This file is way too big... it needs to be broken down into smaller ones.
"""

import logging
import struct
import time
import sys
from threading import Lock

if "linux" in sys.platform:
    import ctypes
    ffs = ctypes.cdll.LoadLibrary('libc.so.6').ffs # this is only for ffs... it should be directly implemented.
else:
    def ffs(x): # modified from https://stackoverflow.com/a/36059264
        return (x&-x).bit_length()
        
import serial 