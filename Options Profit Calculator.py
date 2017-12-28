from wallstreet import Stock, Call, Put

# inputs to ask which stock the user wants to look up
# gticker = input("Input stock ticker")
# optiontype = input("Call or Put?")
# expdate = input("Expiration date? (dd-mm-yyyy)")
# sprice = int(input("Strike price?"))


#test
gticker = 'AAPL'
optiontype = 'call'
expdate = '19-01-2018'
sprice = "170"

if "call" == optiontype.casefold():
    option = Call(gticker, d=int(expdate[0:2]), m=int(expdate[3:5]),
                  y=int(expdate[6:10]), strike=int(sprice), source='yahoo')
else:
    option = Put(gticker, d=int(expdate[0:2]), m=int(expdate[3:5]),
                 y=int(expdate[6:10]), strike=int(sprice), source='yahoo')

class BasicInfo:

    def __init__(self, ticker):
        self.delta = ticker.delta()
        self.gamma = ticker.gamma()
        self.theta = ticker.theta()
        self.vega = ticker.vega()
        self.price = ticker.price
        self.breakeven = ticker.price + int(sprice)

    def initial(self):
        print('Price: %.2f' % self.price)
        print('Break-even at expiry: %.2f' % self.breakeven)
        print('Delta: %.2f' % self.delta)
        print('Gamma: %.2f' % self.gamma)
        print('Theta: %.2f' % self.theta)
        print('Vega: %.2f' % self.vega)


newoption = BasicInfo(option)

newoption.initial()






