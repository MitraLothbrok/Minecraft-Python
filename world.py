from mcpi.minecraft import Minecraft

mc = Minecraft.create()

class Tree:

    def __init__(self, x, y, z, w, l, kind_w, kind_l):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.l = l
        self.kind_w = kind_w
        self.kind_l = kind_l

    def grow_big(self):
        # wood
        mc.setBlocks(self.x, self.y, self.z, self.x + 1, self.y + 8, self.z + 1, self.w, self.kind_w)

        # leaves
        mc.setBlocks(self.x-2, self.y + 3, self.z-2, self.x+2, self.y+4, self.z + 2, self.l, self.kind_l)
        mc.setBlocks(self.x, self.y+3, self.z, self.x, self.y + 4, self.z, self.w, self.kind_w)

        mc.setBlocks(self.x-2, self.y + 7, self.z - 2, self.x+2, self.y + 8, self.z+2, self.l, self.kind_l)
        mc.setBlocks(self.x, self.y + 7, self.z, self.x, self.y + 8, self.z, self.w, self.kind_w)

        mc.setBlocks(self.x-1, self.y+9, self.z-1, self.x+1, self.y+9, self.z+1, self.l, self.kind_l)

        mc.setBlocks(self.x, self.y+10, self.z, self.x, self.y+10, self.z, self.l, self.kind_l)


    def grow_small(self):
        pass

    def grow_medium(self):
        pass


class Flower:
    def __init__(self, x, y, z, f, kind_f):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.kind_f = kind_f

    def grow(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+1, self.z, self.f, self.kind_f)


class River:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw_river(self):
        mc.setBlocks(self.x, self.y, self.z, self.x+2, self.y, self.z+2, 9)  # or 8
        pass


class GreenHouse:
    def __init__(self, x, y, z, f, t_f,  m, t_m):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.m = m
        self.t_f = t_f
        self.t_m = t_m

    def brick_by_brick(self):
        mc.setBlocks(self.x, self.y, self.z, self.x+10, self.y-2, self.z + 5, self.f, self.t_f)
        mc.setBlocks(self.x, self.y+2, self.z, self.x+10, self.y+8, self.z+5, self.m, self.t_m)



