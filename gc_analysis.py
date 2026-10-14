from Bio import SeqIO

# Read the FASTA file
record = SeqIO.read("data/ecoli.fasta", "fasta")
sequence = str(record.seq).upper()

# Count canonical DNA bases
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

# Calculate the number of valid bases
total_bases = a_count + t_count + g_count + c_count

# Count ambiguous or other non-ATGC characters
ambiguous_bases = len(sequence) - total_bases

# Calculate GC content safely
if total_bases > 0:
    gc_content = ((g_count + c_count) / total_bases) * 100
else:
    gc_content = 0

# Display the results
print("Organism: Escherichia coli K-12 MG1655")
print("Accession:", record.id)
print("Sequence length:", len(sequence), "bp")
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print("Ambiguous/other bases:", ambiguous_bases)
print("GC content:", round(gc_content, 2), "%")
