# Write a Celsius / Fahrenheit converter using user prompting

prmpt = 'Insert Celsius temperature >>> '
celsius_t = raw_input(prmpt)
celsius_t= float(celsius_t)
fahrenheit_t = (celsius_t * 9/5) + 32
print celsius_t, 'Celsius degrees  equals to ' 
print fahrenheit_t, '  Fahrenheit degrees.\n'
