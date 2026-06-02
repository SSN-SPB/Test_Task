expected_result = [1, 2, 3, 4, 5]


def unique_order(nums: list) -> list:
    result_list = []
    for x in nums:
        if x not in result_list:
            result_list.append(x)
    return result_list
