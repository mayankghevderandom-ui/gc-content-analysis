
# Comparative GC Content Analysis of Biological Sequences

## 1. Project Overview

This project analyses the guanine-cytosine (GC) content of five biological sequences using Python and bioinformatics libraries. It compares overall GC content and investigates regional GC-content variation using a sliding-window approach.

The project includes sequence retrieval, nucleotide composition analysis, data visualisation, and summary statistics.

## 2. Objectives

- Retrieve biological sequences in FASTA format.
- Calculate the counts of adenine (A), thymine (T), guanine (G), and cytosine (C).
- Calculate the overall GC content of each sequence.
- Compare GC content across five biological sequences.
- Analyse regional GC-content variation using sliding windows.
- Identify the highest- and lowest-GC windows in each sequence.
- Generate CSV tables and plots for further interpretation.

## 3. Biological Sequences

The project analyses the following reference sequences:

| Organism or sample | Accession number |
|---|---|
| Streptomyces coelicolor | NC_003888.3 |
| Mycobacterium tuberculosis H37Rv | NC_000962.3 |
| Escherichia coli K-12 MG1655 | NC_000913.3 |
| Human mitochondrial DNA | NC_012920.1 |
| SARS-CoV-2 | NC_045512.2 |

## 4. Tools and Libraries

- Python: scripting and numerical calculations.
- Biopython: reading FASTA files and handling biological sequences.
- Pandas: tabular data processing and CSV generation.
- Matplotlib: plotting and data visualisation.
- Ubuntu on WSL: command-line development environment.
- Conda: Python environment management.

## 5. Methodology

### 5.1 Sequence Retrieval

Reference sequences were downloaded from the NCBI Nucleotide database in FASTA format using Biopython's Entrez utilities.

### 5.2 Nucleotide Composition and Overall GC Content

The counts of A, T, G, and C were calculated for each sequence. Ambiguous or other characters were counted separately.

GC content was calculated as:

GC content (%) = [(G + C) / (A + T + G + C)] × 100

Only recognised A, T, G, and C bases were included in the denominator.

### 5.3 Sliding-Window Analysis

Regional GC content was calculated using a window size of 1,000 base pairs and a step size of 500 base pairs.

Each window was analysed independently. Consecutive windows overlap by 500 base pairs, and incomplete windows at the end of a sequence were excluded.

### 5.4 Visualisation

A bar chart was generated to compare overall GC content across the five sequences. Separate line plots were generated to show sliding-window GC content along each sequence.

### 5.5 Summary and Validation

The overall GC percentages were compared with the mean window-level GC percentages. The highest- and lowest-GC windows were also identified, and their positions were recorded.

## 6. Results

| Organism or sample | Sequence length (bp) | Overall GC (%) |
|---|---:|---:|
| Streptomyces coelicolor | 8,667,507 | 72.12 |
| Mycobacterium tuberculosis | 4,411,532 | 65.61 |
| Escherichia coli K-12 MG1655 | 4,641,652 | 50.79 |
| Human mitochondrial DNA | 16,569 | 44.36 |
| SARS-CoV-2 | 29,903 | 37.97 |

Streptomyces coelicolor showed the highest overall GC content, while SARS-CoV-2 showed the lowest overall GC content among the sequences analysed.

Regional GC-content variation was observed in all five sequences. Escherichia coli showed the widest range of sliding-window GC percentages in this analysis.

## 7. Output Files

The `results/` directory contains the generated tables and visualisations:

- `gc_content_results.csv`: overall nucleotide composition and GC content.
- `gc_content_comparison.png`: bar chart comparing overall GC content.
- `ecoli_sliding_window_gc.csv`: sliding-window measurements for E. coli.
- `ecoli_sliding_window_gc.png`: sliding-window GC-content plot for E. coli.
- `sliding_window/`: sliding-window CSV files for all five sequences.
- `sliding_window/plots/`: individual sliding-window plots for all five sequences.
- `gc_validation_comparison.csv`: comparison of whole-sequence and mean window GC content.
- `final_gc_summary.csv`: consolidated summary of GC statistics and extreme windows.

## 8. Limitations

GC content describes nucleotide composition but does not independently establish gene function, evolutionary relationships, or biological mechanisms.

Sliding-window results depend on the selected window size and step size. Overlapping windows are not statistically independent, and excluding incomplete final windows can contribute to small differences between whole-sequence and mean window GC content.

## 9. Conclusion

This project demonstrates a reproducible Python-based workflow for comparing GC content across biological sequences. Combining nucleotide composition calculations, sliding-window analysis, CSV outputs, and visualisations provides a foundation for further bioinformatics investigations.

## 10. Reproducibility

The analysis scripts and downloaded sequence files should be retained alongside the results. The Python environment can be recreated using the project's requirements file.

Activate the Conda environment before running the scripts:

conda activate gc-analysis

Run the analysis scripts from the project root directory.
