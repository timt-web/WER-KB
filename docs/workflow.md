# Post-analytical workflow

Once a germline single-nucleotide variant or small indel has been called from a clinical exome or genome, the catalog follows the work in 11 stages. For each stage we give the question, the limit of what that result can decide, and the resources that address the question.

Listing a resource under a stage means it is a reasonable option for that question. It does not mean every laboratory must run it. Evidence type is shown so that a quality metric, an allele count, a prediction score, and a curated assertion stay distinct.

If two resources in the same stage can share assays, training data, annotations, or papers, that overlap is noted there. Concordant results from those resources are not independent evidence.

## 1. Variant-level quality review

**Question.** Are the post-calling quality metrics and the call itself plausible for interpretation?

**Limit.** Technical outputs are pipeline and parameter dependent.

### Resources

#### Technical

- **GATK** (`gatk`). Not a substitute for case-level clinical interpretation.
- **bcftools** (`bcftools`). Does not establish variant validity or pathogenicity.
- **VCFtools** (`vcftools`). Does not replace validation of calls or clinical evidence appraisal.

## 2. Variant-level filtering

**Question.** Which variants remain after documented, case-appropriate filters and normalization?

**Limit.** Filtering does not establish pathogenicity.

### Resources

#### Technical

- **GATK** (`gatk`). Not a substitute for case-level clinical interpretation.
- **bcftools** (`bcftools`). Does not establish variant validity or pathogenicity.
- **VCFtools** (`vcftools`). Does not replace validation of calls or clinical evidence appraisal.

## 3. Genome and transcript annotation

**Question.** Which genome build, gene, transcript, and molecular consequence apply to this variant?

**Limit.** Transcript selection and release differences can alter interpretation.

### Resources

#### Reference/annotation

- **Ensembl** (`ensembl`). Transcript annotations are not a clinical classification.
- **RefSeq** (`refseq`). A transcript record alone does not determine disease relevance.
- **GENCODE** (`gencode`). Does not determine clinical transcript preference by itself.
- **MANE** (`mane`). Does not eliminate the need to consider disease-specific transcript conventions.

### Shared sources

- **Transcript/annotation sources** (Ensembl, RefSeq, GENCODE, MANE). Different transcript sets may produce different consequences; matched sources may overlap. Record genome build, transcript accession, release, and selection rationale.

## 4. Population-frequency assessment

**Question.** Is the observed allele frequency compatible with the proposed disease model and ancestry context?

**Limit.** Rarity alone does not establish pathogenicity.

### Resources

#### Population

- **gnomAD** (`gnomad`). Rarity or absence does not establish pathogenicity.
- **TOPMed** (`topmed`). Frequency alone is not clinical evidence of pathogenicity.
- **1000 Genomes** (`1000-genomes`). Does not establish pathogenicity or fully represent all populations.
- **Iranome** (`iranome`). Should not be assumed to represent all Iranian or neighboring populations.

### Shared sources

- **Population datasets** (gnomAD, TOPMed, 1000 Genomes, Iranome). Cohorts, ancestry labels, and processing differ; some groups may overlap conceptually or not be interchangeable. Interpret frequency in the context of ancestry, coverage, and disease model.

## 5. Phenotype- and gene-based prioritization

**Question.** Which genes or variants rank highest given the structured phenotype and the inheritance context?

**Limit.** Prioritization is not proof of causality.

### Resources

#### Phenotypic

- **HPO** (`hpo`). Phenotype similarity does not independently establish gene–disease causality or variant pathogenicity.

#### Phenotypic/computational

- **Exomiser** (`exomiser`). Ranking is not proof of causality or classification.
- **LIRICAL** (`lirical`). Output does not independently prove causal variant status.
- **Phen2Gene** (`phen2gene`). Does not provide variant classification.

#### Computational/AI

- **MSeqDR-QM** (`mseqdr-qm`). A mitochondrial-disease query result does not establish causality and is not a classification.
- **GeMSTONE** (`gemstone`). A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

## 6. Gene–disease association assessment

**Question.** How strong is the gene–disease relationship for this clinical question?

