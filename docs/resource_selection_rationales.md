# Resource selection rationales

These notes record why a resource is in the catalog, the situation in which it can be useful, and the limit of what its output can support. Presence in the catalog does not mean the resource should be used in every case.

## GATK

- **Identifier:** gatk
- **Class:** tool
- **Analytical function:** Variant-level quality control and filtering
- **Workflow stage(s):** 1;2
- **Evidence type:** Technical
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gatk.broadinstitute.org/

### Selection rationale

Representative toolkit for reproducible variant calling and post-calling quality filtering.

### Appropriate use

Use with validated laboratory pipeline and documented filters.

### Interpretation boundary

Not a substitute for case-level clinical interpretation.

### Inputs and outputs

Input: Variant call files and pipeline metrics

Output: Filtered and annotated VCFs; QC metrics

### Key limitations

Pipeline and parameter dependent; implementation-specific.

### Complementary resources

bcftools; VCFtools

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## bcftools

- **Identifier:** bcftools
- **Class:** tool
- **Analytical function:** Variant-level quality control and filtering
- **Workflow stage(s):** 1;2
- **Evidence type:** Technical
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://samtools.github.io/bcftools/

### Selection rationale

Included as a lightweight, widely used option for normalization, filtering, and inspection of variant calls.

### Appropriate use

Use when transparent VCF-level processing or normalization is required.

### Interpretation boundary

Does not establish variant validity or pathogenicity.

### Inputs and outputs

Input: VCF/BCF

Output: Processed VCF/BCF and QC summaries

### Key limitations

Command and threshold dependent; requires validated local workflow.

### Complementary resources

GATK; VCFtools

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## VCFtools

- **Identifier:** vcftools
- **Class:** tool
- **Analytical function:** Variant-level quality control and filtering
- **Workflow stage(s):** 1;2
- **Evidence type:** Technical
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/legacy use
- **Official resource:** https://vcftools.github.io/

### Selection rationale

Included for transparent VCF-level filtering and summary operations in post-calling workflows.

### Appropriate use

Use for inspection, filtering, and cohort-level VCF summaries as appropriate.

### Interpretation boundary

Does not replace validation of calls or clinical evidence appraisal.

### Inputs and outputs

Input: VCF

Output: Filtered VCFs and summary metrics

### Key limitations

Feature set and outputs depend on VCF quality and local parameters. Maintenance is legacy; bcftools covers many of the same VCF operations.

### Complementary resources

GATK; bcftools

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Ensembl

- **Identifier:** ensembl
- **Class:** database
- **Analytical function:** Genome and transcript annotation
- **Workflow stage(s):** 3
- **Evidence type:** Reference/annotation
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ensembl.org/

### Selection rationale

Included as a maintained reference ecosystem for genome, gene, transcript, and variant annotation.

### Appropriate use

Use when annotation requires explicit genome-build and transcript context.

### Interpretation boundary

Transcript annotations are not a clinical classification.

### Inputs and outputs

Input: Genomic coordinates; variants; genes

Output: Gene/transcript context and annotations

### Key limitations

Transcript choice and release changes can alter consequences.

### Complementary resources

RefSeq; GENCODE; MANE

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## RefSeq

- **Identifier:** refseq
- **Class:** database
- **Analytical function:** Genome and transcript annotation
- **Workflow stage(s):** 3
- **Evidence type:** Reference/annotation
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/

### Selection rationale

Included as a core curated reference-sequence source for transcript-aware interpretation.

### Appropriate use

Use when documenting transcript accessions and reference sequence context.

### Interpretation boundary

A transcript record alone does not determine disease relevance.

### Inputs and outputs

Input: Gene/transcript identifiers; sequence accessions

Output: Reference transcript and sequence records

### Key limitations

Transcript updates and alternative isoforms require explicit selection.

### Complementary resources

Ensembl; MANE; GENCODE

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## GENCODE

- **Identifier:** gencode
- **Class:** database
- **Analytical function:** Genome and transcript annotation
- **Workflow stage(s):** 3
- **Evidence type:** Reference/annotation
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.gencodegenes.org/

### Selection rationale

Included because comprehensive annotation supports transparent transcript and gene context.

### Appropriate use

Use when transcript-model provenance must be documented.

### Interpretation boundary

Does not determine clinical transcript preference by itself.

### Inputs and outputs

Input: Genome coordinates; gene/transcript identifiers

Output: Gene and transcript annotation sets

### Key limitations

Release-specific; transcript-model differences may affect consequence calls.

### Complementary resources

Ensembl; MANE; RefSeq

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## MANE

