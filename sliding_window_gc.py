from Bio import SeqIO
import pandas as pd

record = SeqIO.read("data/E_coli.fasta", "fasta")
sequence = str(record.seq).upper()

window_size = 1000
step_size = 500

results = []

for start in range(0, len(sequence) - window_size + 1, step_size):
    window = sequence[start:start + window_size]

    g_count = window.count("G")
    c_count = window.count("C")
    valid_bases = sum(window.count(base) for base in "ATGC")

    if valid_bases > 0:
        gc_content = ((g_count + c_count) / valid_bases) * 100
    else:
        gc_content = 0

    results.append({
        "Start_Position": start + 1,
        "End_Position": start + window_size,
        "GC_Content_Percent": round(gc_content, 2)
    })

df = pd.DataFrame(results)
df.to_csv("results/ecoli_sliding_window_gc.csv", index=False)

print(df.head())
print(f"\nTotal windows analysed: {len(df)}")
print("Results saved to results/ecoli_sliding_window_gc.csv")
