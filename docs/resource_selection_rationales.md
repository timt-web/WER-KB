# Resource selection rationales

Each entry explains why a resource appears in WER-KB, its appropriate role, and its interpretation boundary. Inclusion does not mean universal or mandatory use.

## GATK

- **Class:** tool
- **Workflow stage(s):** 1;2
- **Analytical function:** Variant-level quality control and filtering
- **Evidence type:** Technical
- **Official resource:** https://gatk.broadinstitute.org/

### Selection rationale
Representative toolkit for reproducible variant calling and post-calling quality filtering.

### Appropriate use
Use with validated laboratory pipeline and documented filters.

### Interpretation boundary
Not a substitute for case-level clinical interpretation.

### Key limitations
Pipeline and parameter dependent; implementation-specific.

### Complementary resources
bcftools;VCFtools

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## bcftools

- **Class:** tool
- **Workflow stage(s):** 1;2
- **Analytical function:** Variant-level quality control and filtering
- **Evidence type:** Technical
- **Official resource:** https://samtools.github.io/bcftools/

### Selection rationale
Included as a lightweight, widely used option for normalization, filtering, and inspection of variant calls.

### Appropriate use
Use when transparent VCF-level processing or normalization is required.

### Interpretation boundary
Does not establish variant validity or pathogenicity.

### Key limitations
Command and threshold dependent; requires validated local workflow.

### Complementary resources
GATK;VCFtools

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## VCFtools

- **Class:** tool
- **Workflow stage(s):** 1;2
- **Analytical function:** Variant-level quality control and filtering
- **Evidence type:** Technical
- **Official resource:** https://vcftools.github.io/

### Selection rationale
Included for transparent VCF-level filtering and summary operations in post-calling workflows.

### Appropriate use
Use for inspection, filtering, and cohort-level VCF summaries as appropriate.

### Interpretation boundary
Does not replace validation of calls or clinical evidence appraisal.

### Key limitations
Feature set and outputs depend on VCF quality and local parameters.

### Complementary resources
GATK;bcftools

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Ensembl

- **Class:** database
- **Workflow stage(s):** 3
- **Analytical function:** Genome and transcript annotation
- **Evidence type:** Reference/annotation
- **Official resource:** https://www.ensembl.org/

### Selection rationale
Included as a maintained reference ecosystem for genome, gene, transcript, and variant annotation.

### Appropriate use
Use when annotation requires explicit genome-build and transcript context.

### Interpretation boundary
Transcript annotations are not a clinical classification.

### Key limitations
Transcript choice and release changes can alter consequences.

### Complementary resources
RefSeq;GENCODE;MANE

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## RefSeq

- **Class:** database
- **Workflow stage(s):** 3
- **Analytical function:** Genome and transcript annotation
- **Evidence type:** Reference/annotation
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/

### Selection rationale
Included as a core curated reference-sequence source for transcript-aware interpretation.

### Appropriate use
Use when documenting transcript accessions and reference sequence context.

### Interpretation boundary
A transcript record alone does not determine disease relevance.

### Key limitations
Transcript updates and alternative isoforms require explicit selection.

### Complementary resources
Ensembl;MANE;GENCODE

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## GENCODE

- **Class:** database
- **Workflow stage(s):** 3
- **Analytical function:** Genome and transcript annotation
- **Evidence type:** Reference/annotation
- **Official resource:** https://www.gencodegenes.org/

### Selection rationale
Included because comprehensive annotation supports transparent transcript and gene context.

### Appropriate use
Use when transcript-model provenance must be documented.

### Interpretation boundary
Does not determine clinical transcript preference by itself.

### Key limitations
Release-specific; transcript-model differences may affect consequence calls.

### Complementary resources
Ensembl;MANE;RefSeq

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## MANE

- **Class:** reference
- **Workflow stage(s):** 3
- **Analytical function:** Genome and transcript annotation
- **Evidence type:** Reference/annotation
- **Official resource:** https://www.ncbi.nlm.nih.gov/refseq/MANE/

### Selection rationale
Included to support consistent transcript selection across RefSeq and Ensembl for clinically relevant reporting.