- **Identifier:** mane
- **Class:** reference
- **Analytical function:** Genome and transcript annotation
- **Workflow stage(s):** 3
- **Evidence type:** Reference/annotation
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/MANE/

### Selection rationale

Included to support consistent transcript selection across RefSeq and Ensembl for clinically relevant reporting.

### Appropriate use

Use when a MANE transcript is available and appropriate to the clinical context.

### Interpretation boundary

Does not eliminate the need to consider disease-specific transcript conventions.

### Inputs and outputs

Input: Gene identifiers; transcript accessions

Output: Matched MANE Select/Plus Clinical transcripts

### Key limitations

Coverage is not universal; updates occur over time.

### Complementary resources

RefSeq; Ensembl; GENCODE

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## gnomAD

- **Identifier:** gnomad
- **Class:** database
- **Analytical function:** Population-frequency assessment
- **Workflow stage(s):** 4
- **Evidence type:** Population
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gnomad.broadinstitute.org/

### Selection rationale

Included because large-scale population data can test compatibility of allele frequency with a suspected disease model.

### Appropriate use

Use for frequency filtering and ancestry-aware contextual assessment.

### Interpretation boundary

Rarity or absence does not establish pathogenicity.

### Inputs and outputs

Input: Variant coordinates or identifiers

Output: Allele frequencies, coverage, ancestry-stratified context

### Key limitations

Uneven ancestry representation, coverage differences, founder effects, and no phenotype linkage.

### Complementary resources

TOPMed; 1000 Genomes; Iranome

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## TOPMed

- **Identifier:** topmed
- **Class:** database
- **Analytical function:** Population-frequency assessment
- **Workflow stage(s):** 4
- **Evidence type:** Population
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://bravo.sph.umich.edu/

### Selection rationale

Included as a complementary large-scale frequency resource. The catalogued URL is the public Bravo browser of TOPMed allele frequencies.

### Appropriate use

Use when its cohort composition and release are relevant to the frequency question.

### Interpretation boundary

Frequency alone is not clinical evidence of pathogenicity.

### Inputs and outputs

Input: Variant coordinates or identifiers

Output: Allele frequencies and coverage context

### Key limitations

Population representation and dataset-specific processing must be considered.

### Complementary resources

gnomAD; 1000 Genomes; Iranome

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## 1000 Genomes

- **Identifier:** 1000-genomes
- **Class:** database
- **Analytical function:** Population-frequency assessment
- **Workflow stage(s):** 4
- **Evidence type:** Population
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/archival
- **Official resource:** https://www.internationalgenome.org/

### Selection rationale

Included as a foundational multi-population reference dataset for complementary frequency and ancestry context.

### Appropriate use

Use as complementary context rather than sole frequency evidence.

### Interpretation boundary

Does not establish pathogenicity or fully represent all populations.

### Inputs and outputs

Input: Variant coordinates or identifiers

Output: Allele frequencies and population context

### Key limitations

Limited sample sizes for rare-variant inference relative to newer datasets.

### Complementary resources

gnomAD; TOPMed; Iranome

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Iranome

- **Identifier:** iranome
- **Class:** database
- **Analytical function:** Population-frequency assessment
- **Workflow stage(s):** 4
- **Evidence type:** Population
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** https://www.iranome.com/

### Selection rationale

Included to provide population-relevant frequency context when patient ancestry is appropriately matched.

### Appropriate use

Use as complementary evidence for appropriately matched Iranian cases.

### Interpretation boundary

Should not be assumed to represent all Iranian or neighboring populations.

### Inputs and outputs

Input: Variant coordinates or identifiers

Output: Allele-frequency information from Iranian individuals

### Key limitations

Sampling, coverage, and representativeness limitations.

### Complementary resources

gnomAD; TOPMed; 1000 Genomes

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## HPO

- **Identifier:** hpo
- **Class:** ontology
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Workflow stage(s):** 5
- **Evidence type:** Phenotypic
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://hpo.jax.org/

### Selection rationale

Included because structured phenotype encoding supports reproducible phenotype–gene and phenotype–disease comparison.

### Appropriate use

Use when clinical findings can be captured with sufficiently specific and temporally appropriate terms.

### Interpretation boundary

Phenotype similarity does not independently establish gene–disease causality or variant pathogenicity.

### Inputs and outputs

Input: Clinical features encoded as HPO terms

Output: Ontology terms and phenotype similarity context

### Key limitations

Incomplete, nonspecific, or inaccurately captured phenotypes reduce performance.

### Complementary resources

Exomiser; LIRICAL; Phen2Gene

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Exomiser

- **Identifier:** exomiser
- **Class:** tool
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Workflow stage(s):** 5
- **Evidence type:** Phenotypic/computational
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://exomiser.readthedocs.io/en/latest/

