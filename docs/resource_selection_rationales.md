# Resource selection rationales

These notes record the analytical purpose of each representative resource, the context in which it may be used, and the key limitations of its output. Resources are representative as opposed to mandatory.

## GATK

- **Identifier:** gatk
- **Class:** tool
- **Analytical function:** Variant-Level Quality Control & Filtering
- **Workflow position:** 1;2
- **Evidence type:** Technical
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gatk.broadinstitute.org/

### Analytical purpose

Variant quality assessment and filtering

### Selection rationale

Representative toolkit for variant quality assessment and filtering.

### Appropriate use

Use with validated laboratory pipeline and documented filters.

### Interpretation boundary

Not a substitute for case-level clinical interpretation.

### Inputs and outputs

Input: Variant call files and pipeline metrics

Output: Filtered and annotated VCFs; QC metrics

### Key limitations

Pipeline- and parameter-dependent.

### Complementary resources

bcftools; VCFtools

### Supporting citation

DePristo MA, Banks E, Poplin R, Garimella KV, Maguire JR, Hartl C, et al. A framework for variation discovery and genotyping using next-generation DNA sequencing data. Nat Genet. 2011;43(5):491-498. doi:10.1038/ng.806.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## bcftools

- **Identifier:** bcftools
- **Class:** tool
- **Analytical function:** Variant-Level Quality Control & Filtering
- **Workflow position:** 1;2
- **Evidence type:** Technical
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://samtools.github.io/bcftools/

### Analytical purpose

Variant quality assessment and filtering

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

Pipeline- and parameter-dependent.

### Complementary resources

GATK; VCFtools

### Supporting citation

Danecek P, Bonfield JK, Liddle J, Marshall J, Ohan V, Pollard MO, et al. Twelve years of SAMtools and BCFtools. GigaScience. 2021;10(2):giab008. doi:10.1093/gigascience/giab008.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## VCFtools

- **Identifier:** vcftools
- **Class:** tool
- **Analytical function:** Variant-Level Quality Control & Filtering
- **Workflow position:** 1;2
- **Evidence type:** Technical
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/legacy use
- **Official resource:** https://vcftools.github.io/

### Analytical purpose

Variant quality assessment and filtering

### Selection rationale

Included for transparent VCF-level filtering and summary operations in variant quality assessment and filtering.

### Appropriate use

Use for inspection, filtering, and cohort-level VCF summaries as appropriate.

### Interpretation boundary

Does not replace validation of calls or clinical evidence appraisal.

### Inputs and outputs

Input: VCF

Output: Filtered VCFs and summary metrics

### Key limitations

Pipeline- and parameter-dependent. Maintenance is legacy; bcftools covers many of the same VCF operations.

### Complementary resources

GATK; bcftools

### Supporting citation

Danecek P, Auton A, Abecasis G, Albers CA, Banks E, DePristo MA, et al. The variant call format and VCFtools. Bioinformatics. 2011;27(15):2156-2158. doi:10.1093/bioinformatics/btr330.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Ensembl

- **Identifier:** ensembl
- **Class:** database
- **Analytical function:** Genome & Transcript Annotation
- **Workflow position:** 3
- **Evidence type:** Reference/annotation
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ensembl.org/

### Analytical purpose

Variant, gene, and transcript annotation

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

Transcript and genome-build discrepancies.

### Complementary resources

RefSeq; GENCODE; MANE

### Supporting citation

Cunningham F, Allen JE, Allen J, Alvarez-Jarreta J, Amode MR, Armean IM, et al. Ensembl 2024. Nucleic Acids Res. 2024;52(D1):D891-D899. doi:10.1093/nar/gkad1049.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## RefSeq

- **Identifier:** refseq
- **Class:** database
- **Analytical function:** Genome & Transcript Annotation
- **Workflow position:** 3
- **Evidence type:** Reference/annotation
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/

### Analytical purpose

Variant, gene, and transcript annotation

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

Transcript and genome-build discrepancies. Transcript updates and alternative isoforms require explicit selection.

### Complementary resources

Ensembl; MANE; GENCODE

### Supporting citation

O’Leary NA, Wright MW, Brister JR, Ciufo S, Haddad D, McVeigh R, et al. Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation. Nucleic Acids Res. 2016;44(D1):D733-D745. doi:10.1093/nar/gkv1189.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## GENCODE

- **Identifier:** gencode
- **Class:** database
- **Analytical function:** Genome & Transcript Annotation
- **Workflow position:** 3
- **Evidence type:** Reference/annotation
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.gencodegenes.org/

### Analytical purpose

Variant, gene, and transcript annotation

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

Transcript and genome-build discrepancies.

### Complementary resources

Ensembl; MANE; RefSeq

### Supporting citation

Frankish A, Diekhans M, Jungreis I, Lagarde J, Loveland JE, Mudge JM, et al. GENCODE 2021. Nucleic Acids Res. 2021;49(D1):D916-D923. doi:10.1093/nar/gkaa1087.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## MANE

- **Identifier:** mane
- **Class:** reference
- **Analytical function:** Genome & Transcript Annotation
- **Workflow position:** 3
- **Evidence type:** Reference/annotation
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/MANE/

### Analytical purpose

