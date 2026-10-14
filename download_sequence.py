from Bio import Entrez

Entrez.email = "mayankghevde.random@gmail.com"

accession = "NC_000913.3"

handle = Entrez.efetch(
    db="nuccore",
    id=accession,
    rettype="fasta",
    retmode="text"
)

sequence_data = handle.read()
handle.close()

output_file = "data/ecoli.fasta"

with open(output_file, "w") as file:
    file.write(sequence_data)

print("Sequence downloaded successfully!")
print("Saved to:", output_file)
