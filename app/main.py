class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden

        if self.health >= 0:
            self.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, prey:Herbivore):
        if prey.hidden != True and prey.__class__ != Carnivore:
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)

