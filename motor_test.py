from pymavlink import mavutil
import time

# connect (change port to /dev/ttyS2 or /dev/ttyTHS1 depending on the board)
print("connecting")
master = mavutil.mavlink_connection('/dev/ttyS2', baud=115200)
master.wait_heartbeat()
print("heartbeat detected")

# arm the drone
# MAV_CMD_COMPONENT_ARM_DISARM: param1=1 to arm
print("starting motors")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0
)

# spin for 3 seconds
time.sleep(3)

# disarm the drone
# MAV_CMD_COMPONENT_ARM_DISARM: param1=0 to disarm
print("disarming motors...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0
)

print("done.")