Variant, gene, and transcript annotation

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

Transcript and genome-build discrepancies. Coverage is not universal; updates occur over time.

### Complementary resources

RefSeq; Ensembl; GENCODE

### Supporting citation

Morales J, Pujar S, Loveland JE, Astashyn A, Bennett R, Berry A, et al. A joint NCBI and EMBL-EBI transcript set for clinical genomics and research. Nature. 2022;604(7905):310-315. doi:10.1038/s41586-022-04558-8.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## gnomAD

- **Identifier:** gnomad
- **Class:** database
- **Analytical function:** Population & Frequency
- **Workflow position:** 4
- **Evidence type:** Population
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gnomad.broadinstitute.org/

### Analytical purpose

Population frequency assessment and frequency-based filtering

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

Population representation and ancestry bias; rarity alone does not establish pathogenicity. Coverage differences, founder effects, and no phenotype linkage.

### Complementary resources

TOPMed; 1000 Genomes; Iranome

### Supporting citation

Gudmundsson S, Singer-Berk M, Watts NA, Phu W, Goodrich JK, Solomonson M, et al. Variant interpretation using population databases: lessons from gnomAD. Hum Mutat. 2022;43(8):1012-1030. doi:10.1002/humu.24309.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## TOPMed

- **Identifier:** topmed
- **Class:** database
- **Analytical function:** Population & Frequency
- **Workflow position:** 4
- **Evidence type:** Population
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://bravo.sph.umich.edu/

### Analytical purpose

Population frequency assessment and frequency-based filtering

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

Population representation and ancestry bias; rarity alone does not establish pathogenicity.

### Complementary resources

gnomAD; 1000 Genomes; Iranome

### Supporting citation

Taliun D, Harris DN, Kessler MD, Carlson J, Szpiech ZA, Torres R, et al. Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. Nature. 2021;590(7845):290-299. doi:10.1038/s41586-021-03205-y.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## 1000 Genomes

- **Identifier:** 1000-genomes
- **Class:** database
- **Analytical function:** Population & Frequency
- **Workflow position:** 4
- **Evidence type:** Population
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/archival
- **Official resource:** https://www.internationalgenome.org/

### Analytical purpose

Population frequency assessment and frequency-based filtering

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

Population representation and ancestry bias; rarity alone does not establish pathogenicity. Limited sample sizes for rare-variant inference relative to newer datasets.

### Complementary resources

gnomAD; TOPMed; Iranome

### Supporting citation

1000 Genomes Project Consortium. A global reference for human genetic variation. Nature. 2015;526(7571):68-74. doi:10.1038/nature15393.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Iranome

- **Identifier:** iranome
- **Class:** database
- **Analytical function:** Population & Frequency
- **Workflow position:** 4
- **Evidence type:** Population
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** https://www.iranome.com/

### Analytical purpose

Population frequency assessment and frequency-based filtering

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

Population representation and ancestry bias; rarity alone does not establish pathogenicity.

### Complementary resources

gnomAD; TOPMed; 1000 Genomes

### Supporting citation

Fattahi Z, Beheshtian M, Mohseni M, Poustchi H, Sellars E, Nezhadi SH, et al. Iranome: a catalog of genomic variations in the Iranian population. Hum Mutat. 2019;40(11):1968-1984. doi:10.1002/humu.23880.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## HPO

- **Identifier:** hpo
- **Class:** ontology
- **Analytical function:** Phenotype & Gene Prioritization
- **Workflow position:** 5
- **Evidence type:** Phenotypic/computational
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://hpo.jax.org/

### Analytical purpose

Phenotype–gene matching and candidate prioritization

### Selection rationale

Included because structured phenotype encoding supports reproducible phenotype–gene and phenotype–disease comparison.

### Appropriate use

Use when clinical findings can be captured with sufficiently specific and temporally appropriate terms.

### Interpretation boundary

HPO is phenotype encoding. Phenotype similarity does not independently establish gene–disease causality or variant pathogenicity.

### Inputs and outputs

Input: Clinical features encoded as HPO terms

Output: Ontology terms and phenotype similarity context

### Key limitations

Incomplete, nonspecific, or inaccurately captured phenotypes.

### Complementary resources

Exomiser; LIRICAL; Phen2Gene

### Supporting citation

Köhler S, Gargano M, Matentzoglu N, Carmody LC, Lewis-Smith D, Vasilevsky NA, et al. The Human Phenotype Ontology in 2021. Nucleic Acids Res. 2021;49(D1):D1207-D1217. doi:10.1093/nar/gkaa1043.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Exomiser

- **Identifier:** exomiser
- **Class:** tool
- **Analytical function:** Phenotype & Gene Prioritization
- **Workflow position:** 5
- **Evidence type:** Phenotypic/computational
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://exomiser.readthedocs.io/en/latest/

### Analytical purpose

Phenotype–gene matching and candidate prioritization

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

Incomplete, nonspecific, or inaccurately captured phenotypes. Dependent on phenotype quality, knowledgebase coverage, inheritance assumptions, and model configuration.

### Complementary resources

HPO; LIRICAL; Phen2Gene

### Supporting citation

