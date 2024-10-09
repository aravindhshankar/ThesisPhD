import numpy as np
from functools import partial 
from scipy.optimize import newton
from manim import *

config.frame_width = 17.30 # units cm 
config.frame_height = 24.60 # units cm
config.pixel_width = int(config.frame_width * 100)
config.pixel_height = int(config.frame_height * 100)


class Hyperbolae(Scene):
	def construct(self):
		def impfun(x,y,a):
			return x**2 - y**2 - a**2 
		
		# titletext = Text('Strongly Correlated electrons in \n Sachdev-Ye-Kitaev models \n and \n Twisted Bilayer Graphene', color = BLUE, should_center=True).scale(1).align_on_border(np.array([0,1,0]),buff=0.5)
		
		titlecol = BLUE
		titlefontscale = 1.5
		namecol = BLUE
		namefontscale = 1.5
		title1 = Text('Strongly correlated electrons in', color = titlecol).scale(titlefontscale).align_on_border(np.array([0,1,0]), buff=0.5)
		title2 = Text('Sachdev-Ye-Kitaev models', color = titlecol).scale(titlefontscale).next_to(title1,DOWN)
		title3 = Text('and', color = titlecol).scale(titlefontscale).next_to(title2,DOWN)
		title4 = Text('Twisted bilayer graphene', color = titlecol).scale(titlefontscale).next_to(title3,DOWN)
		name1 = Text('Aravindh Swaminathan', color = namecol).scale(namefontscale).align_on_border(np.array([0,-1,0]), buff = 2)	
		name2 = Text('Shankar', color = namecol).scale(namefontscale).next_to(name1, DOWN)
		self.add(title1,title2,title3,title4)
		self.add(name1,name2)
		
		alist = np.array([1,2,3,4])				
		for aval in alist :
			graph = ImplicitFunction(partial(impfun, a = aval), color=YELLOW)
			self.add(graph)
		

		######## adding the random color electrons ##########
		Erad = 0.3
		xlist = np.array([1,2.3,3,4.7])	
		ylist = [newton(lambda yval: impfun(x=xlist[i], y=yval, a=alist[i]), x0 = 1) for i in np.arange(len(xlist))]
		print(xlist)
		print(ylist)
		e1 = Dot([xlist[0],ylist[0],0], radius=Erad, color=RED)
		e2 = Dot([xlist[1],ylist[1],0], radius=Erad, color=RED)
		e3 = Dot([xlist[2],ylist[2],0], radius=Erad, color=RED)
		self.add(e1)
		self.add(e2)
		self.add(e3)
		
		######## adding the grid ############
		wratio = 0.4
		xrangetup = (-config.frame_width * wratio, config.frame_width * wratio, 1)
		yrangetup = (-config.frame_height * wratio, config.frame_height * wratio, 1)
		numberplane = NumberPlane(x_range=xrangetup, y_range=yrangetup, faded_line_ratio = 3)
		self.add(numberplane)	

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
