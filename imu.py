from pymavlink import mavutil
import sys

fc = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)
if not fc.wait_heartbeat(timeout=10):
    print("no heartbeat")
    sys.exit(0)
else: 
    print("recieved heartbeat")

# Request HIGHRES_IMU (Message ID 105) at 10Hz (100,000 microseconds)
fc.mav.command_long_send(
    fc.target_system, fc.target_component,
    mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
    105, # Message ID for HIGHRES_IMU
    100000, # Interval in microseconds (10Hz)
    0, 0, 0, 0, 0
)

while True:
    # wait for highres_imu packet
    msg = fc.recv_match(type='HIGHRES_IMU', blocking=True)
    
    if msg:
        # Access the fields using the exact names from the documentation
        x_accel = round(msg.xacc, 2)
        z_gyro = round(msg.zgyro, 2)
        temp = round(msg.temperature, 1)
        
        print(f"Forward Accel: {x_accel} m/s² | Yaw Spin: {z_gyro} rad/s | Temp: {temp}°C")
    else:
        print("waiting for imu packet")