Smedley D, Jacobsen JOB, Jäger M, Köhler S, Holtgrewe M, Schubach M, et al. Next-generation diagnostics and disease-gene discovery with the Exomiser. Nat Protoc. 2015;10(12):2004-2015. doi:10.1038/nprot.2015.124.

### Traceability

Release reviewed on 2026-10-10: 15.1.1. Check the current release again when the resource is used.

## LIRICAL

- **Identifier:** lirical
- **Class:** tool
- **Analytical function:** Phenotype & Gene Prioritization
- **Workflow position:** 5
- **Evidence type:** Phenotypic/computational
- **Genome-build and transcript compatibility:** build independent;build dependent
- **Maintenance:** Active
- **Official resource:** https://lirical.readthedocs.io/

### Analytical purpose

Phenotype–gene matching and candidate prioritization

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

Incomplete, nonspecific, or inaccurately captured phenotypes. Sensitive to phenotype completeness, disease annotations, and input assumptions.

### Complementary resources

HPO; Exomiser; Phen2Gene

### Supporting citation

Robinson PN, Ravanmehr V, Jacobsen JOB, Danis D, Zhang H, Carmody LC, et al. Interpretable clinical genomics with a likelihood ratio paradigm. Am J Hum Genet. 2020;107(3):403-417. doi:10.1016/j.ajhg.2020.06.021.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Phen2Gene

- **Identifier:** phen2gene
- **Class:** tool
- **Analytical function:** Phenotype & Gene Prioritization
- **Workflow position:** 5
- **Evidence type:** Phenotypic/computational
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active/verify current status
- **Official resource:** https://phen2gene.wglab.org/

### Analytical purpose

Phenotype–gene matching and candidate prioritization

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

Incomplete, nonspecific, or inaccurately captured phenotypes. Limited by phenotype encoding and underlying gene–phenotype knowledge.

### Complementary resources

HPO; Exomiser; LIRICAL

### Supporting citation

Zhao M, Havrilla JM, Fang L, Chen Y, Peng J, Liu C, et al. Phen2Gene: rapid phenotype-driven gene prioritization for rare diseases. NAR Genom Bioinform. 2020;2(2):lqaa032. doi:10.1093/nargab/lqaa032.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ClinGen

- **Identifier:** clingen
- **Class:** curation resource
- **Analytical function:** Gene–Disease Association;Clinical Evidence & Curation;Reporting & Reinterpretation
- **Workflow position:** 6;9;11
- **Evidence type:** Clinical/curated
- **Genome-build and transcript compatibility:** build independent;build dependent
- **Maintenance:** Active
- **Official resource:** https://clinicalgenome.org/

### Analytical purpose

Assessment of gene–disease validity and clinical relevance; Retrieval and assessment of clinical and literature-based evidence; Clinical reporting, documentation, and reassessment

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

Evidence is evolving and may vary in strength and curation status. Conflicting, heterogeneous, or incompletely curated evidence. Evidence and interpretations may change over time. This entry does not contain the gene-specific ACMG/AMP specifications, which are catalogued separately.

### Complementary resources

OMIM; Orphanet; PanelApp; ClinVar; ClinGen specifications

### Supporting citation

Rehm HL, Berg JS, Brooks LD, Bustamante CD, Evans JP, Landrum MJ, et al. ClinGen—the Clinical Genome Resource. N Engl J Med. 2015;372(23):2235-2242. doi:10.1056/NEJMsr1406261.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## OMIM

- **Identifier:** omim
- **Class:** database
- **Analytical function:** Gene–Disease Association
- **Workflow position:** 6
- **Evidence type:** Clinical/curated
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://www.omim.org/

### Analytical purpose

Assessment of gene–disease validity and clinical relevance

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

Evidence is evolving and may vary in strength and curation status. Curation depth and update timing vary by entry.

### Complementary resources

ClinGen; Orphanet; PanelApp

### Supporting citation

Hamosh A, Scott AF, Amberger JS, Bocchini CA, McKusick VA. Online Mendelian Inheritance in Man (OMIM), a knowledgebase of human genes and genetic disorders. Nucleic Acids Res. 2005;33(Database issue):D514-D517. doi:10.1093/nar/gki033.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Orphanet

- **Identifier:** orphanet
- **Class:** database
- **Analytical function:** Gene–Disease Association
- **Workflow position:** 6
- **Evidence type:** Clinical/curated
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://www.orpha.net/

### Analytical purpose

Assessment of gene–disease validity and clinical relevance

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

Evidence is evolving and may vary in strength and curation status.

### Complementary resources

ClinGen; OMIM; PanelApp

### Supporting citation

Rath A, Olry A, Dhombres F, Brandt MM, Urbero B, Ayme S. Representation of rare diseases in health information systems: the Orphanet approach to serve a wide range of end users. Hum Mutat. 2012;33(5):803-808. doi:10.1002/humu.22078.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PanelApp

- **Identifier:** panelapp
- **Class:** curation resource
- **Analytical function:** Gene–Disease Association
- **Workflow position:** 6
- **Evidence type:** Clinical/curated
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://panelapp.genomicsengland.co.uk/

### Analytical purpose

Assessment of gene–disease validity and clinical relevance

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

Evidence is evolving and may vary in strength and curation status. Panel content and evidence ratings change; jurisdiction-specific practices may differ.

