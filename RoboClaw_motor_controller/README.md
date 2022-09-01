# RoboClaw Instructions:

1. Wire your roboclaw following [these instructions](https://resources.basicmicro.com/roboclaw-motor-controllers-getting-started-guide/). **Only use steps 1-3**
2. Notes:
    - Power supply MUST be Equal to or Greater than 9V. 6V battery sources won't work. 
    - Ignore step 2, we're not using encoders in this class
3. 

# RoboClaw not working with CircuitPython? Steps to solve:

1. Be sure RoboClaw has at least 9V battery source. 6V battery sources will not chooch 'er, you'll get a constant "logic battery low" error. 
2. Be sure the RC is in the correct mode, via the onboard buttons. 
    - Tank style bots, Mode 1 Opt 4
    - Differential style bots, Mode 2, Opt 4
        ### Set *Mode*
        - Press and release the MODE button to enter mode setup. The STAT2 LED will begin to
        blink out the current mode. Each blink is a half second with a long pause at the end of the
        count. Five blinks with a long pause equals mode 5 and so on.
        - Press SET to increment to the next mode. Press MODE to decrement to the previous
        mode.
        - Press and release the LIPO button to save this mode to memory.
        ### Set Mode *Option* 
        - After the desired mode is set and saved press and release the SET button for options
        setup. The STAT2 LED will begin to blink out the current option setting.
        - Press SET to increment to the next mode. Press MODE to decrement to the previous
        mode.
        - Press and release the LIPO button to save this mode to memory.

You'll know you're successful when STAT1 starts to blink/flash rapidly, indicating it is recieving RC signals. 

## Advanced Fix Steps:

1. Power on RC
2. Connect RC to motion studio in windows PC, connect device. 
    - Note, you need the RC firmware drivers AND basic micro motion studio installed. 
3. Update firmware if needed. 
4. Basic micro settings:
    - RC mode w/ 3 checks enabled, everything else default:
    - Mixing
    - Exponetial
    - MCU
5. Motors should start chooching if your code is correct. 
6. Verify motors function via PWM sliders. 
