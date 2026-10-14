# Post-analytical workflow

The framework organizes post-analytical interpretation and prioritization of germline single-nucleotide variants and small insertions/deletions identified through clinical WES/WGS. The 11 stages are the operational structure for the 13 analytical functions. For each stage, the analytical question, the key limitations, and the representative resources are recorded.

Resources are representative as opposed to mandatory. A resource may be selected, revisited, omitted, or replaced according to the variant, the disease mechanism, the phenotype, the inheritance model, and the evidence already available. Evidence type is shown so that a technical metric, a population frequency, a computational score, and a curated assertion stay distinct.

Where resources may share datasets, annotations, publications, training data, or modelling assumptions, that dependence is noted. Agreement among those resources is not independent evidence.

## 1. Variant quality assessment and filtering

**Analytical question.** Is the variant call of sufficient quality for post-analytical interpretation?

**Key limitations.** Pipeline- and parameter-dependent.

### Resources

#### Technical

- **GATK** (`gatk`). Not a substitute for case-level clinical interpretation.
- **bcftools** (`bcftools`). Does not establish variant validity or pathogenicity.
- **VCFtools** (`vcftools`). Does not replace validation of calls or clinical evidence appraisal.

## 2. Variant quality assessment and filtering

**Analytical question.** Which variants remain after documented filtering?

**Key limitations.** Pipeline- and parameter-dependent. Filtering does not establish pathogenicity.

### Resources

#### Technical

- **GATK** (`gatk`). Not a substitute for case-level clinical interpretation.
- **bcftools** (`bcftools`). Does not establish variant validity or pathogenicity.
- **VCFtools** (`vcftools`). Does not replace validation of calls or clinical evidence appraisal.

## 3. Genome and transcript annotation

**Analytical question.** Which genome build, gene, transcript, and molecular consequence apply to this variant?

**Key limitations.** Transcript and genome-build discrepancies.

### Resources

#### Reference/annotation

- **Ensembl** (`ensembl`). Transcript annotations are not a clinical classification.
- **RefSeq** (`refseq`). A transcript record alone does not determine disease relevance.
- **GENCODE** (`gencode`). Does not determine clinical transcript preference by itself.
- **MANE** (`mane`). Does not eliminate the need to consider disease-specific transcript conventions.

### Shared sources

- **Transcript/annotation sources** (Ensembl, RefSeq, GENCODE, MANE). Different transcript sets may produce different consequences; matched sources may overlap. Record genome build, transcript accession, release, and selection rationale.

## 4. Population-frequency assessment

**Analytical question.** Is the population frequency compatible with the disease model and the ancestry of the individual?

**Key limitations.** Population representation and ancestry bias; rarity alone does not establish pathogenicity.

### Resources

#### Population

- **gnomAD** (`gnomad`). Rarity or absence does not establish pathogenicity.
- **TOPMed** (`topmed`). Frequency alone is not clinical evidence of pathogenicity.
- **1000 Genomes** (`1000-genomes`). Does not establish pathogenicity or fully represent all populations.
- **Iranome** (`iranome`). Should not be assumed to represent all Iranian or neighboring populations.

### Shared sources

- **Population datasets** (gnomAD, TOPMed, 1000 Genomes, Iranome). Cohorts, ancestry labels, and processing differ; some groups may overlap conceptually or not be interchangeable. Interpret frequency in the context of ancestry, coverage, and disease model.

## 5. Phenotype- and gene-based prioritization

**Analytical question.** Which genes or variants show phenotype–gene matching for the recorded phenotype and the mode of inheritance?

**Key limitations.** Incomplete, nonspecific, or inaccurately captured phenotypes. Phenotypic concordance does not establish causality.

### Resources

#### Phenotypic/computational

- **HPO** (`hpo`). HPO is phenotype encoding. Phenotype similarity does not independently establish gene–disease causality or variant pathogenicity.
- **Exomiser** (`exomiser`). Ranking is not proof of causality or classification.
- **LIRICAL** (`lirical`). Output does not independently prove causal variant status.
- **Phen2Gene** (`phen2gene`). Does not provide variant classification.

#### Computational/AI

- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

## 6. Gene–disease evaluation

**Analytical question.** What is the gene–disease validity and clinical relevance for this indication?

**Key limitations.** Evidence is evolving and may vary in strength and curation status.

### Resources

#### Clinical/curated

