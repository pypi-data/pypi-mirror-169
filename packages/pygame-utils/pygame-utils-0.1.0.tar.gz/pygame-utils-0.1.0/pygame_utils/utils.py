import pygame
from pygame.sprite import Group, Sprite
from pygame.key import get_pressed

def add(*tups):
    return tuple([sum(itms) for itms in zip(*tups)])

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

# Have to do it like this rather than a list comp
# since get_pressed() doesn't return a straight list
class __j_pressed:
    def __init__(self, first):
        self.last = first
        self.now = first
    def __getitem__(self, val):
        return (not self.last[val]) and self.now[val]
    def update(self, new_vals):
        self.last = self.now
        self.now = new_vals
press_mem = None
# Returns the instance of __j_pressed, with updated keys
# Could have used events for this but I didn't know at the time
def just_pressed():
    global press_mem
    if press_mem == None:
        press_mem = __j_pressed(get_pressed())
    press_mem.update(get_pressed())
    return press_mem   

class CustomSprite(Sprite):
    x = 0
    y = 0
    def alert(self, event, data=None):
        pass

class CustomGroup(Group):
    # Copied from the pygame codebase almost directly, I only needed a small change
    # Instead of blitting an image, call the custom draw() function
    def draw(self, surface, to_draw=None):
        for spr in self.sprites():
            spr.draw(surface)
            
        self.lostsprites = [] # Need this line for some reason idk

    # This function is new, it pings each sprite to do something
    def alert(self, event, data=None):
        rtn = {}
        for spr in self.sprites():
            rtn[spr] = spr.alert(event, data)
        return rtn

class TextBox:
    def __init__(self, images, bg, **kwargs):
        self.images = images
        self.bg = bg
        self.kwargs = kwargs
    def get_img(self):
        size = (max(t.get_width() for t in self.images),
        sum(t.get_height() for t in self.images))
        box = pygame.Surface(size, pygame.SRCALPHA, **self.kwargs).convert_alpha()
        box.fill(self.bg)
    
        v_offset = 0
        for t in self.images:
            blit_rect = t.get_rect(center=(box.get_width()/2,v_offset+t.get_height()/2))
            box.blit(t, blit_rect)
            v_offset += t.get_height()
        return box
    def get_rects(self):
        size = (max(t.get_width() for t in self.images),
        sum(t.get_height() for t in self.images))
        box = pygame.Surface(size, pygame.SRCALPHA, **self.kwargs)
    
        v_offset = 0
        rects = []
        for t in self.images:
            blit_rect = t.get_rect(center=(box.get_width()/2,v_offset+t.get_height()/2))
            v_offset += t.get_height()
            rects.append(blit_rect)
        return rects
    def get_pos_of(self, t_idx, **box_pos_args):
        rect = self.get_rects()[t_idx]
        img_pos = self.get_img().get_rect(**box_pos_args)
        rect.topleft = add(rect.topleft, img_pos.topleft)
        return rect
    def draw(self, surf, **pos_args):
        img = self.get_img()
        pos = img.get_rect(**pos_args)
        surf.blit(img, pos)

def make_txtbox(objs, bg, obj_to_img: lambda o:o, obj_change: lambda img,rect,o:None, **rect_kwargs):
    images = []
    obj_imgs = {}
    for obj in objs:
        img = obj_to_img(obj)
        images.append(img)
        obj_imgs[obj] = img

    box = TextBox(images, bg)

    for idx, (obj, img) in enumerate(obj_imgs.items()):
        rect = box.get_pos_of(idx, **rect_kwargs)
        obj_change(img, rect, obj)

    return box

def standard_textbox(objs, bg, font, font_args, **pos_args):
    def to_img(obj):
        if isinstance(obj, Button):
            b = pygame.Surface(obj.rect.size, pygame.SRCALPHA).convert_alpha()
            b.fill((255,255,255,0))
            return b
        elif isinstance(obj, str):
            return font.render(obj, True, (255,255,255))
        elif isinstance(obj, tuple) and isinstance(obj[0], str):
            return obj[1].render(obj[0], True, (255,255,255))
        else:
            return obj
            
    def change_obj(img, rect, obj):
        if isinstance(obj, Button):
            obj.rect = rect
    
    # Create textbox
    return make_txtbox(
        objs, bg,
        to_img, change_obj, **pos_args
    )

class Button(CustomSprite):
    def __init__(self, pos, text_img, on_click=None):
        super().__init__()
        self.image = text_img
        self.rect = text_img.get_rect(center=pos)
        self.on_click = (lambda: print("clicked")) if on_click is None else on_click
        self.mouse_down = pygame.mouse.get_pressed(3)[0]
    def draw(self, surf:pygame.Surface):
        surf.blit(self.image, self.rect)
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed(3)[0]
        if self.rect.left < mouse_pos[0] < self.rect.right\
        and self.rect.top < mouse_pos[1] < self.rect.bottom:
            # The 3 is to signify that the mouse has 3
            # buttons, and the 0 is for the first
            if mouse_press and not self.mouse_down:
                self.clicked()
            # else do some hovering stuff if you want
        self.mouse_down = mouse_press
    def clicked(self):
        self.on_click()

def rect_collision(r1:pygame.Rect, r2:pygame.Rect):
    top = max(r1.top, r2.top)
    bottom = min(r1.bottom, r2.bottom)
    left = max(r1.left, r2.left)
    right = min(r1.right, r2.right)
    
    if right > left and bottom > top:
        return pygame.Rect(left, top, right-left, bottom-top)
    else:
        return None