#from enum import Enum
from __future__ import annotations
from abc import ABC, abstractmethod
import Wrapper

#class Wrapper:
#    def __init__(self):
#        pass

class PressureCtrlWrapperImpl(ABC):
    _implType=0
    _channelToPressure=0
    # add more variables here! 
    # make them protected by adding prefix "_"
    def __init__(self):
#        self.ImplType=0
#        self.ChannelToPressure=dict()
        pass
    def connect(self):
        pass
    def disconnect(self):
        pass
    def setPressure(self, pressure, channel):
        pass
    def readPressure(self, channel)->float:
        pass
    # add more interfac function here!

class PressureCtrlWrapperImplPreci(PressureCtrlWrapperImpl):
    def __init__(self):
        super().__init__()
        self._implType=1
        self._channelToPressure=dict()
    def connect(self):
        print("Connected to Pressure Ctrl...")
        #add implementation here!  
    def disconnect(self):
        print("Disconnected from Pressure Ctrl...")
        #add implementation here!       
    def setPressure(self, channel, pressure):
        print("Set pressure...")
        self._channelToPressure.update({channel:pressure})
        #add implementation here! 
    def readPressure(self, channel)->float:
        print("Get pressure...")
        return self._channelToPressure.get(channel) 
    # add more function implementation here!

#class PressureCtrlWrapper(Enum):
class PressureCtrlWrapper(Wrapper.Wrapper):
#   PRECI=1
    _impl=0
    def __init__(self, eImplType):
        if eImplType==1:
            self._impl=PressureCtrlWrapperImplPreci()
        else:
            self._impl=PressureCtrlWrapperImplPreci() #default implementation
# switcher={
#         1:PressureCtrlWrapperImplPreci
# }
# self.Impl=switcher.get(PRECI,PressureCtrlWrapperImplPreci) """
    def connect(self):
        self._impl.connect()
    def disconnect(self):
        self._impl.disconnect()
    def setPressure(self, channel, pressure):
        self._impl.setPressure(channel, pressure)
    def readPressure(self,channel)->float:
        return self._impl.readPressure(channel)


def test_code() -> None:
    rWrpper=PressureCtrlWrapper(1)
    rWrpper.connect()
    rWrpper.setPressure(1,1.34)
    pressure=rWrpper.readPressure(1)
    print("PressureCtrl's channel 1 presure is",pressure)
    rWrpper.disconnect()

if __name__ == "__main__":
    test_code()
    