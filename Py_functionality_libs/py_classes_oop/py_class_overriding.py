class X:
    def call(self):
        print("Calling from X")


class Y(X):
    def call(self):
        print("Calling from Y")


obj = Y()
obj.call()  # Output: 'Calling from Y'
print(Y.mro())