- **ClinGen** (`clingen`). Coverage is incomplete. A validity or evidence assertion does not classify the variant under review and does not replace case-specific appraisal.
- **OMIM** (`omim`). Does not replace formal validity assessment or case-specific classification.
- **Orphanet** (`orphanet`). Does not independently establish causality in an individual case.
- **PanelApp** (`panelapp`). Panel inclusion is not synonymous with definitive causality or variant pathogenicity.

#### Computational/AI

- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

## 7. Functional and computational assessment

**Analytical question.** Which computational predictions, regulatory and expression observations, or protein-structure and protein-function observations apply to this variant?

**Key limitations.** Model-dependent performance and applicability across variant types and populations. Tissue specificity and incomplete functional annotation. Structural prediction and functional uncertainty. Computational outputs are supportive rather than standalone determinants of clinical classification.

### Resources

#### Computational

- **CADD** (`cadd`). Score alone is not clinical pathogenicity evidence.
- **REVEL** (`revel`). Do not treat concordance with related predictors as independent evidence.
- **SIFT** (`sift`). Not a stand-alone clinical classification method.
- **PolyPhen-2** (`polyphen-2`). Not independent confirmation when used with overlapping predictors.
- **AlphaMissense** (`alphamissense`). Do not use as autonomous clinical classification evidence.

#### Computational/AI

- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

#### Regulatory/functional

- **GTEx** (`gtex`). Expression context does not independently establish variant pathogenicity.
- **ENCODE** (`encode`). Annotation overlap does not prove disease mechanism or clinical impact.
- **RegulomeDB** (`regulomedb`). Scores are not direct clinical pathogenicity evidence.
- **FANTOM5** (`fantom5`). Does not by itself establish variant effect or causality.

#### Structural/functional

- **UniProt** (`uniprot`). Protein annotation alone does not determine clinical significance.
- **PDB** (`pdb`). Structure presence does not prove functional or clinical impact.
- **AlphaFold DB** (`alphafold-db`). Predicted structure is not direct functional or clinical evidence.
- **InterPro** (`interpro`). Domain overlap alone does not establish pathogenicity.

### Shared sources

- **Computational predictors** (CADD, REVEL, SIFT, PolyPhen-2, AlphaMissense). Potential overlap in features, training data, annotations, or assumptions. Do not count agreement as automatically independent confirmation.
- **Regulatory resources** (GTEx, ENCODE, RegulomeDB, FANTOM5). Aggregated annotations can reuse shared assays, datasets, or inferred features. Treat outputs as contextual support, not independent proof.
- **Structural resources** (UniProt, PDB, AlphaFold DB, InterPro). Protein annotations and models may be based on related sequences, structures, or databases. Check direct source and mapping before inferring function.

## 8. Splicing assessment

**Analytical question.** Could this variant alter splicing of a clinically relevant transcript?

**Key limitations.** Tissue, transcript, and context dependence.

### Resources

#### Computational/transcript-based

- **SpliceAI** (`spliceai`). Prediction is not direct proof of aberrant splicing or clinical pathogenicity.
- **MaxEntScan** (`maxentscan`). Does not demonstrate in vivo splicing outcome.
- **dbscSNV** (`dbscsnv`). Not direct experimental evidence of aberrant splicing.

#### Computational/AI

- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

#### Regulatory/functional

- **GTEx** (`gtex`). Expression context does not independently establish variant pathogenicity.
- **ENCODE** (`encode`). Annotation overlap does not prove disease mechanism or clinical impact.
- **RegulomeDB** (`regulomedb`). Scores are not direct clinical pathogenicity evidence.
- **FANTOM5** (`fantom5`). Does not by itself establish variant effect or causality.

#### Structural/functional

- **UniProt** (`uniprot`). Protein annotation alone does not determine clinical significance.
- **PDB** (`pdb`). Structure presence does not prove functional or clinical impact.
- **AlphaFold DB** (`alphafold-db`). Predicted structure is not direct functional or clinical evidence.
- **InterPro** (`interpro`). Domain overlap alone does not establish pathogenicity.

### Shared sources

- **Splicing predictors** (SpliceAI, MaxEntScan, dbscSNV). Models differ in features, training era, and transcript context. Agreement is still computational. Concordant splice scores are not experimental evidence of aberrant splicing.
- **Regulatory resources** (GTEx, ENCODE, RegulomeDB, FANTOM5). Aggregated annotations can reuse shared assays, datasets, or inferred features. Treat outputs as contextual support, not independent proof.
- **Structural resources** (UniProt, PDB, AlphaFold DB, InterPro). Protein annotations and models may be based on related sequences, structures, or databases. Check direct source and mapping before inferring function.

