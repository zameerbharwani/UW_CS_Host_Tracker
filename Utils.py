# source: https://www.rosettacode.org/wiki/Averages/Mean_time_of_day#Python

from cmath import rect, phase
from math import radians, degrees

class Utils:
    @staticmethod
    def meanAngle(deg):
        return degrees(phase(sum(rect(1, radians(d)) for d in deg)/len(deg)))

    @staticmethod
    def meanTime(times):
        t = (time.split(':') for time in times)
        seconds = ((float(s) + int(m) * 60 + int(h) * 3600)
                   for h, m, s in t)
        day = 24 * 60 * 60
        to_angles = [s * 360. / day for s in seconds]
        mean_as_angle = Utils.meanAngle(to_angles)
        mean_seconds = mean_as_angle * day / 360.
        if mean_seconds < 0:
            mean_seconds += day
        h, m = divmod(mean_seconds, 3600)
        m, s = divmod(m, 60)
        return '%02i:%02i:%02i' % (h, m, s)
