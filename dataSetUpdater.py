import os
import time

os.system('git add *')
time.sleep(1)
command='git commit -m "Automatic data update"'
os.system(command)
time.sleep(1)
os.system('git push')
time.sleep(1)
print ("Data has been updated")
time.sleep(1)
