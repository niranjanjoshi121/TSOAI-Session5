import timeit
import math
def squared_powered_list(base, start=0, end=0):
    x = []
    if base < 1:
        raise ValueError("While -ve base should work, not supporting this at the moment");

    if start > end:
        raise ValueError("End should be greater than start");
    elif start <0 or end < 0:
        raise ValueError("While -ve powers should work, not supporting this at the moment");

    for i in range(start, end+1):
        x.append(int(base)**i);
    return x;

def temp_converter(temp, temp_given_in='f'):
    if temp_given_in == 'f':
        return (temp -32)*5/9;
    elif temp_given_in == 'c':
        return (9*temp/5 + 32);
    else:
        raise ValueError("Invalid temperature metric" + temp_given_in);

def polygon_area(side_len, sides = 3):
    if sides < 3:
        raise ValueError("Invalid number of sides for polygon. Require minimum 3");
    elif sides > 6:
        raise ValueError("While polygons with sides > 6 should work, not supporting this at the moment");
    angle= math.pi*(sides-2)/sides;
    a = side_len*math.tan(angle/2)/2;
    return a*sides*side_len/2;

def speed_converter(speed, dist='km', time='hr'):
    if speed < 0:
        raise ValueError("Invalid speed. Speed can not be -ve");

    dist_factor = 1
    time_factor = 1
    if dist == 'km':
        dist_factor = 1;
    elif dist == 'm':
        dist_factor = 1000;
    elif dist == 'ft':
        dist_factor = 3280.839895;
    elif dist == 'yrd':
        dist_factor = 1093.613298;
    else:
        raise ValueError("Invalid distance metric" + dist);

    if time == 'hr':
        time_factor = 1;
    elif time == 'min':
        time_factor = 60;
    elif time == 's':
        time_factor = 60*60;
    elif time == 'ms':
        time_factor = 60*60*1000;
    elif time == 'day':
        time_factor = 1/24;
    else:
        raise ValueError("Invalid distance metric" + time);

    return speed*dist_factor/time_factor;

def time_it(fn, *args, repetitions= 1, **kwargs):
    start = timeit.timeit()
    for i in range(0, repetitions):
       fn(*args,**kwargs)
    end = timeit.timeit()

    return (end - start)/repetitions

