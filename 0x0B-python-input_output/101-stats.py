#!/usr/bin/python3
""" Working with Files and JSON  """
import fileinput


def print_out(pr_num, pr_arr):
    print(f"File size: {pr_num}")
    # filter and sort
    pr_arr = sorted(filter(lambda x: x[1], pr_arr))
    arr = [f'{item[0]}: {item[1]}' for item in pr_arr]
    print("\n".join(arr))


def main():
    """ read from stdin and print out """
    tot_size, l_count = 0, 0
    ocr = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0,
    }
    try:
        for line in fileinput.input(encoding="utf-8"):
            # spli line
            line_arr = line.split()
            l_count += 1
            # size is last item, code is second to last
            size, code = line_arr[-1], line_arr[-2]
            tot_size += int(size)
            ocr[code] += 1
            # print dets
            if l_count % 10 == 0:
                print_out(tot_size, ocr.items())
    except KeyboardInterrupt:
        print_out(tot_size, ocr.items())
        exit(0)


if __name__ == "__main__":
    main()
