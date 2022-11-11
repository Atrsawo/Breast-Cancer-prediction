
from util import utl
from os import system

class Speak:

    def __init__(self) -> None:
        pass
        # lock = threading.Lock()
    
    def say_enter_password(self):
        if utl.password:
            system('say Welcome, please enter your user name and password')

    def say_welome(self):
        if utl.work_station:
            system('say This is artificial intelligence based classification system')
            system('say This system is designed to predict whether the patient whose details you entered may have breast cancer')
            utl.work_station = False
    
    def say_runing_model(self):
        if utl.run:
            system('say raning models')
            utl.run = False
    
    def say_advice_with_experts(self):
        if utl.say:
            system('say Note that even though this result was obtained, additional experts should be consulted')
            utl.say = False
    
    def say_bad_input(self):
        system('say You must fill all cells only with numeric values that greater then zero')

    def say_clearing_cells(self):
        system('say clearing all cells')
    
    def say_ilegal_user_and_password(self):
        system('say elegal user name or password, please enter again')
    
    def say_no_connectaion(self):
        system('say Failed to establish network connection, please raise connection to your server and try again')




