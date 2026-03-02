from pymavlink import mavutil

# connect to the jetson's serial port
master = mavutil.mavlink_connection('/dev/ttyTHS1', baud=115200)
master.wait_heartbeat()

# 3 = ArduPilot, 12 = PX4
if master.target_autopilot == 3:
    print("ardupilot")
elif master.target_autopilot == 12:
    print("PX4")
else:
    print(f"unknown firmware ID: {master.target_autopilot}")