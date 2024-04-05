#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Biopython Exercise 1: Parse Genbank files


# In[4]:


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv



def parse_genbank(gb_files, outputfile):
#Write it to a csv
    with open('gb_parse.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        #Makes the titles of columns
        csvwriter.writerow(["Accession", "Family", "Genus", "Species", "Num_Features", "Source"])

        #Parse the GenBank file
        for gb_file in gb_files:
            for seq_record in SeqIO.parse(gb_file, "genbank"):
                accession = seq_record.id
                taxonomy = seq_record.annotations['taxonomy']
                family = taxonomy[-1]
                genus = taxonomy[1]
                species = taxonomy[-2]
                num_features = len(seq_record.features)
                source = seq_record.annotations['source']

                #Add all the info to csv
                csvwriter.writerow([accession, family, genus, species, num_features, source])
            

gb_files = ["NZ_BHVZ01000001.1.gb", "NZ_CAJTFZ010000019.1.gb","NZ_CALPCP010000001.1.gb","NZ_CALPCY010000130.1.gb","NZ_SRYA01000017.1.gb"] 
outputfile = "gb_parse.csv"
parse_genbank(gb_files, outputfile)


# In[ ]:




