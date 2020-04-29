import LED_control as LED

print('command : wakeup think speak')
command, time = raw_input('input <command> <time>: ').split()

time = int(time)

print('input command : ' + command, type(command))
print('input time : ' + str(time), type(time))

if command == 'wakeup':
    LED.wakeup(time)
elif command == 'think':
    LED.think(time)
elif command == 'speak':
    LED.speak(time)
else:
    print('command error')

