import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

class Sphero() :

    def __init__(self, buletooth) :
        # self.toy = scanner.find_toy(
        #     toy_name = buletooth,
        # )
        print(buletooth)

    def sphero(self) :
        with SpheroEduAPI(self.toy) as droid:
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