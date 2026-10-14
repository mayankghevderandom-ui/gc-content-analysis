
import os
import pandas as pd
from Bio import SeqIO

SAMPLES = {
    "Streptomyces coelicolor": "data/Streptomyces_coelicolor.fasta",
    "Mycobacterium tuberculosis": "data/Mycobacterium_tuberculosis.fasta",
    "E. coli K-12 MG1655": "data/E_coli.fasta",
    "Human mitochondrial DNA": "data/Human_mtDNA.fasta",
    "SARS-CoV-2": "data/SARS_CoV_2.fasta",
}

results = []

for organism, filepath in SAMPLES.items():
    record = SeqIO.read(filepath, "fasta")
    sequence = str(record.seq).upper()

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    total_bases = a_count + t_count + g_count + c_count
    sequence_length = len(sequence)
    ambiguous_bases = sequence_length - total_bases

    if total_bases > 0:
        gc_content = ((g_count + c_count) / total_bases) * 100
    else:
        gc_content = 0

    results.append({
        "Organism": organism,
        "Accession": record.id,
        "Sequence_Length_bp": sequence_length,
        "A_Count": a_count,
        "T_Count": t_count,
        "G_Count": g_count,
        "C_Count": c_count,
        "Ambiguous_Bases": ambiguous_bases,
        "GC_Content_Percent": round(gc_content, 2),
    })

os.makedirs("results", exist_ok=True)

df = pd.DataFrame(results)
df.to_csv("results/gc_content_results.csv", index=False)

print(df.to_string(index=False))
print("\nResults saved to results/gc_content_results.csv")
