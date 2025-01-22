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

ds = []
for i in range(8):
    ds.append(robot.getDevice('ps'+ str(i)))
    ds[-1].enable(TIME_STEP)

while robot.step(TIME_STEP) != -1:
    
   sensor_values = []
   for sensor in ds:
       sensor_values.append(sensor.getValue())
   sensor_values = np.asarray(sensor_values)
   sensor_values = sensor_values / 400 * MAX_SPEED
   print(sensor_values)
   
   left_tire = MAX_SPEED - sensor_values[0] - sensor_values[1] - sensor_values[2]
   right_tire = MAX_SPEED - sensor_values[7] - sensor_values[6] - sensor_values[5]
   
   leftMotor.setVelocity(left_tire)
   rightMotor.setVelocity(right_tire)
   pass