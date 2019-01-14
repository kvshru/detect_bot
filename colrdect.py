from sightengine.client import SightengineClient
import json
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return (min_colours[min(min_colours.keys())])

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return (actual_name, closest_name)

	
def ss_detect(url):
	api_user = '684881556'
	api_key = 'fimQmYuoPqEHbdsJfESC'
	client = SightengineClient({api_user},{api_key})
	output = client.check('properties').set_url(url)
	data = (json.dumps(output))
	print(data+"\n")

	if output['status'] == "success":
		print("success ")
		dom_color_hex = (output['colors']['dominant']['hex'])
		dom_color_r = (output['colors']['dominant']['r'])
		dom_color_g = (output['colors']['dominant']['g'])
		dom_color_b = (output['colors']['dominant']['b'])
		actual_dom_color_name, closest_dom_color_name = get_colour_name((dom_color_r,dom_color_b,dom_color_g))
		print("dominant color : {0} {1} {2} closest: {3} ". format((dom_color_r),(dom_color_b),(dom_color_g),closest_dom_color_name)) 
		status = "Screenshot is {0} of Url : - {1}" .format(closest_dom_color_name,(output['media']['uri']))
		if closest_dom_color_name == 'black':
			print(" Ban user; {0}" .format(status))
		else:
			print(" ".format(status))
	
	else:
		print("fail")

link = "http://45.32.113.186/screenshots/I_got_0002.jpg"	
ss_detect(link)