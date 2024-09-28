def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


inner_function()
#   Питон выдаст ошибку, т.к. мы пытаемся вызвать функцию в глобальном пространстве имен,
# тогда как функция "inner_function()" определяется в локальном пространстве имен функции
# "test_function" .
