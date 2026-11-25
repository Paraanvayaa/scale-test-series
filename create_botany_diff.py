# -*- coding: utf-8 -*-
"""
Script to generate engine/neet_engine/curriculum_botany_diff.py
Tier 3: Difficult / 2026-2027 Advanced Predicted Rigor
Botany Curriculum (50 Questions)
"""

code = '''# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Difficult Curriculum (Botany)
Strictly calibrated to NTA NEET-UG standards (2023-2027 Predictive Rigor).
Difficult conceptual and analytical depth: fine-grained NCERT line distinction,
biochemical pathways (C2, C3, C4, CAM, ETS), molecular genetics enzymes,
linkage and recombination calculations, cell cycle checkpoints, and ecological math.
Strictly NCERT-aligned.

Proportions for 50 Questions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_botany_questions_diff(mock_num):
    questions = []
    shift = (mock_num - 41) * 3

    topics_data = [
        # 1. Molecular Biology - Eukaryotic RNA Polymerases (Match List)
        ("Molecular Basis of Inheritance", "Eukaryotic RNA Polymerase Specificities and Transcripts", "Match List",
         "Match List-I with List-II for eukaryotic RNA polymerases and their specific catalytic transcripts:\\n\\n"
         "| List-I (RNA Polymerase) | List-II (Synthesized RNA Species) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** RNA Polymerase I | **I.** $28\\\\text{S}$, $18\\\\text{S}$, and $5.8\\\\text{S}$ rRNAs |\\n"
         "| **B.** RNA Polymerase II | **II.** Heterogeneous nuclear RNA (hnRNA, precursor of mRNA) |\\n"
         "| **C.** RNA Polymerase III | **III.** tRNA, $5\\\\text{S}$ rRNA, and snRNAs |\\n"
         "| **D.** Prokaryotic RNA Polymerase | **IV.** Single core enzyme synthesizing all types of cellular RNAs |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. RNA Polymerase I transcribes ribosomal RNAs ($28\\\\text{S}$, $18\\\\text{S}$, and $5.8\\\\text{S}$) inside the nucleolus $\\\\to$ I.\\n2. RNA Polymerase II transcribes the precursor of mRNA, termed heterogeneous nuclear RNA (hnRNA) $\\\\to$ II.\\n3. RNA Polymerase III transcribes tRNA, small $5\\\\text{S}$ rRNA, and snRNAs (small nuclear RNAs involved in splicing) $\\\\to$ III.\\n4. In bacteria, a single DNA-dependent RNA polymerase core enzyme catalyzes transcription of all three types of RNA (mRNA, tRNA, rRNA) $\\\\to$ IV.",
         "Confusing $5\\\\text{S}$ rRNA (transcribed by Pol III) with other rRNAs ($28\\\\text{S}$, $18\\\\text{S}$, $5.8\\\\text{S}$ transcribed by Pol I).",
         "$5\\\\text{S}$ rRNA is synthesized by RNA Polymerase III, while $28\\\\text{S}$, $18\\\\text{S}$, and $5.8\\\\text{S}$ are synthesized by RNA Polymerase I."),

        # 2. Molecular Biology - Lac Operon Mutations
        ("Molecular Basis of Inheritance", "Lac Operon Operator-Constitutive and Repressor Mutations", "Direct MCQ",
         "In an E. coli mutant strain, a mutation in the operator region ($O^c$) prevents the lac repressor protein from binding to it. In the complete absence of lactose (inducer) in the growth medium, the structural genes of the lac operon will:",
         ["Be expressed constitutively at high levels",
          "Be permanently repressed and completely silent",
          "Be transcribed only upon adding glucose",
          "Undergo immediate RNA interference degradation"], 0,
         "1. The operator locus ($O$) is the physical binding site for the active repressor protein produced by the regulator gene ($i$).\\n2. In an operator-constitutive mutant ($O^c$), the operator DNA sequence is altered such that the repressor can no longer recognize or bind to it.\\n3. Without repressor binding, RNA polymerase is never physically blocked from moving along the DNA from the promoter.\\n4. Consequently, transcription of $z, y, a$ structural genes proceeds continuously (constitutively) regardless of whether lactose is present or absent.",
         "Assuming the operon stays permanently repressed is true for super-repressor ($I^s$) mutants, not operator-constitutive ($O^c$) mutants.",
         "$O^c$ (operator-constitutive) mutants cause continuous transcription of lac structural genes even in the absence of inducer."),

        # 3. Molecular Biology - Genetic Code Degeneracy (Statement I & II)
        ("Molecular Basis of Inheritance", "Degeneracy vs Ambiguity of the Genetic Code", "Statement I & II",
         "Given below are two statements regarding the characteristics of the genetic code:\\n\\n"
         "Statement I: The genetic code is degenerate because most amino acids are coded by more than one triplet codon.\\n\\n"
         "Statement II: The genetic code is unambiguous because one specific triplet codon never codes for more than one amino acid.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. There are 64 codons: 3 are stop/nonsense codons ($UAA, UAG, UGA$), leaving 61 codons specifying 20 amino acids. Except for methionine ($AUG$) and tryptophan ($UGG$), all amino acids have 2 to 6 alternative codons. This property is defined as degeneracy. Statement I is correct.\\n2. Unambiguous (or specific) means each codon specifies one and only one amino acid with zero ambiguity (e.g. $UUU$ specifies phenylalanine and nothing else). Statement II is correct.",
         "Confusing 'degenerate' (multiple codons $\\\\to$ one amino acid) with 'unambiguous' (one codon $\\\\to$ strictly one amino acid).",
         "Degenerate = multiple codons for one amino acid; Unambiguous = one codon specifies strictly one amino acid."),

        # 4. Photosynthesis - Cyclic vs Non-cyclic (Assertion & Reason)
        ("Photosynthesis in Higher Plants", "Stroma Lamellae Absence of PS II and NADP Reductase", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): Stroma lamellae thylakoids perform only cyclic photophosphorylation, producing ATP but no $\\\\text{NADPH} + \\\\text{H}^+$.\\n"
         "Reason (R): Stroma lamellae membranes lack Photosystem II (PS II) and the enzyme NADP reductase.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Cyclic photophosphorylation involves only PS I, where excited electrons from $P_{700}$ cycle through the electron transport chain back to $P_{700}$, driving proton pumping and ATP synthesis without generating NADPH or evolving $O_2$. Assertion is TRUE.\\n2. Granum thylakoids have both PS I and PS II. Stroma lamellae membranes, however, lack both PS II and the NADP reductase enzyme on their stroma-facing surface. Without PS II, water splitting cannot occur; without NADP reductase, electrons cannot be transferred to $\\\\text{NADP}^+$. Thus only cyclic flow can operate. Reason is TRUE and explains Assertion.",
         "Students often know cyclic produces only ATP, but forget the exact enzyme and photosystem deficiencies of stroma lamellae.",
         "Stroma lamellae lack PS II and NADP reductase, restricting electron flow to cyclic photophosphorylation."),

        # 5. Photosynthesis - C4 Pathway Compartmentalization
        ("Photosynthesis in Higher Plants", "Kranz Anatomy and Enzyme Compartmentalization in C4 Plants", "Direct MCQ",
         "In $C_4$ plants (such as maize and sugarcane), initial carbon dioxide fixation and the primary carboxylation reaction take place in:",
         ["Mesophyll cells catalyzed by PEP carboxylase",
          "Bundle sheath cells catalyzed by RuBisCO",
          "Mesophyll cells catalyzed by RuBisCO",
          "Bundle sheath cells catalyzed by PEP carboxylase"], 0,
         "1. $C_4$ plants possess Kranz anatomy with two distinct photosynthetic cell types: mesophyll cells and bundle sheath cells.\\n2. In mesophyll cells, the primary $CO_2$ acceptor is phosphoenolpyruvate (PEP, a 3-carbon molecule). The enzyme PEP carboxylase (PEPcase) fixes atmospheric $CO_2$ (as $HCO_3^-$) to form 4-carbon oxaloacetic acid (OAA).\\n3. PEPcase has very high affinity for $CO_2$ and completely lacks oxygenase activity, functioning efficiently even at low $CO_2$ concentrations.\\n4. RuBisCO is absent in mesophyll cells and is located exclusively in the bundle sheath cells, where decarboxylation of malate raises $CO_2$ concentration to prevent photorespiration.",
         "Bundle sheath cells contain RuBisCO, not PEP carboxylase; mesophyll cells contain PEPcase.",
         "Initial $CO_2$ fixation in $C_4$ plants occurs in mesophyll cells via PEP carboxylase; Calvin cycle occurs in bundle sheath cells via RuBisCO."),

        # 6. Photosynthesis - Photorespiration Wastefulness
        ("Photosynthesis in Higher Plants", "Photorespiration (C2 Cycle) Cellular Organelles and Products", "Direct MCQ",
         "During photorespiration in $C_3$ plants, when RuBisCO functions as an oxygenase by binding $O_2$, the 5-carbon compound RuBP is split into:",
         ["One molecule of 3-PGA ($3C$) and one molecule of 2-phosphoglycolate ($2C$)",
          "Two molecules of 3-phosphoglycerate ($3C$ each)",
          "One molecule of dihydroxyacetone phosphate and one molecule of pyruvate",
          "Two molecules of 2-phosphoglycolate ($2C$ each)"], 0,
         "1. RuBisCO has an active site that can bind both $CO_2$ and $O_2$ competitively.\\n2. When $O_2$ concentration is high or temperature rises, oxygenase activity prevails:\\n   $$\\\\text{RuBP}(5C) + O_2 \\\\xrightarrow{\\\\text{RuBisCO}} \\\\text{3-PGA}(3C) + \\\\text{2-phosphoglycolate}(2C)$$.\\n3. 2-Phosphoglycolate is converted to glycolate and enters the $C_2$ photorespiratory cycle across chloroplast, peroxisome, and mitochondria.\\n4. In mitochondria, two molecules of glycine ($2C$ each) release one $CO_2$ and one $NH_3$ to form serine ($3C$).\\n5. No ATP or NADPH is synthesized; in fact, ATP is consumed, making photorespiration a wasteful process.",
         "In standard carboxylation, RuBP binds $CO_2$ to form two molecules of 3-PGA; oxygenation yields only ONE 3-PGA and ONE 2-phosphoglycolate.",
         "RuBisCO oxygenase reaction: $\\\\text{RuBP} + O_2 \\\\to \\\\text{3-PGA} (3C) + \\\\text{2-phosphoglycolate} (2C)$."),

        # 7. Respiration - ETS Complexes and Mobile Carriers
        ("Respiration in Plants", "Mitochondrial Electron Transport System Complex Components", "Match List",
         "Match List-I with List-II for the respiratory electron transport chain complexes located in the inner mitochondrial membrane:\\n\\n"
         "| List-I (ETS Complex) | List-II (Biochemical Identification / Function) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Complex I | **I.** NADH dehydrogenase (oxidizes NADH and pumps $4H^+$) |\\n"
         "| **B.** Complex II | **II.** Succinate dehydrogenase (FADH$_2$ oxidation, no $H^+$ pumping) |\\n"
         "| **C.** Complex III | **III.** Cytochrome $bc_1$ complex (transfers electrons to mobile cyt $c$) |\\n"
         "| **D.** Complex IV | **IV.** Cytochrome $c$ oxidase (contains cyts $a, a_3$ and two copper centres) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Complex I: NADH:ubiquinone oxidoreductase (NADH dehydrogenase) contains FMN and Fe-S centres $\\\\to$ I.\\n2. Complex II: Succinate dehydrogenase transfers electrons from succinate to ubiquinone via $FADH_2$ without pumping protons across inner membrane $\\\\to$ II.\\n3. Complex III: Cytochrome $bc_1$ complex transfers electrons from ubiquinol ($UQH_2$) to small mobile protein cytochrome $c$ $\\\\to$ III.\\n4. Complex IV: Cytochrome $c$ oxidase contains cyts $a$ and $a_3$ and two copper centers ($Cu_A, Cu_B$), reducing molecular oxygen to water ($2H^+ + \\\\frac{1}{2}O_2 + 2e^- \\\\to H_2O$) $\\\\to$ IV.",
         "Distractors swap Complex II (succinate dehydrogenase) with Complex I (NADH dehydrogenase).",
         "Cytochrome $c$ is a small mobile protein attached to the outer surface of the inner mitochondrial membrane."),

        # 8. Respiration - Respiratory Quotient (RQ)
        ("Respiration in Plants", "Respiratory Quotient of Different Respiratory Substrates", "Direct MCQ",
         "The Respiratory Quotient ($RQ = \\\\text{Volume of } CO_2 \\\\text{ evolved} / \\\\text{Volume of } O_2 \\\\text{ consumed}$) for carbohydrates, tripalmitin (fat), and proteins are respectively:",
         ["$1.0$, $0.7$, and $0.9$",
          "$0.7$, $1.0$, and $0.9$",
          "$1.0$, $0.9$, and $0.7$",
          "$0.9$, $0.7$, and $1.0$"], 0,
         "1. For carbohydrates (e.g. glucose):\\n   $$C_6H_{12}O_6 + 6O_2 \\\\to 6CO_2 + 6H_2O \\\\implies RQ = 6/6 = 1.0$.\\n2. For fats (e.g. tripalmitin):\\n   $$2(C_{51}H_{98}O_6) + 145O_2 \\\\to 102CO_2 + 98H_2O \\\\implies RQ = 102/145 = 0.7$.\\n3. For proteins: $RQ \\\\approx 0.9$ (fats and proteins contain less oxygen in their molecules, requiring more $O_2$ for oxidation).\\n4. Note: for organic acids (malic acid), $RQ > 1.0$; for anaerobic respiration, $RQ = \\\\infty$.",
         "Fats have lower oxygen content than carbohydrates, so their RQ is always less than 1 (0.7).",
         "RQ values: Carbohydrates = 1.0; Fats (tripalmitin) = 0.7; Proteins = 0.9; Organic acids > 1.0."),

        # 9. Plant Growth Regulators - Cytokinins & Apical Dominance
        ("Plant Growth and Development", "Antagonistic Actions of Auxins and Cytokinins", "Direct MCQ",
         "In decapitated tea plantations, lateral branching and bushy growth are promoted by removing the shoot apical bud. Which plant growth regulator can be applied externally to overcome apical dominance without removing the shoot apex?",
         ["Cytokinin", "Auxin (IAA)", "Abscisic acid (ABA)", "Gibberellic acid (GA$_3$)"], 0,
         "1. Apical dominance is caused by auxins synthesized at the shoot apex which translocate basipetally and inhibit the outgrowth of lateral (axillary) buds.\\n2. Cytokinins synthesized in roots translocate acropetally and act antagonistically to auxins by stimulating lateral bud outgrowth and cell division.\\n3. Direct application of cytokinin to lateral buds overrides the auxin inhibition, causing lateral shoots to develop even with an intact shoot apex.\\n4. Cytokinins also delay leaf senescence (Richmond-Lang effect) by mobilizing nutrients.",
         "Applying auxin reinforces apical dominance; applying gibberellin promotes stem elongation, not bushy branching.",
         "Auxin promotes apical dominance; Cytokinin overcomes apical dominance and stimulates lateral shoot branching."),

        # 10. Plant Growth - Photoperiodism and Florigen (Statement I & II)
        ("Plant Growth and Development", "Photoperiodism Site of Perception and Florigen Movement", "Statement I & II",
         "Given below are two statements regarding photoperiodism in flowering plants:\\n\\n"
         "Statement I: The site of perception of light/dark duration for photoperiodic floral induction is the mature leaf blade, not the shoot apex.\\n\\n"
         "Statement II: The hypothetical flowering hormone (florigen), now identified as the FT protein, is synthesized in leaves and translocates via the phloem to the shoot apical meristem to trigger flowering.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Experiments demonstrate that even if a plant is kept under non-inductive photoperiods, exposing a single leaf to the critical inductive photoperiod is sufficient to induce flowering. The site of light perception is strictly the leaf. Statement I is correct.\\n2. Chailakhyan demonstrated that a floral stimulus moves from induced leaves to the shoot apex. Modern molecular biology identified this stimulus as Flowering Locus T (FT) protein, which travels through phloem sieve tubes to the shoot apical meristem, reprogramming it from vegetative to floral development. Statement II is correct.",
         "Assuming the shoot apical meristem perceives the photoperiod directly is a common misconception.",
         "Leaves perceive photoperiodic signals; florigen translocates via phloem to the shoot apical meristem to induce flowering."),

        # 11. Genetics - Dihybrid Recombination Frequencies
        ("Principles of Inheritance and Variation", "Morgan Drosophila Recombination Frequency Distance", "Direct MCQ",
         "In Thomas Hunt Morgan\\'s dihybrid cross experiments on Drosophila melanogaster, the genes for yellow body ($y$) and white eyes ($w$) showed $1.3\\\\%$ recombination, while the genes for white eyes ($w$) and miniature wings ($m$) showed $37.2\\\\%$ recombination. What is the genetic map distance between the yellow body gene and the white eye gene on the X-chromosome?",
         ["$1.3\\\\text{ map units (centiMorgans)}$", "$37.2\\\\text{ map units}$", "$35.9\\\\text{ map units}$", "$0.65\\\\text{ map units}$"], 0,
         "1. Alfred Sturtevant, a student of Morgan, used the frequency of recombination between gene pairs on the same chromosome as a measure of the physical distance between genes.\\n2. By definition: $1\\\\%\\\\text{ recombination} = 1\\\\text{ map unit} = 1\\\\text{ centiMorgan (cM)}$.\\n3. Given recombination frequency between yellow body and white eyes $= 1.3\\\\%$, the genetic distance is directly $1.3\\\\text{ cM}$ (or $1.3\\\\text{ map units}$).\\n4. Genes close together on a chromosome exhibit tight linkage and low recombination (e.g. $1.3\\\\%$); genes located farther apart exhibit loose linkage and high recombination (e.g. $37.2\\\\%$).",
         "Recombination frequency directly equals map units: 1.3% = 1.3 cM (no conversion formula needed).",
         "$1\\\\%$ recombination frequency is defined as $1\\\\text{ map unit}$ ($1\\\\text{ cM}$) on genetic linkage maps."),

        # 12. Genetics - Polygenic Inheritance Bell Curve
        ("Principles of Inheritance and Variation", "Polygenic Inheritance Bell-shaped Phenotypic Distribution", "Direct MCQ",
         "In human skin color inheritance controlled by three polygenic genes ($A, B, C$) with additive cumulative alleles, what is the fraction of individuals in the $F_2$ generation that possess the extreme darkest skin phenotype ($AABBCC$)?",
         ["$1 / 64$", "$6 / 64$", "$15 / 64$", "$20 / 64$"], 0,
         "1. Three genes with 2 alleles each: $F_1$ trihybrid is $AaBbCc$.\\n2. Total possible combinations in $F_2$ generation $= 4^3 = 64$ offspring.\\n3. Number of dominant alleles ranges from 0 to 6:\\n   $6$ dominant alleles ($AABBCC$): $1 / 64$ (extreme darkest),\\n   $5$ dominant alleles: $6 / 64$,\\n   $4$ dominant alleles: $15 / 64$,\\n   $3$ dominant alleles: $20 / 64$ (intermediate mulatto, most frequent),\\n   $2$ dominant alleles: $15 / 64$,\\n   $1$ dominant allele: $6 / 64$,\\n   $0$ dominant alleles ($aabbcc$): $1 / 64$ (extreme lightest/albino).\\n4. The proportion of extreme darkest phenotype is $1/64$.",
         "20/64 represents the intermediate (mulatto) phenotype with 3 dominant alleles.",
         "Polygenic inheritance with 3 genes produces a bell curve with distribution $1:6:15:20:15:6:1$ out of 64."),

        # 13. Cell Cycle - Checkpoint Regulation (Multi-Statement)
        ("Cell Cycle and Cell Division", "Cyclin-CDKs and Checkpoint Control Mechanisms", "Multi-Statement",
         "Consider the regulation of the eukaryotic cell cycle and its checkpoints:\\n\\n"
         "A. The $G_1/S$ checkpoint (restriction point) is the major decision point where the cell determines whether to enter the synthesis phase or withdraw into the quiescent $G_0$ state.\\n"
         "B. Progression through cell cycle checkpoints is driven by cyclin-dependent kinases (CDKs) which are activated by binding to specific regulatory cyclin proteins.\\n"
         "C. The spindle assembly checkpoint (M checkpoint) ensures that all chromosomes are properly attached to kinetochore microtubules before anaphase onset.\\n"
         "D. DNA replication during $S$ phase occurs without any centrosome duplication.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. The $G_1/S$ checkpoint assesses cell size, nutrients, and DNA integrity; once past this point, the cell is committed to divide. Statement A is TRUE.\\n2. CDKs require association with cyclins ($G_1$ cyclins, S cyclins, M cyclins) for kinase catalytic activity. Statement B is TRUE.\\n3. M checkpoint prevents premature anaphase until all kinetochores are under bipolar tension on spindle fibers (mediated by APC/C). Statement C is TRUE.\\n4. In animal cells, while DNA replicates in the nucleus during $S$ phase, the centrosome duplicates simultaneously in the cytoplasm. Statement D is FALSE.",
         "Centrosome duplication occurs during S phase in the cytoplasm concurrently with nuclear DNA replication.",
         "Major checkpoints: $G_1/S$ (commitment), $G_2/M$ (replication completion), and M (spindle kinetochore attachment)."),

        # 14. Cell Division - Meiosis Prophase I Sub-stages (Match List)
        ("Cell Cycle and Cell Division", "Sequential Events of Meiotic Prophase I Sub-stages", "Match List",
         "Match List-I with List-II for the distinctive morphological events occurring during sub-stages of meiotic Prophase I:\\n\\n"
         "| List-I (Prophase I Stage) | List-II (Key Diagnostic Cytological Event) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Leptotene | **I.** Compaction of chromosomes; bouquet stage |\\n"
         "| **B.** Zygotene | **II.** Synaptonemal complex formation; synapsis of homologous pairs |\\n"
         "| **C.** Pachytene | **III.** Crossing over mediated by enzyme recombinase; tetrads visible |\\n"
         "| **D.** Diplotene | **IV.** Dissolution of synaptonemal complex; chiasmata appearance |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Leptotene: chromosomes condense and become visible under light microscopy $\\\\to$ I.\\n2. Zygotene: homologous chromosomes pair up via synapsis with synaptonemal complex formation $\\\\to$ II.\\n3. Pachytene: recombination nodules appear where crossing over occurs between non-sister chromatids mediated by recombinase $\\\\to$ III.\\n4. Diplotene: synaptonemal complex dissolves, leaving X-shaped points of crossing over called chiasmata $\\\\to$ IV.\\n5. Diakinesis is characterized by terminalization of chiasmata.",
         "Distractors swap Pachytene (crossing over) with Diplotene (chiasmata appearance).",
         "Meiosis Prophase I order: Leptotene $\\\\to$ Zygotene (synapsis) $\\\\to$ Pachytene (crossing over) $\\\\to$ Diplotene (chiasmata) $\\\\to$ Diakinesis (terminalization)."),

        # 15. Anatomy of Flowering Plants - Secondary Growth in Dicot Stem
        ("Anatomy of Flowering Plants", "Spring Wood vs Autumn Wood and Annual Rings", "Direct MCQ",
         "In a mature temperate dicot tree trunk, spring wood (early wood) differs from autumn wood (late wood) in that spring wood:",
         ["Has wider xylem vessels with larger cavities and lower density",
          "Has narrow xylem vessels with thick walls and higher density",
          "Is formed when cambium is less active during winter months",
          "Is darker in color with significantly higher density"], 0,
         "1. In temperate regions, climatic conditions are not uniform throughout the year.\\n2. In spring, when the tree produces new foliage, the vascular cambium is highly active, producing a large number of xylary elements having wide vessels with broad lumens.\\n3. This early wood is lighter in color and has a lower physical density.\\n4. In autumn/winter, cambium activity slows down, producing fewer xylary elements with narrow vessels and thicker walls; this late wood is darker and denser.\\n5. An annual ring consists of one spring wood ring and one autumn wood ring, reflecting one year of seasonal growth.",
         "Spring wood has lower density and wider lumens; autumn wood has higher density and narrower vessels.",
         "Spring wood = active cambium, wide vessels, light color, low density; Autumn wood = narrow vessels, dark, high density."),

        # 16. Anatomy - Dicot vs Monocot Root (Statement I & II)
        ("Anatomy of Flowering Plants", "Diagnostic Structural Differences Between Dicot and Monocot Roots", "Statement I & II",
         "Given below are two statements regarding root anatomy:\\n\\n"
         "Statement I: Dicot roots typically possess 2 to 4 (diarch to tetrarch) xylem bundles and a small or inconspicuous central pith.\\n\\n"
         "Statement II: Monocot roots have polyarch condition (more than 6 xylem bundles) and a large, well-developed central pith, but undergo no secondary growth.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In dicot roots, the number of xylem and phloem patches is few (usually 2 to 4, rarely up to 6). The central pith is either absent or very small and reduced. Secondary growth occurs via vascular cambium and cork cambium. Statement I is correct.\\n2. In monocot roots, the number of xylem bundles is always numerous (polyarch, $>6$). The central pith is large, parenchymatous, and conspicuous. Monocot roots completely lack secondary growth because no secondary meristem forms. Statement II is correct.",
         "Confusing stem anatomy (monocot stem has scattered vascular bundles) with root anatomy (radial bundles).",
         "Dicot root = 2-4 xylem bundles, small pith; Monocot root = polyarch (>6) xylem bundles, large prominent pith."),

        # 17. Morphology - Floral Formula & Families (Match List)
        ("Morphology of Flowering Plants", "Diagnostic Floral Formulas of Major Angiosperm Families", "Match List",
         "Match List-I with List-II for family floral formulas and diagnostic floral features:\\n\\n"
         "| List-I (Family) | List-II (Diagnostic Floral Formula / Feature) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Fabaceae | **I.** $\% \\\\, \\\\text{K}_{(5)} \\\\, \\\\text{C}_{1+2+(2)} \\\\, \\\\text{A}_{(9)+1} \\\\, \\\\underline{\\\\text{G}}_1$ (Vexillary aestivation, diadelphous) |\\n"
         "| **B.** Solanaceae | **II.** $\\\\oplus \\\\, \\\\text{K}_{(5)} \\\\, \\\\text{C}_{(5)} \\\\, \\\\text{A}_5 \\\\, \\\\underline{\\\\text{G}}_{(2)}$ (Epipetalous stamens, oblique ovary) |\\n"
         "| **C.** Liliaceae | **III.** $\\\\oplus \\\\, \\\\text{P}_{(3+3)} \\\\, \\\\text{A}_{3+3} \\\\, \\\\underline{\\\\text{G}}_{(3)}$ (Tepals present, epiphyllous stamens) |\\n"
         "| **D.** Brassicaceae | **IV.** $\\\\oplus \\\\, \\\\text{K}_{2+2} \\\\, \\\\text{C}_4 \\\\, \\\\text{A}_{2+4} \\\\, \\\\underline{\\\\text{G}}_{(2)}$ (Cruciform corolla, tetradynamous stamens) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Fabaceae: zygomorphic ($\\%$), papilionaceous corolla ($1+2+(2)$), diadelphous stamens ($(9)+1$), monocarpellary superior ovary $\\\\to$ I.\\n2. Solanaceae: actinomorphic ($\\\\oplus$), bicarpellary syncarpous with obliquely placed swollen placenta and epipetalous stamens $\\\\to$ II.\\n3. Liliaceae: monocot family with perianth of 6 tepals ($3+3$), epiphyllous stamens ($3+3$), tricarpellary ovary $\\\\to$ III.\\n4. Brassicaceae (Mustard): cruciform corolla, tetradynamous stamens ($2$ outer short $+ 4$ inner long), bicarpellary with replum $\\\\to$ IV.",
         "Confusing epipetalous (stamens attached to petals in Solanaceae) with epiphyllous (stamens attached to tepals in Liliaceae).",
         "Fabaceae has diadelphous $(9)+1$ stamens; Solanaceae has epipetalous stamens; Liliaceae has epiphyllous perianth."),

        # 18. Morphology - Placentation Types (Match List)
        ("Morphology of Flowering Plants", "Types of Placentation and Representative Plant Examples", "Match List",
         "Match List-I with List-II for placentation patterns and their characteristic plant examples:\\n\\n"
         "| List-I (Placentation Type) | List-II (Representative Plant Example) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Marginal | **I.** Pea ($Pisum sativum$) |\\n"
         "| **B.** Axile | **II.** China rose, Tomato, Lemon |\\n"
         "| **C.** Parietal | **III.** Mustard, Argemone (with false septum / replum) |\\n"
         "| **D.** Free central | **IV.** Dianthus and Primrose (ovules on central axis, no septa) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-IV, B-II, C-III, D-I"], 0,
         "1. Marginal: placenta forms a ridge along ventral suture of ovary (Pea) $\\\\to$ I.\\n2. Axile: multilocular ovary with septa meeting at central axis (China rose, Tomato, Lemon) $\\\\to$ II.\\n3. Parietal: ovules develop on inner wall of ovary or peripheral part; ovary unilocular but becomes two-celled due to false septum replum (Mustard, Argemone) $\\\\to$ III.\\n4. Free central: ovules borne on central axis and septa are completely absent (Dianthus, Primrose) $\\\\to$ IV.\\n5. Basal: placenta develops at base of ovary with single ovule (Sunflower, Marigold).",
         "Confusing Free central (Dianthus/Primrose) with Axile (Tomato/Lemon).",
         "Free central lacks septa (Dianthus, Primrose); Parietal develops a false septum replum (Mustard, Argemone)."),

        # 19. Plant Kingdom - Algae Classes Pigments and Storage (Match List)
        ("Plant Kingdom", "Algae Major Classes Pigments and Stored Food Reserve", "Match List",
         "Match List-I with List-II for classes of algae and their primary photosynthetic pigments and stored food:\\n\\n"
         "| List-I (Class of Algae) | List-II (Major Pigments & Stored Food) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Chlorophyceae (Green algae) | **I.** Chlorophyll $a, b$; Starch stored in pyrenoids |\\n"
         "| **B.** Phaeophyceae (Brown algae) | **II.** Chlorophyll $a, c$, Fucoxanthin; Laminarin and Mannitol |\\n"
         "| **C.** Rhodophyceae (Red algae) | **III.** Chlorophyll $a, d$, $r$-phycoerythrin; Floridean starch |\\n"
         "| **D.** Cyanophyceae (Blue-green algae) | **IV.** Chlorophyll $a$, Phycocyanin; Cyanophycean starch (prokaryotic) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Chlorophyceae: chlorophyll $a$ and $b$; reserve food is starch stored in pyrenoids (protein surrounded by starch) $\\\\to$ I.\\n2. Phaeophyceae: chlorophyll $a, c$, carotenoids and fucoxanthin (xanthophyll); stored food is complex carbohydrates: laminarin or mannitol $\\\\to$ II.\\n3. Rhodophyceae: chlorophyll $a, d$ and major red pigment $r$-phycoerythrin; stored food is floridean starch which is structurally very similar to amylopectin and glycogen $\\\\to$ III.\\n4. Cyanophyceae: prokaryotic algae with cyanophycean starch $\\\\to$ IV.",
         "Students often confuse floridean starch (red algae) with laminarin (brown algae).",
         "Floridean starch is stored in red algae (Rhodophyceae) and structurally resembles amylopectin and glycogen."),

        # 20. Plant Kingdom - Alternation of Generations
        ("Plant Kingdom", "Haplodiplontic Life Cycle Dominant Phases in Bryophytes vs Pteridophytes", "Direct MCQ",
         "In bryophytes and pteridophytes, the dominant independent photosynthetic phase in their life cycles are respectively:",
         ["Gametophyte in bryophytes and Sporophyte in pteridophytes",
          "Sporophyte in bryophytes and Gametophyte in pteridophytes",
          "Gametophyte in both bryophytes and pteridophytes",
          "Sporophyte in both bryophytes and pteridophytes"], 0,
         "1. Both bryophytes and pteridophytes exhibit an intermediate haplodiplontic life cycle, but differ fundamentally in which generation is dominant.\\n2. In Bryophytes (mosses, liverworts), the dominant, free-living, photosynthetic, independent phase is the haploid gametophyte. The diploid sporophyte is short-lived and completely or partially dependent on the gametophyte for anchorage and nutrition.\\n3. In Pteridophytes (ferns, horsetails), the dominant, independent, photosynthetic vascular plant body is the diploid sporophyte. The gametophyte is a small, inconspicuous, multicellular free-living thallus called a prothallus which requires moist, cool conditions for flagellated antherozoids to fertilize eggs.",
         "Confusing bryophyte sporophyte dependence with pteridophyte independent sporophyte.",
         "Dominant phase: Bryophytes = Haploid Gametophyte; Pteridophytes = Diploid Sporophyte."),

        # 21. Biological Classification - Fungi Spore Types (Statement I & II)
        ("Biological Classification", "Endogenous vs Exogenous Spores in Ascomycetes and Basidiomycetes", "Statement I & II",
         "Given below are two statements regarding fungal spore formation:\\n\\n"
         "Statement I: In Ascomycetes, asexual spores (conidia) are produced exogenously on conidiophores, while sexual spores (ascospores) are produced endogenously inside sac-like asci.\\n\\n"
         "Statement II: In Basidiomycetes, asexual spores are generally not found, while sexual spores (basidiospores) are produced exogenously on club-shaped basidia.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In Ascomycetes (sac fungi like Penicillium, Aspergillus, Neurospora), conidia form asexually by budding from the tip of conidiophores (exogenous). Following karyogamy and meiosis, 8 ascospores are formed inside the enclosed ascus (endogenous). Statement I is correct.\\n2. In Basidiomycetes (mushrooms, bracket fungi, rusts, smuts), asexual spores are typically absent and vegetative reproduction occurs by fragmentation. Plasmogamy occurs by fusion of somatic cells; karyogamy and meiosis inside the basidium produce 4 basidiospores borne outwardly on sterigmata (exogenous). Statement II is correct.",
         "Confusing endogenous ascospores (inside asci) with exogenous basidiospores (on top of basidia).",
         "Ascospores are endogenous in asci (Ascomycetes); Basidiospores are exogenous on basidia (Basidiomycetes)."),

        # 22. Biological Classification - Archaebacteria Extremophiles (Assertion & Reason)
        ("Biological Classification", "Archaebacteria Cell Membrane Ether Lipids and Survival", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): Archaebacteria can survive under extreme harsh environmental conditions such as extreme salinity (halophiles), hot sulphur springs (thermoacidophiles), and marshy areas (methanogens).\\n"
         "Reason (R): Archaebacteria possess a specialized cell wall structure lacking peptidoglycan and cell membranes containing ether-linked branched lipid chains instead of ester-linked fatty acids.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Archaebacteria represent some of the most primitive cellular life forms and thrive in environments lethal to other organisms (e.g. $100^\\\\circ\\\\text{C}$ acidic sulfur pools). Assertion is TRUE.\\n2. Unlike eubacteria, archaebacterial cell walls contain pseudomurein (or complex polysaccharides) instead of peptidoglycan, making them insensitive to lysozyme and penicillin. Moreover, their cell membranes feature branched phytanyl chains linked to glycerol via ether linkages (forming monolayers or rigid bilayers), which provides extreme thermal and chemical stability against membrane hydrolysis. Reason is TRUE and explains Assertion.",
         "Students often know archaebacteria are extremophiles, but forget the exact biochemical basis (ether-linked branched lipids and pseudomurein).",
         "Archaebacterial membrane stability in extreme conditions is due to ether-linked branched lipid chains and pseudomurein cell walls."),

        # 23. Cell Structure - Endomembrane System Components (Multi-Statement)
        ("Cell: The Unit of Life", "Endomembrane System Coordinated Organelles", "Multi-Statement",
         "The endomembrane system includes those cellular membrane-bound organelles whose functions are coordinated with one another:\\n\\n"
         "A. Endoplasmic reticulum (rough and smooth ER) is an integral component of the endomembrane system.\\n"
         "B. Golgi apparatus and lysosomes are components of the endomembrane system.\\n"
         "C. Vacuoles in plant cells function as part of the endomembrane system.\\n"
         "D. Peroxisomes, chloroplasts, and mitochondria are components of the endomembrane system.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. The endomembrane system coordinates synthesis, modification, packaging, transport, and recycling of macromolecules.\\n2. Components included: Endoplasmic Reticulum (ER), Golgi apparatus, Lysosomes, and Vacuoles. Statements A, B, and C are TRUE.\\n3. Mitochondria, Chloroplasts, and Peroxisomes are NOT coordinated with these organelles in their function or biogenesis. Mitochondria and chloroplasts are semi-autonomous with their own circular DNA and 70S ribosomes. Statement D is FALSE.",
         "Including peroxisomes or chloroplasts in the endomembrane system is a classic NCERT trap.",
         "Endomembrane system includes: ER, Golgi, Lysosomes, and Vacuoles ONLY. (Excludes Mitochondria, Chloroplasts, Peroxisomes)."),

        # 24. Cell Structure - Ribosomes Svedberg Unit
        ("Cell: The Unit of Life", "70S vs 80S Ribosomal Subunit rRNA Composition", "Direct MCQ",
         "Which ribosomal RNA (rRNA) molecule functions catalytically as the peptidyl transferase ribozyme during peptide bond formation in prokaryotes?",
         ["$23\\\\text{S}$ rRNA", "$16\\\\text{S}$ rRNA", "$5\\\\text{S}$ rRNA", "$28\\\\text{S}$ rRNA"], 0,
         "1. In prokaryotes, the 70S ribosome consists of a 50S large subunit and a 30S small subunit.\\n2. The 50S large subunit contains $23\\\\text{S}$ rRNA ($2904$ nucleotides) and $5\\\\text{S}$ rRNA ($120$ nucleotides).\\n3. During translation elongation, the $23\\\\text{S}$ rRNA acts as a ribozyme (catalytic RNA) that catalyzes peptide bond formation between the amino acid at the A-site and the peptidyl-tRNA at the P-site.\\n4. $16\\\\text{S}$ rRNA is in the 30S subunit and binds the Shine-Dalgarno consensus sequence; $28\\\\text{S}$ rRNA is the eukaryotic peptidyl transferase ribozyme in 80S ribosomes.",
         "$16\\\\text{S}$ rRNA is involved in mRNA binding; $23\\\\text{S}$ rRNA is the peptidyl transferase ribozyme in bacteria.",
         "$23\\\\text{S}$ rRNA in prokaryotes (and $28\\\\text{S}$ rRNA in eukaryotes) acts as the peptidyl transferase ribozyme."),

        # 25. Sexual Reproduction - Polygonum Embryo Sac
        ("Sexual Reproduction in Flowering Plants", "Monosporic 7-Celled 8-Nucleate Embryo Sac Organization", "Direct MCQ",
         "In a typical angiosperm embryo sac (Polygonum type), the cellular organization at functional maturity consists of:",
         ["7 cells and 8 nuclei (3 antipodals, 1 central cell with 2 polar nuclei, 2 synergids, 1 egg)",
          "8 cells and 8 nuclei",
          "7 cells and 7 nuclei",
          "6 cells and 8 nuclei"], 0,
         "1. Development is monosporic: of the four megaspores formed from megaspore mother cell (MMC), three degenerate at micropylar end and one functional megaspore at chalazal end survives.\\n2. The functional megaspore nucleus undergoes three sequential free-nuclear mitotic divisions to produce 8 haploid nuclei.\\n3. Cellular organization:\\n   Chalazal end: 3 antipodal cells ($3$ nuclei),\\n   Center: 1 large central cell with 2 polar nuclei ($2$ nuclei),\\n   Micropylar end: Egg apparatus containing 2 synergids with filiform apparatus and 1 egg cell ($3$ nuclei).\\n4. Total: $3 + 1 + 2 + 1 = 7\\\\text{ cells}$ containing $3 + 2 + 3 = 8\\\\text{ nuclei}$.",
         "The central cell has TWO polar nuclei before triple fusion, making it 7 cells with 8 nuclei.",
         "Typical mature angiosperm female gametophyte (embryo sac) is 7-celled and 8-nucleate."),

        # 26. Sexual Reproduction - Outbreeding Devices (Statement I & II)
        ("Sexual Reproduction in Flowering Plants", "Mechanisms Preventing Inbreeding Depression in Angiosperms", "Statement I & II",
         "Given below are two statements regarding outbreeding devices in flowering plants:\\n\\n"
         "Statement I: Protandry (pollen released before stigma becomes receptive) and protogyny (stigma receptive before pollen release) prevent autogamy by introducing temporal non-synchronization.\\n\\n"
         "Statement II: Self-incompatibility is a genetic mechanism that prevents self-pollen from the same flower or other flowers of the same plant from fertilizing ovules by inhibiting pollen germination or pollen tube growth in the pistil.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Continued self-pollination leads to severe inbreeding depression. Plants have evolved outbreeding devices: non-synchronization of pollen release and stigma receptivity (dichogamy: protandry in sunflower, protogyny in Datura). Statement I is correct.\\n2. Self-incompatibility is an intracellular genetic recognition system controlled by multiple alleles ($S$-gene). When self-pollen lands on stigma, the pistil recognizes matching alleles and blocks pollen tube germination or growth through the style, ensuring cross-pollination (xenogamy). Statement II is correct.",
         "Confusing spatial separation (herkogamy) with temporal non-synchronization (dichogamy).",
         "Self-incompatibility is a genetically controlled barrier that inhibits self-pollen tube growth in the pistil."),

        # 27. Sexual Reproduction - Endosperm Development and Apomixis
        ("Sexual Reproduction in Flowering Plants", "Free Nuclear Endosperm and Adventive Polyembryony", "Direct MCQ",
         "In coconut ($Cocos nucifera$), the liquid coconut water and the surrounding white firm kernel represent respectively:",
         ["Free nuclear endosperm and cellular endosperm",
          "Cellular endosperm and free nuclear endosperm",
          "Degenerated nucellus and perisperm",
          "Embryo and cotyledon"], 0,
         "1. Following double fertilization, the primary endosperm nucleus (PEN, $3n$) divides mitotically.\\n2. In free-nuclear endosperm development, karyokinesis is not immediately followed by cytokinesis, producing hundreds to thousands of free nuclei in central vacuolar fluid.\\n3. The liquid coconut water from tender coconut is free-nuclear endosperm made up of thousands of free nuclei.\\n4. Later, cell wall formation starts from the periphery and moves inward, forming cellular endosperm which corresponds to the solid white coconut kernel/meat.",
         "Inverting liquid (free nuclear) with solid (cellular) is the standard test question.",
         "Liquid coconut water is free-nuclear endosperm; the solid edible white meat is cellular endosperm."),

        # 28. Ecology - Population Growth Models
        ("Organisms and Populations", "Verhulst-Pearl Logistic Growth Equation and Carrying Capacity", "Direct MCQ",
         "A population growing in a habitat with limited resources exhibits logistic growth described by $\\\\frac{dN}{dt} = r N \\\\left(\\\\frac{K - N}{K}\\\\right)$. At what population density $N$ is the population growth rate ($\\\\frac{dN}{dt}$) maximal?",
         ["$N = K / 2$", "$N = K$", "$N = K / 4$", "$N \\\\to 0$"], 0,
         "1. Logistic growth formula: $\\\\frac{dN}{dt} = r N \\\\left(1 - \\\\frac{N}{K}\\\\right) = r N - \\\\frac{r N^2}{K}$.\\n2. To find maximum growth rate, differentiate $\\\\frac{dN}{dt}$ with respect to $N$ and set to zero:\\n   $$\\\\frac{d}{dN}\\\\left(\\\\frac{dN}{dt}\\\\right) = r - \\\\frac{2r N}{K} = 0 \\\\implies \\\\frac{2r N}{K} = r \\\\implies 2N = K \\\\implies N = \\\\frac{K}{2}$$.\\n3. When $N = K/2$, population growth velocity is at its maximum point of inflection: $\\\\left(\\\\frac{dN}{dt}\\\\right)_{\\\\max} = \\\\frac{r K}{4}$.\\n4. When $N = K$, carrying capacity is reached and growth rate drops to zero ($\\\\frac{dN}{dt} = 0$).",
         "At $N = K$, the population is at maximum size, but its GROWTH RATE is ZERO.",
         "In logistic growth, maximum rate of population increase occurs at half the carrying capacity ($N = K/2$)."),

        # 29. Ecology - Species-Area Relationship
        ("Biodiversity and Conservation", "Alexander von Humboldt Species-Area Relationship Regression Slope", "Direct MCQ",
         "German naturalist Alexander von Humboldt observed that species richness increases with exploring area, described by $\\\\log S = \\\\log C + Z \\\\log A$. When species-area analysis is performed over very large regions such as entire continents (e.g. for frugivorous birds and mammals in tropical forests), the regression coefficient $Z$ is in the range of:",
         ["$0.6\\\\text{ to }1.2$ (specifically $1.15$)",
          "$0.1\\\\text{ to }0.2$",
          "$0.2\\\\text{ to }0.4$",
          "$1.5\\\\text{ to }2.0$"], 0,
         "1. Rectangular hyperbola equation: $S = C A^Z \\\\implies \\\\log S = \\\\log C + Z \\\\log A$.\\n2. For small taxonomic groups in small localized areas (e.g. plants in Britain, birds in California), the slope $Z$ is remarkably consistent in the range of $0.1\\\\text{ to }0.2$.\\n3. However, when species-area relationships are analyzed across very large continental landmasses, the regression line becomes much steeper, with $Z$ values ranging between $0.6\\\\text{ to }1.2$.\\n4. For frugivorous (fruit-eating) birds and mammals in the tropical forests of different continents, the slope $Z$ is found to be $1.15$.",
         "0.1 to 0.2 applies to small local areas; 0.6 to 1.2 applies to entire continents.",
         "Species-area slope $Z$: Local areas $= 0.1-0.2$; Entire continents $= 0.6-1.2$ (frugivorous birds $= 1.15$)."),

        # 30. Ecology - Nitrogen Cycle Microbes (Match List)
        ("Ecosystem and Biogeochemical Cycles", "Nitrification and Denitrification Bacterial Genera", "Match List",
         "Match List-I with List-II for soil nitrogen transformation steps and their specialized catalytic bacteria:\\n\\n"
         "| List-I (Nitrogen Transformation Step) | List-II (Specialized Soil Bacterium) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Ammonia oxidized to Nitrite ($2\\\\text{NH}_3 + 3\\\\text{O}_2 \\\\to 2\\\\text{NO}_2^- + 2\\\\text{H}^+ + 2\\\\text{H}_2\\\\text{O}$) | **I.** $Nitrosomonas$ and $Nitrococcus$ |\\n"
         "| **B.** Nitrite oxidized to Nitrate ($2\\\\text{NO}_2^- + \\\\text{O}_2 \\\\to 2\\\\text{NO}_3^-$) | **II.** $Nitrobacter$ and $Nitrocystis$ |\\n"
         "| **C.** Denitrification (Nitrate reduced to gaseous $\\\\text{N}_2$) | **III.** $Pseudomonas$ and $Thiobacillus$ |\\n"
         "| **D.** Free-living aerobic nitrogen-fixing bacteria | **IV.** $Azotobacter$ and $Beijerinckia$ |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Nitrosomonas and Nitrococcus oxidize ammonia to nitrite $\\\\to$ I.\\n2. Nitrobacter oxidizes nitrite to nitrate $\\\\to$ II.\\n3. Pseudomonas and Thiobacillus convert soil nitrates back into dinitrogen gas (denitrification) $\\\\to$ III.\\n4. Azotobacter and Beijerinckia are free-living aerobic nitrogen fixers (Rhodospirillum is anaerobic) $\\\\to$ IV.",
         "Distractors swap Nitrosomonas (ammonia to nitrite) with Nitrobacter (nitrite to nitrate).",
         "Ammonia $\\\\to$ Nitrite by Nitrosomonas; Nitrite $\\\\to$ Nitrate by Nitrobacter; Nitrate $\\\\to$ $N_2$ by Pseudomonas."),

        # 31. Ecology - Hydrarch Succession Stages
        ("Ecosystem", "Primary Succession in Water (Hydrarch) Correct Sequence", "Direct MCQ",
         "The correct sequential order of seral stages during primary hydrarch succession in a newly formed water body until reaching the climax forest is:",
         ["Phytoplankton $\\\\to$ Submerged plant stage $\\\\to$ Submerged free floating plant stage $\\\\to$ Reed-swamp stage $\\\\to$ Marsh-meadow stage $\\\\to$ Scrub stage $\\\\to$ Climax forest",
          "Phytoplankton $\\\\to$ Reed-swamp $\\\\to$ Submerged plant $\\\\to$ Marsh-meadow $\\\\to$ Scrub $\\\\to$ Forest",
          "Submerged plant $\\\\to$ Phytoplankton $\\\\to$ Free floating $\\\\to$ Marsh-meadow $\\\\to$ Reed-swamp $\\\\to$ Forest",
          "Phytoplankton $\\\\to$ Marsh-meadow $\\\\to$ Reed-swamp $\\\\to$ Submerged plant $\\\\to$ Forest"], 0,
         "1. Hydrarch succession begins in water and proceeds toward mesic conditions.\\n2. Pioneer community: microscopic autotrophic Phytoplankton (diatoms, unicellular green algae).\\n3. Submerged plant stage: rooted submerged hydrophytes (Hydrilla, Vallisneria, Potamogeton).\\n4. Submerged free floating stage: water level decreases; floating plants appear (Pistia, Eichhornia, Lemna).\\n5. Reed-swamp stage: amphibious emergent plants (Typha, Phragmites).\\n6. Marsh-meadow stage: sedges and grasses (Carex, Juncus, Cyperus).\\n7. Scrub stage: woody shrubs (Salix, Cornus).\\n8. Climax community: stable mesophytic Forest.",
         "Confusing Reed-swamp (amphibious reeds) with Marsh-meadow (grasses and sedges).",
         "Hydrarch succession sequence: Phytoplankton $\\\\to$ Submerged $\\\\to$ Floating $\\\\to$ Reed-swamp $\\\\to$ Marsh-meadow $\\\\to$ Scrub $\\\\to$ Forest."),

        # 32. Biotechnology - Ti Plasmid Vector
        ("Biotechnology: Principles and Processes", "Agrobacterium tumefaciens Disarmed Ti Plasmid Vector", "Direct MCQ",
         "The natural genetic engineer $Agrobacterium tumefaciens$ is widely used to transform dicotyledonous plant cells because its tumor-inducing (Ti) plasmid naturally contains:",
         ["T-DNA that integrates randomly into the host plant genome",
          "An intact $amp^R$ gene that protects the plant from fungal infections",
          "A viral coat protein gene that triggers systemic acquired resistance",
          "A unique restriction enzyme that cleaves human genomic DNA"], 0,
         "1. Agrobacterium tumefaciens is a soil pathogen of several dicot plants, causing crown gall disease.\\n2. It delivers a specific segment of its large Ti-plasmid, called the transfer-DNA (T-DNA), into infected plant cells.\\n3. T-DNA integrates stably into the plant host nuclear chromosomes, directing the plant to synthesize plant hormones (auxins and cytokinins causing tumor galls) and opines (food for the bacterium).\\n4. Genetic engineers 'disarm' the Ti-plasmid by deleting the tumor-causing genes while retaining the T-DNA borders and vir genes, allowing insertion of beneficial foreign genes into crop plants.",
         "The tumor-causing genes are REMOVED in cloning vectors; the T-DNA borders deliver the foreign gene.",
         "Agrobacterium tumefaciens Ti plasmid is disarmed by replacing tumor genes with desired recombinant genes."),

        # 33. Biotechnology - RNA Interference in Tobacco (Statement I & II)
        ("Biotechnology and Its Applications", "Nematode Resistance in Tobacco via RNA Interference", "Statement I & II",
         "Given below are two statements regarding RNA interference (RNAi):\\n\\n"
         "Statement I: RNAi is a cellular defense mechanism present in all eukaryotic organisms that silences specific target mRNAs through complementary double-stranded RNA (dsRNA).\\n\\n"
         "Statement II: In transgenic tobacco plants, nematode resistance against $Meloidogyne incognita$ was achieved by introducing nematode-specific genes using Agrobacterium vectors which produced both sense and anti-sense RNA simultaneously in host cells.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. RNA interference (RNAi) takes place in all eukaryotic organisms as a method of cellular defense against viral infection and transposable elements. It involves silencing of a specific mRNA due to a complementary dsRNA molecule that binds to and prevents translation of the mRNA. Statement I is correct.\\n2. Using Agrobacterium vectors, nematode-specific DNA was introduced into tobacco plants such that it produced both sense and anti-sense RNA. These two complementary RNAs hybridized to form double-stranded RNA (dsRNA) that initiated RNAi, silencing the specific mRNA of Meloidogyne incognita. Consequently, the parasite could not survive in the transgenic host. Statement II is correct.",
         "Both sense AND anti-sense RNA must be transcribed to form the initiating dsRNA duplex.",
         "RNAi silences specific mRNA using complementary dsRNA formed by simultaneous transcription of sense and antisense strands."),

        # 34. Mineral Nutrition - Symbiotic Nitrogenase and Leghaemoglobin (Assertion & Reason)
        ("Plant Physiology - Mineral Nutrition", "Oxygen Sensitivity of Nitrogenase and Leghaemoglobin Function", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): The enzyme nitrogenase functions exclusively under strictly anaerobic conditions inside root nodules of leguminous plants.\\n"
         "Reason (R): Legume root nodules contain a pink-colored oxygen-scavenging pigment called leghaemoglobin that protects nitrogenase from irreversible oxygen denaturation.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Nitrogenase (a Mo-Fe protein) catalyzes biological nitrogen fixation: $N_2 + 8e^- + 8H^+ + 16\\\\text{ATP} \\\\to 2NH_3 + H_2 + 16\\\\text{ADP} + 16P_i$. Nitrogenase is extremely sensitive to molecular oxygen and is irreversibly inactivated by $O_2$. Assertion is TRUE.\\n2. Rhizobium bacteria are aerobic under free-living conditions, but during nitrogen fixation inside nodules, they require an anaerobic environment. Root nodules synthesize leghaemoglobin, an oxygen-binding hemoprotein that scavenges free oxygen, maintaining very low partial pressure of $O_2$ around nitrogenase while delivering oxygen to bacterial respiration. Reason is TRUE and explains Assertion.",
         "Students often think nodules must be fully aerobic because Rhizobium is an aerobic bacterium; leghaemoglobin creates localized microaerophilic/anaerobic conditions.",
         "Leghaemoglobin acts as an oxygen scavenger, protecting oxygen-sensitive nitrogenase enzyme from denaturation."),

        # 35. Photosynthesis - Water Splitting Complex (Assertion & Reason)
        ("Photosynthesis in Higher Plants", "Photolysis of Water Inner Thylakoid Membrane Localization", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\\n\\n"
         "Assertion (A): During the light reaction of photosynthesis, protons produced by the photolysis of water accumulate in the thylakoid lumen rather than in the stroma.\\n"
         "Reason (R): The oxygen-evolving water-splitting complex is physically located on the inner side of the thylakoid membrane associated with Photosystem II (PS II).\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. According to Mitchell\\'s chemiosmotic hypothesis, ATP synthesis in chloroplasts requires a proton gradient across the thylakoid membrane, with high $[H^+]$ in lumen and low $[H^+]$ in stroma. Assertion is TRUE.\\n2. Photolysis of water: $2H_2O \\\\to 4H^+ + O_2 + 4e^-$. The water-splitting manganese complex ($Mn_4CaO_5$) is physically anchored to the luminal (inner) face of the thylakoid membrane adjacent to PS II. Therefore, all protons generated from water splitting are dumped directly into the thylakoid lumen, contributing directly to the proton motive force. Reason is TRUE and explains Assertion.",
         "Assuming water splitting occurs in the stroma contradicts the chemiosmotic proton accumulation mechanism.",
         "Photolysis of water occurs on the inner surface of the thylakoid membrane, releasing protons into the lumen."),

        # 36. Molecular Genetics - Meselson and Stahl Experiment
        ("Molecular Basis of Inheritance", "Meselson-Stahl Semiconservative Density Gradient Centrifugation", "Direct MCQ",
         "E. coli cells grown in $^{15}\\\\text{N}$ medium for many generations were transferred to $^{14}\\\\text{N}$ medium and allowed to replicate for two generations ($40\\\\text{ minutes}$). What is the proportion of hybrid ($^{15}\\\\text{N}/^{14}\\\\text{N}$) to light ($^{14}\\\\text{N}/^{14}\\\\text{N}$) DNA molecules observed after CsCl equilibrium density gradient centrifugation?",
         ["$1 : 1$ ($50\\\\% \\\\text{ hybrid} : 50\\\\% \\\\text{ light}$)",
          "$1 : 3$ ($25\\\\% \\\\text{ hybrid} : 75\\\\% \\\\text{ light}$)",
          "$100\\\\% \\\\text{ hybrid}$",
          "$3 : 1$ ($75\\\\% \\\\text{ hybrid} : 25\\\\% \\\\text{ light}$)"], 0,
         "1. E. coli divides every 20 minutes.\\n2. At $t = 0$: $100\\\\%$ of DNA is heavy ($^{15}\\\\text{N}/^{15}\\\\text{N}$).\\n3. After Generation 1 ($20\\\\text{ min}$): all parental strands separate and act as templates in $^{14}\\\\text{N}$. 100% of DNA molecules are intermediate hybrid density ($^{15}\\\\text{N}/^{14}\\\\text{N}$).\\n4. After Generation 2 ($40\\\\text{ min}$): each hybrid DNA replicates in $^{14}\\\\text{N}$. From 2 hybrid molecules, 4 DNA molecules are formed:\\n   2 hybrid molecules ($^{15}\\\\text{N}/^{14}\\\\text{N}$) and 2 light molecules ($^{14}\\\\text{N}/^{14}\\\\text{N}$).\\n5. Ratio of hybrid to light DNA is $2 : 2 = 1 : 1$ (50% hybrid : 50% light).",
         "100% hybrid occurs after generation 1 (20 min); after generation 3 (60 min) the ratio is 1:3 (25% hybrid : 75% light).",
         "Meselson-Stahl experiment at 40 min (2 generations): 50% hybrid ($^{15}N/^{14}N$) and 50% light ($^{14}N/^{14}N$)."),

        # 37. Molecular Genetics - Hershey-Chase Experiment
        ("Molecular Basis of Inheritance", "Hershey-Chase Radioactive Isotope Labeling Proof of DNA", "Direct MCQ",
         "In their landmark 1952 experiment proving that DNA is the genetic material, Alfred Hershey and Martha Chase used radioactive isotopes to label bacteriophage T2 components. Which isotopes were specifically incorporated into DNA and protein coats respectively?",
         ["$^{32}\\\\text{P}$ in DNA and $^{35}\\\\text{S}$ in protein coat",
          "$^{35}\\\\text{S}$ in DNA and $^{32}\\\\text{P}$ in protein coat",
          "$^{15}\\\\text{N}$ in DNA and $^{14}\\\\text{C}$ in protein coat",
          "$^{32}\\\\text{P}$ in DNA and $^{15}\\\\text{N}$ in protein coat"], 0,
         "1. DNA contains phosphorus in its phosphodiester backbone, but strictly contains NO sulfur.\\n2. Viral capsid proteins contain sulfur in amino acids (methionine and cysteine), but contain NO phosphorus.\\n3. Bacteriophages grown in $^{32}\\\\text{P}$ had radioactive DNA; phages grown in $^{35}\\\\text{S}$ had radioactive protein coats.\\n4. Following infection, agitation in a blender sheared off viral coats, and centrifugation pelleted the heavier bacterial cells.\\n5. Radioactivity $^{32}\\\\text{P}$ was detected in the bacterial cell pellet, proving that DNA entered cells. $^{35}\\\\text{S}$ remained in the supernatant fluid, proving protein coats do not enter.",
         "Confusing $^{32}P$ (phosphorus in DNA) with $^{35}S$ (sulfur in methionine/cysteine of proteins).",
         "Hershey-Chase: $^{32}\\\\text{P}$ labels DNA; $^{35}\\\\text{S}$ labels viral capsid proteins."),

        # 38. Genetics - Pleiotropy vs Polygenic (Statement I & II)
        ("Principles of Inheritance and Variation", "Pleiotropy Manifestation vs Polygenic Inheritance", "Statement I & II",
         "Given below are two statements regarding non-Mendelian genetic phenomena:\\n\\n"
         "Statement I: Pleiotropy occurs when a single gene mutation influences multiple, seemingly unrelated phenotypic traits simultaneously (e.g. phenylketonuria in humans).\\n\\n"
         "Statement II: Polygenic inheritance occurs when multiple independent genes cumulatively influence a single quantitative phenotypic trait (e.g. human height and skin color).\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Pleiotropy: single gene $\\\\to$ multiple phenotypic effects. In phenylketonuria (PKU), mutation in the gene coding for phenylalanine hydroxylase enzyme leads to hyperphenylalaninemia, which manifests pleiotropically as mental retardation, eczema, and reduction in skin and hair pigmentation. Statement I is correct.\\n2. Polygenic inheritance: multiple genes $\\\\to$ single phenotypic trait. Traits like human height, kernel color in wheat, and human skin color are controlled by several non-allelic genes whose alleles have an additive cumulative effect, producing continuous quantitative variation. Statement II is correct.",
         "Pleiotropy = 1 gene $\\\\to$ many traits; Polygenic = many genes $\\\\to$ 1 trait.",
         "Pleiotropy: single gene controls multiple phenotypic traits; Polygenic: multiple genes control a single quantitative trait."),

        # 39. Cell Biology - Fluid Mosaic Model
        ("Cell: The Unit of Life", "Singer-Nicolson Fluid Mosaic Model and Protein Mobility", "Direct MCQ",
         "According to the widely accepted Fluid Mosaic Model of cell membranes proposed by Singer and Nicolson (1972), the quasi-fluid nature of the membrane is primarily attributed to:",
         ["Lateral mobility of proteins within the fluid phospholipid bilayer",
          "Frequent transverse (flip-flop) movement of proteins across the bilayer",
          "Rigid, immobile arrangement of integral transmembrane proteins",
          "Presence of a continuous outer carbohydrate cell wall coat"], 0,
         "1. Singer and Nicolson described the plasma membrane as 'protein icebergs floating in a sea of lipids'.\\n2. The phospholipid bilayer is quasi-fluid, allowing phospholipids to move rapidly by lateral diffusion within their own monolayer.\\n3. Integral and peripheral membrane proteins can also move laterally within the lipid bilayer, which is vital for membrane repair, endocytosis, cell division, and cell-cell junctions.\\n4. However, proteins and phospholipids very rarely undergo transverse (flip-flop) movement from one leaflet to the opposite leaflet because moving polar heads across the hydrophobic core requires substantial energy.",
         "Proteins move laterally within the bilayer; they almost NEVER undergo flip-flop movement.",
         "Membrane fluidity reflects lateral mobility of lipids and proteins; flip-flop movement of proteins is virtually absent."),

        # 40. Plant Physiology - Stomatal Opening Mechanism
        ("Transport in Plants - Plant Physiology", "Levitt Potassium Influx Hypothesis of Stomatal Transpiration", "Direct MCQ",
         "According to Levitt\\'s active proton-potassium exchange hypothesis, stomatal opening during the day is triggered by:",
         ["Active pumping of $H^+$ out of guard cells, driving $K^+$ and malate influx that lowers water potential",
          "Passive leakage of $K^+$ out of guard cells into subsidiary cells",
          "Conversion of starch into insoluble glucose polymers inside guard cells",
          "Direct synthesis of abscisic acid inside guard cells in response to sunlight"], 0,
         "1. In daylight, guard cells perform photosynthesis and respiration, leading to decreased internal $CO_2$ and synthesis of malic acid.\\n2. Malic acid dissociates into malate ions and protons ($H^+$).\\n3. An active $H^+$-ATPase pump on guard cell plasma membrane pumps $H^+$ ions out into subsidiary cells.\\n4. To maintain electrical neutrality, $K^+$ ions actively enter guard cells from subsidiary cells, balancing malate ions.\\n5. Accumulation of potassium malate drastically lowers the osmotic potential (and water potential $\\\\Psi_w$) inside guard cells.\\n6. Water enters guard cells by endosmosis; guard cells become turgid, bowing their thin outer walls and opening the stomatal pore.",
         "Exit of K+ causes stomatal CLOSURE; active INFLUX of K+ along with malate causes stomatal OPENING.",
         "Stomatal opening: active $H^+$ efflux $\\\\implies K^+$ influx $\\\\implies$ potassium malate accumulation $\\\\implies$ endosmosis $\\\\implies$ turgidity."),

        # 41. Morphology - Plant Organ Modifications (Match List)
        ("Morphology of Flowering Plants", "Homologous vs Analogous Plant Organ Modifications", "Match List",
         "Match List-I with List-II for plant morphological modifications and their anatomical organ derivations:\\n\\n"
         "| List-I (Modified Plant Structure) | List-II (True Morphological Organ of Origin) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Tendrils of Gourds (Cucumber, Pumpkin) | **I.** Stem modification (axillary buds) |\\n"
         "| **B.** Tendrils of Pea | **II.** Leaf modification (leaflets) |\\n"
         "| **C.** Thorns of $Citrus$ and $Bougainvillea$ | **III.** Stem modification (axillary buds) |\\n"
         "| **D.** Spines of $Opuntia$ (Prickly pear) | **IV.** Leaf modification (defense & transpiration reduction) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Stem tendrils in cucurbits (cucumber, pumpkin, watermelon) and passionflower develop from axillary buds $\\\\to$ I.\\n2. Leaf tendrils in sweet pea and garden pea are modified terminal leaflets $\\\\to$ II.\\n3. Thorns in Citrus and Bougainvillea are hard, straight, pointed modified axillary stem buds $\\\\to$ III.\\n4. Spines in Opuntia and Euphorbia are modified leaves; the green flattened photosynthetic organ is a phylloclade (modified stem) $\\\\to$ IV.",
         "Tendrils in gourds are stem-derived; tendrils in peas are leaf-derived.",
         "Gourd tendrils = stem modification; Pea tendrils = leaf modification; Thorns = stem; Spines = leaf."),

        # 42. Biodiversity Conservation - In-situ vs Ex-situ (Match List)
        ("Biodiversity and Conservation", "In-situ vs Ex-situ Conservation Strategies and Sites", "Match List",
         "Match List-I with List-II for biodiversity conservation approaches and their representative protected sanctuaries:\\n\\n"
         "| List-I (Conservation Strategy) | List-II (Designated Conservation Sanctuary / Facility) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Sacred Groves (In-situ) | **I.** Khasi and Jaintia Hills in Meghalaya, Aravalli Hills in Rajasthan |\\n"
         "| **B.** Biosphere Reserves (In-situ) | **II.** $18$ national reserves in India (e.g. Nilgiri, Nanda Devi) |\\n"
         "| **C.** Cryopreservation (Ex-situ) | **I.** Storage of gametes at $-196^\\\\circ\\\\text{C}$ in liquid nitrogen |\\n"
         "| **D.** Botanical Gardens & Seed Banks (Ex-situ) | **IV.** National Bureau of Plant Genetic Resources (NBPGR, New Delhi) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Sacred groves are culturally protected undisturbed forest tracts: Khasi and Jaintia Hills (Meghalaya), Aravalli Hills (Rajasthan), Western Ghats $\\\\to$ I.\\n2. Biosphere reserves are multi-purpose in-situ protected ecosystems (18 in India) $\\\\to$ II.\\n3. Cryopreservation preserves viable gametes and tissues of threatened species indefinitely at $-196^\\\\circ\\\\text{C}$ $\\\\to$ III.\\n4. Seed banks and botanical gardens maintain ex-situ genetic stock of crop cultivars and endangered flora $\\\\to$ IV.",
         "National parks and biosphere reserves are in-situ; zoological parks, botanical gardens, and seed banks are ex-situ.",
         "In-situ = in natural habitat (National Parks, Biosphere Reserves, Sacred Groves); Ex-situ = outside habitat (Seed Banks, Cryopreservation)."),

        # 43. Ecosystem - Energy Flow GFC vs DFC (Statement I & II)
        ("Ecosystem", "Grazing vs Detritus Food Chain Energy Conduits", "Statement I & II",
         "Given below are two statements regarding energy pathways in ecosystems:\\n\\n"
         "Statement I: In an aquatic ecosystem, the grazing food chain (GFC) is the major conduit for energy flow.\\n\\n"
         "Statement II: In a terrestrial ecosystem, a much larger fraction of energy flows through the detritus food chain (DFC) than through the grazing food chain.\\n\\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In aquatic ecosystems (oceans, lakes), phytoplankton primary production is rapidly consumed by zooplankton and small fishes. High turnover rate and consumption efficiency mean the grazing food chain (GFC) channels the majority of energy. Statement I is correct.\\n2. In terrestrial ecosystems (forests, grasslands), vast amounts of plant biomass (wood, litter, bark, roots) are not consumed directly by herbivores while alive. Instead, fallen leaf litter and dead organic matter feed decomposers (bacteria, fungi, earthworms), channeling over $80-90\\\\%$ of net primary productivity through the detritus food chain (DFC). Statement II is correct.",
         "Students often assume GFC is always dominant in all ecosystems; DFC dominates terrestrial biomes.",
         "Aquatic ecosystems: GFC is major energy conduit; Terrestrial ecosystems: DFC is major energy conduit."),

        # 44. Genetics - Multiple Allelism in ABO Blood Groups
        ("Principles of Inheritance and Variation", "Codominance and Multiple Allele Inheritance in ABO Blood Groups", "Direct MCQ",
         "A man with blood group A ($I^A i$) marries a woman with blood group B ($I^B i$). What are the possible blood groups and their phenotypic probability distribution among their children?",
         ["Equal probability ($25\\\\%$) of blood groups A, B, AB, and O",
          "$50\\\\%$ blood group AB and $50\\\\%$ blood group O",
          "$100\\\\%$ blood group AB only",
          "$75\\\\%$ blood group AB and $25\\\\%$ blood group O"], 0,
         "1. Genotype of father: $I^A i$ (gametes produced: $50\\\\% I^A$ and $50\\\\% i$).\\n2. Genotype of mother: $I^B i$ (gametes produced: $50\\\\% I^B$ and $50\\\\% i$).\\n3. Punnett square crosses:\\n   $I^A \\\\times I^B \\\\to I^A I^B$ (Blood group AB, $25\\\\%$),\\n   $I^A \\\\times i \\\\to I^A i$ (Blood group A, $25\\\\%$),\\n   $i \\\\times I^B \\\\to I^B i$ (Blood group B, $25\\\\%$),\\n   $i \\\\times i \\\\to ii$ (Blood group O, $25\\\\%$).\\n4. All four phenotypic blood groups (A, B, AB, O) appear with equal probability ($1/4$ or $25\\\\%$ each).",
         "Assuming the parents are homozygous ($I^A I^A \\\\times I^B I^B$) produces only AB children; heterozygous parents yield all 4 groups.",
         "A heterozygous A parent and heterozygous B parent can produce children of all 4 human ABO blood groups with equal 25% frequency."),

        # 45. Molecular Biology - DNA Fingerprinting VNTRs
        ("Molecular Basis of Inheritance", "Variable Number Tandem Repeats (VNTR) Minisatellites", "Direct MCQ",
         "In DNA fingerprinting (profiling), the molecular probes used for Southern blot hybridization correspond to:",
         ["Variable Number Tandem Repeats (VNTRs) belonging to minisatellites",
          "Single-copy structural coding genes",
          "Ribosomal RNA gene clusters",
          "Telomeric inverted repeats"], 0,
         "1. DNA fingerprinting developed by Sir Alec Jeffreys utilizes satellite DNA.\\n2. Satellite DNA consists of highly repetitive non-coding DNA sequences which show a high degree of polymorphism (allelic variation).\\n3. Variable Number Tandem Repeats (VNTRs) belong to a class of satellite DNA referred to as minisatellites (repeat unit length $10\\\\text{ to }100\\\\text{ base pairs}$).\\n4. The copy number of VNTR repeats varies from chromosome to chromosome in an individual, creating unique banding patterns when hybridized with radiolabeled VNTR probes.\\n5. Since polymorphisms are inherited from parents, VNTR patterns provide forensic identification and paternity confirmation.",
         "Microsatellites are STRs (1-6 bp); minisatellites are VNTRs (10-100 bp).",
         "DNA fingerprinting uses radiolabeled VNTR (minisatellite) probes to detect variable tandem repeat polymorphisms."),

        # 46. Botany in Agriculture - Biofortification
        ("Strategies for Enhancement in Food Production", "Biofortification and High-Lysine Maize Varieties", "Direct MCQ",
         "Biofortification is the breeding of crops with higher levels of vitamins, minerals, and proteins. Which fortified wheat variety possessing high protein content was used as a donor for improving cultivated wheat in India?",
         ["Atlas 66", "Kalyan Sona", "Sonalika", "Sharbati Sonora"], 0,
         "1. Biofortification is the most practical means to combat 'hidden hunger' (micronutrient deficiencies) in developing nations.\\n2. In 2000, maize hybrids having twice the amount of the essential amino acids lysine and tryptophan were developed.\\n3. Atlas 66 is a wheat variety with exceptionally high protein content ($14\\\\%$) that has been extensively used as a donor parent in Indian wheat breeding programs.\\n4. Golden rice is biofortified with $\\\\beta$-carotene (provitamin A); iron-fortified rice contains over five times the iron of standard varieties.",
         "Sonalika and Kalyan Sona are semi-dwarf high-yielding varieties developed during the Green Revolution, but Atlas 66 is the protein-fortified donor.",
         "Atlas 66 is a biofortified wheat variety rich in protein used as a genetic donor."),

        # 47. Microbes in Human Welfare - Organic Acids (Match List)
        ("Microbes in Human Welfare", "Industrial Microbial Production of Organic Acids", "Match List",
         "Match List-I with List-II for industrial organic chemicals and their microbial fermentation sources:\\n\\n"
         "| List-I (Industrial Product / Enzyme) | List-II (Microbial Producer Organism) |\\n"
         "| :--- | :--- |\\n"
         "| **A.** Citric acid | **I.** $Aspergillus niger$ (fungus) |\\n"
         "| **B.** Acetic acid (vinegar) | **II.** $Acetobacter aceti$ (bacterium) |\\n"
         "| **C.** Butyric acid | **III.** $Clostridium butylicum$ (bacterium) |\\n"
         "| **D.** Clot buster (Streptokinase) | **IV.** $Streptococcus$ (bacterium modified by genetic engineering) |\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Aspergillus niger is a filamentous fungus used for commercial citric acid production $\\\\to$ I.\\n2. Acetobacter aceti is an aerobic bacterium producing acetic acid from ethanol $\\\\to$ II.\\n3. Clostridium butylicum is an anaerobic spore-forming bacterium producing butyric acid $\\\\to$ III.\\n4. Streptokinase produced by Streptococcus bacterium is used as a 'clot buster' for removing intravascular thrombi in myocardial infarction patients $\\\\to$ IV.\\n5. Cyclosporin A (immunosuppressive agent) is produced by fungus Trichoderma polysporum; Statins (cholesterol-lowering) by Monascus purpureus.",
         "Aspergillus niger is a fungus, not a bacterium; Acetobacter and Clostridium are bacteria.",
         "Citric acid: Aspergillus niger (fungus); Butyric acid: Clostridium butylicum; Clot buster: Streptococcus."),

        # 48. Biological Classification - Viroids, Prions, Lichens (Multi-Statement)
        ("Biological Classification", "Acellular Agents Viroids Prions and Lichen Biology", "Multi-Statement",
         "Consider the structural and biological characteristics of acellular infectious agents and lichens:\\n\\n"
         "A. Viroids were discovered by T.O. Diener (1971) as infectious agents causing potato spindle tuber disease, consisting of free low-molecular-weight RNA without any protein coat.\\n"
         "B. Prions are infectious abnormally folded proteins that cause bovine spongiform encephalopathy (BSE / Mad Cow Disease) in cattle and Cr-Jacob disease (CJD) in humans.\\n"
         "C. Lichens are symbiotic associations where the fungal component (mycobiont) provides minerals and water, while the algal component (phycobiont) synthesizes food.\\n"
         "D. Lichens are excellent pollution indicators because they thrive and grow luxuriantly in areas with high sulphur dioxide ($\\\\text{SO}_2$) air pollution.\\n\\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Viroids contain only naked circular single-stranded RNA of low molecular weight, lacking a capsid protein coat. Discovered by T.O. Diener. Statement A is TRUE.\\n2. Prions are proteinaceous infectious particles caused by misfolded conformations of the PrP protein. Statement B is TRUE.\\n3. Lichens consist of phycobiont (autotrophic algae/cyanobacteria) and mycobiont (heterotrophic ascomycete/basidiomycete fungus). Statement C is TRUE.\\n4. Lichens are extremely sensitive to sulphur dioxide ($SO_2$) pollution; they CANNOT grow in polluted industrial cities. Their absence indicates pollution, making them bioindicators. Statement D is FALSE.",
         "Lichens are destroyed by $SO_2$ pollution; they do NOT grow in polluted environments.",
         "Viroids = naked RNA without protein coat; Prions = infectious misfolded proteins; Lichens = sensitive $SO_2$ pollution bioindicators."),

        # 49. Photosynthesis - Blackman's Law of Limiting Factors
        ("Photosynthesis in Higher Plants", "Blackman Law of Limiting Factors and Light Saturation", "Direct MCQ",
         "According to Blackman\\'s Law of Limiting Factors (1905), at what percentage of full sunlight does light saturation typically occur for photosynthesis in most terrestrial plants?",
         ["$10\\\\%$ of full sunlight", "$50\\\\%$ of full sunlight", "$25\\\\%$ of full sunlight", "$100\\\\%$ (full sunlight)"], 0,
         "1. Blackman\\'s Law states: 'If a chemical process is affected by more than one factor, its rate is determined by the factor which is nearest to its minimal value.'\\n2. For light intensity, there is a linear relationship between incident light and $CO_2$ fixation rates at low light intensities.\\n3. However, light saturation occurs at just $10\\\\%$ of full sunlight.\\n4. Except for plants in dense shade or deep forest understories, light is rarely a limiting factor in nature.\\n5. At high light intensities beyond saturation, solarization (chlorophyll breakdown and photoinhibition) occurs, reducing photosynthetic rate.",
         "Assuming plants need full sunlight to reach maximum photosynthesis overlooks that saturation occurs at just 10% of full sunlight.",
         "Light saturation in photosynthesis occurs at only 10% of full sunlight; carbon dioxide is the major limiting factor in nature."),

        # 50. Cell Biology - Cilia and Flagella Ultrastructure
        ("Cell: The Unit of Life", "Axoneme Microtubule 9+2 Organization and Basal Body", "Direct MCQ",
         "The eukaryotic cilium or flagellum exhibits an axoneme core composed of microtubules arranged in which specific pattern, and arises from which cellular organelle structure?",
         ["$9 + 2$ axoneme arrangement arising from a basal body ($9 + 0$ centriole-like organization)",
          "$9 + 0$ axoneme arrangement arising from a basal body ($9 + 2$ organization)",
          "$9 + 2$ axoneme arrangement arising directly from the nuclear envelope",
          "$9 + 3$ axoneme arrangement arising from a kinetochore"], 0,
         "1. Electron microscopy reveals that eukaryotic cilia and flagella are covered by plasma membrane.\\n2. Their core, called the axoneme, possesses 9 peripheral doublets of microtubules arranged radially around a central pair of single microtubules ($9 + 2$ array).\\n3. The peripheral doublets are interconnected by protein bridges (nexin links) and connected to the central sheath by radial spokes.\\n4. Both cilia and flagella emerge from centriole-like structures called basal bodies, which have a cartwheel arrangement of 9 triplet microtubules with no central microtubule ($9 + 0$ pattern).",
         "Centrioles and basal bodies have $9+0$ triplet arrangement; cilia and flagella axonemes have $9+2$ doublet arrangement.",
         "Eukaryotic cilia and flagella: axoneme has $9+2$ arrangement; basal body has $9+0$ cartwheel arrangement.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Botany topics, got {len(topics_data)}"

    # Dynamic rotation across Mocks 41 to 60 so each mock starts with a distinct chapter sequence
    rotated = topics_data[shift % 50:] + topics_data[:shift % 50]

    for i, item in enumerate(rotated):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 1  # 1 to 50
        sec = "Section A" if q_num <= 35 else "Section B"
        q = NeetQuestion(
            q_num=q_num,
            subject="Botany",
            section=sec,
            chapter=chapter,
            topic=topic,
            q_type=q_type,
            text=text,
            options=options,
            correct_idx=correct_idx,
            solution_steps=solution_steps,
            distractor_analysis=distractor_analysis,
            takeaway=takeaway
        )
        questions.append(q)

    return questions
'''

with open('engine/neet_engine/curriculum_botany_diff.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated engine/neet_engine/curriculum_botany_diff.py successfully!")

