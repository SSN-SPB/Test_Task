from pympler import tracker, asizeof
# from service_packages.service_logger.logger_provider import logger

# pip install pympler
tr = tracker.SummaryTracker()

test_list = list()


def main():
    for i in range(0, 1000, 2):
        test_list.append(i)
        if i % 100 == 0:
            print(f"\n===== i = {i} =====")
            print(f"Elements in test_list: {len(test_list)}")
            print(f"Size of test_list: {asizeof.asizeof(test_list)} bytes")
            tr.print_diff()


# tr.print_diff()


if __name__ == "__main__":
    main()

    print("\n===== FINAL =====")
    print(f"Elements in test_list: {len(test_list)}")
    print(f"Size of test_list: {asizeof.asizeof(test_list)} bytes")

# from pympler import tracker
#
# tr = tracker.SummaryTracker()
#
# data = []
#
# for i in range(10):
#     data.extend(range(100_000))
#
#     print(f"\nIteration {i}")
#     tr.print_diff()
