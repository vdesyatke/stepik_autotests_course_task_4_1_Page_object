class Human():
    def __init__(self, age = 0, sex = '?'):
        self.age = age
        self.sex = sex

    def speak(self):
        print('Hello, I am ', self.age, ' years old, I am a', self.sex, '.')

man = Human(35, 'man')

man.speak()