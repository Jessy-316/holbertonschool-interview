#!/usr/bin/python3
"""Statistics module for analyzing logs."""
import sys


def print_stats(stats, total_size):
    """Print the statistics for status codes and total file size."""
    print('File size: {}'.format(total_size))
    for s_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(s_code, count))


if __name__ == "__main__":
    total_size = 0
    count = 0
    stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            count += 1
            try:
                parts = line.split()
                if len(parts) > 2:
                    status_code = parts[-2]
                    file_size = int(parts[-1])

                    if status_code in stats:
                        stats[status_code] += 1
                    total_size += file_size
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(stats, total_size)

        print_stats(stats, total_size)

    except KeyboardInterrupt:
        print_stats(stats, total_size)
        raise