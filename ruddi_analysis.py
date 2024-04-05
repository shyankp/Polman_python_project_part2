#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Biopython Exercise 3: Analyze a genome


# In[3]:


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv



def ruddi(genome_files, output_file):
#Write it to a csv
    with open('ruddi_analysis.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        #Makes the titles of columns
        csvwriter.writerow(["Length of Genome", "GC_Content", "ATG_forward", "ATG_reverse"])
        
        
        #Parse the genome file
        for genome_file in genome_files:
            for seq_record in SeqIO.parse(genome_file, "fasta"):
                #Length of Genome
                genome_length = len(seq_record.seq)
            
                #Calculate GC Content
                gc_count = seq_record.seq.count('G') + seq_record.seq.count('C')
                gc_percentage = (gc_count / genome_length) * 100
            
                #Count ATG in Fwd Strand
                ATG_fwd = seq_record.seq.count('ATG')
            
                #Count ATG in Rev Strand
                reverse_sequence = seq_record.seq.reverse_complement()
                ATG_rev = reverse_sequence.count('ATG')
            
                #Add all the info to csv
                csvwriter.writerow([genome_length, gc_percentage, ATG_fwd, ATG_rev])
            

genome_files = ["GCA_000287275.1_ASM28727v1_genomic.fna"] 
output_file = "ruddi_analysis.csv"
ruddi(genome_files, output_file)
        
        

