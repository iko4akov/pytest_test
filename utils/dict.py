
def get_val(collection, key, default='git'):
    if len(collection) == 0:
        return default

    return collection[key]
