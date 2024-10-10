import numpy as np
from functools import partial 
from scipy.optimize import newton
from manim import *

###### change config #######
config.frame_width = 0.75 # units cm 
config.frame_height = 24.60 # units cm
config.pixel_width = int(config.frame_width * 100)
config.pixel_height = int(config.frame_height * 100)

# class MiddleStrip(Scene):
	# def construct(self):	
		# ####### adding text ######
		# textcol = YELLOW
		# textscale = 0.5
		# toptext = Text('Strongly correlated electrons in Sachdev-Ye-Kitaev models and in Twisted bilayer graphene ', color = textcol, should_center = True,font_size=5,width=5,disable_ligatures=True).rotate(-0.5*PI).scale(1).align_on_border(np.array([0,1,0]), buff=0.5)
		# toptext2 = Text('correlated ', color = textcol, should_center = True).scale(textscale).rotate(-0.5*PI).next_to(toptext, DOWN) 
		# # toptext = Text('Strongly correlated electrons in', color = textcol, size=textscale).align_on_border(np.array([0,1,0]), buff=0.5)
		# 
		# self.add(toptext, toptext2)



###### change config #######
config.frame_height = 0.75 # units cm 
config.frame_width = 24.60 # units cm
config.pixel_width = int(config.frame_width * 100)
config.pixel_height = int(config.frame_height * 100)


class MiddleStrip(Scene):
	def construct(self):
		textcol = YELLOW
		lefttext = Text('Strongly correlated electrons in Sachdev-Ye-Kitaev models and in Twisted bilayer graphene', color = textcol, disable_ligatures = True, font_size=30).scale(1).align_on_border([-1,0,0], buff = 0.5)
		righttext = Text('A. S. Shankar', color = textcol, disable_ligatures = True, font_size=30).scale(1).align_on_border([1,0,0], buff = 0.5)
		self.add(lefttext, righttext)






