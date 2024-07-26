import time
import multiprocessing
from playsound import playsound

class Alarm:
    def __init__(self,hr,mini):
        self.hr = hr
        self.mini = mini
    
    def check(self):
        while not(self.hr == int(time.strftime('%H')) and self.mini == int(time.strftime('%M'))):
            time.sleep(1)
        else:
            self.sound()

    def sound(self):
        # print('\n\nWakeUp!!!!!\n')
        playsound('alarm_tone.wav')

if __name__ == '__main__':
    alarms = []
    while True:
        if input("Enter '+' to add another alarm:") == '+':
            hr = int(input('Enter the hour:'))
            mini = int(input('Enter the minute:'))
            alarm = Alarm(hr,mini)
            p = multiprocessing.Process(target=alarm.check)
            alarms.append(p)
            p.start()
        else:
            print('All alarms set')
            break

    for i in alarms:
        i.join()
    


    






    

    


    


