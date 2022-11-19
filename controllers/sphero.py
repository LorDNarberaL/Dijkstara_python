import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

if __name__ == "__main__" :
    toy = scanner.find_toy()
    with SpheroEduAPI(toy) as droid:
        droid.set_main_led(Color(r=255, g=0, b=0))
        # droid.set_speed(60)
        time.sleep(2)
        # droid.set_speed(0)
        droid.roll(0, 10, 0)
        time.sleep(5)
        droid.roll(90, 10, 0)