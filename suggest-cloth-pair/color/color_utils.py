from webcolors import name_to_rgb
import colorsys

nuetral_colors = ['black', 'white', 'brown', 'cream', 'grey', 'light blue', 'khaki', 'sand', 'biege']

warm_colors = ['Red', 'Orange', 'Yellow','Peach', 'Coral', 'Amber', 'Gold', 'Brown', 'Tan', 'Beige']

def color_name_to_hsv(color):
	rgb = name_to_rgb(color)
	hsv = colorsys.rgb_to_hsv(rgb)


def is_color_nuetral(color):
    if color == '':
        return False
    
    global nuetral_colors
    
    if color in nuetral_colors:
        return True

def is_color_cool(color):
    if color == '':
        return False
    
    r, g, b = name_to_rgb(color)
    
    # Calculate the hue of the color.
    hue = (r * 60 + g * 120 + b * 180) % 360

	# Return True if the hue is in the cool range.
    return hue >= 210 and hue <= 270

def is_color_warm(color):
	if color == '':
		return False

	if color in warm_colors:
		return True

	r, g, b = name_to_rgb(color)

	# Calculate the hue of the color.
	hue = (r * 60 + g * 120 + b * 180) % 360

	# Return True if the hue is in the warm range.
	return hue >= 0 and hue <= 60

# accepts color in hex format
# color combination cancel outs each other, hence complementry
def is_color_complementary(color1, color2):
	r1, g1, b1 = name_to_rgb(color1)
	r2, g2, b2 = name_to_rgb(color2)

	# Calculate the positive difference between the RGB values of the two colors.
	dr = abs(r1 - r2)
	dg = abs(g1 - g2)
	db = abs(b1 - b2)

	# Return True if the difference between the RGB values is equal to 255.
	return dr == 255 and dg == 255 and db == 255

def is_color_contrasting(color1, color2):
	r1, g1, b1 = name_to_rgb(color1)
	r2, g2, b2 = name_to_rgb(color2)

	# Calculate the difference between the two colors.
	difference = abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2)

	# Return True if the difference is greater than a certain threshold, False otherwise.
	return difference > 128

def is_monochromatic(color1, color2):
	color1
	r1, g1, b1 = name_to_rgb(color1)
	h1, s1, v1 = colorsys.rgb_to_hsv(r1, g1, b1)

	r2, g2, b2 = name_to_rgb(color2)
	h2, s2, v2 = colorsys.rgb_to_hsv(r2, g2, b2)

	# Check if the hue values are equal and the saturation and value values are within a certain range.
	return h2 >= (h1 - 15) and h2 <= (h1 + 15) and s1 <= s2 + 0.1 and s2 <= s1 + 0.1 and v1 <= v2 + 0.1 and v2 <= v1 + 0.1