### Appropriate use
Use when a MANE transcript is available and appropriate to the clinical context.

### Interpretation boundary
Does not eliminate the need to consider disease-specific transcript conventions.

### Key limitations
Coverage is not universal; updates occur over time.

### Complementary resources
RefSeq;Ensembl;GENCODE

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## gnomAD

- **Class:** database
- **Workflow stage(s):** 4
- **Analytical function:** Population-frequency assessment
- **Evidence type:** Population
- **Official resource:** https://gnomad.broadinstitute.org/

### Selection rationale
Included because large-scale population data can test compatibility of allele frequency with a suspected disease model.

### Appropriate use
Use for frequency filtering and ancestry-aware contextual assessment.

### Interpretation boundary
Rarity or absence does not establish pathogenicity.

### Key limitations
Uneven ancestry representation, coverage differences, founder effects, and no phenotype linkage.

### Complementary resources
TOPMed;1000 Genomes;Iranome

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## TOPMed

- **Class:** database
- **Workflow stage(s):** 4
- **Analytical function:** Population-frequency assessment
- **Evidence type:** Population
- **Official resource:** https://topmed.nhlbi.nih.gov/

### Selection rationale
Included as a complementary large-scale population resource.

### Appropriate use
Use when its cohort composition and release are relevant to the frequency question.

### Interpretation boundary
Frequency alone is not clinical evidence of pathogenicity.

### Key limitations
Population representation and dataset-specific processing must be considered.

### Complementary resources
gnomAD;1000 Genomes;Iranome

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## 1000 Genomes

- **Class:** database
- **Workflow stage(s):** 4
- **Analytical function:** Population-frequency assessment
- **Evidence type:** Population
- **Official resource:** https://www.internationalgenome.org/

### Selection rationale
Included as a foundational multi-population reference dataset for complementary frequency and ancestry context.

### Appropriate use
Use as complementary context rather than sole frequency evidence.

### Interpretation boundary
Does not establish pathogenicity or fully represent all populations.

### Key limitations
Limited sample sizes for rare-variant inference relative to newer datasets.

### Complementary resources
gnomAD;TOPMed;Iranome

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Iranome

- **Class:** database
- **Workflow stage(s):** 4
- **Analytical function:** Population-frequency assessment
- **Evidence type:** Population
- **Official resource:** http://www.iranome.ir/

### Selection rationale
Included to provide population-relevant frequency context when patient ancestry is appropriately matched.

### Appropriate use
Use as complementary evidence for appropriately matched Iranian cases.

### Interpretation boundary
Should not be assumed to represent all Iranian or neighboring populations.

### Key limitations
Sampling, coverage, and representativeness limitations.

### Complementary resources
gnomAD;TOPMed;1000 Genomes

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## HPO

- **Class:** ontology
- **Workflow stage(s):** 5
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Evidence type:** Phenotypic
- **Official resource:** https://hpo.jax.org/

### Selection rationale
Included because structured phenotype encoding supports reproducible phenotype–gene and phenotype–disease comparison.

### Appropriate use
Use when clinical findings can be captured with sufficiently specific and temporally appropriate terms.

### Interpretation boundary
Phenotype similarity does not independently establish gene–disease causality or variant pathogenicity.

### Key limitations
Incomplete, nonspecific, or inaccurately captured phenotypes reduce performance.

### Complementary resources
Exomiser;LIRICAL;Phen2Gene

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Exomiser

- **Class:** tool
- **Workflow stage(s):** 5
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Evidence type:** Phenotypic/computational
- **Official resource:** https://exomiser.github.io/

### Selection rationale
Included as a representative phenotype-driven prioritization platform that integrates phenotype and variant context.

### Appropriate use
Use for candidate prioritization when structured phenotype and compatible variant data are available.

### Interpretation boundary
Ranking is not proof of causality or classification.

### Key limitations
Dependent on phenotype quality, knowledgebase coverage, inheritance assumptions, and model configuration.

### Complementary resources
HPO;LIRICAL;Phen2Gene

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## LIRICAL

- **Class:** tool
- **Workflow stage(s):** 5
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Evidence type:** Phenotypic/computational
- **Official resource:** https://lirical.readthedocs.io/

