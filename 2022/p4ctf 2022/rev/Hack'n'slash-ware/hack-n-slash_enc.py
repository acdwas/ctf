
import itertools, sys, os

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def hack(a,b):
    return pow(a, 0x10001, 0x6c7bd55985a8fb0991e07a947dd39d29)

def slash(a,b):
    return pow(a, 0x10001, 0x7838f58b2ab7ca1e35a5a0d5371f3917)


def quack_data(data):
    return b''.join([b[0](int.from_bytes(a, 'little'), b[1]).to_bytes(16, 'little') for a, b in zip(chunks(data, 15), itertools.cycle([(x, y) for x, y in zip([hack, slash], [105, 42])]))])


def main() -> None:
    filename = sys.argv[1]
    if not filename.endswith('.encrypt_me'):
        raise AssertionError
    with open(filename, 'rb') as (f):
        data = f.read()
    os.remove(filename)
    with open(f"{filename}.hacked_and_slashed", 'wb') as (f):
        f.write(quack_data(data))


if __name__ == '__main__':
    main()

  
    
    
