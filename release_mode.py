from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.comm.motion_switcher.motion_switcher_client import MotionSwitcherClient
import time

ChannelFactoryInitialize(0, "en0")

time.sleep(2)

msc = MotionSwitcherClient()

print("msc init")
msc.Init()

print("release mode")
ret = msc.ReleaseMode()

print("Return: ", ret)
print("Motion mode released successfully")