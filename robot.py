from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(8,7), right = (10,9))
left_sensor = LineSensor(22)
right_sensor= LineSensor(27)
#r = right_sensor.value()
#l = left_sensor.value()
speed = 0.3
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        ## Stage 1
        print(left_detect)
        if left_detect == 0 and right_detect == 0:
            left_mot = 1
            right_mot = 1
        ## Stage 2
        if left_detect == 0 and right_detect == 1:
            left_mot = -1
        if left_detect == 1 and right_detect == 0:
            right_mot = -1
        if left_detect == 1 and right_detect == 1:
            robot.backward()
            left_mot = -1
            robot.forward()
       #print(r, l)
        yield (right_mot * speed, left_mot * speed)


robot.source = motor_speed()

sleep(90)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
