import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "127.0.0.1"

HumanGreeter = None
memory = None

class HumanGreeterModule(ALModule):

    def __init__(self, name):
        ALModule.__init__(self, name)
        self.tts = ALProxy("ALTextToSpeech")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")

    def onFaceDetected(self, *_args):
        memory.unsubscribeToEvent("FaceDetected", "HumanGreeter")

        self.tts.say("Hello, you")

        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")

def main():
    parser = OptionParser()
    parser.add_option("--pip", help="Parent broker port.  The IP address of your robot", dest="pip")
    parser.add_option("--pport", help = "Parent broker port.  The port NAOqi is listening to",
        dest = "pport",
        type = "int")
    parser.set_defaults(pip=NAO_IP, pport=56454)

    (opts, args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    myBroker = ALBroker("myBroker",
    "0.0.0.0",
    0,
    pip,
    pport)


    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()