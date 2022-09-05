import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    records = reader(args.fasta)
    
    for record in records:

        print(str(record[0])+'\t'+ str(record[1]))
        #print('{}\t{}'.format(record[0],record[1]))
        #print(record[0],"\t",record[1])



def reader(fasta):
    records = []
    name = ""
    sequence = ""
    for line in fasta:
        if line[0] == ">" and not name:
            name = line[1:].strip()
        elif line[0] == ">" and name:
            records.append([name, sequence])
            
            sequence = ""
            name = line[1:].strip()
        else:
            sequence+= line.strip()
    records.append([name, sequence])
    return records


if __name__ == '__main__':
    main()
