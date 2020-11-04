import functools


class sma:
    def sma(self, data):
        return functools.reduce(lambda val1, val2: val1.bidPrice + val2.bidPrice, data.data)/len(data.data)
