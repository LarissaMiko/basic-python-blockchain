import hashlib
import json

#accept various number of inputs *args
def crypto_hash(*args):
    """
    Returns a SHA-256 hash of the given arguments
    Sort arguments before hashing so that the order does not matter
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))

    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 2 , 'three'): {crypto_hash('one', 2 , 'three')}")

if __name__ == '__main__':
    main()