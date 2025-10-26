import random
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    number_cards = int(input('Введите количество карточек: '))

    for num in range(number_cards):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('template.html')

        races = [
            'Орк',
            'Эльф',
            'Гном',
            'Человек',
        ]

        classes = [
            'Маг',
            'Воин',
            'Охотник',
            'Ассасин',
            'Бард',
        ]

        clases_base = {
            'Маг': {
                'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': 15,
                'luck': random.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/wizard.png'
            },
            'Воин': {
                'skills': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                'strength': 15,
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': random.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/warrior.png'
            },
            'Охотник': {
                'skills': ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': random.randint(1, 3),
                'temper': 15,
                'image': '../images/archer.png'
            },
            'Ассасин': {
                'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': 15,
                'temper': random.randint(1, 3),
                'image': '../images/assasin.png'
            },
            'Бард': {
                'skills': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                'strength': random.randint(1, 3),
                'agility': 15,
                'intelligence': random.randint(1, 3),
                'luck': random.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/bard.webp'
            },
        }

        choice_race = int(input('Выберите 1 из расс: \n1.Орк \n 2.Эльф \n 3.Гном \n 4.Человек '))
        choice_class = int(input('Выберите класс для своего персонажа \n 1.Маг\n 2.Воин\n 3.Охотник\n 4.Ассасин\n 5.Бард '))
        character_class = classes[choice_class-1]
        skill = clases_base[character_class]['skills']
        skills = random.sample(skill, 3)

        rendered_page = template.render(
            name=input('Введите имя: '),
            character_race=races[choice_race-1],
            character_class=character_class,
            strength=clases_base[character_class]['strength'],
            agility=clases_base[character_class]['agility'],
            intelligence=clases_base[character_class]['intelligence'],
            luck=clases_base[character_class]['luck'],
            temper=clases_base[character_class]['temper'],
            image=clases_base[character_class]['image'],
            first_skill=skills[0],
            second_skill=skills[1],
            third_skill=skills[2],
        )

        with open(f'characters/index_{num+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()
