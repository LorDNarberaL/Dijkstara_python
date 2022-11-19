import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def sphero(bName) :
    print(bName)
    try:
        toy = scanner.find_toy(toy_name=bName,)
        with SpheroEduAPI(toy) as droid:
            print("start")
            droid.reset_aim()
            droid.set_main_led(Color(r=255, g=255, b=255))
            print("A to D")
            time.sleep(2)
            droid.roll(180, 10, 1)

            print("D to E")
            time.sleep(2)
            droid.roll(90, 10, 1)

            print("E to C")
            time.sleep(2)
            droid.roll(45, 20, 1)
            print("Stop")
    except Exception as err:
        print(err.args)