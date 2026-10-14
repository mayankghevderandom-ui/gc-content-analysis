import pandas as pd
from pathlib import Path

overall = pd.read_csv("results/gc_content_results.csv")

folder = Path("results/sliding_window")
rows = []

for _, sample in overall.iterrows():
    name = sample["Organism"]
    accession = sample["Accession"]

    filename_map = {
        "NC_003888.3": "Streptomyces_coelicolor",
        "NC_000962.3": "Mycobacterium_tuberculosis",
        "NC_000913.3": "E_coli",
        "NC_012920.1": "Human_mtDNA",
        "NC_045512.2": "SARS_CoV_2",
    }

    filename = filename_map[accession]
    path = folder / f"{filename}_sliding_window_gc.csv"

    windows = pd.read_csv(path)
    mean_gc = windows["GC_Content_Percent"].mean()

    rows.append({
        "Organism": name,
        "Whole_Sequence_GC_Percent": sample["GC_Content_Percent"],
        "Mean_Window_GC_Percent": round(mean_gc, 2),
        "Number_of_Windows": len(windows),
    })

comparison = pd.DataFrame(rows)
comparison.to_csv("results/gc_validation_comparison.csv", index=False)

print(comparison.to_string(index=False))
print("\nSaved to results/gc_validation_comparison.csv")
