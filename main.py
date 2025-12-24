student1 = ("Иван", "Иванов", 85, 92)
student2 = ("Мария", "Петрова", 54, 88)
student3 = ("Алексей", "Сидоров", 35, 45)

students = [student1, student2, student3] # Массив студентов
best_average = 0 # Лучший средрний балл
best_student = '' # Студент с лучшим средним баллом

print('ОТЧЕТ ПО СТУДЕНТАМ')
for student in students:
    name, surname, math, physics = student
    average = (math + physics) / 2
    
    if best_average < average:
        best_average = average
        best_student = student
    
    print(f'Студент {name}\nСредний балл: {average}\nСтатус: {'✅ СДАЛ' if average >= 60 else '❌ НЕ СДАЛ'}')
    
print('=' * 40)
print(f'Студент с лучшим средним баллом: {best_student}\nБалл: {best_average}')

