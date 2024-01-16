class ChristmasTree:
    def __init__(self, height, tree_toys):
        self.height = height
        self.tree_toys = tree_toys

    def show_tree(self):
        print(f'Высота елки: {self.height} метров, на ней: {self.tree_toys} игрушек.')

    def decorate_tree(self, new_tree_toys):
        self.tree_toys = new_tree_toys

    def grow_tree(self, new_height):
        self.height = new_height


class HolidayLights:
    def __init__(self, light_bulbs, glow_modes):
        self.light_bulbs = light_bulbs
        self.glow_modes = glow_modes

    def show_lights(self):
        print(f'Украшена {self.light_bulbs}-ти метровой гирляндой, у которой режим {self.glow_modes}.')

    def add_light_bulbs(self, new_light_bulbs):
        self.light_bulbs = new_light_bulbs

    def change_glow_modes(self, new_glow_modes):
        self.glow_modes = new_glow_modes








