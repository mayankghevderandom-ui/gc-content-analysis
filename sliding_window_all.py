
import os
import pandas as pd
from Bio import SeqIO

SAMPLES = {
    "Streptomyces_coelicolor": "data/Streptomyces_coelicolor.fasta",
    "Mycobacterium_tuberculosis": "data/Mycobacterium_tuberculosis.fasta",
    "E_coli": "data/E_coli.fasta",
    "Human_mtDNA": "data/Human_mtDNA.fasta",
    "SARS_CoV_2": "data/SARS_CoV_2.fasta",
}

WINDOW_SIZE = 1000
STEP_SIZE = 500

os.makedirs("results/sliding_window", exist_ok=True)

for name, filepath in SAMPLES.items():
    record = SeqIO.read(filepath, "fasta")
    sequence = str(record.seq).upper()

    results = []

    for start in range(
        0,
        len(sequence) - WINDOW_SIZE + 1,
        STEP_SIZE
    ):
        window = sequence[start:start + WINDOW_SIZE]

        g_count = window.count("G")
        c_count = window.count("C")
        valid_bases = sum(window.count(base) for base in "ATGC")

        if valid_bases > 0:
            gc_content = ((g_count + c_count) / valid_bases) * 100
        else:
            gc_content = 0

        results.append({
            "Start_Position": start + 1,
            "End_Position": start + WINDOW_SIZE,
            "GC_Content_Percent": round(gc_content, 2)
        })

    df = pd.DataFrame(results)
    output_path = f"results/sliding_window/{name}_sliding_window_gc.csv"
    df.to_csv(output_path, index=False)

    print(f"{name}: {len(df)} windows saved to {output_path}")
