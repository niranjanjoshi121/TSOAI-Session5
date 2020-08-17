import pytest
import random
import string
import session5
import os
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
    'time_it',
    'print', 
    'squared_powered_list', 
    'polygon_area',
    'temp_converter', 
    'speed_converter', 
    'repetitions',
    'sep',
    'start',
    'end', 
    'temp_given_in', 
    'dist',
    'time', 
    'km', 
    'ft',
    'm', 
    'yrd',
    'ms',
    's',
    'min',
    'hr',
    'day',
    'args',
    'kwargs'
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            print("Didn't find string" + c)
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_print():
    print(1, 2, 3, sep='-', end= ' ***\n')
    print(1, 4, 3, sep='/', end= ' ***\n')

def test_squared_powered_list_default_args():
    result = session5.squared_powered_list(2)

def test_squared_powered_list_valid_args():
    s = 0
    e = 5 
    result = session5.squared_powered_list(2, start=s, end=e)
    assert len(result) == (e - s + 1), "Size of result not equal to given range"
    for i in range(s, e+1):
        assert (result[i-s] == 2**i), "squared_powered_list failed to generate correct results"
    s = 2
    e = 2 
    result = session5.squared_powered_list(6, start=s, end=e)
    assert len(result) == (e - s + 1), "Size of result not equal to given range"
    for i in range(s, e+1):
        assert (result[i-s] == 6**i), "squared_powered_list failed to generate correct results"
    s = 6
    e = 15 
    result = session5.squared_powered_list(2, start=s, end=e)
    assert len(result) == (e - s + 1), "Size of result not equal to given range"
    for i in range(s, e+1):
        assert (result[i-s] == 2**i), "squared_powered_list failed to generate correct results"

def test_squared_powered_list_invalid_args():
    with pytest.raises(ValueError):
        session5.squared_powered_list(2, start=4, end=3)
    with pytest.raises(ValueError):
        session5.squared_powered_list(2, start=-2, end=0)
    with pytest.raises(ValueError):
        session5.squared_powered_list(2, start=-2, end=-1)

def test_polygon_area_default_args():
    result = session5.polygon_area(15)

def test_polygon_area_valid_args():
    result = session5.polygon_area(15, sides = 4)
    assert math.isclose(result,15*15), "polygon_area failed to generate correct results"
    result = session5.polygon_area(15, sides = 3)
    assert math.isclose(result, math.sqrt(3)*15*15/4), "polygon_area failed to generate correct results"
    result = session5.polygon_area(15, sides = 6)
    assert math.isclose(result, 6*math.sqrt(3)*15*15/4), "polygon_area failed to generate correct results"

    
def test_polygon_area_invalid_args():
    with pytest.raises(ValueError):
        session5.polygon_area(15, sides = 2)
    with pytest.raises(ValueError):
        session5.polygon_area(15, sides = -1)
    with pytest.raises(ValueError):
        session5.polygon_area(15, sides = 7)

def test_temp_converter_default_args():
    result = session5.temp_converter(100)
    assert result == (100 -32)*5/9, "Temperature conversion failed to generate correct results"

def test_temp_converter_valid_args():
    result = session5.temp_converter(100, temp_given_in = 'f')
    assert result == (100 -32)*5/9, "Temperature conversion failed to generate correct results"
    result = session5.temp_converter(-100, temp_given_in = 'c')
    assert result == (-100*9/5 + 32), "Temperature conversion failed to generate correct results"

def test_temp_converter_invalid_args():
    with pytest.raises(ValueError):
        result = session5.temp_converter(100, temp_given_in = 'd')

def test_speed_converter_default_args():
    result = session5.speed_converter(100)
    result = session5.speed_converter(100, dist='m')
    result = session5.speed_converter(100, time='s')

def test_speed_converter_invalid_args():
    with pytest.raises(ValueError):
        result = session5.speed_converter(-20, dist='mm', time='yr')
    with pytest.raises(ValueError):
        result = session5.speed_converter(100, dist='km', time='yr')
    with pytest.raises(ValueError):
        result = session5.speed_converter(100, dist='mm', time='yr')

def test_speed_converter_valid_args():
    result = session5.speed_converter(100, dist='km', time='day')
    result = session5.speed_converter(100, dist='km', time='hr')
    result = session5.speed_converter(100, dist='km', time='min')
    result = session5.speed_converter(100, dist='km', time='s')
    result = session5.speed_converter(100, dist='km', time='ms')

    result = session5.speed_converter(120, dist='m', time='day')
    result = session5.speed_converter(120, dist='m', time='hr')
    result = session5.speed_converter(120, dist='m', time='min')
    result = session5.speed_converter(120, dist='m', time='s')
    result = session5.speed_converter(120, dist='m', time='ms')
    
    result = session5.speed_converter(36, dist='yrd', time='day')
    result = session5.speed_converter(36, dist='yrd', time='hr')
    result = session5.speed_converter(36, dist='yrd', time='min')
    result = session5.speed_converter(36, dist='yrd', time='s')
    result = session5.speed_converter(36, dist='yrd', time='ms')

    result = session5.speed_converter(50, dist='ft', time='day')
    result = session5.speed_converter(50, dist='ft', time='hr')
    result = session5.speed_converter(50, dist='ft', time='min')
    result = session5.speed_converter(50, dist='ft', time='s')
    result = session5.speed_converter(50, dist='ft', time='ms')

def test_time_it_print():
    time_taken = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=500)
    assert ( time_taken >= 0), "Time taken can not be negative, but can be negligible and close to 0"

def test_time_it_squared_powered_list():
    time_taken = session5.time_it(session5.squared_powered_list, 2, start=0, end=5, repetitions=5000)
    assert ( time_taken >= 0), "Time taken can not be negative, but can be negligible and close to 0"

def test_time_it_polygon_area():
    time_taken  = session5.time_it(session5.polygon_area, 15, sides = 3, repetitions=1000)
    assert ( time_taken >= 0), "Time taken can not be negative, but can be negligible and close to 0"

def test_time_it_temp_converter():
    time_taken  = session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitions=1000)
    assert ( time_taken >= 0), "Time taken can not be negative, but can be negligible and close to 0"

def test_time_it_speed_converter():
    time_taken  = session5.time_it(session5.speed_converter, 100, dist='km', time='min', repetitions=2000)
    assert ( time_taken >= 0), "Time taken can not be negative, but can be negligible and close to 0"
