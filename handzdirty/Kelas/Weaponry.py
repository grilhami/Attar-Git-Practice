class Weapons:
    # name = ""
    # damage = None
    # rof = None
    # has_scope = False

    def __init__(self, name, damage, rof):
        self.name = name
        self.damage = damage
        self.rof = rof

    # def scoping(self, has_scope = has_scope):
    #     if has_scope:
    #         return "Can Right Click"
    #     else:
    #         return "Cannot Right Click"