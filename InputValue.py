#Learn Python basics
import datetime
#Taking INPUT
val = str(input("Enter your name: "))
print(val)
print(type(val))
val1 = int(input("Enter your age: "))
print(val1)
print(type(val1))
time_str = input("Enter a time (HH:MM:SS): ")
# Convert string to datetime object
time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
print(time_obj)
#


import signal

class TimeoutExpired(Exception):
    pass

def alarm_handler(signum, frame):
    raise TimeoutExpired

def input_with_timeout(prompt, timeout):
    # Set signal handler
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)  # Produce SIGALRM in `timeout` seconds

    try:
        return input(prompt)
    except TimeoutExpired:
        print('Sorry, time is up')
    finally:
        signal.alarm(0)  # Cancel the alarm

if __name__ == '__main__':
    user_input = input_with_timeout('Enter something: ', 5)
    if user_input is not None:
        print('You entered:', user_input)