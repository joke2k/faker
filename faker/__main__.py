import sys

def main(args=None):
    from faker import fake
    fake.help(*args)


if __name__ == "__main__":
    main(sys.argv[1:])