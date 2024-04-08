"""
# Problem Stetment:
Find the angle between hour and minute hand when time is 3:30
"""

def angle(hrr, mii):
    hr = 30 * (hrr % 12 + (mii / 60))
    mi = 6 * mii
    angle = abs(hr - mi)

    return 360 - angle if angle > 180 else angle

hr = int(input())
mi = int(input())
print(angle(hr, mi))
