# garland
Вычисление минимальной высоты второго конца гирлянды.

Гирлянда состоит из *n*  лампочек на общем проводе. Один её конец закреплён на заданной высоте *A* mm *(h1=A)* .Благодаря силе тяжести гирлянда прогибается: высота каждой неконцевой лампы на 1 мм меньше, чем средняя высота ближайших соседей *(Hi=((Hi-1+Hi+1)/2)-1)* для *1<i<N*.

Требуется найти минимальное значение высоты второго конца *B (B=Hn),* такое что для любого *e>0* при высоте второго конца *B+e* для всех лампочек выполняется условие Hi>0.  Обратите внимание на то, что при данном значении высоты либо ровно одна, либо две соседних лампочки будут иметь нулевую высоту.

Подсказка: для решения этой задачи можно использовать двоичный поиск (метод дихотомии).

# Формат входного файла
> В первой строке входного файла содержится два числа *n* и *A(3<=n<=1000, n-целое, 10<=A<=1000, A-вещественное и дано не более чем с тремя знаками после десятичной точки).*

# Формат выходного файла
> Выведите одно вещественное число *B* инимальную высоту второго конца. Ваш ответ будет засчитан, если он будет отличаться от правильного не более, чем на 10^-6.

# Пример:
|input.txt|output.txt|
|---------|----------|
|8 15|9.75|
|692 532.81|446113.34434782615|