### Complementary resources

ClinGen; OMIM; Orphanet

### Supporting citation

Martin AR, Williams E, Foulger RE, Leigh S, Daugherty LC, Niblock O, et al. PanelApp crowdsources expert knowledge to establish consensus diagnostic gene panels. Nat Genet. 2019;51(11):1560-1565. doi:10.1038/s41588-019-0528-2.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## CADD

- **Identifier:** cadd
- **Class:** predictor
- **Analytical function:** Computational Variant-Effect Prediction
- **Workflow position:** 7
- **Evidence type:** Computational
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://cadd.gs.washington.edu/

### Analytical purpose

Prediction of potential functional effects

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

Model-dependent performance and applicability across variant types and populations.

### Complementary resources

REVEL; SIFT; PolyPhen-2; AlphaMissense

### Supporting citation

Rentzsch P, Witten D, Cooper GM, Shendure J, Kircher M. CADD: predicting the deleteriousness of variants throughout the human genome. Nucleic Acids Res. 2019;47(D1):D886-D894. doi:10.1093/nar/gky1016.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## REVEL

- **Identifier:** revel
- **Class:** predictor
- **Analytical function:** Computational Variant-Effect Prediction
- **Workflow position:** 7
- **Evidence type:** Computational
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://sites.google.com/site/revelgenomics/

### Analytical purpose

Prediction of potential functional effects

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

Model-dependent performance and applicability across variant types and populations. Training-data overlap, calibration, and gene- and variant-specific performance limitations.

### Complementary resources

CADD; SIFT; PolyPhen-2; AlphaMissense

### Supporting citation

Ioannidis NM, Rothstein JH, Pejaver V, Middha S, McDonnell SK, Baheti S, et al. REVEL: an ensemble method for predicting the pathogenicity of rare missense variants. Am J Hum Genet. 2016;99(4):877-885. doi:10.1016/j.ajhg.2016.08.016.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## SIFT

- **Identifier:** sift
- **Class:** predictor
- **Analytical function:** Computational Variant-Effect Prediction
- **Workflow position:** 7
- **Evidence type:** Computational
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://sift.bii.a-star.edu.sg/

### Analytical purpose

Prediction of potential functional effects

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

Model-dependent performance and applicability across variant types and populations. The public website returned an error on a 2026-10-10 check.

### Complementary resources

REVEL; PolyPhen-2; CADD

### Supporting citation

Ng PC, Henikoff S. SIFT: predicting amino acid changes that affect protein function. Nucleic Acids Res. 2003;31(13):3812-3814. doi:10.1093/nar/gkg509.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PolyPhen-2

- **Identifier:** polyphen-2
- **Class:** predictor
- **Analytical function:** Computational Variant-Effect Prediction
- **Workflow position:** 7
- **Evidence type:** Computational
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://genetics.bwh.harvard.edu/pph2/

### Analytical purpose

Prediction of potential functional effects

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

Model-dependent performance and applicability across variant types and populations. Limited clinical specificity.

### Complementary resources

REVEL; SIFT; CADD

### Supporting citation

Adzhubei IA, Schmidt S, Peshkin L, Ramensky VE, Gerasimova A, Bork P, et al. A method and server for predicting damaging missense mutations. Nat Methods. 2010;7(4):248-249. doi:10.1038/nmeth0410-248.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## AlphaMissense

- **Identifier:** alphamissense
- **Class:** predictor
- **Analytical function:** Computational Variant-Effect Prediction
- **Workflow position:** 7
- **Evidence type:** Computational
- **Genome-build and transcript compatibility:** protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://alphamissense.hegelab.org/

### Analytical purpose

Prediction of potential functional effects

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

Model-dependent performance and applicability across variant types and populations.

### Complementary resources

REVEL; CADD; ClinGen

### Supporting citation

Cheng J, Novati G, Pan J, Bycroft C, Žemgulytė A, Applebaum T, et al. Accurate proteome-wide missense variant effect prediction with AlphaMissense. Science. 2023;382(6673):eadg7492. doi:10.1126/science.adg7492.

### Traceability

Release reviewed on 2026-10-10: Cheng et al. 2023. Check the current release again when the resource is used.

## SpliceAI

- **Identifier:** spliceai
- **Class:** predictor
- **Analytical function:** Splicing Assessment
- **Workflow position:** 8
- **Evidence type:** Computational/transcript-based
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://spliceailookup.broadinstitute.org/

### Analytical purpose

Assessment of potential splicing effects

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

Tissue, transcript, and context dependence.

### Complementary resources

MaxEntScan; dbscSNV

### Complementary context

RNA evidence

### Supporting citation

Jaganathan K, Kyriazopoulou Panagiotopoulou S, McRae JF, Darbandi SF, Knowles D, Li YI, et al. Predicting splicing from primary sequence with deep learning. Cell. 2019;176(3):535-548.e24. doi:10.1016/j.cell.2018.12.015.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## MaxEntScan

- **Identifier:** maxentscan
- **Class:** predictor
- **Analytical function:** Splicing Assessment
- **Workflow position:** 8
- **Evidence type:** Computational/transcript-based
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/legacy use
- **Official resource:** https://pubmed.ncbi.nlm.nih.gov/15285897/

