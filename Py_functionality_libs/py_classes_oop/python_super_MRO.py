class X:
    def call(self):
        print("Calling from X")


class Y(X):
    def call(self):
        print("Calling from Y")


class Z(X):
    def call(self):
        print("Calling from Z")
        print("The next line calls X from from Z")
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
w1.call()
print(W.mro())