### Selection rationale

Included as a representative phenotype-driven prioritization platform that integrates phenotype and variant context.

### Appropriate use

Use for candidate prioritization when structured phenotype and compatible variant data are available.

### Interpretation boundary

Ranking is not proof of causality or classification.

### Inputs and outputs

Input: HPO terms; variant data; pedigree where applicable

Output: Ranked genes/variants with explanatory scores

### Key limitations

Dependent on phenotype quality, knowledgebase coverage, inheritance assumptions, and model configuration.

### Complementary resources

HPO; LIRICAL; Phen2Gene

### Traceability

Release reviewed on 2026-10-10: 15.1.1. Check the current release again when the resource is used.

## LIRICAL

- **Identifier:** lirical
- **Class:** tool
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Workflow stage(s):** 5
- **Evidence type:** Phenotypic/computational
- **Genome build:** build independent;build dependent
- **Maintenance:** Active
- **Official resource:** https://lirical.readthedocs.io/

### Selection rationale

Included as a complementary phenotype-driven method emphasizing explicit likelihood-based reasoning.

### Appropriate use

Use when transparent phenotype-based diagnostic prioritization is desired.

### Interpretation boundary

Output does not independently prove causal variant status.

### Inputs and outputs

Input: HPO terms; genotype information when available

Output: Ranked diagnoses/genes with likelihood-based output

### Key limitations

Sensitive to phenotype completeness, disease annotations, and input assumptions.

### Complementary resources

HPO; Exomiser; Phen2Gene

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Phen2Gene

- **Identifier:** phen2gene
- **Class:** tool
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Workflow stage(s):** 5
- **Evidence type:** Phenotypic/computational
- **Genome build:** build independent
- **Maintenance:** Active/verify current status
- **Official resource:** https://phen2gene.wglab.org/

### Selection rationale

Included as a focused phenotype-to-gene prioritization option.

### Appropriate use

Use for rapid gene prioritization from structured phenotypes.

### Interpretation boundary

Does not provide variant classification.

### Inputs and outputs

Input: HPO terms

Output: Ranked candidate genes

### Key limitations

Limited by phenotype encoding and underlying gene–phenotype knowledge.

### Complementary resources

HPO; Exomiser; LIRICAL

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ClinGen

- **Identifier:** clingen
- **Class:** curation resource
- **Analytical function:** Gene–disease association assessment;Clinical evidence retrieval and curation
- **Workflow stage(s):** 6;9
- **Evidence type:** Clinical/curated
- **Genome build:** build independent;build dependent
- **Maintenance:** Active
- **Official resource:** https://clinicalgenome.org/

### Selection rationale

Included because ClinGen expert curation supports gene–disease validity assessment and evidence review when a current assertion exists.

### Appropriate use

Use for gene–disease validity and related curated evidence when current curation exists. Gene- and disease-specific classification specifications are the separate ClinGen specifications entry.

### Interpretation boundary

Coverage is incomplete. A validity or evidence assertion does not classify the variant under review and does not replace case-specific appraisal.

### Inputs and outputs

Input: Gene, disease, variant, evidence context

Output: Curated gene–disease validity assertions and supporting evidence summaries

### Key limitations

Curation status and coverage evolve. This entry does not contain the gene-specific ACMG/AMP specifications, which are catalogued separately.

### Complementary resources

OMIM; Orphanet; PanelApp; ClinVar; ClinGen specifications

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## OMIM

- **Identifier:** omim
- **Class:** database
- **Analytical function:** Gene–disease association assessment
- **Workflow stage(s):** 6
- **Evidence type:** Clinical/curated
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://www.omim.org/

### Selection rationale

Included as a widely used gene–phenotype knowledge source for evaluating clinical relevance.

### Appropriate use

Use to contextualize known gene–disease relationships and inheritance patterns.

### Interpretation boundary

Does not replace formal validity assessment or case-specific classification.

### Inputs and outputs

Input: Gene/disease identifiers

Output: Gene–phenotype and disease records

### Key limitations

Curation depth and update timing vary by entry.

### Complementary resources

ClinGen; Orphanet; PanelApp

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Orphanet

- **Identifier:** orphanet
- **Class:** database
- **Analytical function:** Gene–disease association assessment
- **Workflow stage(s):** 6
- **Evidence type:** Clinical/curated
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://www.orpha.net/

### Selection rationale

Included for rare-disease nomenclature and gene–disease context.

### Appropriate use

Use when rare-disease terminology and cross-referenced disease context are needed.

### Interpretation boundary

Does not independently establish causality in an individual case.

### Inputs and outputs

Input: Disease/gene identifiers

Output: Rare disease and gene association context

