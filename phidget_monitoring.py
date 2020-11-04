#Add Phidgets Library files
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.HumiditySensor import *
from Phidget22.Devices.LightSensor import *
from Phidget22.Devices.SoundSensor import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.VoltageInput import *

#Required for sleep statement
import time

#Create
statusLED = DigitalOutput()
sound = SoundSensor()
light = LightSensor()
humidity = HumiditySensor()
temperature = TemperatureSensor()
motion = VoltageInput()


#address
statusLED.setIsHubPortDevice(True)
statusLED.setHubPort(0)

motion.setIsHubPortDevice(True)
motion.setHubPort(4)

#Open
statusLED.openWaitForAttachment(1000)
sound.openWaitForAttachment(1000)
light.openWaitForAttachment(1000)
humidity.openWaitForAttachment(1000)
temperature.openWaitForAttachment(1000)
motion.openWaitForAttachment(1000)

#Use your Phidgets
while(True):
    print(sound.getdB(), light.getIlluminance(), humidity.getHumidity(), temperature.getTemperature(), motion.getVoltage())
    statusLED.setState(not(statusLED.getState()))
    time.sleep(0.5)
  


