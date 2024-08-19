# import matplotlib.pyplot
# from poppy.creatures import PoppyErgoJr


# poppy = PoppyErgoJr(simulator='vrep')
# poppy.chain.end_effector
# zero = [0] * 6

# ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
# poppy.chain.plot(poppy.chain.convert_to_ik_angles(zero), ax)

from ipywidgets import interact, FloatSlider

poppy.reset_simulation()

c = poppy.chain

x, y, z = c.end_effector
size = 0.3

def goto(x, y, z):
    c.goto((x, y, z), .1)
    
interact(goto, 
         x=FloatSlider(min=x-size, max=x+size, value=x, step=0.01), 
         y=FloatSlider(min=y-size, max=y+size, value=y, step=0.01), 
         z=FloatSlider(min=z-size, max=z+size, value=z, step=0.01))