### Key limitations

Coverage, curation, and update timing vary.

### Complementary resources

ClinGen; OMIM; PanelApp

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PanelApp

- **Identifier:** panelapp
- **Class:** curation resource
- **Analytical function:** Gene–disease association assessment
- **Workflow stage(s):** 6
- **Evidence type:** Clinical/curated
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://panelapp.genomicsengland.co.uk/

### Selection rationale

Included because diagnostic panel curation can provide disease-specific gene relevance context.

### Appropriate use

Use as a complementary source when panel evidence and panel scope are relevant.

### Interpretation boundary

Panel inclusion is not synonymous with definitive causality or variant pathogenicity.

### Inputs and outputs

Input: Gene/disease/panel queries

Output: Panel membership and evidence level

### Key limitations

Panel content and evidence ratings change; jurisdiction-specific practices may differ.

### Complementary resources

ClinGen; OMIM; Orphanet

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## CADD

- **Identifier:** cadd
- **Class:** predictor
- **Analytical function:** Computational variant-effect prediction
- **Workflow stage(s):** 7
- **Evidence type:** Computational
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://cadd.gs.washington.edu/

### Selection rationale

Included as a representative broad variant-effect predictor.

### Appropriate use

Use as one supportive computational feature when applicable to the variant class.

### Interpretation boundary

Score alone is not clinical pathogenicity evidence.

### Inputs and outputs

Input: Variant coordinates and alleles

Output: Phred-scaled deleteriousness scores

### Key limitations

Model and training-data dependence; calibration and applicability vary by context.

### Complementary resources

REVEL; SIFT; PolyPhen-2; AlphaMissense

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## REVEL

- **Identifier:** revel
- **Class:** predictor
- **Analytical function:** Computational variant-effect prediction
- **Workflow stage(s):** 7
- **Evidence type:** Computational
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://sites.google.com/site/revelgenomics/

### Selection rationale

Included as a representative ensemble predictor for missense variants.

### Appropriate use

Use only for applicable missense variants and with gene/disease mechanism context.

### Interpretation boundary

Do not treat concordance with related predictors as independent evidence.

### Inputs and outputs

Input: Missense variants

Output: Ensemble prediction scores

### Key limitations

Training-data overlap, calibration, and gene/variant-specific performance limitations.

### Complementary resources

CADD; SIFT; PolyPhen-2; AlphaMissense

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## SIFT

- **Identifier:** sift
- **Class:** predictor
- **Analytical function:** Computational variant-effect prediction
- **Workflow stage(s):** 7
- **Evidence type:** Computational
- **Genome build:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://sift.bii.a-star.edu.sg/

### Selection rationale

Included as a commonly used conservation/function-based missense predictor.

### Appropriate use

Use as one supporting predictor for applicable missense variants.

### Interpretation boundary

Not a stand-alone clinical classification method.

### Inputs and outputs

Input: Protein change or variant input

Output: Predicted tolerated/deleterious output

### Key limitations

Limited scope; performance and dependence on shared features must be considered. The public website returned an error on a 2026-10-10 check.

### Complementary resources

REVEL; PolyPhen-2; CADD

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PolyPhen-2

- **Identifier:** polyphen-2
- **Class:** predictor
- **Analytical function:** Computational variant-effect prediction
- **Workflow stage(s):** 7
- **Evidence type:** Computational
- **Genome build:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://genetics.bwh.harvard.edu/pph2/

### Selection rationale

Included as a historical and commonly used missense-effect predictor.

### Appropriate use

Use as supportive context for applicable missense variants.

### Interpretation boundary

Not independent confirmation when used with overlapping predictors.

### Inputs and outputs

Input: Protein change or variant input

Output: Predicted impact categories and scores

### Key limitations

Variant- and gene-specific performance; limited clinical specificity.

### Complementary resources

REVEL; SIFT; CADD

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## AlphaMissense

- **Identifier:** alphamissense
- **Class:** predictor
- **Analytical function:** Computational variant-effect prediction
- **Workflow stage(s):** 7
- **Evidence type:** Computational
- **Genome build:** protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://alphamissense.hegelab.org/

### Selection rationale

Included as a modern missense-focused predictor that may add complementary computational context.

### Appropriate use

Use for applicable missense variants with explicit transcript/protein mapping.

### Interpretation boundary

Do not use as autonomous clinical classification evidence.

### Inputs and outputs

Input: Protein missense variants

Output: Prediction scores for amino-acid substitutions

### Key limitations

Model applicability, calibration, and biological/clinical context remain limiting.

### Complementary resources

REVEL; CADD; ClinGen

### Traceability

Release reviewed on 2026-10-10: Cheng et al. 2023. Check the current release again when the resource is used.

