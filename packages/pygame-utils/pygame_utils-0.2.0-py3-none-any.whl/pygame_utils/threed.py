# Couldn't name it 3d.py since you can't start a name with a number

import pygame
from pygame import draw
from pygame.sprite import Sprite
from .utils import add, clamp, CustomGroup
from . import sceneman
import math

# Camera angles by scene
scene_angles = {}

# Screen size (for determining center)
SIZE = pygame.display.get_surface().get_size()

# Takes a point (2D) and rotates it the specified number of radians
def rotate(x, y, rad):
    ca = math.cos(rad)
    sa = math.sin(rad)
    tx = x*ca - y*sa
    ty = x*sa + y*ca
    return (tx, ty)

def cam_rotate(axy, axz):
    angles = (0,0)
    if sceneman.curr_scene in scene_angles:
        angles = scene_angles[sceneman.curr_scene]
    scene_angles[sceneman.curr_scene] = add(angles, (axy, axz))
    
def cam_reset_rotation():
    scene_angles[sceneman.curr_scene] = (0,0)

def get_angles():
    angles = (0,0)
    if sceneman.curr_scene in scene_angles:
        angles = scene_angles[sceneman.curr_scene]
    return angles

# Takes a 3d point, rotates it, and determines its 2d equivalent
def twofromthree(x,y,z):
    axy, axz = get_angles()
    tx, tz = rotate(x, z, axz)
    tx, ty = rotate(tx, y, axy)
    return (ty-tx, -(tx+ty)/2+tz)

# Simple enough, takes a point and returns its position on the screen
def toscreenpos(x, y, z=0):
    # Going to call width, x, left side, depth, y, right side, and height, z, up
    twod = twofromthree(x,y,z)
    return [d+s/2 for d,s in zip(twod, SIZE)]

# Draws a line in 3d space onto the screen
def line3d(surf, col, pos1, pos2):
    draw.line(surf, col, toscreenpos(*pos1), toscreenpos(*pos2))

# Draws a quadrilateral in 3d space
def rect3d(surf, col, p1, p2, p3, p4):
    draw.polygon(surf, col, [toscreenpos(*p) for p in (p1, p2, p3, p4)])

# Draws a cube (or similar) in 3d space
def cube3d(surf, cols, tfl, tfr, tbl, tbr, bfl, bfr, bbl, bbr, order=None):
    rects = [i for i in enumerate([
        # Back sides
        (tbl, bbl, bbr, tbr, cols[0]),
        (tfr, bfr, bbr, tbr, cols[1]),
        # Bottom
        (bfl, bfr, bbr, bbl, cols[2]),
        # Front sides
        (tfl, bfl, bfr, tfr, cols[0]),
        (tfl, bfl, bbl, tbl, cols[1]),
        # Top
        (tfl, tfr, tbr, tbl, cols[2])
    ])]
    get_dist = lambda r: min(cam_dist(*p) for p in r[1][:4])
    if order is not None:
        blocks = [rects[i] for i in order]
        for idx, (p1, p2, p3, p4, c) in blocks:
            rect3d(surf, c, p1, p2, p3, p4)
        return order
    else:
        o = []
        for idx, (p1, p2, p3, p4, c) in order_closelast(rects, get_dist)[3:]:
            o.append(idx)
            rect3d(surf, c, p1, p2, p3, p4)
        return o

# Basic 3d sprite class, works best in a Group3D
class Sprite3d(Sprite):
    def __init__(self, x, y, z, w, h, d, vel):
        super().__init__()
        self.x, self.y, self.z = x,y,z
        self.width, self.height, self.depth = w,h,d
        self.vel = vel

    @property
    def pos(self):
        return (self.x, self.y, self.z)
    @pos.setter
    def pos(self, val):
        self.x, self.y, self.z = val

    @property
    def size(self):
        return (self.width, self.depth, self.height)
    @size.setter
    def size(self, val):
        self.width, self.depth, self.height = val

    @property
    def back_pos(self):
        return add(self.pos, self.size)

    @property
    def center(self):
        return add(self.pos, [s/2 for s in self.size])
    
    @property
    def top_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.depth)
    
    def move3d(self, x, y, z=0):
        self.x += x
        self.y += y
        self.z += z

    def update(self):
        self.move3d(*self.vel)

    def dist_point(self):
        crd = [z for z in zip(self.back_pos, self.pos)]
        positions = [(x,y,z) for x in crd[0] for y in crd[1] for z in crd[2]]
        positions.sort(key=lambda p: cam_dist(*p))
        return positions[int((len(positions)+1)/2)]
        # It's the corner that has the median distance to the camera (roughly)

# A basic implementation of the Sprite3d class that renders the sprite as a cube.
# Nice for testing, and for subclassing to make a lot of other things.
class Cube(Sprite3d):
    def __init__(self, x, y, z, width, depth, height, color, vel=(0,0,0)):
        super().__init__(x,y,z,width,height,depth,vel)
        self.color = color
        self.side_select = {}
    
    def draw(self, surf):
        # Colors
        unclamped_cols = (add(self.color,c) for c in (
            (-99,-99,-99), (-50, -50, -50), (0,0,0)
        ))
        cols = [[clamp(c, 0, 255) for c in col] for col in unclamped_cols]

        # Shorthand
        w, h, d = self.width, self.height, self.depth
        # Positions
        pos = [add(p, self.pos) for p in (
            (0,0,0), (w,0,0), (0,d,0), (w,d,0), (0,0,h), (w,0,h), (0,d,h), (w,d,h)
        )]

        # Draw the cube
        cam_angle = get_angles()
        sides = None if cam_angle not in self.side_select else self.side_select[cam_angle]
        new_order = cube3d(surf, cols, *pos, sides)
        self.side_select[cam_angle] = new_order

# Test which object is highest (least Z) in an array
def highest(objects:list):
    obj_copy = objects.copy()
    obj_copy.sort(key=lambda o: o.z)
    return obj_copy[0]

# Determines position of "camera" in 3d space
def cam_pos():
    cdist = -5000
    axy, axz = get_angles()
    tx, ty = rotate(cdist,cdist,-axy)
    tx, tz = rotate(tx, cdist, -axz)
    return (tx, ty, tz)
    
# Not an exact distance measure, but it works well enough. I think.
# 45 degree angles might be a problem sometimes though.
def cam_dist(x,y,z):
    # tx, tz = rotate(x, z, axz)
    # tx, ty = rotate(tx, y, axy)
    # return sum(c for c in (tx, ty, tz))
    return sum(abs(p-cp) for p,cp in zip((x,y,z), cam_pos()))

# Sprite implementation of the cam_dist function
def spr3d_cam_dist(spr3d):
    return cam_dist(*spr3d.dist_point())

# Given an array of sprites, returns a copy sorted by distance
def order_closelast(objects:list, dist = spr3d_cam_dist):
    obj_copy = objects.copy()
    obj_copy.sort(key=lambda o: dist(o), reverse=True)
    return obj_copy

# Basic group for 3D sprites, uses order_closelast to draw
class Group3D(CustomGroup):
    def draw(self, surface, to_draw=None):
        for spr in order_closelast(self.sprites()):
            spr.draw(surface)
            
        self.lostsprites = []