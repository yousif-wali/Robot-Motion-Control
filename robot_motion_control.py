from controller import Robot, Motor
import numpy as np
import time

# Constants
TIME_STEP = 64
MAX_SPEED = 6.28
AVOID_DURATION = 10
BACKWARD_DURATION = 3

# Create the Robot instance
robot = Robot()

# Initialize motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motors to velocity mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Helper function to initialize sensors
def initialize_sensors(sensor_prefix, count):
    sensors = []
    for i in range(count):
        sensor = robot.getDevice(f"{sensor_prefix}{i}")
        sensor.enable(TIME_STEP)
        sensors.append(sensor)
    return sensors

# Initialize distance and light sensors
distance_sensors = initialize_sensors('ps', 8)
light_sensors = initialize_sensors('ls', 8)

# Normalize sensor values
def normalize_sensor_values(sensors, divisor):
    values = np.asarray([sensor.getValue() for sensor in sensors])
    return (values / divisor) * MAX_SPEED

# Robot state
state = 'FOLLOW'
avoid_start_time = None

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Read and normalize sensor values
    distance_values = normalize_sensor_values(distance_sensors, 400)
    light_values = normalize_sensor_values(light_sensors, 31415)

    print(f"Distance Sensor Values: {distance_values}")
    # print(f"Light Sensor Values: {light_values}")

    left_tire, right_tire = 0, 0

    # State machine logic
    if state == 'FOLLOW':
        print("The bot is in Follow mode")
        left_tire = (
            MAX_SPEED
            - np.sum(distance_values[:3])  # Front-left sensors
            + np.sum(light_values[5:8])   # Right-side light sensors
            - np.sum(light_values[3:5])   # Center light sensors
        )
        right_tire = (
            MAX_SPEED
            - np.sum(distance_values[5:8])  # Front-right sensors
            + np.sum(light_values[:3])     # Left-side light sensors
            - np.sum(light_values[3:5])    # Center light sensors
        )
        if np.max(distance_values) > 3:
            state = 'AVOID'
            avoid_start_time = time.time()

    elif state == 'AVOID':
        print("The bot is in Avoid mode")
        left_tire = MAX_SPEED - np.sum(distance_values[:3])  # Avoid obstacle by reducing left tire speed
        right_tire = MAX_SPEED - np.sum(distance_values[5:8])  # Avoid obstacle by reducing right tire speed

        if time.time() - avoid_start_time >= AVOID_DURATION:
            state = 'BACKWARD' if np.max(distance_values) > 3 else 'FOLLOW'
            avoid_start_time = time.time()

    elif state == 'BACKWARD':
        print("The bot is in Backward mode")
        left_tire = -MAX_SPEED * 0.25
        right_tire = -MAX_SPEED * 0.25

        if time.time() - avoid_start_time >= BACKWARD_DURATION:
            state = 'AVOID' if np.max(distance_values) > 3 else 'FOLLOW'
            avoid_start_time = time.time()

    # Set motor velocities
    left_motor.setVelocity(left_tire)
    right_motor.setVelocity(right_tire)