### Analytical purpose

Assessment of potential splicing effects

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

Tissue, transcript, and context dependence.

### Complementary resources

SpliceAI; dbscSNV

### Complementary context

RNA evidence

### Supporting citation

Yeo G, Burge CB. Maximum entropy modeling of short sequence motifs with applications to RNA splicing signals. J Comput Biol. 2004;11(2-3):377-394. doi:10.1089/1066527041410418.

### Traceability

Release reviewed on 2026-10-10: Yeo and Burge 2004. The release cited here is fixed.

## dbscSNV

- **Identifier:** dbscsnv
- **Class:** database
- **Analytical function:** Splicing Assessment
- **Workflow position:** 8
- **Evidence type:** Computational/transcript-based
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/legacy use
- **Official resource:** http://www.liulab.science/dbscsnv.html

### Analytical purpose

Assessment of potential splicing effects

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

Tissue, transcript, and context dependence. The scored set is the frozen v1.1 release and is limited to consensus-region SNVs. Distribution through dbNSFP does not make dbNSFP this resource.

### Complementary resources

SpliceAI; MaxEntScan

### Complementary context

RNA evidence

### Supporting citation

Jian X, Boerwinkle E, Liu X. In silico prediction of splice-altering single nucleotide variants in the human genome. Nucleic Acids Res. 2014;42(22):13534-13544. doi:10.1093/nar/gku1206.

### Traceability

Release reviewed on 2026-10-10: v1.1. The release cited here is fixed.

## GTEx

- **Identifier:** gtex
- **Class:** database
- **Analytical function:** Regulatory & Expression
- **Workflow position:** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://gtexportal.org/

### Analytical purpose

Assessment of regulatory and expression-related evidence

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

Tissue specificity and incomplete functional annotation. Donor composition, tissue availability, and association limitations.

### Complementary resources

ENCODE; RegulomeDB; FANTOM5

### Supporting citation

GTEx Consortium. The GTEx Consortium atlas of genetic regulatory effects across human tissues. Science. 2020;369(6509):1318-1330. doi:10.1126/science.aaz1776.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ENCODE

- **Identifier:** encode
- **Class:** database
- **Analytical function:** Regulatory & Expression
- **Workflow position:** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.encodeproject.org/

### Analytical purpose

Assessment of regulatory and expression-related evidence

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

Tissue specificity and incomplete functional annotation. Cell-type and experimental-context specificity; incomplete coverage.

### Complementary resources

GTEx; RegulomeDB; FANTOM5

### Supporting citation

ENCODE Project Consortium. An integrated encyclopedia of DNA elements in the human genome. Nature. 2012;489(7414):57-74. doi:10.1038/nature11247.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## RegulomeDB

- **Identifier:** regulomedb
- **Class:** database
- **Analytical function:** Regulatory & Expression
- **Workflow position:** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://regulomedb.org/

### Analytical purpose

Assessment of regulatory and expression-related evidence

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

Tissue specificity and incomplete functional annotation.

### Complementary resources

ENCODE; GTEx; FANTOM5

### Supporting citation

Boyle AP, Hong EL, Hariharan M, Cheng Y, Schaub MA, Kasowski M, et al. Annotation of functional variation in personal genomes using RegulomeDB. Genome Res. 2012;22(9):1790-1797. doi:10.1101/gr.137323.112.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## FANTOM5

- **Identifier:** fantom5
- **Class:** database
- **Analytical function:** Regulatory & Expression
- **Workflow position:** 7;8;9
- **Evidence type:** Regulatory/functional
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/verify current status
- **Official resource:** https://fantom.gsc.riken.jp/5/

### Analytical purpose

Assessment of regulatory and expression-related evidence

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

Tissue specificity and incomplete functional annotation. Update status must be checked.

### Complementary resources

ENCODE; GTEx; RegulomeDB

### Supporting citation

Forrest ARR, Kawaji H, Rehli M, Baillie JK, de Hoon MJL, Haberle V, et al. A promoter-level mammalian expression atlas. Nature. 2014;507(7493):462-470. doi:10.1038/nature13182.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## UniProt

- **Identifier:** uniprot
- **Class:** database
- **Analytical function:** Structural & Protein Function
- **Workflow position:** 7;8;9
- **Evidence type:** Structural/functional
- **Genome-build and transcript compatibility:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.uniprot.org/

### Analytical purpose

Assessment of protein structure and function

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

Structural prediction and functional uncertainty. Annotation completeness and isoform mapping can vary.

### Complementary resources

InterPro; PDB; AlphaFold DB

### Supporting citation

UniProt Consortium. UniProt: the Universal Protein Knowledgebase in 2023. Nucleic Acids Res. 2023;51(D1):D523-D531. doi:10.1093/nar/gkac1052.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PDB

- **Identifier:** pdb
- **Class:** database
- **Analytical function:** Structural & Protein Function
- **Workflow position:** 7;8;9
- **Evidence type:** Structural/functional
- **Genome-build and transcript compatibility:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.rcsb.org/

### Analytical purpose

Assessment of protein structure and function

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

Structural prediction and functional uncertainty. Incomplete protein coverage; construct and experimental context limitations.

### Complementary resources

