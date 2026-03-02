class X:
    def call(self):
        print("Calling from X")


class Y(X):
    def call(self):
        print("Calling from Y")


class Z(X):
    def call(self):
        print("Calling from Z")


class W(Y, Z):
    def call(self):
        super().call()


w = W()
w.call()
