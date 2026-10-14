
import pandas as pd
from Bio import SeqIO

samples = {
    "NC_003888.3": "data/Streptomyces_coelicolor.fasta",
    "NC_000962.3": "data/Mycobacterium_tuberculosis.fasta",
    "NC_000913.3": "data/E_coli.fasta",
    "NC_012920.1": "data/Human_mtDNA.fasta",
    "NC_045512.2": "data/SARS_CoV_2.fasta",
}

saved_results = pd.read_csv("results/gc_content_results.csv")

for accession, filepath in samples.items():
    record = SeqIO.read(filepath, "fasta")
    sequence = str(record.seq).upper()

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    valid_bases = a + t + g + c
    gc_percent = round((g + c) / valid_bases * 100, 2)

    row = saved_results.loc[
        saved_results["Accession"] == accession
    ].iloc[0]

    length_matches = len(sequence) == row["Sequence_Length_bp"]
    gc_matches = gc_percent == row["GC_Content_Percent"]

    print(
        f"{accession}: "
        f"length={'PASS' if length_matches else 'FAIL'}, "
        f"GC={'PASS' if gc_matches else 'FAIL'} "
        f"(recalculated {gc_percent}%, saved "
        f"{row['GC_Content_Percent']}%)"
    )