UniProt; AlphaFold DB; InterPro

### Supporting citation

wwPDB Consortium. Protein Data Bank: the single global archive for 3D macromolecular structure data. Nucleic Acids Res. 2019;47(D1):D520-D528. doi:10.1093/nar/gky949.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## AlphaFold DB

- **Identifier:** alphafold-db
- **Class:** database
- **Analytical function:** Structural & Protein Function
- **Workflow position:** 7;8;9
- **Evidence type:** Structural/functional
- **Genome-build and transcript compatibility:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://alphafold.ebi.ac.uk/

### Analytical purpose

Assessment of protein structure and function

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

Structural prediction and functional uncertainty. Prediction confidence, conformational dynamics, complexes, and mapping limitations.

### Complementary resources

PDB; UniProt; InterPro

### Supporting citation

Varadi M, Anyango S, Deshpande M, Nair S, Natassia C, Yordanova G, et al. AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. Nucleic Acids Res. 2022;50(D1):D439-D444. doi:10.1093/nar/gkab1061.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## InterPro

- **Identifier:** interpro
- **Class:** database
- **Analytical function:** Structural & Protein Function
- **Workflow position:** 7;8;9
- **Evidence type:** Structural/functional
- **Genome-build and transcript compatibility:** build independent;protein or transcript mapping
- **Maintenance:** Active
- **Official resource:** https://www.ebi.ac.uk/interpro/

### Analytical purpose

Assessment of protein structure and function

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

Structural prediction and functional uncertainty. Annotation coverage and functional specificity vary.

### Complementary resources

UniProt; PDB; AlphaFold DB

### Supporting citation

Paysan-Lafosse T, Blum M, Chuguransky S, Grego T, Pinto BL, Salazar GA, et al. InterPro in 2022. Nucleic Acids Res. 2023;51(D1):D418-D427. doi:10.1093/nar/gkac993.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## GeMSTONE

- **Identifier:** gemstone
- **Class:** tool
- **Analytical function:** Computational & AI
- **Workflow position:** 5;6;7;8;9
- **Evidence type:** Computational/AI
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** http://gemstone.yulab.org/

### Analytical purpose

Computational support for variant and gene prioritization

### Selection rationale

Included as a representative cloud workflow that can filter and prioritize germline variants from a VCF using a saved recipe. Use across stages 5–9 is context dependent. Component databases and predictors still have to be appraised on their own.

### Appropriate use

Use when the documented inputs, recipe, and version fit the case, including optional pedigree or control files.

### Interpretation boundary

A prioritized list does not establish gene–disease validity, a splice effect, or a clinical classification.

### Inputs and outputs

Input: Variant and phenotype data

Output: Prioritized candidate variants/genes

### Key limitations

Bias, interpretability, model dependence, and variable validation. Results depend on the selected filters, predictor thresholds, and embedded data releases. Concordance among embedded predictors is not independent evidence.

### Complementary resources

Exomiser; ClinGen

### Supporting citation

Chen S, Francioli LC, Goodrich JK, Collins RL, Kanai M, Wang Q, et al. GeMSTONE: orchestrated prioritization of human germline mutations in the cloud. Nucleic Acids Res. 2017;45(W1):W207-W214. doi:10.1093/nar/gkx398.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ClinVar

- **Identifier:** clinvar
- **Class:** database
- **Analytical function:** Clinical Evidence & Curation;Reporting & Reinterpretation
- **Workflow position:** 9;11
- **Evidence type:** Clinical/literature
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://www.ncbi.nlm.nih.gov/clinvar/

### Analytical purpose

Retrieval and assessment of clinical and literature-based evidence; Clinical reporting, documentation, and reassessment

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

Conflicting, heterogeneous, or incompletely curated evidence. Evidence and interpretations may change over time.

### Complementary resources

ClinGen; PubMed; Mastermind; HGMD

### Supporting citation

Landrum MJ, Lee JM, Benson M, Brown G, Chao C, Chitipiralla S, et al. ClinVar: improving access to variant interpretations and supporting evidence. Nucleic Acids Res. 2018;46(D1):D1062-D1067. doi:10.1093/nar/gkx1153.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## HGMD

- **Identifier:** hgmd
- **Class:** database
- **Analytical function:** Clinical Evidence & Curation
- **Workflow position:** 9
- **Evidence type:** Clinical/literature
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/subscription
- **Official resource:** https://www.hgmd.cf.ac.uk/

### Analytical purpose

Retrieval and assessment of clinical and literature-based evidence

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

Conflicting, heterogeneous, or incompletely curated evidence. Subscription access, curation criteria, and need for primary-source appraisal.

### Complementary resources

ClinVar; PubMed; Mastermind

### Supporting citation

Stenson PD, Mort M, Ball EV, Chapman M, Evans K, Azevedo L, et al. The Human Gene Mutation Database (HGMD): optimizing its use in a clinical diagnostic or research setting. Hum Genet. 2020;139(10):1197-1207. doi:10.1007/s00439-020-02199-3.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Mastermind

- **Identifier:** mastermind
- **Class:** database
- **Analytical function:** Clinical Evidence & Curation
- **Workflow position:** 9
- **Evidence type:** Clinical/literature
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/subscription tiered
- **Official resource:** https://mastermind.genomenon.com/

