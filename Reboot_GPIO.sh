#   Reboot functioning using GPIO
              
# Exports pin 11 as an output
gpio export 11 out

#Shutdown the module
# Sets pin 11 to high
gpio -g write 11 1

sleep 1

# Sets pin 11 to low
gpio -g write 11 0

sleep 40

#Start module again
# Sets pin 11 to high
gpio -g write 11 1

sleep 1

# Sets pin 11 to low
gpio -g write 11 0

# Unexport the pin
gpio unexport 11
#exit
