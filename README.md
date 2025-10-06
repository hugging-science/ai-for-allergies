<style>
table, th, td { border: 3px solid #777; }
table { display: table; width: 100%; }
th.name { width:10%; }
th.description { width:75%; }
th.source { width:5%; }
th.license { width:5%; }
th.tags { width:5%; }
td.plain { color:#000000; }
/* Legend styles */
.legend { margin:8px 0 16px 0; font-size:90%; }
.legend .item { display:inline-flex; align-items:center; margin-right:12px; }
.legend .swatch { width:14px; height:14px; border:1px solid #ccc; margin-right:6px; display:inline-block; }
</style>

# Awesome Food Allergy Datasets 

> A curated list of datasets, databases, and resources for food allergy research, allergen identification, drug development, and clinical applications.

<div class="legend">
<span class="item"><span class="swatch" style="background:#e6ffea"></span>Open source</span>
<span class="item"><span class="swatch" style="background:#f7d6d6"></span>Gated</span>
<span class="item"><span class="swatch" style="background:#ffffff"></span>Unknown</span>
</div>

## Allergen Identification & Prediction

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="http://stitch.embl.de/cgi/download.pl?UserId=o7OnPFVV3JJ4&amp;sessionId=e44tciEEXzEc">STITCH</a></td>
      <td class="plain">A database that itegrates known and predicted interactions between chemicals and proteins, combining evidence from experiments, databases, text mining and prediction algorithms</td>
      <td><a href="http://stitch.embl.de/cgi/download.pl?UserId=o7OnPFVV3JJ4&amp;sessionId=e44tciEEXzEc">http://stitch.embl.de/cgi/download.pl?UserId=o7OnPFVV3JJ4&amp;sessionId=e44tciEEXzEc</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC522748/">Allermatch</a></td>
      <td class="plain">Webtool for standardized allergenicity prediction according to FAO/WHO Codex alimentarius guidelines using sliding window approach</td>
      <td><a href="http://allermatch.org">http://allermatch.org</a></td>
      <td><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC522748/">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC522748/</a></td>
      <td class="plain">Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="Multiple publications">AllerHunter</a></td>
      <td class="plain">Computational tool for allergen prediction with internal and external validation achieving MCC 0.738 on external dataset</td>
      <td><a href="Contact authors">Contact authors</a></td>
      <td class="plain">Multiple publications</td>
      <td class="plain">Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#ffffff">
      <td><a href="https://academic.oup.com/bioinformaticsadvances/article/3/1/vbad151/7319372?login=false">NetAllergen</a></td>
      <td class="plain">A curated database of IgE-inducing allergens based on AllergenOnline, carefully removed allergen redundancy with a novel protein partitioning pipeline, and developed a new allergen prediction method, introducing MHC presentation propensity as a novel feature.</td>
      <td><a href="https://services.healthtech.dtu.dk/services/NetAllergen-1.0/">https://services.healthtech.dtu.dk/services/NetAllergen-1.0/</a></td>
      <td><a href="https://academic.oup.com/bioinformaticsadvances/article/3/1/vbad151/7319372?login=false">https://academic.oup.com/bioinformaticsadvances/article/3/1/vbad151/7319372?login=false</a></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.nature.com/articles/s41564-023-01464-1">Akkermansia muciniphila exacerbates food allergy in fibre-deprived mice</a></td>
      <td class="plain">Study on alteration of mice gut microbioma, focusing on Akkermansia muciniphila.</td>
      <td><a href="https://www.ebi.ac.uk/ena/browser/view/PRJEB53451">https://www.ebi.ac.uk/ena/browser/view/PRJEB53451</a></td>
      <td><a href="https://www.nature.com/articles/s41564-023-01464-1">https://www.nature.com/articles/s41564-023-01464-1</a></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://www.nature.com/articles/s41467-023-40336-4#data-availability">CHILD cohort</a></td>
      <td class="plain">Multi-omics; microbiome maturation predicts allergic disease</td>
      <td class="plain"></td>
      <td><a href="https://www.nature.com/articles/s41467-023-40336-4#data-availability">https://www.nature.com/articles/s41467-023-40336-4#data-availability</a></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/29625844/">WHO/IUIS Allergen Nomenclature Database</a></td>
      <td class="plain">The WHO/IUIS Allergen Nomenclature is the authoritative system for naming allergenic proteins, approved by the World Health Organization and International Union of Immunological Societies. Established in 1984, this sub-committee maintains a unique, systematic nomenclature based on the Linnaean taxonomy for proteins causing IgE-mediated allergic reactions, supporting global consistency in allergen research and publication</td>
      <td><a href="https://allergen.org/">https://allergen.org/</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/29625844/">https://pubmed.ncbi.nlm.nih.gov/29625844/</a></td>
      <td class="plain">Text Mining</td>
    </tr>
  </tbody>
</table>

## Computational Method Development

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/24723570/">DAVIS (DrugTarget)</a></td>
      <td class="plain">Drug-target affinity dataset containing Kd values for 68 drugs and 379 protein targets, widely used for benchmarking drug-target interaction prediction models</td>
      <td><a href="https://staff.cs.utu.fi/~aatapa/data/DrugTarget/">https://staff.cs.utu.fi/~aatapa/data/DrugTarget/</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/24723570/">https://pubmed.ncbi.nlm.nih.gov/24723570/</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubs.rsc.org/en/content/articlelanding/2022/CP/D2CP03966D">nabla²DFT</a></td>
      <td class="plain">nabla²DFT is a large-scale dataset and benchmark in computational quantum chemistry that is designed to support machine learning models for predicting molecular electronic structure properties. Per molecule, it contains quantum-level properties like total electronic energy, DFT Hamilton matrices, forces, overlap matrices, etcetera. In addition to the data, it also contains benchmark tasks. Can be used to train neural network potentials.</td>
      <td><a href="https://github.com/AIRI-Institute/nablaDFT/tree/1.0">https://github.com/AIRI-Institute/nablaDFT/tree/1.0</a></td>
      <td><a href="https://pubs.rsc.org/en/content/articlelanding/2022/CP/D2CP03966D">https://pubs.rsc.org/en/content/articlelanding/2022/CP/D2CP03966D</a></td>
      <td class="plain">Structural Analysis, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://quantum-machine.org/datasets/">QM Datasets</a></td>
      <td class="plain">Benchmarks quantum chemistry datasets of small organic molecules (&lt;=9 heavy atoms) where molecular properties have been computed via quantum chemistry. WIDELY USED for molecular property prediction</td>
      <td><a href="https://quantum-machine.org/datasets/">https://quantum-machine.org/datasets/</a></td>
      <td class="plain"></td>
      <td class="plain">Property Prediction, Text Mining</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.nature.com/articles/s41597-025-04972-3">QDπ Dataset</a></td>
      <td class="plain">The QDπ dataset enables creation of flexible target loss functions for neural network training relevant to drug discovery, including information-dense data sets of relative conformational energies and barriers, intermolecular interactions, tautomers and relative protonation energies of drug-like compounds and biomolecular fragments. Useful for training universal machine learning potentials (MLPs).</td>
      <td><a href="https://zenodo.org/records/14970869">https://zenodo.org/records/14970869</a></td>
      <td><a href="https://www.nature.com/articles/s41597-025-04972-3">https://www.nature.com/articles/s41597-025-04972-3</a></td>
      <td class="plain">Property Prediction, Text Mining</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/33201237/">AlgPred 2.0 Dataset</a></td>
      <td class="plain">Large-scale dataset with 10075 allergens and 10075 non-allergens plus 10451 validated IgE epitopes for machine learning</td>
      <td><a href="https://webs.iiitd.edu.in/raghava/algpred2/">https://webs.iiitd.edu.in/raghava/algpred2/</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/33201237/">https://pubmed.ncbi.nlm.nih.gov/33201237/</a></td>
      <td class="plain">Allergenicity Assessment, Cross-Reactivity Modeling, Drug Design</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://github.com/Trustii-team/AllergenChip">Allergen Chip data challenge</a></td>
      <td class="plain">The goal of the competition was to develop Machine Learning models that can predict the presence and severity of an allergic disease based on this personalized profile. The dataset has been constructed from data of more than 4,000 patients includes tabular data associated with image files.</td>
      <td><a href="https://github.com/Trustii-team/AllergenChip">https://github.com/Trustii-team/AllergenChip</a></td>
      <td class="plain"></td>
      <td class="plain">Risk Stratification, Severity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141">TIP Dataset</a></td>
      <td class="plain">Tolerance Induction Program dataset containing data from 530 pedriatic patients. From &quot;Food anaphylaxis diagnostic marker compilation in machine learning design and validation&quot;</td>
      <td><a href="https://github.com/TPIRC/ai_paper_2022">https://github.com/TPIRC/ai_paper_2022</a></td>
      <td><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141">https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141</a></td>
      <td class="plain">Risk Stratification, Severity Assessment</td>
    </tr>
  </tbody>
</table>

## Cross-Reactivity Analysis

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="https://link.springer.com/article/10.1007/s12161-022-02353-9">Allergen30</a></td>
      <td class="plain">Dataset containing structural and sequence information for 30 major allergen families to support allergenicity prediction and cross-reactivity analysis</td>
      <td><a href="https://data.mendeley.com/datasets/9ygs9vhnpw/1">https://data.mendeley.com/datasets/9ygs9vhnpw/1</a></td>
      <td><a href="https://link.springer.com/article/10.1007/s12161-022-02353-9">https://link.springer.com/article/10.1007/s12161-022-02353-9</a></td>
      <td class="plain">Allergenicity Assessment, Allergen Identification, Structural Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/18395549/">AllFam</a></td>
      <td class="plain">Database classifying allergens into 134 protein families based on WHO/IUIS and AllergenOnline data with Pfam definitions</td>
      <td><a href="https://www.meduniwien.ac.at/allfam/">https://www.meduniwien.ac.at/allfam/</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/18395549/">https://pubmed.ncbi.nlm.nih.gov/18395549/</a></td>
      <td class="plain">Structural Analysis, Cross-Reactivity Modeling</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://academic.oup.com/nar/article/47/W1/W502/5494780">IEDB Analysis Resource</a></td>
      <td class="plain">Companion to IEDB providing computational tools for B and T cell epitope prediction including MHC binding predictions</td>
      <td><a href="http://tools.iedb.org/">http://tools.iedb.org/</a></td>
      <td><a href="https://academic.oup.com/nar/article/47/W1/W502/5494780">https://academic.oup.com/nar/article/47/W1/W502/5494780</a></td>
      <td class="plain">Epitope Mapping</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11230160/">AllergenAI</a></td>
      <td class="plain">Allergenicity prediction based on protein sequences. Processed data from SDAP 2.0, COMPARE, and AlgPred 2</td>
      <td><a href="https://compbio.uth.edu/AllergenAI/">https://compbio.uth.edu/AllergenAI/</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11230160/">https://pmc.ncbi.nlm.nih.gov/articles/PMC11230160/</a></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.meduniwien.ac.at/allfam/">Allergen Family Database</a></td>
      <td class="plain">A curated database that classifies known allergens into protein families to support analysis of allergenicity and cross-reactivity across sources and exposure routes. It integrates entries from WHO/IUIS Allergen Nomenclature and AllergenOnline with Pfam domain annotations, providing family-level pages with biochemical descriptions, allergological significance, and links to primary records and references.</td>
      <td><a href="https://www.meduniwien.ac.at/allfam/">https://www.meduniwien.ac.at/allfam/</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment, Drug Design, Target Interaction, Structural Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://github.com/maitreyeepaliwal/Alleropedia-Database-for-Allergens">Alleropedia Database for Allergens</a></td>
      <td class="plain">The Alleropedia database is a comprehensive metadatabase consolidating 13,146 allergen records from six freely accessible sources, including major allergen databases like COMPARE, AllergenOnline, WHO/IUIS, and Allergome. It offers a user-friendly web interface and additional features such as data integration with sources like NCBI, facilitating easy access, analysis, and navigation of allergen-related information for researchers and clinician</td>
      <td><a href="https://github.com/maitreyeepaliwal/Alleropedia-Database-for-Allergens">https://github.com/maitreyeepaliwal/Alleropedia-Database-for-Allergens</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Allergenicity Assessment, Cross-Reactivity Modeling, Epitope Mapping, Structural Analysis</td>
    </tr>
  </tbody>
</table>

## Drug & Immunotherapy Development

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10509899/">SDAP 2.0</a></td>
      <td class="plain">SDAP is a Web server that integrates a database of allergenic proteins with various computational tools that can assist structural biology studies related to allergens. SDAP is an important tool in the investigation of the cross-reactivity between known allergens, in testing the FAO/WHO allergenicity rules for new proteins, and in predicting the IgE-binding potential of genetically modified food proteins.</td>
      <td><a href="https://fermi.utmb.edu/">https://fermi.utmb.edu/</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10509899/">https://pmc.ncbi.nlm.nih.gov/articles/PMC10509899/</a></td>
      <td class="plain">Drug Design, Structural Analysis, Epitope Mapping, Cross-Reactivity Modeling</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://qsardb.org/">QSAR Database</a></td>
      <td class="plain">QsarDB is a smart repository for (Q)SAR/QSPR models and datasets, providing access to peer-reviewed quantitative structure-activity relationship models</td>
      <td><a href="https://qsardb.org/">https://qsardb.org/</a></td>
      <td><a href="https://qsardb.org/">https://qsardb.org/</a></td>
      <td class="plain">Property Prediction, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5846051/">e-Drug3D Database</a></td>
      <td class="plain">Three-dimensional database of drug-like compounds and their molecular conformations for structure-based drug design applications</td>
      <td><a href="https://zenodo.org/records/17063565">https://zenodo.org/records/17063565</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5846051/">https://pmc.ncbi.nlm.nih.gov/articles/PMC5846051/</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3382018/">Stanford Drug Data (Effects &amp; Interactions)</a></td>
      <td class="plain">Comprehensive dataset of drug effects and drug-drug interactions compiled from clinical data and pharmacological studies</td>
      <td><a href="https://purl.stanford.edu/zq918jm7358/version/1">https://purl.stanford.edu/zq918jm7358/version/1</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3382018/">https://pmc.ncbi.nlm.nih.gov/articles/PMC3382018/</a></td>
      <td class="plain">Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://drugcentral.org/download">DrugCentral</a></td>
      <td class="plain">Open-access online drug information repository covering over 4950 drugs with structural, physicochemical, and pharmacological details to support drug discovery and repositioning</td>
      <td><a href="https://drugcentral.org/download">https://drugcentral.org/download</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://link.springer.com/article/10.1007/s11030-025-11164-z">MedKG</a></td>
      <td class="plain">Comprehensive medical knowledge graph integrating data from 35 authoritative sources with 34 node types and 79 relationships for precision medicine and drug discovery</td>
      <td><a href="https://github.com/chemplusx/MedKG">https://github.com/chemplusx/MedKG</a></td>
      <td><a href="https://link.springer.com/article/10.1007/s11030-025-11164-z">https://link.springer.com/article/10.1007/s11030-025-11164-z</a></td>
      <td class="plain">Drug Design, Target Interaction, Treatment Planning</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://arxiv.org/html/2308.09639v2">PDBBind+</a></td>
      <td class="plain">Enhanced version of PDBBind database providing protein-ligand binding affinity data with refined experimental measurements and structural information</td>
      <td><a href="https://www.pdbbind-plus.org.cn/download">https://www.pdbbind-plus.org.cn/download</a></td>
      <td><a href="https://arxiv.org/html/2308.09639v2">https://arxiv.org/html/2308.09639v2</a></td>
      <td class="plain">Target Interaction, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC1899095/">Human Metabolome Database (HMDB)</a></td>
      <td class="plain">Freely available electronic database containing detailed information about 220,945 small molecule metabolites found in the human body for metabolomics and biomarker discovery</td>
      <td><a href="https://www.hmdb.ca/downloads">https://www.hmdb.ca/downloads</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC1899095/">https://pmc.ncbi.nlm.nih.gov/articles/PMC1899095/</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://academic.oup.com/nar/article/52/D1/D1465/7275004">Therapeutic Target Database (TTD)</a></td>
      <td class="plain">Database providing information about known therapeutic protein and nucleic acid targets, targeted diseases, pathway information, and corresponding drugs</td>
      <td><a href="https://db.idrblab.net/ttd/full-data-download">https://db.idrblab.net/ttd/full-data-download</a></td>
      <td><a href="https://academic.oup.com/nar/article/52/D1/D1465/7275004">https://academic.oup.com/nar/article/52/D1/D1465/7275004</a></td>
      <td class="plain">Drug Design, Treatment Planning, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.nature.com/articles/s41597-025-04720-7">QCML Dataset</a></td>
      <td class="plain">Quantum chemistry reference dataset with 33.5 m. DFT calculations and 14.7 billion semi empirical entries. It covers small molecules (up to 8 heavy atoms) and provide a wide variety of computed molecular properties</td>
      <td><a href="https://zenodo.org/records/14859804">https://zenodo.org/records/14859804</a></td>
      <td><a href="https://www.nature.com/articles/s41597-025-04720-7">https://www.nature.com/articles/s41597-025-04720-7</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://arxiv.org/html/2412.06847v2">M3-20M: Multi-Modal Molecular Dataset</a></td>
      <td class="plain">M3-20M is an extensive multi-modal molecular dataset containing over 20 million molecules with 1D, 2D, and 3D molecular representations, physicochemical properties, and text descriptions. It supports AI-driven drug discovery, molecular property prediction, lead optimization, and drug-target interaction modeling across various applications, including allergy-related therapeutic design.</td>
      <td><a href="https://huggingface.co/datasets/Alex99Gsy/M-3_Multi-Modal-Molecule">https://huggingface.co/datasets/Alex99Gsy/M-3_Multi-Modal-Molecule</a></td>
      <td><a href="https://arxiv.org/html/2412.06847v2">https://arxiv.org/html/2412.06847v2</a></td>
      <td class="plain">Target Interaction, Property Prediction, Drug Design</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://go.sandboxaq.com/rs/175-UKR-711/images/sair_paper.pdf">SAIR Dataset</a></td>
      <td class="plain">The SAIR dataset is a massive repository containing over one million protein-ligand 3D cofolded structures paired with experimental binding affinity measurements (e.g., IC50). It supports AI-driven drug discovery by enabling prediction of molecular binding potency and facilitating the design and optimization of new therapeutic compounds targeting allergenic proteins and other disease-related targets.</td>
      <td><a href="https://huggingface.co/datasets/SandboxAQ/SAIR">https://huggingface.co/datasets/SandboxAQ/SAIR</a></td>
      <td><a href="https://go.sandboxaq.com/rs/175-UKR-711/images/sair_paper.pdf">https://go.sandboxaq.com/rs/175-UKR-711/images/sair_paper.pdf</a></td>
      <td class="plain">Target Interaction, Structural Analysis, Property Prediction, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://tdcommons.ai/">TDC</a></td>
      <td class="plain">Curated collection of AI (ready) datasets and tasks in the therapeutic pipeline, with consistent splits and evals</td>
      <td><a href="https://tdcommons.ai/">https://tdcommons.ai/</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://arxiv.org/abs/2503.20158">RxRx3</a></td>
      <td class="plain">Cell imaging phenomics dataset, that provides a map for biology for ML methods, including knockouts small molecule perturbations and embeddings</td>
      <td><a href="https://www.recursion.com/news/accelerating-ai-drug-discovery-with-open-source-datasets">https://www.recursion.com/news/accelerating-ai-drug-discovery-with-open-source-datasets</a></td>
      <td><a href="https://arxiv.org/abs/2503.20158">https://arxiv.org/abs/2503.20158</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://archive.ics.uci.edu/ml/datasets/dorothea">Dorothea</a></td>
      <td class="plain">Gene regulatory network of signed TF-&gt; target interactions (human/mouse) with confidence levels</td>
      <td><a href="https://archive.ics.uci.edu/ml/datasets/dorothea">https://archive.ics.uci.edu/ml/datasets/dorothea</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965">Simulated Allergen Immunotherapy Trials Dataset</a></td>
      <td class="plain">Simulated datasets implementing an enchanced three stage trial design for allergen immunotherapy (AIT). It captures realistic features like corssover, discontinuation and staged enrollment</td>
      <td><a href="https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965">https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.guidetopharmacology.org/download.jsp">IUPHAR Pharmacology Datasets</a></td>
      <td class="plain">Pharmacology data curated from experts that links drug/ligand information to molecular targets</td>
      <td><a href="https://www.guidetopharmacology.org/download.jsp">https://www.guidetopharmacology.org/download.jsp</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5">Enamine REAL Database</a></td>
      <td class="plain">Massive virtual libary of synthesizable compunds and enumerated subsets for large scale virtual screening and hit expansion</td>
      <td><a href="https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5">https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.nature.com/articles/s41597-024-03788-x">Quantum Chemistry Database with Ground- and Excited-State (QCDGE) Dataset</a></td>
      <td class="plain">more than 400k small organic molecules (&lt;=10 heavy atoms) for which both ground state and excited state quantum chemical properties have already been computed</td>
      <td><a href="https://springernature.figshare.com/collections/QCDGE_database_Quantum_Chemistry_Database_with_Ground-_and_Excited-State_Properties/7259125/1">https://springernature.figshare.com/collections/QCDGE_database_Quantum_Chemistry_Database_with_Ground-_and_Excited-State_Properties/7259125/1</a></td>
      <td><a href="https://www.nature.com/articles/s41597-024-03788-x">https://www.nature.com/articles/s41597-024-03788-x</a></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.probes-drugs.org/download">Probes &amp; Drugs Datasets</a></td>
      <td class="plain">The Probes &amp; Drugs (P&amp;D) portal is a comprehensive resource integrating high-quality bioactive compound sets for analysis and comparison, focusing on chemical probes and drugs. It includes compound data from multiple sources, provides expert scoring based on potency and selectivity, and offers standardized compound forms to unify data. The portal supports research by tagging probes, scoring probe-likeness, and highlighting structural alerts for compound reliability</td>
      <td><a href="https://www.probes-drugs.org/download">https://www.probes-drugs.org/download</a></td>
      <td class="plain"></td>
      <td class="plain">Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://academic.oup.com/database/article/doi/10.1093/database/bax066/4157991">AllerBase</a></td>
      <td class="plain">Comprehensive allergen knowledgebase integrating data from multiple sources with extensive experimental validation and IgE epitope data</td>
      <td><a href="http://algpred.tu-bs.de/allerbase/">http://algpred.tu-bs.de/allerbase/</a></td>
      <td><a href="https://academic.oup.com/database/article/doi/10.1093/database/bax066/4157991">https://academic.oup.com/database/article/doi/10.1093/database/bax066/4157991</a></td>
      <td class="plain">Cross-Reactivity Modeling, Allergenicity Assessment, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965">Simulated AIT Trials Dataset</a></td>
      <td class="plain">Simulated datasets with enhanced three-stage trial design for allergen immunotherapy capturing realistic features like crossover and discontinuation</td>
      <td><a href="https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965">https://figshare.com/articles/dataset/Simulated_datasets_for_enhanced_three-stage_design_for_allergen_immunotherapy_trials/23638965</a></td>
      <td class="plain"></td>
      <td class="plain">Treatment Planning, Drug Design</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141">Food Anaphylaxis ML Dataset (TIP)</a></td>
      <td class="plain">Dataset from Tolerance Induction Program with 530 juvenile patients featuring 241 allergy assays per patient achieving 95.2% recall for peanut anaphylaxis prediction</td>
      <td><a href="Contact authors">Contact authors</a></td>
      <td><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141">https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283141</a></td>
      <td class="plain">Drug Design, Treatment Planning</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://onlinelibrary.wiley.com/doi/10.1111/all.15839">Food Allergy Risk Stratification Dataset</a></td>
      <td class="plain">EMR-based dataset with 4077 children with food allergies and 95686 controls for predicting FA development with AUC 0.80</td>
      <td><a href="Contact authors">Contact authors</a></td>
      <td><a href="https://onlinelibrary.wiley.com/doi/10.1111/all.15839">https://onlinelibrary.wiley.com/doi/10.1111/all.15839</a></td>
      <td class="plain">Treatment Planning</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5">Enamine REAL Database</a></td>
      <td class="plain">Massive virtual library of synthesizable compounds and enumerated subsets for large-scale virtual screening and hit expansion</td>
      <td><a href="https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5">https://gist.github.com/matteoferla/b1eee8656079d006835f2d8dc159fbb5</a></td>
      <td class="plain"></td>
      <td class="plain">Drug Design, Target Interaction</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/35157755/">AllerCatPro 2.0</a></td>
      <td class="plain">Tool predicting allergenicity using amino acid sequence and 3D structure similarity with database of 4979 allergens 162 mild allergenic proteins and 165 autoimmune allergens</td>
      <td><a href="https://allercatpro.bii.a-star.edu.sg/">https://allercatpro.bii.a-star.edu.sg/</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/35157755/">https://pubmed.ncbi.nlm.nih.gov/35157755/</a></td>
      <td class="plain">Allergenicity Assessment, Drug Design</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-14-S6-S4">AllerTOP v1.1</a></td>
      <td class="plain">First alignment-free server for in silico prediction of allergens based on physicochemical properties of proteins, achieving 94% sensitivity in allergen prediction</td>
      <td><a href="https://ddg-pharmfac.net/allertop/cite/">https://ddg-pharmfac.net/allertop/cite/</a></td>
      <td><a href="https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-14-S6-S4">https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-14-S6-S4</a></td>
      <td class="plain">Structural Analysis, Drug Design, Allergenicity Assessment, Allergen Identification</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://research.foodallergy.org/#_ga=2.222605656.279038653.1759159933-230927819.1759159933">FARE Food Allergy Research</a></td>
      <td class="plain">The Data Coordinating Center will support critical FARE Clinical Network activities for the design, development, execution, monitoring, and analysis of translational research.</td>
      <td><a href="https://research.foodallergy.org/#_ga=2.222605656.279038653.1759159933-230927819.1759159933">https://research.foodallergy.org/#_ga=2.222605656.279038653.1759159933-230927819.1759159933</a></td>
      <td class="plain"></td>
      <td class="plain">Risk Stratification, Severity Assessment, Symptom Analysis, Treatment Planning</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/27542726/">Allergy dataset</a></td>
      <td class="plain">Dataset supporting the conclusions for article: &quot;The epidemiologic characteristics of healthcare provider-diagnosed eczema, asthma, allergic rhinitis, and food allergy in children: a retrospective cohort study&quot; by Hill et al.</td>
      <td><a href="https://zenodo.org/records/44529">https://zenodo.org/records/44529</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/27542726/">https://pubmed.ncbi.nlm.nih.gov/27542726/</a></td>
      <td class="plain">Risk Stratification, Ingredient Analysis, Treatment Planning, Product Development, Genetic Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.jacionline.org/article/S0091-6749(04)03615-2/fulltext">Allergome</a></td>
      <td class="plain">A comprehensive, curated platform documenting allergenic molecules and their sources across all taxa and exposure routes, with monographs, literature integration, and tools tailored for clinicians and researchers in allergy and immunology.</td>
      <td><a href="https://www.allergome.org/">https://www.allergome.org/</a></td>
      <td><a href="https://www.jacionline.org/article/S0091-6749(04)03615-2/fulltext">https://www.jacionline.org/article/S0091-6749(04)03615-2/fulltext</a></td>
      <td class="plain">Allergenicity Assessment, Drug Design, Allergen Identification</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2639349/">GWAS Database</a></td>
      <td class="plain">The NHGRI-EBI GWAS Catalog is a curated, standardized repository of human genome-wide association study results, offering hundreds of thousands of variant–trait associations and tens of thousands of full summary-statistics datasets suitable for downstream analyses like meta-analysis and fine-mapping. Because it indexes GWAS signals across many immune and barrier-function traits and includes loci implicated in food allergy (e.g., HLA, FLG, SERPINB cluster), it is directly usable to query, aggregate, and reanalyze genetic associations relevant to food allergies and specific allergens such as peanut</td>
      <td><a href="https://www.ebi.ac.uk/gwas/">https://www.ebi.ac.uk/gwas/</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2639349/">https://pmc.ncbi.nlm.nih.gov/articles/PMC2639349/</a></td>
      <td class="plain">Ingredient Analysis, Product Development</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://comparefasta.comparedatabase.org/">COMPARE</a></td>
      <td class="plain">The COMPARE database provides an annually updated, peer-reviewed collection of clinically relevant protein sequences of allergens, along with tools for aligning and assessing the allergenic potential of novel proteins based on established regulatory guidelines</td>
      <td><a href="https://comparefasta.comparedatabase.org/">https://comparefasta.comparedatabase.org/</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Cross-Reactivity Modeling, Allergenicity Assessment, Epitope Mapping, Risk Stratification, Ingredient Analysis, Target Interaction, Severity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://world.openfoodfacts.org/data">Open Food Facts</a></td>
      <td class="plain">The Open Food Facts database is a large, publicly accessible collection of detailed product information including ingredients, nutrition, and labeling, available in multiple data formats with open licenses for broad reuse in food transparency and research.This dataset mainly supports food-related analyses including allergen detection, labeling validation, chemical and nutritional content analysis, and research into hypoallergenic or alternative food products</td>
      <td><a href="https://world.openfoodfacts.org/data">https://world.openfoodfacts.org/data</a></td>
      <td class="plain"></td>
      <td class="plain">Ingredient Analysis, Labeling Compliance, Property Prediction, Treatment Planning, Product Development, Alternative Ingredients</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3042621">IEDB (Immune Epitope Database)</a></td>
      <td class="plain">Comprehensive database containing over 1.6 million immune epitopes including antibody and T cell epitopes for allergens, with analysis and prediction tools</td>
      <td><a href="https://www.iedb.org/">https://www.iedb.org/</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3042621">https://pmc.ncbi.nlm.nih.gov/articles/PMC3042621</a></td>
      <td class="plain">Epitope Mapping, Target Interaction, Drug Design, Product Development</td>
    </tr>
  </tbody>
</table>

## Food Product Development & Safety

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="https://link.springer.com/article/10.1007/s12161-022-02353-9">Allergen30</a></td>
      <td class="plain">More than 6,000 images of 30 commonly used food items which can cause an adverse reaction within a human body. The goal is building a robust detection model that can assist people in avoiding possible allergic reactions.</td>
      <td><a href="https://universe.roboflow.com/allergen30/food_new-uuulf">https://universe.roboflow.com/allergen30/food_new-uuulf</a></td>
      <td><a href="https://link.springer.com/article/10.1007/s12161-022-02353-9">https://link.springer.com/article/10.1007/s12161-022-02353-9</a></td>
      <td class="plain">Ingredient Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/boltcutters/food-allergens-and-allergies">Food: allergen and allergy</a></td>
      <td class="plain">A comprehensive list of food items with their corresponding allergies.</td>
      <td><a href="https://www.kaggle.com/datasets/boltcutters/food-allergens-and-allergies">https://www.kaggle.com/datasets/boltcutters/food-allergens-and-allergies</a></td>
      <td class="plain"></td>
      <td class="plain">Ingredient Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens/">Food Ingredients and Allergens</a></td>
      <td class="plain">The Food Allergens Dataset is a collection of information regarding allergens present in various food items. The dataset contains allergen information for a range of food ingredients, enabling the identification and analysis of potential allergens in different dishes and products. It serves as a valuable resource for researchers, food manufacturers, healthcare professionals, and individuals with food allergies.</td>
      <td><a href="https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens/">https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens/</a></td>
      <td class="plain"></td>
      <td class="plain">Ingredient Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8075505/">AllergyMap</a></td>
      <td class="plain">A corpus that maps free-text allergy mentions (medications, foods, etc.) in EHRs to standard terminologies (SNOMED, etc.)</td>
      <td><a href="https://github.com/amywangmd/AllergyMap">https://github.com/amywangmd/AllergyMap</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8075505/">https://pmc.ncbi.nlm.nih.gov/articles/PMC8075505/</a></td>
      <td class="plain">Text Mining</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/nandhanasuresh/allergen-status-of-food-products">Allergen Status of Food Products</a></td>
      <td class="plain">This dataset contains allergen status information for 400 food products, detailing ingredients, allergens present, pricing, and customer ratings, enabling allergen detection and analysis for researchers, manufacturers, and consumers</td>
      <td><a href="https://www.kaggle.com/datasets/nandhanasuresh/allergen-status-of-food-products">https://www.kaggle.com/datasets/nandhanasuresh/allergen-status-of-food-products</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Ingredient Analysis, Labeling Compliance, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/khochawongwat/ingredients-with-17-allergen-tags">Ingredients with 16 Allergen Tags</a></td>
      <td class="plain">This dataset lists 10,000 USDA ingredients, each tagged with 16 common allergen labels such as dairy, eggs, peanuts, gluten, and shellfish, with annotations indicating certainty or uncertainty of allergen presence.</td>
      <td><a href="https://www.kaggle.com/datasets/khochawongwat/ingredients-with-17-allergen-tags">https://www.kaggle.com/datasets/khochawongwat/ingredients-with-17-allergen-tags</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Ingredient Analysis, Allergenicity Assessment</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens">Food Ingredients and Allergens</a></td>
      <td class="plain">This Food Allergens dataset contains 400 records detailing food products, their ingredients, associated allergens, and allergen presence prediction, supporting allergen detection and analysis for diverse applications.</td>
      <td><a href="https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens">https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Ingredient Analysis, Allergenicity Assessment, Text Mining</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/26450949/">ProPepper</a></td>
      <td class="plain">ProPepper is a database of cereal prolamin epitopes, peptides and proteins for expert users that are dealing with protein chemistry, proteomics and mass spectrometry, method developments and related applications in food science, agricultural breeding or medical studies.</td>
      <td><a href="https://ngdc.cncb.ac.cn/databasecommons/database/id/1686">https://ngdc.cncb.ac.cn/databasecommons/database/id/1686</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/26450949/">https://pubmed.ncbi.nlm.nih.gov/26450949/</a></td>
      <td class="plain">Ingredient Analysis, Product Development</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.allergenpeptidebrowser.org/">Allergen Peptide Browser</a></td>
      <td class="plain">Allergen Detection using Mass Spectrometry (MS)</td>
      <td><a href="https://www.allergenpeptidebrowser.org/">https://www.allergenpeptidebrowser.org/</a></td>
      <td class="plain"></td>
      <td class="plain">Ingredient Analysis, Product Development</td>
    </tr>
  </tbody>
</table>

## Patient Management & Clinical Decision Support

<table>
  <thead>
    <tr>
      <th class="name">Name</th>
      <th class="description">Description</th>
      <th class="source">Source</th>
      <th class="license">License</th>
      <th class="tags">Tags</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#e6ffea">
      <td><a href="https://datahub.io/@RuthvikUppala30/US-food-allergy-dataset">Food Allergy &amp; Intolerance Dataset</a></td>
      <td class="plain">This dataset contains data related to food allergies and intolerances. It includes key features such as age, gender, symptoms, food type consumed, IgE levels, and allergy history, helping in predictive modeling for food allergy detection and reaction severity assessment.</td>
      <td><a href="https://datahub.io/@RuthvikUppala30/US-food-allergy-dataset">https://datahub.io/@RuthvikUppala30/US-food-allergy-dataset</a></td>
      <td class="plain"></td>
      <td class="plain">Severity Assessment, Risk Stratification</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6361419/">DIABIMMUNE</a></td>
      <td class="plain">The DIABIMMUNE three-country cohort dataset tracks infants from Finland, Estonia, and Russia with similar HLA genetic risk for type 1 diabetes, collecting comprehensive longitudinal data including monthly stool microbiome sequencing (16S rRNA and whole-genome shotgun), clinical records, and lifestyle factors. It investigates the role of gut microbiome variations and early immune education in allergy and autoimmune disease development, providing valuable data to explore microbial and genetic influences on immune-related conditions</td>
      <td><a href="https://diabimmune.broadinstitute.org/diabimmune/three-country-cohort">https://diabimmune.broadinstitute.org/diabimmune/three-country-cohort</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6361419/">https://pmc.ncbi.nlm.nih.gov/articles/PMC6361419/</a></td>
      <td class="plain">Microbiome Analysis, Genetic Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.kaggle.com/datasets/fda/adverse-food-events">CFSAN Adverse Event Reporting System (CAERS)</a></td>
      <td class="plain">The CFSAN Adverse Event Reporting System (CAERS) dataset contains approximately 90,000 reports of adverse events related to foods, dietary supplements, and cosmetics submitted to the FDA from 2004 to 2017. It includes detailed data on food products suspected in adverse reactions and associated symptoms, supporting analysis of patient risk factors, symptoms classification, and identification of allergenic ingredients in food products</td>
      <td><a href="https://www.kaggle.com/datasets/fda/adverse-food-events">https://www.kaggle.com/datasets/fda/adverse-food-events</a></td>
      <td class="plain"></td>
      <td class="plain">Risk Stratification, Symptom Analysis, Ingredient Analysis</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/25678091/">DNA Methilation GSE59999</a></td>
      <td class="plain">Genome wide DNA methylation profiling study of PBMC from 71 unique primary patient blood samples. The Illumina Human Methylation 450k array was used. 29 challenge proven food allergy, 29 sensitized but oral tolerant, 13 non food allergics Mixture of food allergy phenotypes (egg allergic (15), peanut allergic (14)), food sensitization phenotypes (egg sensitized (14), peanut sensitized (15)). 4 samples had technical replicate hybridzations. From &quot;Blood DNA methylation biomarkers predict clinical reactivity in food-sensitized infants&quot;</td>
      <td><a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59999">https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE59999</a></td>
      <td><a href="https://pubmed.ncbi.nlm.nih.gov/25678091/">https://pubmed.ncbi.nlm.nih.gov/25678091/</a></td>
      <td class="plain">Risk Stratification</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://www.nature.com/articles/s41597-022-01861-x#Sec6">HealthNuts Study</a></td>
      <td class="plain">Mass citometry data from 36 participants encompassing non-allergic, peanut sensitized with tolerance, and clinically peanut allergic infants</td>
      <td><a href="https://www.immport.org/shared/search?text=SDY2015">https://www.immport.org/shared/search?text=SDY2015</a></td>
      <td><a href="https://www.nature.com/articles/s41597-022-01861-x#Sec6">https://www.nature.com/articles/s41597-022-01861-x#Sec6</a></td>
      <td class="plain">Risk Stratification</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7923212/#notes5">Dysfunctional Gut Microbiome Networks in Childhood IgE-Mediated Food Allergy</a></td>
      <td class="plain">To identify potential target microbes, which may play a key role in regulating/ influencing the microbe-microbe interactions, leading to the onset of food allergy. 16S rRNA, 33 allergic vs 27 controls</td>
      <td><a href="https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA699997">https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA699997</a></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7923212/#notes5">https://pmc.ncbi.nlm.nih.gov/articles/PMC7923212/#notes5</a></td>
      <td class="plain">Risk Stratification</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4954633/">PEAR – Partners’ Enterprise-wide Allergy Repository (Food entries subset)</a></td>
      <td class="plain">Allergy entries from EHRs across a health system, with food terms extracted and normalized (approx. 158,552 food allergen records).</td>
      <td class="plain"></td>
      <td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4954633/">https://pmc.ncbi.nlm.nih.gov/articles/PMC4954633/</a></td>
      <td class="plain">Risk Stratification</td>
    </tr>
    <tr style="background-color:#f7d6d6">
      <td><a href="https://www.nal.usda.gov/research-tools/food-safety-research-projects/allergen-database-service">FSA Allergen Database Service (UK Nut allergy Registry)</a></td>
      <td class="plain">Clinical and laboratory data from patients attending a UK allergy clinic for suspected nut allergy, including reaction history, severity, and lab tests.</td>
      <td><a href="https://www.nal.usda.gov/research-tools/food-safety-research-projects/allergen-database-service">https://www.nal.usda.gov/research-tools/food-safety-research-projects/allergen-database-service</a></td>
      <td class="plain"></td>
      <td class="plain">Risk Stratification</td>
    </tr>
    <tr style="background-color:#e6ffea">
      <td><a href="https://github.com/foodopendata/food-allergens-ch">Swiss legislation on food allergens data</a></td>
      <td class="plain">This dataset is a German-language, hand-curated list of common food allergens based on Swiss legislation, compiled to support allergen identification and text matching for developers and researchers, with a focus on enabling structured, multilingual allergen data relevant to Switzerland</td>
      <td><a href="https://github.com/foodopendata/food-allergens-ch">https://github.com/foodopendata/food-allergens-ch</a></td>
      <td class="plain"></td>
      <td class="plain">Allergen Identification, Ingredient Analysis, Labeling Compliance, Text Mining, Risk Stratification</td>
    </tr>
  </tbody>
</table>