### Analytical purpose

Retrieval and assessment of clinical and literature-based evidence

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

Conflicting, heterogeneous, or incompletely curated evidence. Indexing scope, access tier, normalization, and literature quality vary.

### Complementary resources

PubMed; ClinVar; ClinGen

### Supporting citation

Chunn LM, Nefcy DC, Scouten RW, Tarpey RP, Chauhan G, Lim MS, et al. Mastermind: a comprehensive genomic association search engine for empirical evidence curation and genetic variant interpretation. Front Genet. 2020;11:577152. doi:10.3389/fgene.2020.577152.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## PubMed

- **Identifier:** pubmed
- **Class:** database
- **Analytical function:** Clinical Evidence & Curation
- **Workflow position:** 9
- **Evidence type:** Clinical/literature
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://pubmed.ncbi.nlm.nih.gov/

### Analytical purpose

Retrieval and assessment of clinical and literature-based evidence

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

Conflicting, heterogeneous, or incompletely curated evidence. Indexing, query design, publication bias, and access limitations.

### Complementary resources

Mastermind; ClinVar; ClinGen

### Supporting citation

Sayers EW, Cavanaugh M, Clark K, Pruitt KD, Schoch CL, Sherry ST, et al. Database resources of the National Center for Biotechnology Information in 2025. Nucleic Acids Res. 2025;53(D1):D20-D29. doi:10.1093/nar/gkae979.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## ClinGen specifications

- **Identifier:** clingen-specifications
- **Class:** guideline
- **Analytical function:** ACMG/AMP Classification
- **Workflow position:** 10
- **Evidence type:** Integrated clinical evidence
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://cspec.genome.network/cspec/ui/svi/about

### Analytical purpose

Clinical variant classification using ACMG/AMP criteria

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

Requires contextual assessment and expert review. Coverage is incomplete; applicability and version must be checked.

### Complementary resources

ClinGen

### Supporting citation

ClinGen Sequence Variant Interpretation Working Group; ClinGen Variant Curation Expert Panels. ClinGen Criteria Specification Registry: ACMG/AMP variant-classification criteria specifications [Internet]. ClinGen; [cited 2026 Oct 13]. Available from: https://cspec.genome.network/cspec/ui/svi/about.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-13. Check the current release again when the resource is used.

## InterVar

- **Identifier:** intervar
- **Class:** tool
- **Analytical function:** ACMG/AMP Classification
- **Workflow position:** 10
- **Evidence type:** Integrated clinical evidence
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active/verify current status
- **Official resource:** https://github.com/WGLab/InterVar

### Analytical purpose

Clinical variant classification using ACMG/AMP criteria

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

Requires contextual assessment and expert review. Rule implementation, versioning, and context-specific criteria limitations.

### Complementary resources

VarSome; Franklin; ClinGen specifications

### Supporting citation

Li Q, Wang K. InterVar: clinical interpretation of genetic variants by the 2015 ACMG-AMP guidelines. Am J Hum Genet. 2017;100(2):267-280. doi:10.1016/j.ajhg.2017.01.004.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## VarSome

- **Identifier:** varsome
- **Class:** tool
- **Analytical function:** ACMG/AMP Classification
- **Workflow position:** 10
- **Evidence type:** Integrated clinical evidence
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://varsome.com/

### Analytical purpose

Clinical variant classification using ACMG/AMP criteria

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

Requires contextual assessment and expert review. Underlying data updates, rule implementation, and source dependence.

### Complementary resources

InterVar; Franklin; ClinGen specifications

### Supporting citation

Kopanos C, Tsiolkas V, Kouris A, Chapple CE, Albarca Aguilera M, Meyer R, et al. VarSome: the human genomic variant search engine. Bioinformatics. 2019;35(11):1978-1980. doi:10.1093/bioinformatics/bty897.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

## Franklin

- **Identifier:** franklin
- **Class:** tool
- **Analytical function:** ACMG/AMP Classification
- **Workflow position:** 10
- **Evidence type:** Integrated clinical evidence
- **Genome-build and transcript compatibility:** GRCh37;GRCh38
- **Maintenance:** Active
- **Official resource:** https://franklin.genoox.com/clinical-db/home

### Analytical purpose

Clinical variant classification using ACMG/AMP criteria

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

Requires contextual assessment and expert review. Evidence aggregation, versioning, and implementation differences.

### Complementary resources

InterVar; VarSome; ClinGen specifications

### Supporting citation

Franklin by Genoox. Franklin Clinical Database and variant classification platform [Internet]. Genoox; [cited 2026 Oct 13]. Available from: https://franklin.genoox.com/clinical-db/home.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-13. Check the current release again when the resource is used.

## ACMG NGS technical standard

- **Identifier:** reporting-standards
- **Class:** guideline
- **Analytical function:** Reporting & Reinterpretation
- **Workflow position:** 11
- **Evidence type:** Clinical/reporting
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Context dependent
- **Official resource:** https://www.nature.com/articles/s41436-021-01139-4

### Analytical purpose

Clinical reporting, documentation, and reassessment

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

Evidence and interpretations may change over time. This entry cites the 2021 revision. Later ACMG documents, CAP or ISO requirements, and laboratory procedures may also apply.

