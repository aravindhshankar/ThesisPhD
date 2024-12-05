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
        movelocation = DOWN*1.1 #DOWN Is of type Point3D which is basically a tuple of 3 floats
        def impfun(x,y,a):
            return x**2 - 2 * (y)**2 - a**2 

        ######## adding the grid ############
        wratio = 0.5
        hratiotop = 0.3
        hratiobottom = 0.3
        xrangetup = (-config.frame_width * wratio, config.frame_width * wratio, 1)
        yrangetup = (-config.frame_height * hratiobottom, config.frame_height * hratiotop, 1)
        numberplane = NumberPlane(x_range=xrangetup, y_range=yrangetup, faded_line_ratio = 3).move_to(movelocation)
        self.add(numberplane)	
        ########### Adding the text and the hyperbolae ###############	
        titlecol = BLUE
        titlefontscale = 1.5
        namecol = BLUE
        namefontscale = 1.5
        title1 = Text('Strongly correlated electrons in', color = titlecol).scale(titlefontscale).align_on_border(np.array([0,1,0]), buff=1.2)
        title2 = Text('Sachdev-Ye-Kitaev models', color = titlecol).scale(titlefontscale).next_to(title1,DOWN)
        title3 = Text('and', color = titlecol).scale(titlefontscale).next_to(title2,DOWN)
        title4 = Text('Twisted bilayer graphene', color = titlecol).scale(titlefontscale).next_to(title3,DOWN)
        name1 = Text('Aravindh Swaminathan', color = namecol).scale(namefontscale).align_on_border(np.array([0,-1,0]), buff = 2.5)	
        name2 = Text('Shankar', color = namecol).scale(namefontscale).next_to(name1, DOWN)
        self.add(title1,title2,title3,title4)
        self.add(name1,name2)

        alist = np.array([1,2,3,4])				
        for aval in alist :
            graph = ImplicitFunction(partial(impfun, a = aval), color=YELLOW).move_to(movelocation)
            self.add(graph)


        ######## adding the random color electrons ##########
        Erad = 0.3
        colorlist = [RED_A, TEAL_A, MAROON_D, GOLD_D, ORANGE, GREEN_B]
        xlist = np.array([1,2.3,3.6,4.7,6.1,3.5])	
        plotalist = np.array([0,1,2,3,0,1]) #alist[i] will be chosen
        xsignlist = np.array([-1,1,1,-1,1,-1])
        ysignlist = np.array([-1,1,-1,-1,1,1])
        ylist = [newton(lambda yval: impfun(x=xlist[i], y=yval, a=alist[plotalist[i]]), x0 = 1) for i in np.arange(len(xlist))]
        print(xlist)
        print(ylist)
        elist = [Dot([xsignlist[i]*xlist[i],ysignlist[i]*ylist[i] + movelocation[1] , 0], radius=Erad, color=colorlist[i]) for i in range(len(xlist))]
        for electron in elist: 
            self.add(electron)	




class BackPage(Scene):
    def construct(self):
        ##### added some indentation reference #########
        print('Empty page')

















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