## SpliceAI

- **Identifier:** spliceai
- **Class:** predictor
- **Analytical function:** Splicing assessment
- **Workflow stage(s):** 8
- **Evidence type:** Computational/transcript-based
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://spliceailookup.broadinstitute.org/

### Selection rationale

Included as a representative splice-effect predictor for variants with plausible splicing consequences.

### Appropriate use

Use with explicit transcript selection and consideration of relevant splice mechanisms.

### Interpretation boundary

Prediction is not direct proof of aberrant splicing or clinical pathogenicity.

### Inputs and outputs

Input: Variant coordinates and alleles

Output: Splice alteration delta scores and positions

### Key limitations

Tissue, transcript, mechanism, and calibration dependence.

### Complementary resources

MaxEntScan; dbscSNV

### Complementary context

RNA evidence

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## MaxEntScan

- **Identifier:** maxentscan
- **Class:** predictor
- **Analytical function:** Splicing assessment
- **Workflow stage(s):** 8
- **Evidence type:** Computational/transcript-based
- **Genome build:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://pubmed.ncbi.nlm.nih.gov/15285897/

### Selection rationale

Included as a complementary sequence-based splicing assessment method.

### Appropriate use

Use for relevant canonical or near-canonical splice-site questions.

### Interpretation boundary

Does not demonstrate in vivo splicing outcome.

### Inputs and outputs

Input: Sequence/variant context

Output: Splice-site score changes

### Key limitations

Limited representation of tissue-specific and broader regulatory context.

### Complementary resources

SpliceAI; dbscSNV

### Complementary context

RNA evidence

### Traceability

Release reviewed on 2026-10-10: Yeo and Burge 2004. The release cited here is fixed.

## dbscSNV

- **Identifier:** dbscsnv
- **Class:** database
- **Analytical function:** Splicing assessment
- **Workflow stage(s):** 8
- **Evidence type:** Computational/transcript-based
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/legacy use
- **Official resource:** http://www.liulab.science/dbscsnv.html

### Selection rationale

Included as a supplementary source of precomputed splicing prediction context.

### Appropriate use

Use as complementary computational information for applicable SNVs.

### Interpretation boundary

Not direct experimental evidence of aberrant splicing.

### Inputs and outputs

Input: SNV coordinates

Output: Splicing-related prediction scores

### Key limitations

Scope is limited to consensus-region SNVs and to the underlying models. The scored set is the frozen v1.1 release. Distribution through dbNSFP does not make dbNSFP this resource.

### Complementary resources

SpliceAI; MaxEntScan

### Complementary context

RNA evidence

### Traceability

Release reviewed on 2026-10-10: v1.1. The release cited here is fixed.

## GTEx

- **Identifier:** gtex
- **Class:** database
- **Analytical function:** Regulatory and expression evidence
- **Workflow stage(s):** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gtexportal.org/

### Selection rationale

Included because tissue-specific expression context can inform biological plausibility and regulatory interpretation.

### Appropriate use

Use when relevant tissues and biological context are available.

### Interpretation boundary

Expression context does not independently establish variant pathogenicity.

### Inputs and outputs

Input: Gene/variant queries

Output: Expression and regulatory association context

### Key limitations

Donor composition, tissue availability, context dependence, and association limitations.

### Complementary resources

ENCODE; RegulomeDB; FANTOM5

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ENCODE

- **Identifier:** encode
- **Class:** database
- **Analytical function:** Regulatory and expression evidence
- **Workflow stage(s):** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.encodeproject.org/

### Selection rationale

Included for experimentally derived functional-genomic context around noncoding or regulatory variants.

### Appropriate use

Use when genomic coordinates overlap relevant regulatory annotations.

### Interpretation boundary

Annotation overlap does not prove disease mechanism or clinical impact.

### Inputs and outputs

Input: Genomic coordinates

Output: Regulatory and functional genomic tracks

### Key limitations

Cell-type and experimental-context specificity; incomplete coverage.

### Complementary resources

GTEx; RegulomeDB; FANTOM5

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## RegulomeDB

- **Identifier:** regulomedb
- **Class:** database
- **Analytical function:** Regulatory and expression evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Regulatory/functional
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://regulomedb.org/

### Selection rationale

Included as an integrative entry point for regulatory annotation.

### Appropriate use

Use for hypothesis generation regarding regulatory context.

### Interpretation boundary

Scores are not direct clinical pathogenicity evidence.

### Inputs and outputs

Input: Variant coordinates

Output: Regulatory evidence scores/annotations

### Key limitations

Evidence aggregation and tissue/context limitations.

### Complementary resources

