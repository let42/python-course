# This is a tutorial about math functions
import math

# function that calculate the ratio between signal and noise power
# and return the decibel value 
def decibelCalc(signal_power, noise_power):
    ratio = signal_power / noise_power
    return 10.0 * math.log10(ratio)

# Simple function that call sin function to calculate the sin of
# radians express
def sinCalc(radians):
    # Sin of a radian
    return math.sin(radians)

# function that convert degrees to radiant
def d2r (degrees):
    return degrees / 360.0 * 2 * math.pi

def main():
    
    signal_power = 0
    noise_power = 0
    # this try manage the user input and relative conversion to float
    try:
        signal_power = raw_input("Insert the signal power >>>")
        noise_power = raw_input("Insert the noise power >>>")
        signal_power = float(signal_power)
        noise_power = float(noise_power)
    except:
        print "Insert what i say"
        exit()
    # call the function to calc decibel and print the value
    print decibelCalc(signal_power, noise_power)

    degrees = 0

    try:
        degrees = raw_input("Insert the degrees of an angle >>>")
        degrees = float(degrees)
    except:
        print "Insert what i say"
        exit()
    
    print sinCalc(d2r(degrees))

    radians = 0
    try:
        radians = raw_input("Insert a radian value >>>")
        radians = float(radians)
    except:
        print "Insert what i say"
        exit()
     
    print sinCalc(radians)
    exit()

main()