import math
import json
from market_maker.sma import sma


class BollingerBands:
    def __init__(self, data):
        newdict = {
            'data': data
        }
        self.data = json.loads(json.dumps(newdict))
        self.middle = sma(self.data)
        self.deviation = self.volatility(self)
        self.lower = self.lowerBand(self)
        self.upper = self.upperBand(self)

    def volatility(self):
        lista2 = [pow(x.bidPrice - self.middle, 2) for x in self.data.data]
        return math.sqrt(sma(lista2))

    def upperBand(self):
        return self.middle + self.deviation * 2

    def lowerBand(self):
        return self.middle - self.deviation * 2

    def percentB(self):
        return (((self.middle - self.lower) / (self.upper - self.lower)) * 100)
