import time

def get_current_time ():
    localtime = time.localtime()
    return time.strftime("%Y%M%D %H%M%S", localtime)

def hello_world():
    return "hello world"