ENCODE; GTEx; FANTOM5

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## FANTOM5

- **Identifier:** fantom5
- **Class:** database
- **Analytical function:** Regulatory and expression evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Regulatory/functional
- **Genome build:** build dependent
- **Maintenance:** Active/verify current status
- **Official resource:** https://fantom.gsc.riken.jp/5/

### Selection rationale

Included as a complementary functional-genomics resource for promoter/enhancer and expression context.

### Appropriate use

Use when relevant cell-type or regulatory annotation is needed.

### Interpretation boundary

Does not by itself establish variant effect or causality.

### Inputs and outputs

Input: Gene/genomic region queries

Output: Regulatory and expression annotations

### Key limitations

Coverage and context dependence; update status must be checked.

### Complementary resources

ENCODE; GTEx; RegulomeDB

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## UniProt

- **Identifier:** uniprot
- **Class:** database
- **Analytical function:** Structural and protein-function evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Structural/functional
- **Genome build:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.uniprot.org/

### Selection rationale

Included for curated protein-function and domain context relevant to variant interpretation.

### Appropriate use

Use when a variant can be mapped reliably to a protein sequence and functional feature.

### Interpretation boundary

Protein annotation alone does not determine clinical significance.

### Inputs and outputs

Input: Protein/gene identifiers

Output: Protein functional annotations

### Key limitations

Annotation completeness and isoform mapping can vary.

### Complementary resources

InterPro; PDB; AlphaFold DB

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PDB

- **Identifier:** pdb
- **Class:** database
- **Analytical function:** Structural and protein-function evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Structural/functional
- **Genome build:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.rcsb.org/

### Selection rationale

Included where experimentally resolved structure can inform residue-level or domain-level context.

### Appropriate use

Use when reliable structural coverage and mapping are available.

### Interpretation boundary

Structure presence does not prove functional or clinical impact.

### Inputs and outputs

Input: Protein identifiers/sequence mapping

Output: Structural models and experimental metadata

### Key limitations

Incomplete protein coverage; construct and experimental context limitations.

### Complementary resources

UniProt; AlphaFold DB; InterPro

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## AlphaFold DB

- **Identifier:** alphafold-db
- **Class:** database
- **Analytical function:** Structural and protein-function evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Structural/functional
- **Genome build:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://alphafold.ebi.ac.uk/

### Selection rationale

Included for structural hypothesis generation when experimental structures are unavailable.

### Appropriate use

Use with confidence measures and in conjunction with known protein biology.

### Interpretation boundary

Predicted structure is not direct functional or clinical evidence.

### Inputs and outputs

Input: Protein identifiers

Output: Predicted structures and confidence measures

### Key limitations

Prediction confidence, conformational dynamics, complexes, and mapping limitations.

### Complementary resources

PDB; UniProt; InterPro

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## InterPro

- **Identifier:** interpro
- **Class:** database
- **Analytical function:** Structural and protein-function evidence
- **Workflow stage(s):** 7;9
- **Evidence type:** Structural/functional
- **Genome build:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.ebi.ac.uk/interpro/

### Selection rationale

Included for standardized domain and family context during protein-level interpretation.

### Appropriate use

Use when variant localization relative to known domains is relevant.

### Interpretation boundary

Domain overlap alone does not establish pathogenicity.

### Inputs and outputs

Input: Protein sequences/identifiers

Output: Domain/family/function annotations

### Key limitations

Annotation coverage and functional specificity vary.

### Complementary resources

UniProt; PDB; AlphaFold DB

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## MSeqDR-QM

- **Identifier:** mseqdr-qm
- **Class:** tool
- **Analytical function:** Computational and AI-assisted prioritization
- **Workflow stage(s):** 5
- **Evidence type:** Computational/AI
- **Genome build:** build dependent
- **Maintenance:** Active/verify current status
- **Official resource:** https://mseqdr.org/

### Selection rationale

Included because MSeqDR provides mitochondrial-disease phenotype, gene, and variant context when that disease group is part of the clinical question.

### Appropriate use

Use for prioritization when the differential includes mitochondrial disease, and review the underlying sources returned by the query.

### Interpretation boundary

A mitochondrial-disease query result does not establish causality and is not a classification.

### Inputs and outputs

Input: Phenotype, gene, and variant queries related to mitochondrial disease

Output: Mitochondrial-disease knowledge retrieval and prioritization context

### Key limitations

Scope is mitochondrial disease rather than general Mendelian interpretation. Coverage, update timing, and dependence on upstream databases have to be reviewed.

### Complementary resources

HPO; ClinGen; ClinVar; Exomiser

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## GeMSTONE

