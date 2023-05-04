# Human-Hamster-Wheel-Speed-Display
Human Hamster Wheel GUI for displaying speed (arduino code and python)

### GUI
- png file and python code necessary to run GUI
- DO NOT alter the data being read from the serial port in the python file
- rename serial port in the first few lines from "COM5" to the same port the arduino is connected to
- formatting was specified to my specifc computer's fullscreen, so formatting may need adjusting for other computer displays
- Note for EHousers: if you have any questions about the code, reach out to me on the discord, my phone number is also in there somewhere

### Arduino Code
- needs to be attached to the rotary encoder (otherwise it has no input)
- yes, the arduino needs to be plugged in (computer or outlet or other power source) at all times to run
- if you want to alter the number or the text being displayed to the GUI, change it in the C++/Arduino code
- whatever you want to be displayed, print to the serial monitor, GUI reads data from the serial monitor

### Note:
- Only one program can be reading the serial port at a given time. You can't be running the GUI and the Serial Monitor in the Arduino software at the same time.
It will give you an error message about access. 
