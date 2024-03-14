
if __name__ == '__main__':
    while True:
        cache = [{}]

        address = input(" >>> ")

        # first 7 bits are the tag
        tag = address[:6]

        # next 3 bits are the index
        index = address[6:9]

        # last two bits are the offset
        offset = address[9:]

        # convert the binary results to hex, and print
        print(f"Tag: {hex(int(tag, 2))}")
        print(f"Index: {hex(int(index, 2))}")
        print(f"Offset: {hex(int(offset, 2))}")





