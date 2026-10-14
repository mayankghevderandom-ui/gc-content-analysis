
import os
import pandas as pd
import matplotlib.pyplot as plt

SAMPLES = {
    "Streptomyces_coelicolor": 72.12,
    "Mycobacterium_tuberculosis": 65.61,
    "E_coli": 50.79,
    "Human_mtDNA": 44.36,
    "SARS_CoV_2": 37.97,
}

os.makedirs("results/sliding_window/plots", exist_ok=True)

for name, overall_gc in SAMPLES.items():
    input_path = f"results/sliding_window/{name}_sliding_window_gc.csv"
    df = pd.read_csv(input_path)

    plt.figure(figsize=(12, 5))

    plt.plot(
        df["Start_Position"] / 1_000_000,
        df["GC_Content_Percent"],
        linewidth=0.8,
        label="Sliding-window GC content"
    )

    plt.axhline(
        y=overall_gc,
        linestyle="--",
        linewidth=1.5,
        label=f"Whole-sequence GC content ({overall_gc}%)"
    )

    plt.title(f"Sliding-Window GC Content: {name}")
    plt.xlabel("Sequence Position (Mb)")
    plt.ylabel("GC Content (%)")
    plt.legend()
    plt.tight_layout()

    output_path = f"results/sliding_window/plots/{name}_gc_plot.png"
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Saved: {output_path}")

print("All sliding-window plots created successfully.")
