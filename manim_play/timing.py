from manim import *
config.verbosity = 'ERROR'
config.quality = sys.argv[1]
self = Scene()
before = self.renderer.time
self.play(Create(Circle()), run_time=0.25)
self.play(Create(Circle()), run_time=0.25)
self.play(Create(Circle()), run_time=0.25)
self.play(Create(Circle()), run_time=0.25)
print("calculated render time: %s" % (self.renderer.time - before))
self.render()


