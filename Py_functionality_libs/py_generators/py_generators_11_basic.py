def orders_generator():
    print("Start generator")
    try:
        print("yield start:")
        yield 101
        yield 102
        yield 103
    finally:
        print("execute finally")


def orders_generator2():
    print("Start generator2")
    try:
        print("yield start2:")
        yield 101
        yield 102
    finally:
        print("execute finally2")


stream = orders_generator()
print(next(stream), "done 101")
print(next(stream), "done 102")
# print(next(stream), "done 103")  # This will raise StopIteration
print("Before close")
# Close the generator explicitly
stream.close()
print("After close")
# Remark: unlike the first generator, the second generator
# is not closed explicitly, but finally block will be executed
# when the generator is garbage collected AFTER closing console process
stream2 = orders_generator2()
print(next(stream2))
