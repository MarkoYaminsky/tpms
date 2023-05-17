def rounded(function):
    def wrapper(*args, **kwargs):
        return round(function(*args, *kwargs), 2)

    return wrapper
