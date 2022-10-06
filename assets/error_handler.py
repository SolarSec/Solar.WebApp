"""
    Edit any functions return statements as a error that will be outputted to the main functions.
"""

#Handle ARGUMENT error.
def handle_argerr () -> dict:
    return "python {} Webserver_port rate_limit_port debug\n Webserver_port: int, rate_limit_timeout: int, debug: bool"

#Handle No_ID error | Flask
def flask_noiderr () -> dict:
    return dict({"Error" : "You have to specify a ID. http://..../api/v1/scripts?id=...."})

#Handle Incorrect data_type error | Flask
def flask_dterror () -> dict:
    return dict({"Error" : "The ID parameter you've provided must be a string, not {}"})
