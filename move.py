
import sys
import time
import math

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

def deg(f):
    if f > 180:
        num = int(math.ceil(float(f) / 180))
        print(num)
        for _ in range(0, num-1):
            motion.moveTo(0.0, 0.0, deg(180))
        return deg(f % 180)
    elif f < -180:
        num = int(math.ceil(float(math.fabs(f)) / 180))
        print(num)
        for _ in range(0, num-1):
            motion.moveTo(0.0, 0.0, deg(-180))
        return deg(-(f % 180))

    return f*3.1415/180




#broker = ALBroker("broker", "0.0.0.0", 0, "127.0.0.1", 55161)

motion =ALProxy("ALMotion", "127.0.0.1", 56454)


# Limits values to max or min values
motion.moveTo(0.0, 0.0, deg(-270))
