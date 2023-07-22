# Parallelize the parsing of xml files
# Author Namuna Panday; UCLA, 2023

import xml.etree.ElementTree as ET
from multiprocessing import Pool
from parser.splited_xml_parser import SplitedEntryParser
import os
import json as json

def parse_file(file_path): 
    tree = ET.parse(file_path)
    root = tree.getroot()

    # create parser object
    SEP = SplitedEntryParser(root)

    # parse the entry
    entry_dict = {'accession': SEP.get_accession(),\
                   'name': SEP.get_name(),\
                    'gene': SEP.get_gene(),\
                    'organism': SEP.get_organism(),\
                    'sequence': SEP.get_sequence(),\
                    'uniprotId': SEP.get_uniprotId(),\
                    'ptm': SEP.get_ptm(),
                    'references': SEP.get_references()}
        
    return entry_dict
    
if __name__ == '__main__':
    file_dir = 'xmldataset'


    # get the first 10 files
    #nfiles = 10
    #nfiles = len(file_paths)

    # get the file paths or add [0:nfiles] to get the first nfiles
    file_paths = [os.path.join(file_dir, file) \
                  for file in os.listdir(file_dir) if file.endswith('.xml')]
    
    
    
    #parallisize the parsing
    with Pool() as pool:
        results = pool.map(parse_file, file_paths)

    # Now `results` is a list of the return values of `parse_file` function
    #print(results)


    with open('output/all_uniprot_data.json', 'w') as f:
        json.dump(results, f)