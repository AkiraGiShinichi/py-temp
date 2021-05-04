import argparse


# ----------------------------------- Main ----------------------------------- #
def _main_(args):
    print(f'This is {args.desc}')
# ---------------------------------------------------------------------------- #


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Sample')
    argparser.add_argument('-d', '--desc', help='Description', default='.')
    args = argparser.parse_args()

    _main_(args)