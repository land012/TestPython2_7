# coding: utf-8

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k1", help="k1 args")
    parser.add_argument("--mparams", help="method-s params", nargs="+")

    args = parser.parse_args()

    print(args.k1)

    print(",".join(args.mparams))

    if args.mparams:
        print(type(args.mparams))  # <type 'list'>
        print(args.mparams)


if __name__ == "__main__":
    main()
