#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Biopython Exercise 2: Fasta fun with proteins


# In[3]:


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv



def parse_fasta(fasta_files, output_file):
#Write it to a csv
    with open('fasta_parse.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        #Makes the titles of columns
        csvwriter.writerow(["ID", "First_10_AA", "Length", "Number_Cs"])
        
        #Parse the Fasta file
        for fasta_file in fasta_files:
            for seq_record in SeqIO.parse(fasta_file, "fasta"):
                ID = seq_record.id
                first10aa = str(seq_record.seq[:10])
                length = len(seq_record.seq)
                number_cs = seq_record.seq.count('C')
            
                #Add all the info to csv
                csvwriter.writerow([ID, first10aa, length, number_cs])
            

fasta_files = ["AGI40145.1.fasta", "AGJ87295.1.fasta","WVS05366.1.fasta","WVV45440.1.fasta"] 
output_file = "fasta_parse.csv"
parse_fasta(fasta_files, output_file)


# In[ ]:




