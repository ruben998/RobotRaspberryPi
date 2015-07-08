# RobotRaspberryPi
[IN PROGRESS]
A protocol to move of the robot with Raspberry Pi and Pololu Chasis

## Abstract
This protocol is used for the client/server application for a robot with raspberry pi and Pololu chasis

## Table of contents

### 1. Introduction
### 2. The robot specification   
      This section shows the protocol used for the application.
### 2.1 Client Commands Semantics   	  
	First, we defined the commands used by the client, we have six commands.
      
      FRWD
      	This command is used to pull forward with the robot
      BACK
      	This command is used to pull back with the robot
      LEFT
      	This command is used to pull to left with the robot
      RGHT
      	This command is used to pull to right with the robot
      STOP
      	This command is used for stop the robot
      CLSE
      	This command is used for stop the robot and the close application
        
### 2.2 Server Commands Semantics  
### 2.3 Command syntax