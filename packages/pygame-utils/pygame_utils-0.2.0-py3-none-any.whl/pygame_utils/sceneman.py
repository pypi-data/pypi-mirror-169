import pygame, os, sys, inspect
clock = pygame.time.Clock()

# This class is meant to be inherited/overridden
# Any class that does so is a scene (a collection
# of groups and variables that acts as a "room" in
# the game)
class Scene:

    def __init__(self, *groups):
        self.groups = groups

    def draw(self, surf):
        surf.fill((0, 0, 0))
        for g in self.groups:
            g.draw(surf)

    def update(self):
        for g in self.groups:
            g.update()
        return True

    def update_raw(self):
        rtn = self.update()
        clock.tick(30)
        return rtn if rtn is not None else True

    def on_start(self):
        pass

    def on_end(self):
        pass

    def play(self, surf):
        self.on_start(surf)
        run = True
        while run:
            run = self.update()
            self.draw(surf)
        self.on_end(surf)

# Some globals for management
curr_scene = None
_surf = None
running = True

# Run this to start the scene management
def init(surf, start_scene):
    # need this for _scene_cls to work
    currentdir = os.path.dirname(os.getcwd())
    print(currentdir)
    sys.path.insert(0, currentdir) 
    global _surf
    _surf = surf
    set_scene(start_scene)
    
# Run this every frame to update the scene
def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    global running
    running = curr_scene.update_raw()

# Run this to draw the scene to a screen surface
def draw(surf=None):
    curr_scene.draw(surf if surf is not None else _surf)
    pygame.display.update()

# Run this to change the scene
def set_scene(scene):
    global curr_scene
    if curr_scene is not None:
        curr_scene.on_end()
    curr_scene = scenes[scene]
    curr_scene.on_start()

# Run this to restart the current scene
def restart_scene():
    curr_scene.on_end()
    curr_scene.on_start()

# Basic thing for finding scene files
class _scene_cls(dict):
    def __getitem__(self, val):
        try:
            return super().__getitem__(val)
        except KeyError:
            self[val] = __import__(val+"scene").scene
            print(f"found {self[val]}")
            return self[val]

# Effectively a runtime dictionary of scenes
# Finds them by name, then looks for
# [name]scene.py and takes the "scene" var
scenes = _scene_cls()