import my_lib
import pytest
import tests.test_Fib as testFib
import tests.test_Calc as testCalc
import tests.test_Sort as testSort

if __name__ == '__main__':
    #Тест функции, которая выводит первые "n" чисел Фибоначчи
    testFib.test_on_correct()
    testFib.test_on_negative()
    #Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
    testSort.test_on_ordered()
    testSort.test_on_unordered()
    testSort.test_on_equal()
    testSort.test_on_string()
    #Тест функции, которая производит математические операции
    testCalc.test_add()
    testCalc.test_sub()
    testCalc.test_multi()
    testCalc.test_div()
    testCalc.test_div_by_zero()