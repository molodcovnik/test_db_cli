"""
BEGIN - начало транзакции.
ROLLBACK - откат текущей (самой внутренней) транзакции
COMMIT - фиксация изменений текущей (самой внутренней) транзакции
"""

"""
Пример
> BEGIN
> SET A 10
> BEGIN
> SET A 20
> BEGIN
> SET A 30
> GET A
30
> ROLLBACK
> GET A
20
> COMMIT
> GET A
20
"""



if __name__ == "__main__":
    lst = [{'a':10}, {'a':12}]
    print(lst)