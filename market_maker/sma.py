import functools


class sma:
    def sma(data):
        return functools.reduce(lambda val1, val2: val1 + val2, data)/len(data)
