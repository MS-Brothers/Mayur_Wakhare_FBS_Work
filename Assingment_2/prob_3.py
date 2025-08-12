#
# Total inches = (5 ft × 12) + 4 in = 60 in + 4 in = 64 in
# Total centimeters = 64 in × 2.54 cm/in = 162.56 cm
# This is equivalent to 1 meter and 62.56 centimeters.

feet = float(input('Enter the Feet : '))
inches = float(input('Enter the inches : '))
feet_in_inch = feet * 12
total_inch = inches+feet_in_inch
total_centi = total_inch * 2.54
meter = total_centi // 100
remainng_centi = total_centi % 100

print(f'Meter is : {meter} , Centimeter is : {remainng_centi}')
