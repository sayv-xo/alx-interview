#!/usr/bin/python3
"""
log parser
"""
import sys


def print_stat(stat_count, delta_size):
    """
    prints the file size and status code counts.
    """
    print("File size: {}".format(delta_size))
    for stat_id in sorted(stat_count):
        count = stat_count[stat_id]
        if count > 0:
            print("{}: {}".format(stat_id, count))


total_file_size = 0
line_counter = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            file_size_str = parts[-1]
            status_code = parts[-2]
            try:
                file_size = int(file_size_str)
                total_file_size += file_size
                line_counter += 1

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                if line_counter == 10:
                    print_stat(status_code_counts, total_file_size)
                    line_counter = 0

            except ValueError:
                continue

finally:
    if line_counter > 0:
        print_stat(status_code_counts, total_file_size)
