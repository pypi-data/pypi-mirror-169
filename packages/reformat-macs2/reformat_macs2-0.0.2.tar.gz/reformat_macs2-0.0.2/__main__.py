import sys

if __package__:
    from .reformat_macs2 import main
else:
    from reformat_macs2 import main


main(sys.argv[1:])