### Selection rationale
Included as a complementary phenotype-driven method emphasizing explicit likelihood-based reasoning.

### Appropriate use
Use when transparent phenotype-based diagnostic prioritization is desired.

### Interpretation boundary
Output does not independently prove causal variant status.

### Key limitations
Sensitive to phenotype completeness, disease annotations, and input assumptions.

### Complementary resources
HPO;Exomiser;Phen2Gene

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Phen2Gene

- **Class:** tool
- **Workflow stage(s):** 5
- **Analytical function:** Phenotype encoding and phenotype-driven gene prioritization
- **Evidence type:** Phenotypic/computational
- **Official resource:** https://phen2gene.wglab.org/

### Selection rationale
Included as a focused phenotype-to-gene prioritization option.

### Appropriate use
Use for rapid gene prioritization from structured phenotypes.

### Interpretation boundary
Does not provide variant classification.

### Key limitations
Limited by phenotype encoding and underlying gene–phenotype knowledge.

### Complementary resources
HPO;Exomiser;LIRICAL

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## ClinGen

- **Class:** curation resource
- **Workflow stage(s):** 6;9;10
- **Analytical function:** Gene–disease association assessment; clinical evidence curation; ACMG/AMP classification
- **Evidence type:** Clinical/curated
- **Official resource:** https://clinicalgenome.org/

### Selection rationale
Included because expert curation helps determine whether variant-level evidence is interpreted within an established gene–disease context.

### Appropriate use
Use for gene–disease validity and applicable specifications when current curation exists.

### Interpretation boundary
Coverage is incomplete and resources do not replace case-specific evidence appraisal.

### Key limitations
Curation status evolves; specifications are context dependent.

### Complementary resources
OMIM;Orphanet;PanelApp;ClinVar

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## OMIM

- **Class:** database
- **Workflow stage(s):** 6
- **Analytical function:** Gene–disease association assessment
- **Evidence type:** Clinical/curated
- **Official resource:** https://www.omim.org/

### Selection rationale
Included as a widely used gene–phenotype knowledge source for evaluating clinical relevance.

### Appropriate use
Use to contextualize known gene–disease relationships and inheritance patterns.

### Interpretation boundary
Does not replace formal validity assessment or case-specific classification.

### Key limitations
Curation depth and update timing vary by entry.

### Complementary resources
ClinGen;Orphanet;PanelApp

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Orphanet

- **Class:** database
- **Workflow stage(s):** 6
- **Analytical function:** Gene–disease association assessment
- **Evidence type:** Clinical/curated
- **Official resource:** https://www.orpha.net/

### Selection rationale
Included for rare-disease nomenclature and gene–disease context.

### Appropriate use
Use when rare-disease terminology and cross-referenced disease context are needed.

### Interpretation boundary
Does not independently establish causality in an individual case.

### Key limitations
Coverage, curation, and update timing vary.

### Complementary resources
ClinGen;OMIM;PanelApp

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## PanelApp

- **Class:** curation resource
- **Workflow stage(s):** 6
- **Analytical function:** Gene–disease association assessment
- **Evidence type:** Clinical/curated
- **Official resource:** https://panelapp.genomicsengland.co.uk/

### Selection rationale
Included because diagnostic panel curation can provide disease-specific gene relevance context.

### Appropriate use
Use as a complementary source when panel evidence and panel scope are relevant.

### Interpretation boundary
Panel inclusion is not synonymous with definitive causality or variant pathogenicity.

### Key limitations
Panel content and evidence ratings change; jurisdiction-specific practices may differ.

### Complementary resources
ClinGen;OMIM;Orphanet

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## CADD

- **Class:** predictor
- **Workflow stage(s):** 7
- **Analytical function:** Computational variant-effect prediction
- **Evidence type:** Computational
- **Official resource:** https://cadd.gs.washington.edu/

### Selection rationale
Included as a representative broad variant-effect predictor.

### Appropriate use
Use as one supportive computational feature when applicable to the variant class.

### Interpretation boundary
Score alone is not clinical pathogenicity evidence.

### Key limitations
Model and training-data dependence; calibration and applicability vary by context.