- **Identifier:** gemstone
- **Class:** tool
- **Analytical function:** Computational and AI-assisted prioritization
- **Workflow stage(s):** 5;9
- **Evidence type:** Computational/AI
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** http://gemstone.yulab.org/

### Selection rationale

Included as a representative cloud workflow that can filter and prioritize germline variants from a VCF using a saved recipe. Component databases and predictors still have to be appraised on their own.

### Appropriate use

Use when the documented inputs, recipe, and version fit the case, including optional pedigree or control files.

### Interpretation boundary

A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

### Inputs and outputs

Input: Variant and phenotype data

Output: Prioritized candidate variants/genes

### Key limitations

Results depend on the selected filters, predictor thresholds, and embedded data releases. Concordance among embedded predictors is not independent evidence.

### Complementary resources

Exomiser; MSeqDR-QM; ClinGen

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ClinVar

- **Identifier:** clinvar
- **Class:** database
- **Analytical function:** Clinical evidence retrieval and curation;Reporting, documentation, and reinterpretation
- **Workflow stage(s):** 9;11
- **Evidence type:** Clinical/literature
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/clinvar/

### Selection rationale

Included to retrieve prior clinical assertions, review status, conflicts, and associated evidence context.

### Appropriate use

Use when reviewing previously reported clinical interpretations.

### Interpretation boundary

Entries are not definitive conclusions and must be appraised in context.

### Inputs and outputs

Input: Variant identifiers/coordinates

Output: Clinical significance submissions, review status, conflicts

### Key limitations

Conflicting submissions, variable review status, curation lag, and heterogeneous evidence.

### Complementary resources

ClinGen; PubMed; Mastermind; HGMD

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## HGMD

- **Identifier:** hgmd
- **Class:** database
- **Analytical function:** Clinical evidence retrieval and curation
- **Workflow stage(s):** 9
- **Evidence type:** Clinical/literature
- **Genome build:** build dependent
- **Maintenance:** Active/subscription
- **Official resource:** https://www.hgmd.cf.ac.uk/

### Selection rationale

Included as a literature-derived variant resource that may support evidence retrieval where access is available.

### Appropriate use

Use as a starting point for primary-literature verification.

### Interpretation boundary

A reported disease association is not a final classification.

### Inputs and outputs

Input: Gene/variant queries

Output: Reported disease-associated variant records

### Key limitations

Subscription access, curation criteria, and need for primary-source appraisal.

### Complementary resources

ClinVar; PubMed; Mastermind

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Mastermind

- **Identifier:** mastermind
- **Class:** database
- **Analytical function:** Clinical evidence retrieval and curation
- **Workflow stage(s):** 9
- **Evidence type:** Clinical/literature
- **Genome build:** build dependent
- **Maintenance:** Active/subscription tiered
- **Official resource:** https://mastermind.genomenon.com/

### Selection rationale

Included to support efficient retrieval of relevant published evidence.

### Appropriate use

Use to identify literature for direct appraisal.

### Interpretation boundary

Search results do not replace assessment of study quality or applicability.

### Inputs and outputs

Input: Gene/variant/disease queries

Output: Literature links and indexed evidence context

### Key limitations

Indexing scope, access tier, normalization, and literature quality vary.

### Complementary resources

PubMed; ClinVar; ClinGen

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PubMed

- **Identifier:** pubmed
- **Class:** database
- **Analytical function:** Clinical evidence retrieval and curation
- **Workflow stage(s):** 9
- **Evidence type:** Clinical/literature
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://pubmed.ncbi.nlm.nih.gov/

### Selection rationale

Included as a core bibliographic source for retrieving primary studies, guidelines, and resource documentation.

### Appropriate use

Use for direct appraisal of source evidence.

### Interpretation boundary

Search retrieval is not evidence appraisal or clinical classification.

### Inputs and outputs

Input: Keyword/gene/variant/disease queries

Output: Bibliographic records and links to literature

### Key limitations

Indexing, query design, publication bias, and access limitations.

### Complementary resources

Mastermind; ClinVar; ClinGen

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ACMG/AMP guidelines

- **Identifier:** acmg-amp-guidelines
- **Class:** guideline
- **Analytical function:** ACMG/AMP-based variant classification
- **Workflow stage(s):** 10
- **Evidence type:** Integrated clinical evidence
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4544753/

### Selection rationale

Included because formal clinical classification should follow the 2015 ACMG/AMP joint consensus recommendation. Applicable ClinGen specifications are catalogued as a separate entry.

### Appropriate use

Use after evidence selection and appraisal within defined gene–disease/inheritance context.

### Interpretation boundary

Criteria do not replace evidence quality review, clinical context, or expert judgment.

### Inputs and outputs

Input: Variant evidence and gene/disease context

