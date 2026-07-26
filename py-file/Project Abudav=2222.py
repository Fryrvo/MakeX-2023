
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