### Complementary resources

ClinVar; ClinGen; ACMG reanalysis points to consider

### Complementary context

laboratory SOPs

### Supporting citation

Rehm HL, Bick D, Chao E, Chung WK, Das S, Dimmock D, et al. Next-generation sequencing for constitutional variants in the clinical laboratory, 2021 revision: a technical standard of the American College of Medical Genetics and Genomics (ACMG). Genet Med. 2021;23(8):1399-1415. doi:10.1038/s41436-021-01139-4.

### Traceability

Release reviewed on 2026-10-10: 2021 revision. Check the current release again when the resource is used.

## ACMG reanalysis points to consider

- **Identifier:** reanalysis-guidance
- **Class:** guideline
- **Analytical function:** Reporting & Reinterpretation
- **Workflow position:** 11
- **Evidence type:** Clinical/reporting
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Context dependent
- **Official resource:** https://www.nature.com/articles/s41436-019-0478-1

### Analytical purpose

Clinical reporting, documentation, and reassessment

### Selection rationale

Included as the ACMG points to consider in the reevaluation and reanalysis of genomic test results, cited with the 2021 technical standard as reporting and reanalysis guidance.

### Appropriate use

Use when documenting why a previous interpretation is being reevaluated or reanalyzed, including which resources and versions informed the earlier assessment.

### Interpretation boundary

The statement does not assign ACMG/AMP criteria to a variant and does not replace laboratory procedure.

### Inputs and outputs

Input: Prior genomic test results, classifications, and the evidence used to reach them

Output: Points to consider for reevaluation and reanalysis

### Key limitations

Evidence and interpretations may change over time.

### Complementary resources

ACMG NGS technical standard; ClinVar; ClinGen

### Complementary context

laboratory SOPs

### Supporting citation

Deignan JL, Chung WK, Kearney HM, Monaghan KG, Rehder CW, Chao EC, et al. Points to consider in the reevaluation and reanalysis of genomic test results: a statement of the American College of Medical Genetics and Genomics (ACMG). Genet Med. 2019;21(6):1267-1270. doi:10.1038/s41436-019-0478-1.

### Traceability

Release reviewed on 2026-10-13: Deignan et al. 2019. The release cited here is fixed.

## Retired entries

These entries are retained for traceability. They are not representative resources in the current workflow mapping.

### MSeqDR-QM

- **Identifier:** mseqdr-qm
- **Class:** tool
- **Analytical function:** Computational & AI
- **Workflow position:** 5
- **Evidence type:** Computational/AI
- **Genome-build and transcript compatibility:** build dependent
- **Maintenance:** Active/verify current status
- **Official resource:** https://mseqdr.org/

### Analytical purpose

Computational support for variant and gene prioritization

### Selection rationale

Retired from the core representative set. MSeqDR-QM is not listed among the representative resources in Table 1. Mitochondrial variants are outside the scope of the framework.

### Appropriate use

Not used in the current representative mapping. Retained so an earlier citation of this entry can be traced.

### Interpretation boundary

A mitochondrial-disease query result does not establish causality and is not a classification.

### Inputs and outputs

Input: Phenotype, gene, and variant queries related to mitochondrial disease

Output: Mitochondrial-disease knowledge retrieval and prioritization context

### Key limitations

Bias, interpretability, model dependence, and variable validation. Mitochondrial variants are outside the scope of the framework.

### Complementary resources

HPO; ClinGen; ClinVar; Exomiser

### Supporting citation

Not cited among the representative resources in the manuscript. Mitochondrial variants are outside the framework scope.

### Traceability

No release identifier was captured when this entry was reviewed on 2026-10-10. Check the current release again when the resource is used.

### ACMG/AMP guidelines

- **Identifier:** acmg-amp-guidelines
- **Class:** guideline
- **Analytical function:** ACMG/AMP Classification
- **Workflow position:** 10
- **Evidence type:** Integrated clinical evidence
- **Genome-build and transcript compatibility:** build independent
- **Maintenance:** Active
- **Official resource:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4544753/

### Analytical purpose

Clinical variant classification using ACMG/AMP criteria

### Selection rationale

Retired from the core representative set. Table 1 lists InterVar, VarSome, Franklin, and ClinGen specifications for ACMG/AMP classification. Richards et al. 2015 remains the classification standard cited by the framework.

### Appropriate use

Not a selected resource in the ACMG/AMP classification row. The criteria remain the standard applied at clinical variant classification.

### Interpretation boundary

Criteria do not replace evidence quality review, clinical context, or expert judgment.

### Inputs and outputs

Input: Variant evidence and gene/disease context

Output: Pathogenicity classification framework

### Key limitations

Requires contextual assessment and expert review.

### Complementary resources

ClinGen specifications; InterVar; VarSome; Franklin

### Complementary context

laboratory SOPs

### Supporting citation

Richards S, Aziz N, Bale S, Bick D, Das S, Gastier-Foster J, et al. Standards and guidelines for the interpretation and reporting of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med. 2015;17(5):405-424. doi:10.1038/gim.2015.30.

### Traceability

Release reviewed on 2026-10-10: Richards et al. 2015. The release cited here is fixed.
