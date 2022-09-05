import argparse
import sys
from fastarecs import reader


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()


    #print(f"Now I need to process the records in {args.fasta}")
    #print(f"and the coordinates in {args.coords}")

    indexedFASTA = indexFASTA(args.fasta)
    for coord in args.coords:
        coordinate = list(filter(None,coord.strip().split(" ")))
        seq = indexedFASTA[coordinate[0]]
        print(seq[int(coordinate[1])-1:int(coordinate[2])-1])
        


def indexFASTA(fasta):
    dic = {}
    records = reader(fasta)
    for record in records:
        dic[record[0]] = record[1]
    return dic


if __name__ == '__main__':
    main()
