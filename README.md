
# Robot Motion Control

This project is a simple robot motion control program written for the Webots simulation environment. The robot's motors are controlled using an array of proximity sensors (ps0 to ps7). The sensor values are used to adjust the speed of the left and right motors to guide the robot.

## Description

The robot has two motors (left and right), and eight proximity sensors (ps0 to ps7). The proximity sensors are used to sense the surroundings and the robot adjusts its movement based on these sensor inputs.

- The sensor readings are scaled to determine the motor speeds.
- The robot will move according to the inputs from the sensors, and the speed of the motors is adjusted dynamically.
- The program runs in a loop where it constantly reads the sensor values and updates the motor speeds accordingly.

## Requirements

This project is designed to be run in the Webots simulator. Ensure that you have Webots installed on your machine to run the simulation.

### Installation Steps:

1. Install Webots: [Webots Installation Guide](https://cyberbotics.com/doc/guide/installation)
2. Clone or download this repository to your local machine.
3. Set up your robot model in Webots (if not already set).
4. Run the program to control the robot using proximity sensor inputs.

## How to Run

1. Open the Webots simulation environment.
2. Load the robot model with the required motors and sensors.
3. Set the `TIME_STEP` and motor parameters based on your setup.
4. Run the script inside the Webots environment to see the robot in action.

```bash
$ python robot_motion_control.py
```

### Notes

- The motor speed is calculated dynamically based on the proximity sensor values.
- The program uses NumPy to process the sensor readings and scale them for motor speed adjustments.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