### Complementary resources
REVEL;SIFT;PolyPhen-2;AlphaMissense

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## REVEL

- **Class:** predictor
- **Workflow stage(s):** 7
- **Analytical function:** Computational variant-effect prediction
- **Evidence type:** Computational
- **Official resource:** https://sites.google.com/site/revelgenomics/

### Selection rationale
Included as a representative ensemble predictor for missense variants.

### Appropriate use
Use only for applicable missense variants and with gene/disease mechanism context.

### Interpretation boundary
Do not treat concordance with related predictors as independent evidence.

### Key limitations
Training-data overlap, calibration, and gene/variant-specific performance limitations.

### Complementary resources
CADD;SIFT;PolyPhen-2;AlphaMissense

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## SIFT

- **Class:** predictor
- **Workflow stage(s):** 7
- **Analytical function:** Computational variant-effect prediction
- **Evidence type:** Computational
- **Official resource:** https://sift.bii.a-star.edu.sg/

### Selection rationale
Included as a commonly used conservation/function-based missense predictor.

### Appropriate use
Use as one supporting predictor for applicable missense variants.

### Interpretation boundary
Not a stand-alone clinical classification method.

### Key limitations
Limited scope; performance and dependence on shared features must be considered.

### Complementary resources
REVEL;PolyPhen-2;CADD

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## PolyPhen-2

- **Class:** predictor
- **Workflow stage(s):** 7
- **Analytical function:** Computational variant-effect prediction
- **Evidence type:** Computational
- **Official resource:** http://genetics.bwh.harvard.edu/pph2/

### Selection rationale
Included as a historical and commonly used missense-effect predictor.

### Appropriate use
Use as supportive context for applicable missense variants.

### Interpretation boundary
Not independent confirmation when used with overlapping predictors.

### Key limitations
Variant- and gene-specific performance; limited clinical specificity.

### Complementary resources
REVEL;SIFT;CADD

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## AlphaMissense

- **Class:** predictor
- **Workflow stage(s):** 7
- **Analytical function:** Computational variant-effect prediction
- **Evidence type:** Computational
- **Official resource:** https://alphafold.ebi.ac.uk/

### Selection rationale
Included as a modern missense-focused predictor that may add complementary computational context.

### Appropriate use
Use for applicable missense variants with explicit transcript/protein mapping.

### Interpretation boundary
Do not use as autonomous clinical classification evidence.

### Key limitations
Model applicability, calibration, and biological/clinical context remain limiting.

### Complementary resources
REVEL;CADD;ClinGen

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## SpliceAI

- **Class:** predictor
- **Workflow stage(s):** 8
- **Analytical function:** Splicing assessment
- **Evidence type:** Computational/transcript-based
- **Official resource:** https://spliceailookup.broadinstitute.org/

### Selection rationale
Included as a representative splice-effect predictor for variants with plausible splicing consequences.

### Appropriate use
Use with explicit transcript selection and consideration of relevant splice mechanisms.

### Interpretation boundary
Prediction is not direct proof of aberrant splicing or clinical pathogenicity.

### Key limitations
Tissue, transcript, mechanism, and calibration dependence.

### Complementary resources
MaxEntScan;dbscSNV;RNA evidence

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## MaxEntScan

- **Class:** predictor
- **Workflow stage(s):** 8
- **Analytical function:** Splicing assessment
- **Evidence type:** Computational/transcript-based
- **Official resource:** http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html

### Selection rationale
Included as a complementary sequence-based splicing assessment method.

### Appropriate use
Use for relevant canonical or near-canonical splice-site questions.

### Interpretation boundary
Does not demonstrate in vivo splicing outcome.

### Key limitations
Limited representation of tissue-specific and broader regulatory context.

### Complementary resources
SpliceAI;dbscSNV;RNA evidence

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## dbscSNV

- **Class:** database
- **Workflow stage(s):** 8
- **Analytical function:** Splicing assessment
- **Evidence type:** Computational/transcript-based
- **Official resource:** https://sites.google.com/site/jpopgen/dbNSFP

### Selection rationale
Included as a supplementary source of precomputed splicing prediction context.

