
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/gc_content_results.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["Organism"], df["GC_Content_Percent"])

plt.title("GC Content Comparison of Five Biological Sequences")
plt.xlabel("Organism")
plt.ylabel("GC Content (%)")
plt.ylim(0, 100)
plt.xticks(rotation=25, ha="right")

plt.tight_layout()
plt.savefig("results/gc_content_comparison.png", dpi=300)
plt.show()

print("Bar chart saved to results/gc_content_comparison.png")
