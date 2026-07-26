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

