import os
from Bio import Entrez

Entrez.email = "your-valid-email@example.com"

SAMPLES = {
    "Streptomyces_coelicolor": "NC_003888.3",
    "Mycobacterium_tuberculosis": "NC_000962.3",
    "E_coli": "NC_000913.3",
    "Human_mtDNA": "NC_012920.1",
    "SARS_CoV_2": "NC_045512.2",
}

os.makedirs("data", exist_ok=True)

for name, accession in SAMPLES.items():
    output_path = f"data/{name}.fasta"

    if os.path.exists(output_path):
        print(f"Already downloaded: {output_path}")
        continue

    print(f"Downloading {name} ({accession})...")

    with Entrez.efetch(
        db="nuccore",
        id=accession,
        rettype="fasta",
        retmode="text"
    ) as handle:
        sequence_data = handle.read()

    with open(output_path, "w") as file:
        file.write(sequence_data)

    print(f"Saved: {output_path}")