## 9. Evidence integration

**Analytical question.** Which functional, clinical, and literature-based observations are relevant, and which of them share underlying datasets, annotations, or publications?

**Key limitations.** Conflicting, heterogeneous, or incompletely curated evidence. Agreement is not independent evidence when resources share datasets, annotations, publications, or modelling assumptions.

### Resources

#### Clinical/curated

- **ClinGen** (`clingen`). Coverage is incomplete. A validity or evidence assertion does not classify the variant under review and does not replace case-specific appraisal.

#### Computational/AI

- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

#### Regulatory/functional

- **GTEx** (`gtex`). Expression context does not independently establish variant pathogenicity.
- **ENCODE** (`encode`). Annotation overlap does not prove disease mechanism or clinical impact.
- **RegulomeDB** (`regulomedb`). Scores are not direct clinical pathogenicity evidence.
- **FANTOM5** (`fantom5`). Does not by itself establish variant effect or causality.

#### Structural/functional

- **UniProt** (`uniprot`). Protein annotation alone does not determine clinical significance.
- **PDB** (`pdb`). Structure presence does not prove functional or clinical impact.
- **AlphaFold DB** (`alphafold-db`). Predicted structure is not direct functional or clinical evidence.
- **InterPro** (`interpro`). Domain overlap alone does not establish pathogenicity.

#### Clinical/literature

- **ClinVar** (`clinvar`). Entries are not definitive conclusions and must be appraised in context.
- **HGMD** (`hgmd`). A reported disease association is not a final classification.
- **Mastermind** (`mastermind`). Search results do not replace assessment of study quality or applicability.
- **PubMed** (`pubmed`). Search retrieval is not evidence appraisal or clinical classification.

### Shared sources

- **Clinical assertion sources** (ClinVar, ClinGen, HGMD, Mastermind, PubMed). Assertions and summaries may trace to the same primary studies or submissions. Trace claims to primary evidence where possible.
- **Regulatory resources** (GTEx, ENCODE, RegulomeDB, FANTOM5). Aggregated annotations can reuse shared assays, datasets, or inferred features. Treat outputs as contextual support, not independent proof.
- **Structural resources** (UniProt, PDB, AlphaFold DB, InterPro). Protein annotations and models may be based on related sequences, structures, or databases. Check direct source and mapping before inferring function.

## 10. Clinical variant classification

**Analytical question.** Which ACMG/AMP criteria and ClinGen specifications apply after the evidence has been appraised?

**Key limitations.** Requires contextual assessment and expert review.

### Resources

#### Integrated clinical evidence

- **ClinGen specifications** (`clingen-specifications`). Absence of a specification does not justify overinterpretation.
- **InterVar** (`intervar`). Automated suggestions are not final clinical classifications.
- **VarSome** (`varsome`). Platform output is not a substitute for expert clinical review.
- **Franklin** (`franklin`). Do not accept automated classifications without contextual review.

### Shared sources

- **Classification-support tools** (InterVar, VarSome, Franklin). Implementations can share ACMG/AMP rules, population annotations, and submitted assertions. Compare the activated criteria with the underlying evidence rather than treating concordant classifications as confirmation.

## 11. Reporting and reinterpretation

**Analytical question.** What resource identities, versions, evidence, and limitations must be documented for clinical reporting and later reinterpretation?

**Key limitations.** Evidence and interpretations may change over time.

### Resources

#### Clinical/curated

- **ClinGen** (`clingen`). Coverage is incomplete. A validity or evidence assertion does not classify the variant under review and does not replace case-specific appraisal.

#### Clinical/literature

- **ClinVar** (`clinvar`). Entries are not definitive conclusions and must be appraised in context.

#### Clinical/reporting

- **ACMG NGS technical standard** (`reporting-standards`). The standard does not assign ACMG/AMP criteria to a variant and does not replace local or jurisdictional reporting rules.
- **ACMG reanalysis points to consider** (`reanalysis-guidance`). The statement does not assign ACMG/AMP criteria to a variant and does not replace laboratory procedure.

### Shared sources

- **Clinical assertion sources** (ClinVar, ClinGen). Assertions and summaries may trace to the same primary studies or submissions. Trace claims to primary evidence where possible.
