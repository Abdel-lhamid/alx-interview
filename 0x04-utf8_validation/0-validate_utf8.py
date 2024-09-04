#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    def is_continuation(byte):
        """Check if a byte is a valid continuation byte."""
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i] & 0xFF  # Ensure we only consider the last 8 bits
        if (byte & 0b10000000) == 0:
            i += 1
        elif (byte & 0b11100000) == 0b11000000:
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif (byte & 0b11110000) == 0b11100000:
            if (i + 2 >= len(data) or
                    not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2])):
                return False
            i += 3
        elif (byte & 0b11111000) == 0b11110000:
            if (i + 3 >= len(data) or
                    not is_continuation(data[i + 1]) or
                    not is_continuation(data[i + 2]) or
                    not is_continuation(data[i + 3])):
                return False
            i += 4
        else:
            return False
    return True
