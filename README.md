# Session-5 assignment: 
## time_it function to time various functions with variable arguments

## Problem statement
### This assignment consists of writing time_it function that runs a given function for given number of iterations and returns average run time per iteration.

* Write a function which gives out average run time per call, such that it's definition is:

 def time_it(fn, *args, repetitions= 1, **kwargs):

#### We should be able to call it like this:

* time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitions=5)
* time_it(squared_power_list, 2, start=0, end=5, repetitions=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
* time_it(polygon_area, 15, sides = 3, repetitions=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
* time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100) # 100 is the base temperature given to be converted
* time_it(speed_converter, 100, dist='km', time='min', repetitions=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph
* It implements these functions (with exactly the same names)

### Description of various functions

* print is the regular print function which takes variable number of arguments with optional sep and end for formatting.
* squared_powered_list that takes a positional required argument base, positional optional arguments start and end indicating the range and computes start to end powers of the given base. 
* polygon_area that takes a required positional argument side_len indicating the length of the side, an optional positional argument sides with default value of 3 and returns the area of regular polygon with specified number of sides and the length of each side. The function raises an appropriate Value error if no of sides are less than 3. The function supports polygons only upto the number of sides 6 and raise the appropriate Value error if sides is > 6.
* temp_converter that converts a given temperature value specified in given unit (either Fahreinheit or Celsius) and converts the value in other unit. It takes a required positional argument temperature and an optional positional argument temp_given_in with default value 'f' indicating the unit Fahreinheit. temp_given_in can also take value 'c' indicating the unit Celsius. The function raises a value error if the temp_given_in is set to anything other than 'f' or 'c'. 
* speed_converter that takes a required positional argument speed specifying given value of speed in km/hr and optional arguments dist indicating the required unit of dist and time specifying required unit of time. The function converts given speed in km/hr into unit specified by dist and time. speed can take only non-negative values and function raises an appropriate error if speed is negative.  dist can take one of km , m , ft or yrd and nothing else. The function raises an appropriate value error if dist is set to anything other than one of these supported values. time can take one of hr , min , s , ms , day and nothing else. The function raises an appropriate value error if time is set to anything other than one of these supported values.
* time_it function that takes fn as a required positional argument indicating the function to time, followed by args - variable set of arguments to be passed to the function, followed by another argument repetitions indicating number of iterations the given function should be executed for, and at last kwargs for any other set of argument.
* The time_it function starts the timer, executes the given function for specified number of iterations, ends the timer and returns the average time taken per iteration of the function.
### The following tests are used to validate the functions above:
* test_readme_exists() - Checks if this file i.e. README.md exists or not
* test_readme_contents() - Checks if this file i.e. README.md contains more than 500 words.
* test_readme_proper_description() - Checks if this file i.e. README.md has valid contents by checking against a set of relevant keywords     (e.g. function names used in session4.py) 
* test_readme_file_for_formatting() - Checks if this file i.e. README.md has appropriate formatting.
* test_indentations() - Checks if the indentation is correct or not by ensuring the number of spaces in the code is a multiple of 4.
* test_function_name_had_cap_letter() - Checks if the function names has a capital letter in it or not.* test_addition():
* test_print():
* test_squared_powered_list_default_args():
* test_squared_powered_list_valid_args():
* test_squared_powered_list_invalid_args():
* test_polygon_area_default_args():
* test_polygon_area_valid_args():
* test_polygon_area_invalid_args():
* test_temp_converter_default_args():
* test_temp_converter_valid_args():
* test_temp_converter_invalid_args():
* test_speed_converter_default_args():
* test_speed_converter_invalid_args():
* test_speed_converter_valid_args():
* test_time_it_print():
* test_time_it_squared_powered_list():
* test_time_it_polygon_area():
* test_time_it_temp_converter():
* test_time_it_speed_converter():
