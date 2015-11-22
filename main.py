import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window(800, 600)
#image = pyglet.image.load('kitten.jpg')

"""
label = pyglet.text.Label('Hello, world',
						  font_name='Times New Roman',
						  font_size = 36,
						  x=window.width//2, y=window.height//2,
						  anchor_x='center', anchor_y='center')
"""

@window.event
def on_draw():
	window.clear()
	#image.blit(0, 0)
	#label.draw()

@window.event
def on_key_press(symbol, modifiers):
	#print 'A key was pressed'
	if symbol == key.A:
		print 'The "A" key was pressed.'
	if symbol == key.LEFT:
		print 'The "left arrow key was pressed.'

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		print 'The left mouse button was pressed', x, y

window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()