
import sys
import time
import math

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

def deg(f):
    sign = (1, -1)[f < 0]
    f=math.fabs(f)
    if f > 180:
        num = int(math.ceil(float(f) / 180))
        print(num)
        for _ in range(0, num-1):
            motion.moveTo(0.0, 0.0, deg(sign*180))
        return deg(sign*(f % 180))
    return sign*(f*3.1415/180)




#broker = ALBroker("broker", "0.0.0.0", 0, "127.0.0.1", 55161)

motion =ALProxy("ALMotion", "127.0.0.1", 56454)


# Limits values to max or min values
motion.moveTo(0.0, 0.0, deg(-270))
