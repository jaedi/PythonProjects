import pyautogui
import time
import string
import random

#This is the number of random string generated.
numberOfRandomString=10
#Ask how many number of comments you want.
val = int(input("Enter number of comments: "))

#Time Delay to find a text field (eg. facebook commentbox, etc.)
timeDelay=5
#You have 5 seconds to select your text field input
print("\n You have " + str(timeDelay) + " seconds to select your text field input...")
time.sleep(timeDelay)

for i in range(val):
    randomString = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(numberOfRandomString))
    print("\nFinished: " + str(i+1))
    pyautogui.typewrite(randomString)
    pyautogui.typewrite("\n")
    time.sleep(2)