
class Link:
    def __init__(self, node1, node2):
        self.id = (node1.id, node2.id)
        self.load = 0
    
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

        self.load = 0

class Area:
    pass

class Patch:
    pass

class World:
    def __init__(self):
        self.nodes = {}
        self.links = {}

    def load(self, filename):
        for i in range(20):
            for j in range(20):
                x = i * 100
                y = j * 100
                node = Node(i*20+j, x, y)
                self.nodes[node.id] = node

        for i in range(20):
            for j in range(20):
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if i+di >= 20 or i+di < 0 or j+dj>=20 or j+dj<0:
                        continue

                    node1 = self.nodes[i*20+j]
                    ni = i+di
                    nj = j+dj
                    node2 = self.nodes[ni*20+nj]

                    link = Link(node1, node2)
                    self.links[link.id] = link

    def split(self, n):
        pass

    def step(self, n):
        pass

    def balance(self):
        pass

    def apply(self, patchs):
        pass

def main():
    world = World()
    world.load("chengdu.shp")

    areas = world.split(4)

    for i in range(100):
        world.step()
        patchs  = world.balance()
        world.apply(patchs)