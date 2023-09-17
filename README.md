![Image alt](https://github.com/Irregulariti/help_me_please_laba1/raw/master/forreadme/first.jpg)  



# А теперь к делу: 

Машину тьюринга писать на сайте: https://turingmachine.io/


# ***ГАЙДИК***

1. Справа на сайте вы видите **поле для кода** - туда надо его написать, чтобы что-то получилось.
2. **input:** '(блаблаблабла)' - поле для ввода на ленту, что хотите ввести на ленту для теста - пишете сюда
3. **blank**: 'B' - знак пустой клетки ленты, по умолчанию это пробел(" ") - я использую "B"
4. **start state**: стартовое состояние машины - это то состояние, в котором указатель смотрит на первую цифру в числе
5. **table**: заголовок после которого начинается описание состояний машины тьюринга.

# Пример:

![Image alt](https://github.com/Irregulariti/help_me_please_laba1/raw/master/forreadme/example.png)  

# Алгоритм 

1. Сначала вы даёте название своему состоянию: в примере - *right*, *carry* и *done*.
2. Теперь начинаем описывать работу этого состояния:
   "*символ который сейчас находится под указателем*: *направление* // {write: *символ*, *направление*: *состояние в которое переходит машина*}

Направление - **R** or **L** - вправо и влево соответственно

Конечным состоянием будет являться ***done*** - в котором машина должна остановиться на первом символе ответа, и на самой ленте не будет ничего, кроме ответного числа.  


# Разбор примера *(по строкам)*
#Эта машина добавляет 1 к бинарному числу
1.  input - **1011** - двоичный код
2.  blank = **' '** - пробел в пустых клетках
3.  start state - стартовое состояние - оно **right** - то есть в начальный момент времени машина находится в состоянии right
4.  table: - начинаем описание состояний
5.  **состояние ***right*****
6.  Если под указателем **1** - то перемещаем указатель **вправо**
7.  Если под указателем **0** - тоже перемещаем **вправо**
8.  Если под указателем символ **' '** - то есть пробел - { перемещаем **влево** и переходим в состояние **carry**
9.  **состояние *carry***
10. Если под указателем **1** - то {заменяем на **0**, смещаемся **влево**}
11. Если под указателем **0** - то {заменяем на **1**, смещаемся **влево** и переходим в конечное состояние **done**}
12. Если под указателем **' '** - то {заменяем на **1**, смещаемся **влево** и переходим в конечное состояние **done**}
13. **состояние *done*** - конечное

Здесь хотелось бы пояснить что например мы можем заменить *11* и *12* строку на одну - записав это так:
  "**[0,' ']: {write: 1, L: done}**"


## Правила написания:
input, blank, start_state - в разных строках

# Ниже интерпретатор пайтона

https://www.onlinegdb.com/online_python_interpreter

# Инструкция:  

"1: Зайти на сайт интерпретатора" 

"2: Вставить код скрипта"  

"3: Снизу выбрать формат входных данных TEXT и вставить туда код машины"  

"4: Не забудьте дописать:  "-1" в конце скрипта, а иначе попадёте в беск цикл"  

"5: Enjoy"  

# Откройте окно, сейчас будет душно
![Image alt](https://github.com/Irregulariti/help_me_please_laba1/raw/master/forreadme/second.jpg)

пусть i - состояние машины, si - количество операций в данном состоянии

тогда num = sum(si) по всем i

Выводные данные:

  num строк - представление машины в виде "пятёрок":
  
    "начальное состояние, текущий символ, печатающийся символ, направление движения, новое состояние"
    
  оставшиеся строки - текст для отчёта, который описывает машину в словесном формате.
  

Хорошей первой лабы!
©Irregulariti <3
