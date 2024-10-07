# How to Connect Omron LD90 by Socket [OMRON ROS Robot Driver]

The OMRON LD-90 is a self-navigating Autonomous Mobile Robot (AMR) that can dynamically move materials in challenging environments, including confined passageways and dynamic, populated locations. With a maximum speed of **1.35 m/s** and a payload capacity of **90 kg**, the LD-90 is designed to meet the latest industry requirements.

It is easy to get up and running, requiring minimal programming and no construction. In addition, its software can integrate with other systems, making it easy to use and deploy.

The LD-90 is designed to interact with people, promoting a collaborative and safe working environment. Its safety lasers and sonar allow the robot to detect obstacles in its path and prevent collisions, ensuring safe operation. Additionally, it can optimize routing and adapt to changing conditions on the fly, making it an intelligent and reliable solution for your automated production needs.

![Omron LD90](https://github.com/user-attachments/assets/4d17860d-b4ad-4e16-8a26-ad46ba7e83de)

![Omron LD90](https://github.com/user-attachments/assets/43f238bd-15bf-4586-8840-1647f2b384cb)

## I Use Python Language to Write and Use Lib Socket to Connect Robot

### Required Parameters

- **Host IP**: String, e.g. `192.168.1.1`
- **Host Port**: String, e.g. `8080`

### Robot Commands

- `b'dock\n'` = The robot returns to the charging station.
- `b'undock\n'` = The robot leaves the charging station.
- `b'stopped\n'` = Order the robot to stop.
- `go` = Prepare to receive orders.
- `b'goto goal' + {Points determined from Omron's website which are numbers.} + b'\n'` = Order to go to the specified goal.
