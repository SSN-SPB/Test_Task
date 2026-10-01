class A:
    def send(self):
        return ["class A"]


class B(A):
    def send(self):
        return ["class B"] + super().send()


class C(A):
    def send(self):
        return ["class C"] + super().send()


class D(B, C):
    pass


def main():
    result_d = D()
    print(result_d.send())
    # class B is called first, then class C because of MRO D(B, C),
    # and finally class A
    assert result_d.send() == ["class B", "class C", "class A"]
    result_b = B()
    print(result_b.send())
    # class B is called first, then class A because of MRO B(A)
    assert result_b.send() == ["class B", "class A"]


if __name__ == "__main__":
    main()
