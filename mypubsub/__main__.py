if __name__ == "__main__" and __package__ is None:
    import sys
    import pathlib
    import os
    print("Called from __main__.py as script cwd = {}".format(os.getcwd()))
    sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))

    __package__ = "project"

from mypubsub import MyPubSub

def main():
    print("Called from main()")
    p = MyPubSub()

if __name__ == "__main__":
    print("Called from __main__.py")
    main()