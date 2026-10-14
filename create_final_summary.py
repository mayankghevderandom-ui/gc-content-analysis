
import pandas as pd
from pathlib import Path

overall = pd.read_csv("results/gc_content_results.csv")
folder = Path("results/sliding_window")

filename_map = {
    "NC_003888.3": "Streptomyces_coelicolor",
    "NC_000962.3": "Mycobacterium_tuberculosis",
    "NC_000913.3": "E_coli",
    "NC_012920.1": "Human_mtDNA",
    "NC_045512.2": "SARS_CoV_2",
}

summary = []

for _, sample in overall.iterrows():
    accession = sample["Accession"]
    filename = filename_map[accession]

    path = folder / f"{filename}_sliding_window_gc.csv"
    windows = pd.read_csv(path)

    highest = windows.loc[windows["GC_Content_Percent"].idxmax()]
    lowest = windows.loc[windows["GC_Content_Percent"].idxmin()]

    high_gc = highest["GC_Content_Percent"]
    low_gc = lowest["GC_Content_Percent"]

    summary.append({
        "Organism": sample["Organism"],
        "Accession": accession,
        "Sequence_Length_bp": sample["Sequence_Length_bp"],
        "Whole_Sequence_GC_Percent": sample["GC_Content_Percent"],
        "Mean_Window_GC_Percent": round(
            windows["GC_Content_Percent"].mean(), 2
        ),
        "Highest_Window_GC_Percent": high_gc,
        "Highest_Window_Start_bp": int(highest["Start_Position"]),
        "Highest_Window_End_bp": int(highest["End_Position"]),
        "Lowest_Window_GC_Percent": low_gc,
        "Lowest_Window_Start_bp": int(lowest["Start_Position"]),
        "Lowest_Window_End_bp": int(lowest["End_Position"]),
        "GC_Range_Percentage_Points": round(high_gc - low_gc, 2),
        "Number_of_Windows": len(windows),
    })

final_df = pd.DataFrame(summary)

output_path = "results/final_gc_summary.csv"
final_df.to_csv(output_path, index=False)

print(final_df.to_string(index=False))
print(f"\nFinal summary saved to {output_path}")
