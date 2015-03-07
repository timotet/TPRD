# script for figuring TBPRD on C2000 launchpad for pwm 
# and
# to figure timer frequency in 1khz increments


TPWM = 0.133 # .133 fixed TPWM for 7.5 Mhz clock (sysClk / 8)
TBPRD = 180  # 190 to start for 19.8 Khz

def figFreq(TBPRD):
    
    tFreq = (2 * TBPRD) * TPWM
    freq = 1 / tFreq

    return freq * 1000  # for Khz

with open("TBPRD.txt","w") as f:
        f.write("\n")
        f.write("TBPRD.txt \n")
        f.write("This figures the timer period for the EPWM module on the C2000 Launch Pad \n")

        for i in range(0,3600):
            
            f.write("%d \n" % i)
            f.write("TBPRD = %f \n" % TBPRD)
            f.write("PWM frequency = %f Khz \n" % figFreq(TBPRD))
            TBPRD += 1
    
print("DONE")
    
    
    
    

  