### Appropriate use
Use as complementary computational information for applicable SNVs.

### Interpretation boundary
Not direct experimental evidence of aberrant splicing.

### Key limitations
Scope limited to annotated variants and underlying model limitations.

### Complementary resources
SpliceAI;MaxEntScan;RNA evidence

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## GTEx

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Regulatory and expression evidence
- **Evidence type:** Regulatory/functional
- **Official resource:** https://gtexportal.org/

### Selection rationale
Included because tissue-specific expression context can inform biological plausibility and regulatory interpretation.

### Appropriate use
Use when relevant tissues and biological context are available.

### Interpretation boundary
Expression context does not independently establish variant pathogenicity.

### Key limitations
Donor composition, tissue availability, context dependence, and association limitations.

### Complementary resources
ENCODE;RegulomeDB;FANTOM5

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## ENCODE

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Regulatory and expression evidence
- **Evidence type:** Regulatory/functional
- **Official resource:** https://www.encodeproject.org/

### Selection rationale
Included for experimentally derived functional-genomic context around noncoding or regulatory variants.

### Appropriate use
Use when genomic coordinates overlap relevant regulatory annotations.

### Interpretation boundary
Annotation overlap does not prove disease mechanism or clinical impact.

### Key limitations
Cell-type and experimental-context specificity; incomplete coverage.

### Complementary resources
GTEx;RegulomeDB;FANTOM5

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## RegulomeDB

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Regulatory and expression evidence
- **Evidence type:** Regulatory/functional
- **Official resource:** https://regulomedb.org/

### Selection rationale
Included as an integrative entry point for regulatory annotation.

### Appropriate use
Use for hypothesis generation regarding regulatory context.

### Interpretation boundary
Scores are not direct clinical pathogenicity evidence.

### Key limitations
Evidence aggregation and tissue/context limitations.

### Complementary resources
ENCODE;GTEx;FANTOM5

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## FANTOM5

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Regulatory and expression evidence
- **Evidence type:** Regulatory/functional
- **Official resource:** https://fantom.gsc.riken.jp/5/

### Selection rationale
Included as a complementary functional-genomics resource for promoter/enhancer and expression context.

### Appropriate use
Use when relevant cell-type or regulatory annotation is needed.

### Interpretation boundary
Does not by itself establish variant effect or causality.

### Key limitations
Coverage and context dependence; update status must be checked.

### Complementary resources
ENCODE;GTEx;RegulomeDB

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## UniProt

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Structural and protein-function evidence
- **Evidence type:** Structural/functional
- **Official resource:** https://www.uniprot.org/

### Selection rationale
Included for curated protein-function and domain context relevant to variant interpretation.

### Appropriate use
Use when a variant can be mapped reliably to a protein sequence and functional feature.

### Interpretation boundary
Protein annotation alone does not determine clinical significance.

### Key limitations
Annotation completeness and isoform mapping can vary.

### Complementary resources
InterPro;PDB;AlphaFold DB

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## PDB

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Structural and protein-function evidence
- **Evidence type:** Structural/functional
- **Official resource:** https://www.rcsb.org/

### Selection rationale
Included where experimentally resolved structure can inform residue-level or domain-level context.

### Appropriate use
Use when reliable structural coverage and mapping are available.

### Interpretation boundary
Structure presence does not prove functional or clinical impact.

### Key limitations
Incomplete protein coverage; construct and experimental context limitations.

### Complementary resources
UniProt;AlphaFold DB;InterPro

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## AlphaFold DB

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Structural and protein-function evidence
- **Evidence type:** Structural/functional
- **Official resource:** https://alphafold.ebi.ac.uk/

### Selection rationale
Included for structural hypothesis generation when experimental structures are unavailable.

### Appropriate use
Use with confidence measures and in conjunction with known protein biology.

### Interpretation boundary
Predicted structure is not direct functional or clinical evidence.

### Key limitations
Prediction confidence, conformational dynamics, complexes, and mapping limitations.

### Complementary resources
PDB;UniProt;InterPro

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## InterPro

- **Class:** database
- **Workflow stage(s):** 7;8;9
- **Analytical function:** Structural and protein-function evidence
- **Evidence type:** Structural/functional
- **Official resource:** https://www.ebi.ac.uk/interpro/

