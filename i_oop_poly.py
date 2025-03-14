# 多态
# 多态是指根据对象（或类）类型的不同而表现出不同的行为。
# 这使得代码更加灵活和可扩展。

class Animal:
    def say(self):
        print("Animal sound")

class Dog(Animal):
    def say(self):
        print("Dog Wang Wang ...")

class Cat(Animal):
    def say(self):
        print("Cat Miao Miao ...")

if __name__ == '__main__':
    # 创建Animal、Dog和Cat对象，并调用各自的say方法
    animals = [Animal(), Dog(), Cat()]
    for animal in animals:
        animal.say()