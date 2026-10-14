
import pandas as pd
from pathlib import Path

folder = Path("results/sliding_window")

files = {
    "Streptomyces coelicolor": "Streptomyces_coelicolor",
    "Mycobacterium tuberculosis": "Mycobacterium_tuberculosis",
    "E. coli K-12 MG1655": "E_coli",
    "Human mitochondrial DNA": "Human_mtDNA",
    "SARS-CoV-2": "SARS_CoV_2",
}

for organism, filename in files.items():
    path = folder / f"{filename}_sliding_window_gc.csv"
    df = pd.read_csv(path)

    highest = df.loc[df["GC_Content_Percent"].idxmax()]
    lowest = df.loc[df["GC_Content_Percent"].idxmin()]

    print(f"\n{organism}")
    print(
        f"Highest GC: {highest['GC_Content_Percent']}% "
        f"(positions {int(highest['Start_Position'])}-"
        f"{int(highest['End_Position'])} bp)"
    )
    print(
        f"Lowest GC: {lowest['GC_Content_Percent']}% "
        f"(positions {int(lowest['Start_Position'])}-"
        f"{int(lowest['End_Position'])} bp)"
    )
