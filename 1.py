# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int (input ('Введите порядковый номер дня недели и нажмите Enter: '))
if day == 6 or day == 7:
    print ('Введеный день является выходным')
elif day >= 1 and day <=5:
    print ('Введенный день - будничный')
else:
    print ('В неделе семь дней, балбес...Попробуй еще раз!')
