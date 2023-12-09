"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: Исходный список.
    :param index: Индекс извлекаемого элемента.
    :param default: Значение по-умолчанию.
    :return: Значение по индексу или значение по-умолчанию.
    """

    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: Исходный список.
    :param start: Индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: Индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: Массив элементов
    """

    length = len(coll)

    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    else:
        normalized_start = start

    if end is None or end > length:
        normalized_end = length
    else:
        normalized_end = end

    return coll[normalized_start:normalized_end]