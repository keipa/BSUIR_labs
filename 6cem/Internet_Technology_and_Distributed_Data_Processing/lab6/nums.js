//4-2-2017

// В бесконечном цикле делается запрос на ввод двух чисел (два отдельных
// prompt). Числа сравниваются и выводится одна из трёх фраз: «числа равны»,
// «первое число меньше», «второе число меньше». Если пользователь ввёл не
// число, выводится фраза «первый ввод – не число» (или «второй ввод – не
// число»), и выполнение скрипта прекращается.

while (true) {
    var a = +prompt("Введите число", '');

    if (!a) {
        alert('первый ввод - не число');
        break;
    }
    var b = +prompt("Введите число", '');

    if (!b) {
        alert('второй ввод - не число');
        break;
    }

    if (a === b) alert('числа равны');

    if (a > b) alert('первое число больше');

    if (a < b) alert('второе число больше');

}
