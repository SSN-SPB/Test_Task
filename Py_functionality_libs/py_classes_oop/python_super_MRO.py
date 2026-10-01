class X:
    def call(self):
        print("Calling from X directly")


class Y(X):
    def call(self):
        print("Calling from Y")
        # the next line calls from the next class
        # in the MRO (in this case it is X)
        super().call()


class Z(X):
    def call(self):
        print("Calling from Z")
        print("The next line calls X from from Z")
        # it calls not from base class but from the next class in the MRO!!!
        super().call()


class W(Z, Y):
    def call(self):
        print("Calling from W")
        super().call()


class W1(Z):
    def call(self):
        print("Calling from W1")
        super().call()


w = W()
w1 = W1()
w.call()
# w1.call()
print(W.mro())
