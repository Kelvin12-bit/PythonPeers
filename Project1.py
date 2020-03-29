# This program converts temperatures from degree Fahrenheit to degree Celsius and run the values to two decimal places
print('Convert degree Fahrenheit to degree Celsius')
degreeFahrenheit= float(input('Temperature in degree Fahrenheit=')) # Temperatures are recoreded in decimal points 
degreeCelsuis=float((degreeFahrenheit-32)*5/9 )
newdegreeCelsius=round(degreeCelsuis,2) # Rounds temperatures to two decimal points
print('Temperature in degree Celsius= '+ str(newdegreeCelsius))
