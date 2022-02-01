import os

cmd = 'echo $(/opt/vc/bin/vcgencmd measure_temp) | cut -c 6- | cut -c -4'
os.system(cmd)