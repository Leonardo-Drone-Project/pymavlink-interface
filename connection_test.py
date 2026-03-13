from pymavlink import mavutil

# test3
# connect to the jetson's serial port
fc = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)
msg = fc.wait_heartbeat(timeout=10)

if msg is None:
    print("no heartbeat")
else:
    print("yes heartbeat")
    if msg.autopilot == 3:
        print ("ardupilot")
    elif msg.autopilot ==12:
        print("px4")
    else:
        print("unknown")
    
