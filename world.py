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
    def __init__(self, x, y, z, kind):
        self.x = x
        self.y = y
        self.z = z
        self.kind = kind

    def grow(self):
        mc.setBlocks()