# https://leetcode.com/problems/zigzag-conversion/
# version 2026-Apr-09 in progress


tested_string = "PAYPALISHIRING"
num_rows = 3
expected_output = "PINALSIGYAHRPI"

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        draft_columns = len(s)/numRows
        number_of_columns = int(draft_columns) + (draft_columns > int(draft_columns))
        print(f"number of columns = {number_of_columns}")
        combined_list = [[0 for _ in range(number_of_columns)] for _ in range(numRows)]
        e = -1
        c = -1
        for y in s:
            c += 1
            t_index = c
            counter = num_rows
            h, v = 0, 0
            calculated_index = t_index%numRows
            print(f"{y} - {t_index} - {calculated_index}")
            combined_list[h][v] = y

        return combined_list






def main():
    c = Solution()
    print(f" result : {c.convert(s=tested_string, numRows=num_rows)}")
    # assert c.convert(s=tested_string, numRows=num_rows) == expected_output



if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
