import numpy as np
from functools import partial 
from manim import *

config.frame_width = 17.30 # units mm 
config.frame_height = 24.60 # units mm
config.pixel_width = int(config.frame_width * 100)
config.pixel_height = int(config.frame_height * 100)


class Hyperbolae(Scene):
	def construct(self):
		def impfun(x,y,a):
			return x**2 - y**2 - a**2 
		
		titletext = Text('Strongly Correlated electrons in \n Sachdev-Ye-Kitaev models \n and \n Twisted Bilayer Graphene', color = BLUE).scale(1).align_on_border(np.array([0,1,0]),buff=0.5)
		self.add(NumberPlane(), titletext)	
		for aval in  np.array([1,2,3,4]):
			graph = ImplicitFunction(partial(impfun, a = aval), color=YELLOW)
			self.add(graph)


class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)






def main():
	BraceAnnotation()

if __name__ == '__main__':
	main()
