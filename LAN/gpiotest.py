import gpio

def toggle(pin):
	
	if gpio.read(pin) == 0:
		gpio.setup(pin, gpio.OUT)
		gpio.set(pin, 1)
	elif gpio.read(pin) == 1:
		gpio.setup(pin, gpio.OUT)
		gpio.set(pin, 0)
	else:
		print('There was some sort of error, are you using the right pin?')
	print(gpio.read(pin))

pinnum = raw_input("What pin are you looking for?\nHint: it's probably 57 ")
pinst = gpio.read(pinnum)
cmd = raw_input('Pin %s is %s, do you want to change it? (y/n) ' % (pinnum, pinst))

if cmd.lower() == 'y':
	toggle(pinnum)
	print('Pin %s was toggled' % pinnum)
elif cmd.lower() == 'n':
	pass
else:
	print("Something didn't work")

