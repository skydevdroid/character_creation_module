from random import randint
from graphic_arts.start_game_banner import run_screensaver



def attack(char_name: str, char_class: str) -> str:
    """Описание алгоритма атаки."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон - {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон - {5 + randint(-3, -1)}')
    return (f'{char_name} не нанес урон')


def defence(char_name: str, char_class: str) -> str:
    """Описание алгоритма защиты."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_class} не блокировал урон')


def special(char_name: str, char_class: str) -> str:
    """Описание алгоритма спецспособности."""
    if char_class == 'warrior':
        return (f'{char_name} применил «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил «Защита {10 + 30}»')
    return (f'{char_name} ничего не применил')


def start_training(char_name: str, char_class: str) -> str:
    """Описание алгоритма тренировки."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Команды: attack (атака), defence (защита), special (суперсила).')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор класса персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — ближний бой, сильный и выносливый.')
        if char_class == 'mage':
            print('Маг — дальний бой, высокий интеллект.')
        if char_class == 'healer':
            print('Лекарь — заклинатель. Черпает силы из природы.')
        approve_choice = input('(Y), - подтвердить, другое для отмены').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


