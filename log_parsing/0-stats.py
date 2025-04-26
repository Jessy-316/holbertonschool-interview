#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """Print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    valid_codes = status_codes.keys()
    
    try:
        for line in sys.stdin:
            line = line.strip()
            
            try:
                # Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
                parts = line.split('"')
                if len(parts) != 3:
                    continue
                
                # Check if the format matches what we expect
                request_info = parts[1]
                if not request_info.startswith("GET /projects/"):
                    continue
                
                # Get the status code and file size
                status_and_size = parts[2].strip().split()
                if len(status_and_size) != 2:
                    continue
                
                try:
                    status_code = int(status_and_size[0])
                    file_size = int(status_and_size[1])
                except ValueError:
                    continue
                
                total_size += file_size
                if status_code in valid_codes:
                    status_codes[status_code] += 1
                
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
            except Exception:
                continue
    
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)