### Selection rationale
Included for standardized domain and family context during protein-level interpretation.

### Appropriate use
Use when variant localization relative to known domains is relevant.

### Interpretation boundary
Domain overlap alone does not establish pathogenicity.

### Key limitations
Annotation coverage and functional specificity vary.

### Complementary resources
UniProt;PDB;AlphaFold DB

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## MSeqDR-QM

- **Class:** tool
- **Workflow stage(s):** 5;6;7;8;9
- **Analytical function:** Computational and AI-assisted prioritization
- **Evidence type:** Computational/AI
- **Official resource:** https://mseqdr.org/

### Selection rationale
Included as a representative knowledge-driven platform supporting Mendelian variant and gene prioritization.

### Appropriate use
Use as supportive retrieval/prioritization context with transparent review of contributing sources.

### Interpretation boundary
Integrated output is not independent evidence or autonomous classification.

### Key limitations
Underlying data provenance, update timing, and source dependence require review.

### Complementary resources
HPO;ClinGen;ClinVar;Exomiser

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## GEMSTONE

- **Class:** tool
- **Workflow stage(s):** 5;6;7;8;9
- **Analytical function:** Computational and AI-assisted prioritization
- **Evidence type:** Computational/AI
- **Official resource:** https://gemstone.yulab.org/

### Selection rationale
Included as a representative integrative prioritization platform.

### Appropriate use
Use when its documented inputs, version, and assumptions fit the case.

### Interpretation boundary
Output does not replace review of primary evidence or formal classification.

### Key limitations
Model/data dependence, configuration sensitivity, and variable validation.

### Complementary resources
Exomiser;MSeqDR-QM;ClinGen

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## ClinVar

- **Class:** database
- **Workflow stage(s):** 9;11
- **Analytical function:** Clinical evidence retrieval and curation; reporting and reinterpretation
- **Evidence type:** Clinical/literature
- **Official resource:** https://www.ncbi.nlm.nih.gov/clinvar/

### Selection rationale
Included to retrieve prior clinical assertions, review status, conflicts, and associated evidence context.

### Appropriate use
Use when reviewing previously reported clinical interpretations.

### Interpretation boundary
Entries are not definitive conclusions and must be appraised in context.

### Key limitations
Conflicting submissions, variable review status, curation lag, and heterogeneous evidence.

### Complementary resources
ClinGen;PubMed;Mastermind;HGMD

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## HGMD

- **Class:** database
- **Workflow stage(s):** 9
- **Analytical function:** Clinical evidence retrieval and curation
- **Evidence type:** Clinical/literature
- **Official resource:** https://www.hgmd.cf.ac.uk/

### Selection rationale
Included as a literature-derived variant resource that may support evidence retrieval where access is available.

### Appropriate use
Use as a starting point for primary-literature verification.

### Interpretation boundary
A reported disease association is not a final classification.

### Key limitations
Subscription access, curation criteria, and need for primary-source appraisal.

### Complementary resources
ClinVar;PubMed;Mastermind

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Mastermind

- **Class:** database
- **Workflow stage(s):** 9
- **Analytical function:** Clinical evidence retrieval and curation
- **Evidence type:** Clinical/literature
- **Official resource:** https://mastermind.genomenon.com/

### Selection rationale
Included to support efficient retrieval of relevant published evidence.

### Appropriate use
Use to identify literature for direct appraisal.

### Interpretation boundary
Search results do not replace assessment of study quality or applicability.

### Key limitations
Indexing scope, access tier, normalization, and literature quality vary.

### Complementary resources
PubMed;ClinVar;ClinGen

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## PubMed

- **Class:** database
- **Workflow stage(s):** 9
- **Analytical function:** Clinical evidence retrieval and curation
- **Evidence type:** Clinical/literature
- **Official resource:** https://pubmed.ncbi.nlm.nih.gov/

### Selection rationale
Included as a core bibliographic source for retrieving primary studies, guidelines, and resource documentation.

### Appropriate use
Use for direct appraisal of source evidence.

### Interpretation boundary
Search retrieval is not evidence appraisal or clinical classification.

