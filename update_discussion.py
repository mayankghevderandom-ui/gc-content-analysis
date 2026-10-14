from pathlib import Path
import re

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

new_section = """## 11. Discussion

### 11.1 Overall GC Content

The five biological sequences showed a wide range of GC content, from 72.12% in *Streptomyces coelicolor* to 37.97% in SARS-CoV-2. *Mycobacterium tuberculosis* had a GC content of 65.61%, while *Escherichia coli* had an intermediate value of 50.79%. Human mitochondrial DNA had a GC content of 44.36%.

These differences illustrate how nucleotide composition varies between organisms and genome types. GC content can be influenced by evolutionary processes, including mutation patterns and natural selection. Codon usage and the composition of coding and non-coding regions may also contribute. However, this project measures nucleotide composition and does not directly test the mechanisms responsible for the observed differences.

SARS-CoV-2 has a comparatively low-GC RNA genome, while human mitochondrial DNA has a distinct genome organisation and evolutionary history from nuclear DNA. Their nucleotide composition should therefore be interpreted in the context of their different biological and evolutionary characteristics.

### 11.2 Regional GC Variation

*E. coli* showed the widest observed sliding-window GC range among the five sequences, from 28.6% to 69.6%, a difference of 41.0 percentage points. This indicates substantial variation in nucleotide composition across the genome.

Regional variation may reflect differences in gene and intergenic-region composition, horizontally acquired DNA, or genomic features such as ribosomal RNA operons. These are possible explanations rather than conclusions established by this analysis. Further investigation using genome annotations and known genomic features would be required to test these possibilities.

### 11.3 Genome Size and Window-Level Results

The analysed sequences differed considerably in length. The bacterial genomes ranged from approximately 4.4 to 8.7 million base pairs, whereas human mitochondrial DNA was 16,569 base pairs and the SARS-CoV-2 genome was 29,903 base pairs.

With a window size of 1,000 base pairs and a step size of 500 base pairs, the shorter sequences produced substantially fewer sliding windows than the bacterial genomes. Consequently, their regional profiles contain fewer observations for comparison.

Mean sliding-window GC percentages were close to the corresponding whole-sequence GC percentages. Small differences can arise because incomplete final windows were excluded, overlapping windows represent some regions multiple times, and window percentages were rounded before being saved.

### 11.4 Interpretation and Limitations

The results demonstrate differences in overall GC content and regional nucleotide composition across the five analysed sequences. However, GC content alone cannot establish the evolutionary, functional, or environmental mechanisms responsible for these patterns.

Further work could combine GC analysis with genome annotations, GC skew, codon-position analysis, and statistical comparisons to investigate the biological significance of regional variation."""

pattern = r"(?ms)^## 11\. Discussion\s*\n.*?(?=^## 12\. Visualisations\s*$)"

updated, count = re.subn(
    pattern,
    new_section + "\n\n",
    text,
    count=1
)

if count != 1:
    raise SystemExit(
        "ERROR: Expected exactly one Section 11 before Section 12. "
        "README.md was not changed."
    )

readme.write_text(updated, encoding="utf-8")
print("Success: Replaced Section 11 only.")
