#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 46
# formats

seq1 = "atgcttcggcaagactcaaaaaata23"
seq2 = "atscttcsscaagactaaaaaaata9"


def main():
    zip_seqs = zip(seq1, seq2)
    enum_seqs = enumerate(zip_seqs)
    for i, (a, b) in enum_seqs:
        if a != b:
            print(f"index: {i}, first line: {a}, second: {b}")


if __name__ == "__main__":
    main()