**Limit.** Curation coverage and strength vary.

### Resources

#### Clinical/curated

- **ClinGen** (`clingen`). Coverage is incomplete. A validity or evidence assertion does not classify the variant under review and does not replace case-specific appraisal.
- **OMIM** (`omim`). Does not replace formal validity assessment or case-specific classification.
- **Orphanet** (`orphanet`). Does not independently establish causality in an individual case.
- **PanelApp** (`panelapp`). Panel inclusion is not synonymous with definitive causality or variant pathogenicity.

## 7. Computational variant-effect assessment

**Question.** Which computational, regulatory, or protein-level observations apply to this variant class?

**Limit.** Predictions and annotations are supportive, not autonomous clinical evidence.

### Resources

#### Computational

- **CADD** (`cadd`). Score alone is not clinical pathogenicity evidence.
- **REVEL** (`revel`). Do not treat concordance with related predictors as independent evidence.
- **SIFT** (`sift`). Not a stand-alone clinical classification method.
- **PolyPhen-2** (`polyphen-2`). Not independent confirmation when used with overlapping predictors.
- **AlphaMissense** (`alphamissense`). Do not use as autonomous clinical classification evidence.

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

**Question.** Could this variant alter splicing of a clinically relevant transcript?

**Limit.** Predicted splice effects require contextual and, where possible, experimental corroboration.

### Resources

#### Computational/transcript-based

- **SpliceAI** (`spliceai`). Prediction is not direct proof of aberrant splicing or clinical pathogenicity.
- **MaxEntScan** (`maxentscan`). Does not demonstrate in vivo splicing outcome.
- **dbscSNV** (`dbscsnv`). Not direct experimental evidence of aberrant splicing.

#### Regulatory/functional

- **GTEx** (`gtex`). Expression context does not independently establish variant pathogenicity.
- **ENCODE** (`encode`). Annotation overlap does not prove disease mechanism or clinical impact.

### Shared sources

- **Splicing predictors** (SpliceAI, MaxEntScan, dbscSNV). Models differ in features, training era, and transcript context. Agreement is still computational. Concordant splice scores are not experimental evidence of aberrant splicing.
- **Regulatory resources** (GTEx, ENCODE). Aggregated annotations can reuse shared assays, datasets, or inferred features. Treat outputs as contextual support, not independent proof.

## 9. Functional, clinical, and literature evidence integration

**Question.** Which functional, clinical, and literature observations are relevant, and which of them repeat the same underlying data?

**Limit.** A collected set of observations does not establish pathogenicity, and sources that share underlying data do not provide independent confirmation.

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

## 10. ACMG/AMP-based classification

**Question.** Which ACMG/AMP criteria and ClinGen specifications apply after the evidence has been appraised?

**Limit.** Automated support tools do not replace contextual expert classification.

### Resources

#### Integrated clinical evidence

- **ACMG/AMP guidelines** (`acmg-amp-guidelines`). Criteria do not replace evidence quality review, clinical context, or expert judgment.
- **ClinGen specifications** (`clingen-specifications`). Absence of a specification does not justify overinterpretation.
- **InterVar** (`intervar`). Automated suggestions are not final clinical classifications.
- **VarSome** (`varsome`). Platform output is not a substitute for expert clinical review.
- **Franklin** (`franklin`). Do not accept automated classifications without contextual review.

### Shared sources

- **Classification-support tools** (InterVar, VarSome, Franklin). Implementations can share ACMG/AMP rules, population annotations, and submitted assertions. Compare the activated criteria with the underlying evidence rather than treating concordant classifications as confirmation.

## 11. Reporting, documentation, and reinterpretation

**Question.** What resources, versions, evidence, decisions, and limitations must the report preserve for later reinterpretation?

**Limit.** Evidence and interpretations may change over time.

### Resources

#### Clinical/literature

- **ClinVar** (`clinvar`). Entries are not definitive conclusions and must be appraised in context.

#### Clinical/reporting

- **ACMG NGS technical standard** (`reporting-standards`). The standard does not assign ACMG/AMP criteria to a variant and does not replace local or jurisdictional reporting rules.
