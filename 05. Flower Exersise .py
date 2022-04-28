class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, param):
        if param >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if not self.is_happy:
            return f"{self.name} is not happy"
        else:
            return f"{self.name} is happy"


flower = Flower("Ivan", 100)
flower.water(10)
print(flower.status())
flower.water(10)
print(flower.status())
flower.water(100000000)
print(flower.status())
