"""
Реализовать иерархию классов согласно приложенной UML-даиграмме.
Она описывает упрощенные элементы популярной игры Counter-Strike,
в которой команда контер-террористов пытается предотвратить планы
террористов.

Есть общий класс Person, от которого наследуются классы Terrorist
и CounterTerrorist. Помимо этого, есть класс Gun, от которого
наследуются AK и M4, каждый из которых состоит в отношении агрегации
соответственно игровой роли (АК для террористов, М4 для контер-террористов).

Реализации стрельбы и перезарядки для каждого класса остаются на усмотрение
разработчика. При желании что-то можно добавить.

В личный кабинет приложить .py файл с реализацией или же ссылку на github
репозиторий.
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, health):
        self.health = health


class CounterTerrorist(Person):
    def __init__(self, counter_terrorist_gun, health=60):
        self.counter_terrorist_gun = counter_terrorist_gun
        super().__init__(health)

    def shoot(self):
        self.counter_terrorist_gun.shoot()
        print(f'у {bcolors.OKBLUE}контр-террориста{bcolors.ENDC}.')

    def reload(self):
        self.counter_terrorist_gun.reload()
        print(f'у {bcolors.OKBLUE}контр-террориста{bcolors.ENDC}.')


class Terrorist(Person):
    def __init__(self, terrorist_gun, health=60):
        self.terrorist_gun = terrorist_gun
        super().__init__(health)
        print(f"{bcolors.FAIL}Террористы{bcolors.ENDC} снова рашат B!")

    def shoot(self):
        self.terrorist_gun.shoot()
        print(f'у {bcolors.FAIL}террориста{bcolors.ENDC}.')

    def reload(self):
        self.terrorist_gun.reload()
        print(f'у {bcolors.FAIL}террориста{bcolors.ENDC}.')


class Gun:
    def __init__(self, ammo=10):
        self.ammo = ammo

    def shoot(self):
        self.ammo -= 1
        print(f'Пиф-паф, осталось {self.ammo} патронов ', end='')

    def reload(self):
        self.ammo = 10
        print(f'Оружие перезаряжено. Теперь снова {self.ammo} патронов ', end='')


class M4(Gun):
    def shoot(self):
        self.ammo -= 1
        print(f'Пыщ-пыщ, осталось {self.ammo} патронов ', end='')


class AK(Gun):
    pass


def main():
    terrorist_gun = AK()
    counter_terrorist_gun = M4()

    terrorist = Terrorist(terrorist_gun)
    counter_terrorist = CounterTerrorist(counter_terrorist_gun)

    terrorist.shoot()
    terrorist.shoot()
    terrorist.shoot()
    terrorist.reload()
    terrorist.shoot()

    print()

    counter_terrorist.shoot()
    counter_terrorist.shoot()
    counter_terrorist.shoot()
    counter_terrorist.reload()
    counter_terrorist.shoot()


if __name__ == '__main__':
    main()
