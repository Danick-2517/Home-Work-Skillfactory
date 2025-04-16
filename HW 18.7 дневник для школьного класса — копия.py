import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        5. Удалить оценку ученика по предмету
        6. Удалить предмет у ученика
        7. Удалить ученика
        8. Отредактировать оценки учеников
        9. Отредактировать предметы учеников
        10. Отредактировать имена учеников
        11. Вывести все  оценки определенного ученика
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 5:
        print('5. Удалить оценку ученика по предмету :')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f'''{student}
        {class_} - {students_marks[student][class_]}''')
            mark = int(input('Введите индекс оценки которую нужно  удалить : '))
            del students_marks[student][class_][mark]
            print(f'''{student}
        {class_} - {students_marks[student][class_]}''')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 6:
        print('6. Удалить предмет у ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys() :
            print(f'''{student}
               {classes} ''')
            del_class = input('Введите название предме6та который нужно удалить : ')
            if student in students_marks.keys() and del_class in students_marks[student].keys():
                del students_marks[student][del_class]
                print(f'Предмет {del_class} удален у ученика {student}')
                print(f'''Итоговый список : {student}: {students_marks[student]} ''')
            else:
                print('ОШИБКА: Данного предмета нет в списке ученика')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 7:
        print('7. Удалить ученика')
        print(f'Список учеников : {students}')
        student = input('Введите имя ученика которого нужно удалить : ')
        if student in students_marks.keys():
            del students_marks[student]
            print(f'Ученик {student} удален')
            print('Итоговый список учеников :')
            for i in range(len(students_marks)):
                print(f'{i + 1}. {students[i]}')
        else:
            print('ОШИБКА: Этого имени нет в списке учащихся')
    elif command == 8:
        print(f'Исходный список {students_marks}')
        student = input('Введите  имя ученика : ')
        class_ = input('Введите предмет : ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_] = [int(input('Введите оценки через запятую : '))]
            print(f'Итоговый список : {students_marks}')
        else:
            print('Ошибка : неверно введено имя ученика или название предмета !')
    elif command == 9:
        print(f'Исходный список {students_marks}')
        student = input('Введите  имя ученика : ')
        if student in students_marks.keys():
            students_marks[student] = {input('Введите  название предметов : ')}
            print(f'Итоговый список {students_marks}')
        else:
            print('Ошибка : неверно введено имя ученика !')
    elif command == 10:
        print(f'Исходный список {students_marks}')
        students_marks = {input('Введите новые имена учеников : ')}
        print(f'Итоговый список {students_marks}')

    elif command == 11:
        student = input('Введите имя ученика : ')
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'\tСредний балл - {marks_sum // marks_count}')
            print()
    elif command == 12:
        print('Выход из программы')
        break
    else:
        print('Ошибка, Введите номер команды из предложенного списка !)')
        print()
        print('''
                Список команд:
                1. Добавить оценки ученика по предмету
                2. Вывести средний балл по всем предметам по каждому ученику
                3. Вывести все оценки по всем ученикам
                5. Удалить оценку ученика по предмету
                6. Удалить предмет у ученика
                7. Удалить ученика
                8. Отредактировать оценки учеников
                9. Отредактировать предметы учеников
                10. Отредактировать имена учеников
                11. Вывести все  оценки определенного ученика
                12. Выход из программы
                ''')

