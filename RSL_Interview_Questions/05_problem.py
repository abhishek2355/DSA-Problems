# Write code for the angle between the "Minute hand" and "hour hand".
# Link: https://leetcode.com/problems/angle-between-hands-of-a-clock/

def ans(hour, minutes):
    hr = 30 * (hour % 12 + (minutes / 60))   # 360 / 12
    mi = minutes * 6  # 360 / 60
    angle = abs(hr - mi)
    
    if(angle > 180):
        return 360 - angle
    else:
        return angle

print(ans(12, 30))