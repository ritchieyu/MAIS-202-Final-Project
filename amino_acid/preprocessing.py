# Libraries
from google.colab import files
import Bio
from Bio import SeqIO
from datetime import datetime
import re


# Import data
data = list(SeqIO.parse(fasta_path, "fasta"))


### Preprocessing ###
# Clean amino acid sequences
# Select sequences by location
# Order sequences by sequence collection date

def clean_sequence(fasta_list, target_length):
  # Ignore sequences with "X", ignore duplicate IDs
  sequences = {}
  for seq_record in fasta_list:
    id = seq_record.id
    sequence = str(seq_record.seq)
    if (len(sequence) == target_length) and (sequence.count("X") == 0):
      if id not in sequences:
        sequences[id] = sequence
 
  with open(clean_fasta_path, "w+") as output_file:
    for id in sequences:
      output_file.write(">" + id + "\n" + sequences[id] + "\n")


def select_location(fasta_list, geo_location):
  sequences = {}
  checker = "Spike|hCoV-19/" + geo_location + "/"
  counter = 0
  for seq_record in fasta_list:
    id = str(seq_record.id)
    sequence = str(seq_record.seq)
    if checker in id:
      sequences[id] = sequence
  
  with open(location_fasta_path, "w+") as output_file:
    for id in sequences:
      output_file.write(">" + id + "\n" + sequences[id] + "\n")


def sort_by_date(fasta_list):
  sequences = {}
  date_id = []
  sorted = []
  for seq_record in fasta_list:
    id = str(seq_record.id)
    sequence = str(seq_record.seq)
    sequences[id] = sequence   # Define hash table
    match = re.search(r'\d{4}-\d{2}-\d{2}', id)
    if match:
      if match.group()[-2:] != "00":
        date = datetime.strptime(match.group(), '%Y-%m-%d')
        date_id.append((id, date))
  
  date_id.sort(key=lambda x:x[1]) 

  for date_id_tuple in date_id:
    id = date_id_tuple[0]
    sequence = sequences[id]
    sorted.append((id, sequence))

  with open(ordered_fasta_path, "w+") as output_file:
    for id_seq in sorted:
        output_file.write(">" + id_seq[0] + "\n" + id_seq[1] + "\n")


clean_sequence(data, 1273) # 1273 is size of original Wuhan
data1 = list(SeqIO.parse(clean_fasta_path, "fasta"))

select_location(data1, "USA")
data2 = list(SeqIO.parse(location_fasta_path, "fasta"))

sort_by_date(data2)
data3 = list(SeqIO.parse(ordered_fasta_path, "fasta"))
