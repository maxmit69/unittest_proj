def get_val(collection, key, default='git'):
    """
    Возвращает значение по ключу из коллекции, если ключ существует.
    Если ключ не существует, возвращает значение по умолчанию.
    :param collection: Коллекция.
    :param key: Ключ.
    :param default: Значение по-умолчанию.
    :return: Значение по ключу или значение по-умолчанию.
    """

    if key in collection:
        return collection[key]
    return default
