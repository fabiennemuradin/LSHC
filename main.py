"""
This is the main execution environment for the MSMP++ procedure.

https://github.com/stefanvanberkum/MSMP
"""

from data_loader import load
from LSH import common_binary, convert_binary, convert_binary_old, minhash, lsh
import time

def main():
    """
    Runs the whole MSMP++ procedure, and stores results.

    :return:
    """

    identify_common_binary = False
    run_lsh = True

    file_path = "data/TVs.json"

    start_time = time.time()

    data_list, data_dict = load(file_path)

    if identify_common_binary:
        common_binary(data_list)

    if run_lsh:
        do_lsh(data_list, 0.8)

    end_time = time.time()
    print("Elapsed time:", end_time - start_time, "seconds")


def do_lsh(data_list, t):
    binary_vec = convert_binary(data_list)
    n = round(round(0.5 * len(binary_vec)) / 100) * 100
    signature = minhash(binary_vec, n)
    candidates = lsh(signature, t)
    print()

if __name__ == '__main__':
    main()
