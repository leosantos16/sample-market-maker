import math
import json
from market_maker.sma import sma


class BollingerBands:
    def __init__(self, data):
        newdict = {
            'data': data
        }
        self.data = json.loads(json.dumps(newdict))
        self.data = list(map(lambda val: val['bidPrice'], self.data['data']))
        self.middle = sma.sma(self.data)
        self.deviation = self.volatility()
        self.lower = self.lowerBand()
        self.upper = self.upperBand()
        self.percent_b = self.percentB()

    def volatility(self):
        lista2 = [pow(x - self.middle, 2)
                  for x in self.data]
        return math.sqrt(sma.sma(lista2))

    def upperBand(self):
        return self.middle + self.deviation * 2

    def lowerBand(self):
        return self.middle - self.deviation * 2

    def percentB(self):
        return (((self.middle - self.lower) / (self.upper - self.lower)) * 100)