Output: Pathogenicity classification framework

### Key limitations

General framework requires contextual and gene/disease-specific application.

### Complementary resources

ClinGen; VarSome

### Complementary context

laboratory SOPs

### Traceability

Release reviewed on 2026-10-10: Richards et al. 2015. The release cited here is fixed.

## ClinGen specifications

- **Identifier:** clingen-specifications
- **Class:** guideline
- **Analytical function:** ACMG/AMP-based variant classification
- **Workflow stage(s):** 10
- **Evidence type:** Integrated clinical evidence
- **Genome build:** build independent
- **Maintenance:** Active
- **Official resource:** https://clinicalgenome.org/working-groups/sequence-variant-interpretation/

### Selection rationale

Included because applicable expert specifications can improve consistency of ACMG/AMP criteria application.

### Appropriate use

Use when a current, applicable specification exists.

### Interpretation boundary

Absence of a specification does not justify overinterpretation.

### Inputs and outputs

Input: Variant and relevant gene/disease context

Output: Context-specific evidence specifications

### Key limitations

Coverage is incomplete; applicability and version must be checked.

### Complementary resources

ACMG/AMP guidelines; ClinGen

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## InterVar

- **Identifier:** intervar
- **Class:** tool
- **Analytical function:** ACMG/AMP-based variant classification
- **Workflow stage(s):** 10
- **Evidence type:** Integrated clinical evidence
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** https://github.com/WGLab/InterVar

### Selection rationale

Included as a representative tool that can organize ACMG/AMP evidence for review.

### Appropriate use

Use as a structured aid with current specifications and expert review.

### Interpretation boundary

Automated suggestions are not final clinical classifications.

### Inputs and outputs

Input: Variants and annotations

Output: Automated or semi-automated criteria suggestions

### Key limitations

Rule implementation, versioning, and context-specific criteria limitations.

### Complementary resources

VarSome; Franklin; ClinGen specifications

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## VarSome

- **Identifier:** varsome
- **Class:** tool
- **Analytical function:** ACMG/AMP-based variant classification
- **Workflow stage(s):** 10
- **Evidence type:** Integrated clinical evidence
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://varsome.com/

### Selection rationale

Included as a representative integrated annotation and classification-support platform.

### Appropriate use

Use with transparent review of evidence, criteria activation, and current specifications.

### Interpretation boundary

Platform output is not a substitute for expert clinical review.

### Inputs and outputs

Input: Variant identifiers/coordinates

Output: Aggregated annotations and classification support

### Key limitations

Underlying data updates, rule implementation, and source dependence.

### Complementary resources

InterVar; Franklin; ClinGen specifications

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Franklin

- **Identifier:** franklin
- **Class:** tool
- **Analytical function:** ACMG/AMP-based variant classification
- **Workflow stage(s):** 10
- **Evidence type:** Integrated clinical evidence
- **Genome build:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://franklin.genoox.com/

### Selection rationale

Included as a representative classification-support platform.

### Appropriate use

Use as a support tool alongside manual evidence appraisal and applicable specifications.

### Interpretation boundary

Do not accept automated classifications without contextual review.

### Inputs and outputs

Input: Variant identifiers/coordinates

Output: Classification-support outputs and evidence context

### Key limitations

Evidence aggregation, versioning, and implementation differences.

### Complementary resources

InterVar; VarSome; ClinGen specifications

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ACMG NGS technical standard

- **Identifier:** reporting-standards
- **Class:** guideline
- **Analytical function:** Reporting, documentation, and reinterpretation
- **Workflow stage(s):** 11
- **Evidence type:** Clinical/reporting
- **Genome build:** build independent
- **Maintenance:** Context dependent
- **Official resource:** https://www.nature.com/articles/s41436-021-01139-4

### Selection rationale

Included as the ACMG technical standard for constitutional gene-panel, exome, and genome sequencing, including what a clinical report should document. It is a different document from the 2015 ACMG/AMP classification framework.

### Appropriate use

Use when recording methods, coverage, variant description, classification, limitations, and secondary-finding policy for a constitutional exome or genome report.

### Interpretation boundary

The standard does not assign ACMG/AMP criteria to a variant and does not replace local or jurisdictional reporting rules.

### Inputs and outputs

Input: Case evidence, classification, and laboratory context

Output: Traceable report and reassessment documentation

### Key limitations

This entry cites the 2021 revision. Later ACMG documents, CAP or ISO requirements, and laboratory procedures may also apply.

### Complementary resources

ClinVar; ClinGen

### Complementary context

laboratory SOPs

### Traceability

Release reviewed on 2026-10-10: 2021 revision. Check the current release again when the resource is used.