### Key limitations
Indexing, query design, publication bias, and access limitations.

### Complementary resources
Mastermind;ClinVar;ClinGen

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## InterVar

- **Class:** tool
- **Workflow stage(s):** 10
- **Analytical function:** ACMG/AMP-based variant classification
- **Evidence type:** Integrated clinical evidence
- **Official resource:** https://wintervar.wglab.org/

### Selection rationale
Included as a representative tool that can organize ACMG/AMP evidence for review.

### Appropriate use
Use as a structured aid with current specifications and expert review.

### Interpretation boundary
Automated suggestions are not final clinical classifications.

### Key limitations
Rule implementation, versioning, and context-specific criteria limitations.

### Complementary resources
VarSome;Franklin;ClinGen specifications

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## VarSome

- **Class:** tool
- **Workflow stage(s):** 10
- **Analytical function:** ACMG/AMP-based variant classification
- **Evidence type:** Integrated clinical evidence
- **Official resource:** https://varsome.com/

### Selection rationale
Included as a representative integrated annotation and classification-support platform.

### Appropriate use
Use with transparent review of evidence, criteria activation, and current specifications.

### Interpretation boundary
Platform output is not a substitute for expert clinical review.

### Key limitations
Underlying data updates, rule implementation, and source dependence.

### Complementary resources
InterVar;Franklin;ClinGen specifications

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Franklin

- **Class:** tool
- **Workflow stage(s):** 10
- **Analytical function:** ACMG/AMP-based variant classification
- **Evidence type:** Integrated clinical evidence
- **Official resource:** https://franklin.genoox.com/

### Selection rationale
Included as a representative classification-support platform.

### Appropriate use
Use as a support tool alongside manual evidence appraisal and applicable specifications.

### Interpretation boundary
Do not accept automated classifications without contextual review.

### Key limitations
Evidence aggregation, versioning, and implementation differences.

### Complementary resources
InterVar;VarSome;ClinGen specifications

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## ACMG/AMP guidelines

- **Class:** guideline
- **Workflow stage(s):** 10
- **Analytical function:** ACMG/AMP-based variant classification
- **Evidence type:** Integrated clinical evidence
- **Official resource:** https://www.acmg.net/

### Selection rationale
Included because formal clinical classification should follow established ACMG/AMP criteria and applicable specifications.

### Appropriate use
Use after evidence selection and appraisal within defined gene–disease/inheritance context.

### Interpretation boundary
Criteria do not replace evidence quality review, clinical context, or expert judgment.

### Key limitations
General framework requires contextual and gene/disease-specific application.

### Complementary resources
ClinGen;laboratory SOPs;VarSome

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## ClinGen specifications

- **Class:** guideline
- **Workflow stage(s):** 10
- **Analytical function:** ACMG/AMP-based variant classification
- **Evidence type:** Integrated clinical evidence
- **Official resource:** https://clinicalgenome.org/working-groups/sequence-variant-interpretation/

### Selection rationale
Included because applicable expert specifications can improve consistency of ACMG/AMP criteria application.

### Appropriate use
Use when a current, applicable specification exists.

### Interpretation boundary
Absence of a specification does not justify overinterpretation.

### Key limitations
Coverage is incomplete; applicability and version must be checked.

### Complementary resources
ACMG/AMP guidelines;ClinGen

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.

## Reporting standards

- **Class:** guideline
- **Workflow stage(s):** 11
- **Analytical function:** Reporting, documentation, and reinterpretation
- **Evidence type:** Clinical/reporting
- **Official resource:** https://www.acmg.net/

### Selection rationale
Included because transparent reporting and documentation preserve interpretive traceability and support later reinterpretation.

### Appropriate use
Use to document resources, versions, evidence, rationale, limitations, and reportable conclusions.

### Interpretation boundary
Reporting standards do not replace classification or clinical judgment.

### Key limitations
Jurisdictional, laboratory, and regulatory requirements vary.

### Complementary resources
ClinVar;ClinGen;laboratory SOPs

### Traceability note
Record the resource version or release, access date, genome build and transcript context when applicable, and the case-specific reason for use.
