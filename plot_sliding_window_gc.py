
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/ecoli_sliding_window_gc.csv")

plt.figure(figsize=(12, 5))

plt.plot(
    df["Start_Position"],
    df["GC_Content_Percent"],
    linewidth=0.8,
    label="Sliding-window GC content"
)

plt.axhline(
    y=50.79,
    linestyle="--",
    linewidth=1.5,
    label="Whole-genome GC content (50.79%)"
)

plt.title("Sliding-Window GC Content Across the E. coli Genome")
plt.xlabel("Genome Position (bp)")
plt.ylabel("GC Content (%)")
plt.legend()
plt.tight_layout()

plt.savefig("results/ecoli_sliding_window_gc.png", dpi=300)
plt.show()

print("Sliding-window graph saved successfully.")
