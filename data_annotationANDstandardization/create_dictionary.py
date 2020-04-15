import pandas as pd
import argparse, sys

parser = argparse.ArgumentParser()
   
parser.add_argument("-o", "--outputfile", help="Output file name with extension", required=True)
parser.add_argument("-i", "--inputfile", help="Input file name with extension", required=True)
#parser.add_argument("-o", "--outputfile", help="Output file name with extension", default='mydict.tsv')
#parser.add_argument("-i", "--inputfile", help="Input file name with extension", default='mesh_ctd_rxnorm.tsv')

args = parser.parse_args()
#args = parser.parse_args(sys.argv[3:])  #if pycharm console
input_file = args.inputfile
output_file = args.outputfile

data = pd.read_csv(input_file, sep = "\t", encoding="utf-8")

data['term'] = data.term.astype(str).str.lower()
data['cui'] = data.cui.astype(str).str.lower()

#print(data['term'])
#print(data['cui'])

header = ["cui", "term"]

data.to_csv(output_file, columns = header, sep = "\t", encoding="utf-8", index=False)