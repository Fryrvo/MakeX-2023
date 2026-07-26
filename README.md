# MakeX - 2023: Robotics Competition Explorer (Abu Dhabi)

code my team used in the **MakeX Robotics Competition (Explorer category) 2023** in Abu Dhabi. 

more infomation about it is here! **[MakeX](https://res-cn.makeblock.com/makex/doc/2022-2023%20Season%20MakeX%20Explorer%20Eco-Pioneer%20Rules%20Guide%20V2.0.pdf)**

Against all odds, this code get **4th place (3rd runner-up)** for my team! 

I built this entire project using block coding because I can't remember the Python scripts.
we were the only team in the entire competition using block code, and we still landed right near the top. 

The repository includes a mix of `.mblock` files and generated Python scripts.

this is my work from scratch.

* **Software Used:** mBlock & VS Code.

---
### Code Preview

<details>
<summary>WHateverThisis</summary>

 ```text
import event, time, cyberpi, mbot2, mbuild
import time
# initialize variables
bp = 0
kp = 0
lp = 0
rp = 0
Chaang = 0
startpoint = 0
turnleft = 0
turnright = 0

@event.start
def on_start():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.console.print("Loading-------")
    cyberpi.led.show('green black black black black')
    time.sleep(0.1)
    cyberpi.led.show('green green black black black')
    time.sleep(0.2)
    cyberpi.led.show('green green green black black')
    time.sleep(0.3)
    cyberpi.led.show('green green green green black')
    time.sleep(0.4)
    cyberpi.led.show('green green green green green')
    time.sleep(0.5)
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    cyberpi.console.clear()
    cyberpi.console.print("StartComplet")
    time.sleep(0.5)
    cyberpi.console.clear()
    Chaang = 1
    cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)
    cyberpi.console.print(Chaang)
    if Chaang == 1:
      cyberpi.display.show_label("blue/right", 16, "center", index= 0)
      cyberpi.led.show('blue blue blue blue purple')

def c():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.servo_drive(90,90,105,75)

def o():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.servo_drive(90,90,60,120)

def all():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    o()
    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    c()
    mbot2.EM_stop("ALL")
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    mbot2.backward(20, 1)
    mbot2.turn(-180)
    mbot2.EM_stop("ALL")
    mbot2.forward(20, 1)
    o()
    mbot2.backward(20, 1)
    mbot2.turn(90)

@event.is_press('down')
def is_joy_press():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.stop_other()
    Chaang = Chaang + -1
    cyberpi.console.clear()
    cyberpi.console.print(Chaang)
    cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)
    cyberpi.led.off("all")
    if Chaang > 4:
      cyberpi.console.clear()
      Chaang = 1
      cyberpi.console.print(Chaang)
      cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)

    if Chaang < 1:
      cyberpi.console.clear()
      Chaang = 4
      cyberpi.console.print(Chaang)
      cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)

    if Chaang == 1:
      cyberpi.display.show_label("blue/right", 16, "center", index= 0)
      cyberpi.led.show('blue blue blue blue purple')

    if Chaang == 2:
      cyberpi.display.show_label("blue/left", 16, "center", index= 0)
      cyberpi.led.show('purple blue blue blue blue')

    if Chaang == 3:
      cyberpi.display.show_label("Red/right", 16, "center", index= 0)
      cyberpi.led.show('red red red red purple')

    if Chaang == 4:
      cyberpi.display.show_label("Red/left", 16, "center", index= 0)
      cyberpi.led.show('purple red red red red')

@event.is_press('up')
def is_joy_press1():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.stop_other()
    Chaang = Chaang + 1
    cyberpi.console.clear()
    cyberpi.console.print(Chaang)
    cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)
    cyberpi.led.off("all")
    if Chaang > 4:
      cyberpi.console.clear()
      Chaang = 1
      cyberpi.console.print(Chaang)
      cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)

    if Chaang < 1:
      cyberpi.console.clear()
      Chaang = 4
      cyberpi.console.print(Chaang)
      cyberpi.display.show_label("<---Left....Right--->", 16, "bottom_mid", index= 7)

    if Chaang == 1:
      cyberpi.display.show_label("blue/right", 16, "center", index= 0)
      cyberpi.led.show('blue blue blue blue purple')

    if Chaang == 2:
      cyberpi.display.show_label("blue/left", 16, "center", index= 0)
      cyberpi.led.show('purple blue blue blue blue')

    if Chaang == 3:
      cyberpi.display.show_label("Red/right", 16, "center", index= 0)
      cyberpi.led.show('red red red red purple')

    if Chaang == 4:
      cyberpi.display.show_label("Red/left", 16, "center", index= 0)
      cyberpi.led.show('purple red red red red')

@event.is_press('middle')
def is_joy_press2():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.stop_other()
    if Chaang < 1:
      cyberpi.console.clear()
      cyberpi.console.print("invalid number")
      cyberpi.led.show('red orange orange orange red')

    if Chaang == 1:
      NotComplet()
      mbot2.EM_stop("ALL")
      cyberpi.stop_other()

    if Chaang == 2:
      Blue_Left()
      mbot2.EM_stop("ALL")
      cyberpi.stop_other()
      mbot2.forward(50, 0.5)
      worklight()

    if Chaang == 3:
      worklight()
      mbot2.EM_stop("ALL")
      cyberpi.stop_other()
      mbot2.forward(50, 0.5)
      Red_Right()

    if Chaang == 4:
      NotComplet()
      mbot2.EM_stop("ALL")
      cyberpi.stop_other()

    if Chaang > 4:
      cyberpi.console.clear()
      cyberpi.console.print("function not support")
      cyberpi.led.show('red orange orange orange red')

@event.is_press('b')
def is_btn_press():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.display.show_label("Manual", 16, "center", index= 0)
    cyberpi.stop_other()
    NotComplet()

@event.is_press('right')
def is_joy_press3():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    find()
    all()
    find()
    all()
    find()
    all()
    find()

@event.is_press('left')
def is_joy_press4():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.console.clear()
    cyberpi.stop_other()
    while True:
      cyberpi.console.println(mbuild.quad_rgb_sensor.get_color_sta("R2",1))
      cyberpi.display.show_label(mbuild.quad_rgb_sensor.get_offset_track(1), 16, "top_right", index= 3)
      time.sleep(0.1)

def find():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

@event.is_press('a')
def is_btn_press1():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.stop_other()
    cyberpi.console.clear()
    cyberpi.console.print("Reset")
    cyberpi.led.show('purple purple purple purple purple')
    cyberpi.restart()

def Red_Right():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(1, 208, 43, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    cyberpi.console.clear()
    time.sleep(1)
    cyberpi.led.show('red orange yellow green cyan')
    time.sleep(1)
    while not ((mbuild.quad_rgb_sensor.is_color("red","R1",1)) or (mbuild.quad_rgb_sensor.is_color("red","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(5)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(1, 208, 43, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)

def Blue_Left():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(1, 208, 43, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    cyberpi.console.clear()
    time.sleep(1)
    cyberpi.led.show('red orange yellow green cyan')
    time.sleep(1)
    while not ((mbuild.quad_rgb_sensor.is_color("blue","R1",1)) or (mbuild.quad_rgb_sensor.is_color("blue","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(5)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(1, 208, 43, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(90)
    while not ((mbuild.quad_rgb_sensor.is_color("yellow","R1",1)) or (mbuild.quad_rgb_sensor.is_color("yellow","L1",1))):
      Walk()

    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")
    cyberpi.led.on(0, 42, 208, "all")
    time.sleep(1)
    cyberpi.led.on(0, 0, 0, "all")
    time.sleep(1)
    mbot2.backward(20, 1)
    mbot2.turn(-90)

def Walk():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    bp = 60
    kp = 0.7
    lp = (bp - kp * mbuild.quad_rgb_sensor.get_offset_track(1))
    rp = -1 * ((bp + kp * mbuild.quad_rgb_sensor.get_offset_track(1)))
    mbot2.drive_speed(lp, rp)

def l1001():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.turn_left(50, 0.2)
    while not mbuild.quad_rgb_sensor.get_ground_sta("all", 1) == 9:
      mbot2.turn_left(50)

    mbot2.motor_stop("all")

def r1001():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.turn_right(50, 0.2)
    while not mbuild.quad_rgb_sensor.get_ground_sta("all", 1) == 9:
      mbot2.turn_right(50)

    mbot2.motor_stop("all")

def my_000():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    while not mbuild.quad_rgb_sensor.get_ground_sta("all", 1) == 0:
      Walk()

    mbot2.motor_stop("all")

def ry():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")

def ly():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    mbot2.EM_stop("ALL")
    mbot2.straight(10)
    mbot2.turn(-90)
    mbot2.forward(20, 1)
    mbot2.EM_stop("ALL")

def worklight():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.console.clear()
    cyberpi.console.print("RunningCode")
    cyberpi.led.on(1, 208, 132, "all")
    time.sleep(3)
    cyberpi.led.on(0, 0, 0, "all")
    cyberpi.led.play('rainbow')

def NotComplet():
    global bp, kp, lp, rp, Chaang, startpoint, turnleft, turnright
    cyberpi.led.on(208, 2, 27, "all")
    time.sleep(3)
    cyberpi.led.on(0, 0, 0, "all")
    cyberpi.led.off("all")
    cyberpi.console.clear()
    cyberpi.console.print("Error")


 ```
</details>














<details>
<summary>Project Abudav=2222</summary>

 ```text

import event, time, cyberpi, mbot2, gamepad
# initialize variables
base_power = 0
kp = 0
left_power = 0
right_power = 0

@event.is_press('up')
def is_joy_press():
    global base_power, kp, left_power, right_power
    # energyball
    cyberpi.stop_other()
    mbot2.servo_set(90,"S1")
    mbot2.servo_set(90,"S2")
    mbot2.servo_set(60,"S3")
    mbot2.straight(30)
    mbot2.EM_set_speed(-30, "EM2")
    time.sleep(2.6)
    mbot2.EM_stop("EM2")
    mbot2.straight(25)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(15)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.EM_set_speed(30, "EM2")
    time.sleep(1)
    mbot2.EM_stop("EM2")
    mbot2.straight(10)
    mbot2.straight(-10)

@event.is_press('middle')
def is_joy_press1():
    global base_power, kp, left_power, right_power
    # ball rack red
    cyberpi.stop_other()
    mbot2.servo_set(70,"S3")
    mbot2.servo_set(90,"S1")
    mbot2.servo_set(90,"S2")
    mbot2.straight(70)
    mbot2.turn(-45)
    mbot2.forward(50, 0.7)
    mbot2.turn(-45)
    mbot2.straight(40)
    mbot2.turn(-95)
    mbot2.backward(90, 1.2)
    mbot2.forward(50, 1)
    mbot2.servo_release("all")

@event.is_press('b')
def is_btn_press():
    global base_power, kp, left_power, right_power
    # Red Cube2
    cyberpi.stop_other()
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(90,"S4")
    mbot2.straight(29)
    mbot2.servo_set(110,"S1")
    mbot2.servo_set(110,"S2")
    mbot2.straight(-25)
    mbot2.turn(-120)
    mbot2.straight(80)
    mbot2.turn(-50)
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(50,"S2")
    mbot2.straight(-10)

@event.is_press('a')
def is_btn_press1():
    global base_power, kp, left_power, right_power
    # Red  Cube 1
    cyberpi.stop_other()
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(50,"S2")
    mbot2.straight(84)
    mbot2.turn(-75)
    mbot2.straight(7)
    mbot2.straight(-10)

@event.is_press('right')
def is_joy_press2():
    global base_power, kp, left_power, right_power
    # blue cube 2
    cyberpi.stop_other()
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(90,"S4")
    mbot2.straight(29)
    mbot2.servo_set(110,"S1")
    mbot2.servo_set(110,"S2")
    mbot2.straight(-25)
    mbot2.turn(120)
    mbot2.straight(80)
    mbot2.turn(50)
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(50,"S2")
    mbot2.straight(-10)

@event.is_press('down')
def is_joy_press3():
    global base_power, kp, left_power, right_power
    # blue cube 1
    cyberpi.stop_other()
    mbot2.servo_set(90,"S3")
    mbot2.servo_set(50,"S1")
    mbot2.servo_set(50,"S2")
    mbot2.straight(84)
    mbot2.turn(75)
    mbot2.straight(7)
    mbot2.straight(-10)

@event.is_press('left')
def is_joy_press4():
    global base_power, kp, left_power, right_power
    # ball rack blue
    cyberpi.stop_other()
    mbot2.straight(66)
    mbot2.turn(45)
    mbot2.forward(50, 1.1)
    mbot2.turn(45)
    mbot2.straight(69)
    mbot2.turn(-95)
    mbot2.forward(50, 1)
    mbot2.turn(-90)
    mbot2.forward(50, 3.4)
    mbot2.backward(50, 1)

@event.start
def on_start():
    global base_power, kp, left_power, right_power
    while True:
      if gamepad.is_key_pressed('N2'):
        mbot2.servo_set(90,"S1")
        mbot2.servo_set(90,"S2")
        mbot2.servo_set(110,"S3")

      if gamepad.is_key_pressed('N3'):
        mbot2.servo_set(90,"S1")
        mbot2.servo_set(90,"S2")
        mbot2.servo_set(60,"S3")

      if gamepad.is_key_pressed('Left'):
        mbot2.servo_set(110,"S1")
        mbot2.servo_set(110,"S2")

      if gamepad.is_key_pressed('Right'):
        mbot2.servo_set(50,"S1")
        mbot2.servo_set(50,"S2")

      if gamepad.is_key_pressed('Up'):
        mbot2.servo_set(60,"S3")

      if gamepad.is_key_pressed('Down'):
        mbot2.servo_set(90,"S3")

      if False:
        mbot2.drive_power(-100, 100)

      else:
        mbot2.drive_power(gamepad.get_joystick('Ly') / 1.8, -1 * (gamepad.get_joystick('Ry') / 1.8))

      if False:
        mbot2.drive_power(100, -100)

      else:
        mbot2.drive_power(gamepad.get_joystick('Ly') / 1.8, -1 * (gamepad.get_joystick('Ry') / 1.8))


         ```
</details>


```
