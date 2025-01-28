from controller import Robot, Motor
import numpy as np

TIME_STEP = 64

MAX_SPEED = 6.28
# create the Robot instance.
robot = Robot()

# get the motor devices
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
# set the target position of the motors
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Distance Sensors
ds = []
for i in range(8):
    ds.append(robot.getDevice('ps'+ str(i)))
    ds[-1].enable(TIME_STEP)
# Light Sensors
ls = []
for i in range(8):
    ls.append(robot.getDevice('ls' + str(i)))
    ls[-1].enable(TIME_STEP)
 
while robot.step(TIME_STEP) != -1:
    
   distance_sensor_values = []
   for sensor in ds:
       distance_sensor_values.append(sensor.getValue())
   
   distance_sensor_values = np.asarray(distance_sensor_values)
   distance_sensor_values = distance_sensor_values / 400 * MAX_SPEED
   #print(distance_sensor_values)
   
   light_sensor_values = []
   for sensor in ls:
       light_sensor_values.append(sensor.getValue())
   
   light_sensor_values = np.asarray(light_sensor_values)
   light_sensor_values = light_sensor_values / 31415 * MAX_SPEED
   print(light_sensor_values)
   
   left_tire = MAX_SPEED - distance_sensor_values[0] - distance_sensor_values[1] - distance_sensor_values[2] + light_sensor_values[7] + light_sensor_values[6] + light_sensor_values[5] - light_sensor_values[3] - light_sensor_values[4]
   right_tire = MAX_SPEED - distance_sensor_values[7] - distance_sensor_values[6] - distance_sensor_values[5] + light_sensor_values[0] + light_sensor_values[1] + light_sensor_values[2] - light_sensor_values[3] - light_sensor_values[4]
   
   leftMotor.setVelocity(left_tire)
   rightMotor.setVelocity(right_tire)
   pass