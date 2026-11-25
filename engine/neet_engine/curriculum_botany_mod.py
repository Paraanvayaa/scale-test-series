# -*- coding: utf-8 -*-
"""
Moderate Rigor Full Curriculum Botany Generator for NEET (UG) - Mocks 21 to 40
Calibrated to 2026 NTA NEET-UG distribution:
  - Direct MCQ: 29 (58%)
  - Statement I & II: 7 (14%)
  - Match List: 7 (14%)
  - Assertion & Reason: 4 (8%)
  - Multi-Statement: 3 (6%)
Total: 50 Questions (35 Section A + 15 Section B)
"""
import random
from neet_models import NeetQuestion

def get_botany_questions_mod(mock_num):
    rng = random.Random(mock_num * 3000 + 999)
    questions = []
    
    # 50 Distinct Moderate Botany Topics covering Class 11 & 12 NCERT Syllabus
    botany_topics = [
        # 1. Statement I & II: Biological Classification
        ("Biological Classification", "Nitrogen Fixation and Heterocysts in Cyanobacteria", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Filamentous cyanobacteria such as *Nostoc* and *Anabaena* possess specialised thick-walled cells called heterocysts for atmospheric nitrogen fixation.\n\n"
         "**Statement II:** Heterocysts lack Photosystem II (PS-II) and possess only Photosystem I (PS-I), preventing photosynthetic oxygen evolution that would otherwise irreversibly poison the enzyme nitrogenase.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Nitrogenase enzyme is extremely sensitive to molecular oxygen (irreversibly poisoned by $\\text{O}_2$).\n2. Heterocysts create an anaerobic microenvironment: they possess thick walls impermeable to gas diffusion.\n3. They lack PS-II (so no water splitting or $\\text{O}_2$ evolution occurs), retaining only PS-I for cyclic photophosphorylation to generate ATP required by nitrogenase.\n4. Hence both Statement I and Statement II are completely correct.",
         "Distractors claim PS-II is active or that heterocysts evolve oxygen.", "Heterocysts lack PS-II and have thick oxygen-impermeable walls, protecting nitrogenase from $\\text{O}_2$ inactivation."),

        # 2. Assertion & Reason: Plant Kingdom
        ("Plant Kingdom", "Life Cycle Patterns and Exceptions in Algae", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "**Assertion (A):** Unlike the majority of algal genera which exhibit a haplontic life cycle, the brown alga *Fucus* exhibits a diplontic life cycle.\n\n"
         "**Reason (R):** In *Fucus*, the dominant photosynthetic free-living plant body is a diploid sporophyte, and the haploid phase is represented solely by gametes.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. In most algae (*Spirogyra*, *Volvox*, *Chlamydomonas*), the dominant phase is the free-living haploid gametophyte (haplontic life cycle).\n2. *Fucus*, an advanced brown alga (rockweed), exhibits a diplontic life cycle where the plant body is diploid sporophyte ($2n$) and gametes ($n$) are the only haploid stage.\n3. Therefore, both Assertion (A) and Reason (R) are true, and (R) correctly explains why *Fucus* has a diplontic life cycle.",
         "*Ectocarpus* and *Polysiphonia* are haplo-diplontic.", "*Fucus* uniquely exhibits a diplontic life cycle among algae."),

        # 3. Match List: Morphology (1/7)
        ("Morphology of Flowering Plants", "Position of Floral Parts on Thalamus", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Type of Flower) | List-II (Ovary Position and Examples) |\n"
         "| :--- | :--- |\n"
         "| **A.** Hypogynous | **I.** Superior ovary; sepals, petals, and stamens situated below ovary (Mustard, China rose, Brinjal) |\n"
         "| **B.** Perigynous | **II.** Half-inferior ovary; gynoecium in centre and other parts on rim of thalamus at same level (Plum, Rose, Peach) |\n"
         "| **C.** Epigynous | **III.** Inferior ovary; thalamus margin grows upward enclosing ovary completely and fused with it (Guava, Cucumber, ray florets of Sunflower) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III", "A-II, B-I, C-III", "A-I, B-III, C-II", "A-III, B-II, C-I"], 0,
         "1. Hypogynous: Ovary superior $\\to$ Mustard, China rose, Brinjal (I).\n2. Perigynous: Ovary half-inferior $\\to$ Plum, Rose, Peach (II).\n3. Epigynous: Ovary inferior $\\to$ Guava, Cucumber, Sunflower ray florets (III).",
         "Distractors swap superior (hypogynous) and inferior (epigynous) definitions.", "Ovary position: Hypogynous (superior, Mustard), Perigynous (half-inferior, Rose), Epigynous (inferior, Guava)."),

        # 4. Direct MCQ: Morphology (1/29)
        ("Morphology of Flowering Plants", "Leaf Modifications (Phyllode in Australian Acacia)", "Direct MCQ",
         "In Australian *Acacia*, leaves are small and short-lived. The petioles expand, become green and sickle-shaped, and synthesize food. Such a modified photosynthetic petiole is termed a:",
         ["Phyllode", "Cladode", "Phylloclade", "Scale leaf"], 0,
         "1. A phyllode is a modified, flattened, green, photosynthetic petiole or rachis (e.g. Australian *Acacia*).\n2. A phylloclade is a modified photosynthetic stem of unlimited growth (e.g. *Opuntia*, *Euphorbia*).\n3. A cladode is a photosynthetic stem branch of limited growth, usually one internode long (e.g. *Asparagus*, *Ruscus*).",
         "Phylloclade is a stem modification of unlimited growth (*Opuntia*).", "A phyllode is a green, flattened, photosynthetic petiole found in Australian *Acacia*."),

        # 5. Multi-Statement: Anatomy (1/3)
        ("Anatomy of Flowering Plants", "Components of Periderm in Dicot Stems", "Multi-Statement",
         "Consider the following statements regarding secondary growth and periderm in a dicotyledonous stem:\n\n"
         "A. Phellogen (cork cambium) is a secondary meristem that arises in the cortex region.\n"
         "B. Phellogen cuts off cells towards the outside that differentiate into phellem (cork) with suberized impervious walls.\n"
         "C. Phelloderm is secondary xylem cut off towards the inner side by phellogen.\n"
         "D. Periderm collectively comprises phellogen, phellem, and phelloderm.\n"
         "E. Lenticels are aerating pores formed in the periderm for gaseous exchange.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, D and E only", "A, B and C only", "B, C, D and E only", "A, C and D only"], 0,
         "1. Phellogen develops in the outer cortex during secondary growth (A is correct).\n2. Phellogen cuts off cork (phellem) outwards, which has suberin deposition impermeable to water (B is correct).\n3. Phelloderm is secondary cortex (parenchymatous), NOT secondary xylem (C is incorrect).\n4. Periderm = Phellem + Phellogen + Phelloderm (D is correct).\n5. Lenticels permit gas exchange between internal tissues and outer atmosphere (E is correct).\n6. Therefore, A, B, D and E only are correct.",
         "Statement C erroneously claims phelloderm is secondary xylem.", "Periderm consists of phellogen, phellem, and phelloderm; phelloderm is secondary cortex."),

        # 6. Direct MCQ: Anatomy (2/29)
        ("Anatomy of Flowering Plants", "Stomatal Guard Cell Morphology", "Direct MCQ",
         "Guard cells regulating the opening and closing of stomata differ anatomically between dicots and grasses. In grasses (monocots), the guard cells are characteristically:",
         ["Dumbbell-shaped, with thick inner walls and thin outer bulbous ends",
          "Kidney-shaped (reniform), with thick inner concave walls",
          "Spherical and devoid of chloroplasts",
          "Triangular with radial cellulose microfibrils"], 0,
         "1. In dicotyledonous leaves, guard cells are bean-shaped or kidney-shaped (reniform).\n2. In grasses (monocots like maize, wheat, sugarcane), guard cells are dumbbell-shaped.\n3. In dumbbell-shaped guard cells, the central narrow part has thickened walls while the bulbous ends have thin walls; expansion of the bulbous ends opens the pore.\n4. Guard cells possess chloroplasts and are surrounded by specialized epidermal subsidiary cells.",
         "Kidney-shaped guard cells are characteristic of dicots.", "Guard cells are dumbbell-shaped in grasses (monocots) and bean/kidney-shaped in dicots."),

        # 7. Statement I & II: Cell Biology
        ("Cell - The Unit of Life", "Functions of Glyoxysomes in Plant Seeds", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Glyoxysomes are specialized plant microbodies containing enzymes of the glyoxylate cycle that convert stored lipids into carbohydrates during the germination of fatty seeds such as castor.\n\n"
         "**Statement II:** Glyoxysomes are abundantly present in green photosynthesizing leaves of spinach, where they catalyze the primary steps of photorespiration.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Glyoxysomes are specialized microbodies in germinating fat-storing oil seeds (castor, groundnut) carrying out $\\beta$-oxidation and glyoxylate cycle to convert fats to sucrose (gluconeogenesis); Statement I is correct.\n2. Peroxisomes, not glyoxysomes, are present in green photosynthetic leaves and participate in photorespiration (glycolate metabolism); Statement II is incorrect.\n3. Hence Statement I is correct but Statement II is incorrect.",
         "Peroxisomes function in photorespiration in leaves; glyoxysomes mobilize fats in germinating seeds.", "Glyoxysomes convert fats into sugars in oil seeds; peroxisomes function in photorespiration in green leaves."),

        # 8. Direct MCQ: Cell Division (3/29)
        ("Cell Cycle and Cell Division", "Enzymatic Basis of Genetic Recombination", "Direct MCQ",
         "During the pachytene stage of meiotic Prophase-I, crossing over between non-sister chromatids of homologous chromosomes is an enzyme-mediated process catalyzed by:",
         ["Recombinase (a complex containing endonucleases and ligases)",
          "DNA polymerase I",
          "RNA polymerase III",
          "Peptidyl transferase"], 0,
         "1. In pachytene, recombination nodules appear at intervals on the synaptonemal complex.\n2. Crossing over is the exchange of genetic material between non-sister chromatids of homologous chromosomes.\n3. It is mediated by the enzyme recombinase, which breaks, swaps, and reseals the non-sister chromatid strands.\n4. Recombination is completed by the end of pachytene.",
         "DNA polymerase replicates DNA in S-phase; peptidyl transferase forms peptide bonds.", "Crossing over during pachytene is mediated by the enzyme complex recombinase."),

        # 9. Assertion & Reason: Cell Division
        ("Cell Cycle and Cell Division", "Arrest of Mitosis by Colchicine", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "**Assertion (A):** Treatment of dividing plant root meristematic cells with colchicine arrests mitosis specifically at metaphase and induces polyploidy.\n\n"
         "**Reason (R):** Colchicine binds to tubulin heterodimers, inhibiting microtubule polymerization and preventing mitotic spindle assembly.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Colchicine prevents assembly of mitotic spindle microtubules by binding to free tubulin dimers.\n2. Chromosomes condense and line up at the equatorial plane during metaphase, but cannot separate to opposite poles at anaphase without spindle fibres.\n3. Nuclear membrane reforms around the full duplicated chromosome set ($2n \\to 4n$), doubling chromosome number and inducing polyploidy.\n4. Both Assertion and Reason are true, and (R) provides the exact biochemical explanation for (A).",
         "Colchicine inhibits spindle assembly, not DNA replication.", "Colchicine inhibits tubulin polymerization, arresting mitosis at metaphase and inducing polyploidy."),

        # 10. Direct MCQ: Photosynthesis (4/29)
        ("Photosynthesis in Higher Plants", "Non-Cyclic Photophosphorylation (Z-Scheme) Sequence", "Direct MCQ",
         "In non-cyclic photophosphorylation, the correct sequence of electron transfer from water to $\\text{NADP}^+$ according to redox potential scale is:",
         ["$\\text{H}_2\\text{O} \\to \\text{PS-II} (P_{680}) \\to \\text{Pheophytin} \\to \\text{Plastoquinone (PQ)} \\to \\text{Cytochrome } b_6f \\to \\text{Plastocyanin (PC)} \\to \\text{PS-I} (P_{700}) \\to \\text{Ferredoxin (Fd)} \\to \\text{NADP}^+$",
          "$\\text{PS-I} \\to \\text{PS-II} \\to \\text{Plastoquinone} \\to \\text{Cytochrome } b_6f \\to \\text{NADP}^+$",
          "$\\text{H}_2\\text{O} \\to \\text{PS-I} \\to \\text{Plastocyanin} \\to \\text{PS-II} \\to \\text{Ferredoxin} \\to \\text{NADP}^+$",
          "$\\text{PS-II} \\to \\text{Ferredoxin} \\to \\text{Cytochrome } b_6f \\to \\text{Plastocyanin} \\to \\text{NADP}^+$"], 0,
         "1. Photolysis of water releases electrons to $P_{680}$ (PS-II).\n2. Excited electron is captured by primary acceptor pheophytin, transferred downhill through plastoquinone (PQ), cytochrome $b_6f$ complex, and copper-containing plastocyanin (PC).\n3. PC delivers electron to $P_{700}$ (PS-I).\n4. Excited electron from PS-I is accepted by iron-sulfur protein and ferredoxin (Fd).\n5. $\\text{FNR}$ (ferredoxin-NADP+ reductase) transfers electron to $\\text{NADP}^+$ to form $\\text{NADPH} + \\text{H}^+$.",
         "Distractors swap PS-I and PS-II or invert electron carriers.", "Z-scheme sequence: $\\text{H}_2\\text{O} \\to \\text{PS-II} \\to \\text{PQ} \\to \\text{Cyt } b_6f \\to \\text{PC} \\to \\text{PS-I} \\to \\text{Fd} \\to \\text{NADP}^+$."),

        # 11. Statement I & II: Photosynthesis
        ("Photosynthesis in Higher Plants", "Conditions Favoring Cyclic Photophosphorylation", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Cyclic photophosphorylation occurs predominantly in stroma lamellae membranes because they lack Photosystem II and NADP reductase enzyme.\n\n"
         "**Statement II:** Cyclic photophosphorylation produces both ATP and NADPH, accompanied by the photolysis of water and evolution of oxygen.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Stroma lamellae membranes lack PS-II and $\\text{NADP}$ reductase; hence when illuminated with light of wavelength $>680\\text{ nm}$, only PS-I operates (Statement I is correct).\n2. In cyclic photophosphorylation, excited electrons return to PS-I via ferredoxin and cytochrome $b_6f$, generating a proton gradient for ATP synthesis alone. No $\\text{NADPH}$ is formed, no water is photolyzed, and no oxygen is evolved (Statement II is incorrect).\n3. Therefore, Statement I is correct but Statement II is incorrect.",
         "Cyclic photophosphorylation produces ATP only, with NO NADPH or oxygen.", "Cyclic photophosphorylation generates ATP alone without $\\text{NADPH}$ or $\\text{O}_2$ evolution."),

        # 12. Assertion & Reason: Photosynthesis
        ("Photosynthesis in Higher Plants", "CO2 Saturation and Photorespiration Suppression in C4 Plants", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "**Assertion (A):** $C_4$ plants have higher photosynthetic efficiency and greater biomass productivity than $C_3$ plants under conditions of high light intensity and elevated temperatures.\n\n"
         "**Reason (R):** In $C_4$ bundle sheath cells, decarboxylation of $C_4$ acids maintains a high intracellular $\\text{CO}_2$ concentration around RuBisCO, completely suppressing its oxygenase activity and preventing photorespiration.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Photorespiration (the binding of $\\text{O}_2$ to RuBisCO) wastes up to $25\\%$ of fixed carbon in $C_3$ plants at elevated temperatures.\n2. $C_4$ plants overcome this via Kranz anatomy: mesophyll fixes $\\text{CO}_2$ into oxaloacetate via PEP carboxylase, which is converted to malate and transported to bundle sheath cells.\n3. Malate is decarboxylated in bundle sheath cells, releasing concentrated $\\text{CO}_2$ directly around RuBisCO, ensuring it acts exclusively as a carboxylase.\n4. Both Assertion and Reason are true, and (R) provides the direct scientific rationale for (A).",
         "$C_3$ plants suffer from photorespiration; $C_4$ plants suppress it completely.", "$C_4$ plants maximize productivity by maintaining high $\\text{CO}_2$ around RuBisCO, suppressing photorespiration."),

        # 13. Match List: Respiration (2/7)
        ("Respiration in Plants", "Complexes of Mitochondrial Electron Transport Chain", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Mitochondrial ETS Complex) | List-II (Name and Characteristic Components) |\n"
         "| :--- | :--- |\n"
         "| **A.** Complex I | **I.** NADH dehydrogenase (contains FMN and Fe-S centres) |\n"
         "| **B.** Complex II | **II.** Succinate dehydrogenase (contains FAD and Fe-S centres) |\n"
         "| **C.** Complex III | **III.** Cytochrome $bc_1$ complex (contains Cyt b, Cyt $c_1$, and Fe-S) |\n"
         "| **D.** Complex IV | **IV.** Cytochrome $c$ oxidase (contains Cytochromes a and $a_3$, and two copper centres) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Complex I: NADH:ubiquinone oxidoreductase (NADH dehydrogenase) with FMN $\\to$ I.\n2. Complex II: Succinate:ubiquinone oxidoreductase (Succinate dehydrogenase) with FAD $\\to$ II.\n3. Complex III: Ubiquinol:cytochrome $c$ oxidoreductase (Cytochrome $bc_1$) $\\to$ III.\n4. Complex IV: Cytochrome $c$ oxidase containing Cyt a, $a_3$, and two copper centres transferring electrons to $\\text{O}_2$ $\\to$ IV.",
         "Distractors swap Complex I and Complex II components.", "ETS Complexes: I (NADH dehydrogenase), II (Succinate dehydrogenase), III (Cyt $bc_1$), IV (Cyt $c$ oxidase with two copper centres)."),

        # 14. Direct MCQ: Plant Growth (5/29)
        ("Plant Growth and Development", "Critical Night Length in Short-Day Plants", "Direct MCQ",
         "A short-day plant (SDP) with a critical photoperiod of $12\\text{ hours}$ will flower only when:",
         ["The uninterrupted continuous dark period equals or exceeds its critical dark period of 12 hours",
          "It receives light for more than 14 hours per day",
          "Its dark period is interrupted by a flash of red light",
          "It is kept in continuous illumination without darkness"], 0,
         "1. Short-day plants (SDPs) are more accurately described as long-night plants.\n2. Flowering requires an uninterrupted dark period exceeding a critical dark duration.\n3. If the dark period is interrupted even briefly by a flash of red light ($660\\text{ nm}$), flowering is completely inhibited.\n4. Long-day plants (LDPs) flower when day length exceeds critical photoperiod.",
         "Interruption of dark period by red light inhibits SDP flowering.", "Short-day plants flower only when the continuous, uninterrupted night length exceeds critical dark duration."),

        # 15. Statement I & II: Reproduction
        ("Sexual Reproduction in Flowering Plants", "Invariable Autogamy in Cleistogamous Flowers", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Cleistogamous flowers of *Viola*, *Oxalis*, and *Commelina* never open, ensuring assured seed-set even in the complete absence of pollinators through obligate autogamy.\n\n"
         "**Statement II:** Continuous cleistogamy generates immense genetic variation and completely prevents inbreeding depression in subsequent generations.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Cleistogamous flowers remain permanently closed; pollen falls directly on stigma of same flower, providing assured seed-set without pollinators (Statement I is correct).\n2. Because cross-pollination is completely impossible, obligate self-pollination leads to homozygous inbreeding depression and lack of genetic diversity (Statement II is incorrect).\n3. Hence Statement I is correct but Statement II is incorrect.",
         "Cleistogamy leads to inbreeding depression, not increased genetic variation.", "Cleistogamous flowers ensure seed-set without pollinators, but cause inbreeding depression due to obligate autogamy."),

        # 16. Direct MCQ: Genetics (6/29)
        ("Principles of Inheritance and Variation", "Genetic Linkage Mapping Calculation", "Direct MCQ",
         "In a dihybrid test cross between $AaBb \\times aabb$, the progeny obtained are: $420$ $AB/ab$, $430$ $ab/ab$, $75$ $Ab/ab$, and $75$ $aB/ab$ (total 1000 progeny). The recombination frequency and map distance between genes $A$ and $B$ are:",
         ["15% recombination frequency, corresponding to 15 cM (map units)",
          "7.5% recombination frequency, corresponding to 7.5 cM",
          "30% recombination frequency, corresponding to 30 cM",
          "85% recombination frequency, corresponding to 85 cM"], 0,
         "1. Parental types: $AB/ab$ (420) + $ab/ab$ (430) = 850.\n2. Recombinant types: $Ab/ab$ (75) + $aB/ab$ (75) = 150.\n3. Recombination Frequency ($RF$):\n   $$RF = \\frac{\\text{Total Recombinants}}{\\text{Total Progeny}} \\times 100 = \\frac{150}{1000} \\times 100 = 15\\%$$.\n4. Alfred Sturtevant defined 1 map unit (centiMorgan, cM) as $1\\%$ recombination.\n5. Hence the genetic distance between genes $A$ and $B$ is $15\\text{ cM}$ (or 15 map units).",
         "7.5% considers only one recombinant class; 85% is parental frequency.", "Recombination frequency $= \\frac{\\text{Recombinants}}{\\text{Total}} \\times 100$. $1\\% RF = 1\\text{ cM}$ map unit."),

        # 17. Match List: Genetics (3/7)
        ("Principles of Inheritance and Variation", "Patterns of Inheritance in Human Pedigrees", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Genetic Disorder) | List-II (Mode of Inheritance / Pedigree Signature) |\n"
         "| :--- | :--- |\n"
         "| **A.** Haemophilia / Colour blindness | **I.** X-linked recessive (criss-cross inheritance: carrier mother to affected son) |\n"
         "| **B.** Myotonic dystrophy | **II.** Autosomal dominant (affected child must have at least one affected parent, no skipped generations) |\n"
         "| **C.** Sickle cell anaemia / Phenylketonuria | **III.** Autosomal recessive (unaffected carrier parents can produce affected child, skips generations) |\n"
         "| **D.** Hypertrichosis of ear pinna | **IV.** Y-linked (holandric, strictly father to all sons) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Haemophilia: X-linked recessive $\\to$ I.\n2. Myotonic dystrophy: Autosomal dominant (NCERT pedigree diagram example) $\\to$ II.\n3. Sickle cell anaemia: Autosomal recessive (chromosome 11, $Hb^S$) $\\to$ III.\n4. Hypertrichosis: Y-linked holandric trait $\\to$ IV.",
         "Distractors confuse autosomal dominant (Myotonic dystrophy) with autosomal recessive (Sickle cell).", "Pedigree modes: X-linked recessive (criss-cross), Autosomal dominant (no skips), Autosomal recessive (skips generations)."),

        # 18. Match List: Genetics (4/7)
        ("Principles of Inheritance and Variation", "Chromosomal Disorders and Karyotypes", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Genetic Syndrome) | List-II (Karyotype and Characteristic Symptoms) |\n"
         "| :--- | :--- |\n"
         "| **A.** Down's syndrome | **I.** Trisomy of chromosome 21 ($47, XX+21$ or $47, XY+21$); furrowed tongue, flat face, broad palm with single crease |\n"
         "| **B.** Klinefelter's syndrome | **II.** $47, XXY$; overall masculine development with feminine features (gynaecomastia), sterile male |\n"
         "| **C.** Turner's syndrome | **III.** $45, XO$; sterile female with rudimentary ovaries, webbed neck, lack of secondary sexual characters |\n"
         "| **D.** Thalassemia | **IV.** Quantitative defect in globin chain synthesis on autosomes (chromosome 16 or 11) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Down's syndrome: Trisomy 21 (discovered by Langdon Down, 1866) $\\to$ I.\n2. Klinefelter's syndrome: Karyotype 47, XXY, gynaecomastia, sterile $\\to$ II.\n3. Turner's syndrome: Monosomy of X (45, XO), rudimentary ovaries $\\to$ III.\n4. Thalassemia: Quantitative globin synthesis defect (autosomal recessive) $\\to$ IV.",
         "Distractors swap Klinefelter (XXY) and Turner (XO) karyotypes.", "Chromosomal syndromes: Down (Trisomy 21), Klinefelter (47, XXY sterile male), Turner (45, XO sterile female)."),

        # 19. Multi-Statement: Molecular Basis (2/3)
        ("Molecular Basis of Inheritance", "Semiconservative DNA Replication Evidence", "Multi-Statement",
         "Consider the following statements regarding the experimental proof of semi-conservative DNA replication by Meselson and Stahl (1958):\n\n"
         "A. *E. coli* cells were grown for many generations in a medium containing $^{15}\\text{NH}_4\\text{Cl}$ as the sole nitrogen source.\n"
         "B. $^{15}\\text{N}$ is a radioactive isotope of nitrogen with a short half-life.\n"
         "C. Heavy and light DNA molecules were separated by density gradient centrifugation in cesium chloride ($\\text{CsCl}$).\n"
         "D. After one generation of transfer to $^{14}\\text{N}$ medium ($20\\text{ minutes}$), all extracted DNA molecules had an intermediate hybrid density.\n"
         "E. After two generations ($40\\text{ minutes}$), the extracted DNA consisted of equal proportions of light and hybrid density molecules.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, C, D and E only", "A, B and C only", "B, C and D only", "A, B, D and E only"], 0,
         "1. $^{15}\\text{N}$ is a heavy stable isotope of nitrogen, NOT a radioactive isotope (B is incorrect).\n2. Density gradient centrifugation in $\\text{CsCl}$ separates $^{15}\\text{N}$ and $^{14}\\text{N}$ based on buoyant density (C is correct).\n3. After 20 min (generation 1), $100\\%$ of DNA is hybrid ($^{15}\\text{N}-^{14}\\text{N}$) (D is correct).\n4. After 40 min (generation 2), DNA consists of $50\\%$ hybrid and $50\\%$ light ($1:1$) (E is correct).\n5. Therefore, statements A, C, D and E only are correct.",
         "Statement B is false because $^{15}\\text{N}$ is a stable isotope, not radioactive.", "Meselson-Stahl used heavy non-radioactive $^{15}\\text{N}$ and CsCl density centrifugation to prove semiconservative replication."),

        # 20. Assertion & Reason: Molecular Basis
        ("Molecular Basis of Inheritance", "Hershey-Chase Bacteriophage Experiment", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "**Assertion (A):** In the Hershey-Chase experiment, when *E. coli* cells were infected with $^{35}\\text{S}$-labelled bacteriophages, radioactivity was detected primarily in the supernatant rather than the bacterial pellet after centrifugation.\n\n"
         "**Reason (R):** Sulfur is incorporated into sulfur-containing amino acids (methionine and cysteine) of viral capsid proteins, but is entirely absent from the DNA sugar-phosphate backbone.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Viral protein coats remain on the outside of the host bacterial cell during infection.\n2. Blending detaches the viral coats from bacteria, and centrifugation leaves the lighter protein ghosts in the supernatant.\n3. Since $^{35}\\text{S}$ specifically labels viral protein (due to methionine/cysteine) and not DNA, radioactivity stays in the supernatant.\n4. Both Assertion and Reason are true, and (R) correctly explains why $^{35}\\text{S}$ marks protein rather than DNA.",
         "$^{32}\\text{P}$ was found in the pellet (DNA); $^{35}\\text{S}$ in the supernatant (protein).", "Hershey and Chase used $^{35}\\text{S}$ (protein) and $^{32}\\text{P}$ (DNA) to prove DNA is the genetic material."),

        # 21. Match List: Biotechnology (5/7)
        ("Biotechnology - Principles and Processes", "Selectable Markers and Restriction Sites on pBR322", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Restriction Site on pBR322) | List-II (Selectable Marker Gene Affected) |\n"
         "| :--- | :--- |\n"
         "| **A.** *BamHI* / *SalI* | **I.** Tetracycline resistance gene ($tet^R$) |\n"
         "| **B.** *PstI* / *PvuI* | **II.** Ampicillin resistance gene ($amp^R$) |\n"
         "| **C.** *EcoRI* / *ClaI* / *HindIII* | **III.** Neither marker (located outside antibiotic resistance genes) |\n"
         "| **D.** *PvuII* | **IV.** *rop* gene (codes for proteins involved in plasmid replication) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. *BamHI* and *SalI* reside within the $tet^R$ gene $\\to$ I.\n2. *PstI* and *PvuI* reside within the $amp^R$ gene $\\to$ II.\n3. *EcoRI*, *ClaI*, *HindIII* lie outside both antibiotic resistance markers $\\to$ III.\n4. *PvuII* lies within the *rop* gene $\\to$ IV.",
         "Distractors swap *BamHI* (tetR) with *PstI* (ampR).", "On pBR322: *BamHI/SalI* in $tet^R$, *PstI/PvuI* in $amp^R$, *PvuII* in $rop$."),

        # 22. Direct MCQ: Biotechnology (7/29)
        ("Biotechnology - Principles and Processes", "Insertional Inactivation of lacZ Gene", "Direct MCQ",
         "In recombinant DNA technology, blue-white colony screening differentiates transformants carrying recombinant plasmids from non-recombinants based on insertional inactivation of the enzyme:",
         ["$\\beta$-galactosidase (encoded by $lacZ$), where recombinants form white colonies in the presence of chromogenic substrate X-gal",
          "Taq DNA polymerase",
          "DNA ligase",
          "Alkaline phosphatase"], 0,
         "1. A foreign DNA fragment is inserted within the coding sequence of the enzyme $\\beta$-galactosidase ($lacZ$ gene).\n2. This insertion disrupts the reading frame, inactivating the enzyme (insertional inactivation).\n3. Non-recombinants produce active $\\beta$-galactosidase, hydrolysing chromogenic substrate (X-gal) to produce blue-coloured colonies.\n4. Recombinants with inactivated enzyme fail to hydrolyse X-gal and appear as white colonies.",
         "Distractors claim recombinants form blue colonies (inverting color screening).", "Insertional inactivation of $lacZ$ ($\\beta$-galactosidase) causes recombinant colonies to appear white on X-gal."),

        # 23. Statement I & II: Biotechnology
        ("Biotechnology and Its Applications", "Mechanism of RNA Interference against Nematodes", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** RNA interference (RNAi) is a gene silencing mechanism present in all eukaryotic organisms as a method of cellular defense against viral infection and transposable genetic elements.\n\n"
         "**Statement II:** In RNAi technology against the nematode *Meloidogyne incognita*, transgenic host tobacco plants produce both sense and antisense RNA, which form double-stranded RNA (dsRNA) that initiates specific mRNA cleavage.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. RNAi takes place in all eukaryotic organisms as a method of cellular defense (Statement I is correct).\n2. Using *Agrobacterium* vectors, nematode-specific genes were introduced into the tobacco host, synthesizing both sense and antisense RNA.\n3. These two complementary RNAs form double-stranded RNA (dsRNA) that binds to RISC and silences the specific nematode mRNA, preventing infestation (Statement II is correct).\n4. Both Statement I and Statement II are correct.",
         "Distractors propose that RNAi works via single-stranded DNA probes.", "RNAi silences nematode mRNA via complementary dsRNA produced inside the transgenic host plant."),

        # 24. Direct MCQ: Ecology (8/29)
        ("Organisms and Populations", "Logistic vs Exponential Growth Equations", "Direct MCQ",
         "In nature, a population growing in a habitat with limited resources exhibits logistic growth described by the Verhulst-Pearl Logistic equation: $\\frac{dN}{dt} = rN\\left(\\frac{K - N}{K}\\right)$. In this equation, when population size $N$ approaches the carrying capacity $K$ ($N \\to K$), the population growth rate $\\frac{dN}{dt}$:",
         ["Approaches zero, reaching a stable asymptote (stationary phase)",
          "Increases exponentially without limit",
          "Becomes negative and crashes instantly to zero",
          "Equals the intrinsic rate of natural increase $r$"], 0,
         "1. Logistic growth equation: $\\frac{dN}{dt} = rN\\left(1 - \\frac{N}{K}\\right)$.\n2. As population density $N$ approaches environmental carrying capacity $K$, the term $\\left(1 - \\frac{N}{K}\\right)$ approaches $(1 - 1) = 0$.\n3. Therefore, growth rate $\\frac{dN}{dt} \\to 0$.\n4. The sigmoid (S-shaped) curve levels off into an asymptote (stationary plateau).",
         "Option (2) describes exponential J-shaped growth where resources are unlimited.", "In logistic growth, as $N \\to K$, the term $(1 - N/K) \\to 0$, causing population growth rate $dN/dt$ to approach zero."),

        # 25. Direct MCQ: Ecology (9/29)
        ("Biodiversity and Conservation", "Alexander von Humboldt's Species-Area Relationship", "Direct MCQ",
         "The relationship between species richness ($S$) and area ($A$) explored by Alexander von Humboldt is rectangular hyperbola on a linear scale, given on a logarithmic scale as: $\\log S = \\log C + Z \\log A$. For very large areas like entire continents, the regression coefficient (slope $Z$) typically ranges between:",
         ["0.6 to 1.2", "0.1 to 0.2", "0.01 to 0.05", "1.5 to 2.5"], 0,
         "1. Ecologists have discovered that for small regional areas (e.g. plants in Britain, birds in California), the slope $Z$ lies in the narrow range of $0.1$ to $0.2$, regardless of taxonomic group.\n2. When the species-area relationship is analysed across vastly larger areas like an entire continent, the slope of the line becomes much steeper, with $Z$ values in the range of $0.6$ to $1.2$ (e.g. frugivorous birds in tropical forests have $Z = 1.15$).",
         "0.1 to 0.2 applies to small regional areas, not entire continents.", "The slope $Z$ of species-area relationship is $0.1 - 0.2$ for small regions, and steepens to $0.6 - 1.2$ for entire continents.")
    ]

    # Additional 25 high-yield moderate topics to complete 50
    more_botany = [
        # 26. Direct MCQ: Ecology (10/29)
        ("Organisms and Populations", "Allen's Rule of Ecological Adaptation", "Direct MCQ",
         "According to Allen's Rule, mammals living in colder polar climates typically possess:",
         ["Shorter ears and shorter limbs to minimize heat loss through body surface area",
          "Larger ears to dissipate excess heat efficiently",
          "Thin layer of subcutaneous fat to facilitate cooling",
          "Higher metabolic respiration rates with large appendages"], 0,
         "1. Allen's Rule states that mammals from colder climates have shorter ears, tails, and limbs (extremities).\n2. Shorter appendages decrease the surface-area-to-volume ratio, conserving core body heat.\n3. Bergmann's rule states that body size tends to be larger in colder climates.\n4. Desert animals (like Fennec fox) have very large ears to dissipate heat.",
         "Larger ears characterize warm desert animals for heat dissipation.", "Allen's rule states that cold-climate mammals have shorter ears and limbs to minimize surface heat loss."),

        # 27. Match List: Ecology (6/7)
        ("Biodiversity and Conservation", "The Evil Quartet of Biodiversity Loss", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Cause of Biodiversity Loss) | List-II (Textbook Example) |\n"
         "| :--- | :--- |\n"
         "| **A.** Habitat loss and fragmentation | **I.** Amazon rainforest cleared for soybean cultivation and beef cattle pastures |\n"
         "| **B.** Over-exploitation | **II.** Extinction of Steller's sea cow and Passenger pigeon by humans |\n"
         "| **C.** Alien species invasion | **III.** Introduction of Nile perch into Lake Victoria causing extinction of >200 cichlid fish species |\n"
         "| **D.** Co-extinctions | **IV.** Obligate mutualism between yucca plant and pronuba moth |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Habitat loss: Amazon clearing $\\to$ I.\n2. Over-exploitation: Steller's sea cow and Passenger pigeon $\\to$ II.\n3. Alien invasion: Nile perch in Lake Victoria; *Lantana*, *Eichhornia*, *Clarias gariepinus* $\\to$ III.\n4. Co-extinction: Host-parasite or pollinator-plant mutualism $\\to$ IV.",
         "Distractors swap alien invasion with over-exploitation.", "The Evil Quartet: Habitat loss (Amazon), Over-exploitation (Steller's cow), Alien invasion (Nile perch), Co-extinction."),

        # 28. Multi-Statement: Ecology (3/3)
        ("Organisms and Populations", "Adaptations to Extreme Environmental Conditions", "Multi-Statement",
         "Consider the following statements regarding ecological adaptations in plants and animals:\n\n"
         "A. Desert plants like *Opuntia* have leaves modified into spines and stems flattened into photosynthetic phylloclades.\n"
         "B. Stomata in xerophytic plants are sunken in deep pits (sunken stomata) and operate through CAM pathway to minimize transpiration.\n"
         "C. Kangaroo rat in North American deserts can meet all its internal water requirements through metabolic oxidation of fats.\n"
         "D. Allen's Rule states that mammals inhabiting polar climates have longer ears and limbs to radiate body heat.\n"
         "E. Halophytes like *Rhizophora* growing in saline swamps possess specialized negative geotropic breathing roots called pneumatophores.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and E only", "A, B and D only", "B, C, D and E only", "A, C and D only"], 0,
         "1. Opuntia leaves are reduced to spines; stem forms succulent phylloclade (A is correct).\n2. Sunken stomata and CAM reduce transpiration loss (B is correct).\n3. Kangaroo rat survives without drinking water via metabolic water from fat oxidation (C is correct).\n4. Allen's Rule states polar mammals have SHORTER ears and limbs to reduce heat loss, not longer (D is incorrect).\n5. Pneumatophores in Rhizophora grow vertically upwards to obtain oxygen (E is correct).\n6. Therefore, A, B, C and E only are correct.",
         "Statement D violates Allen's rule by claiming polar mammals have longer limbs.", "Adaptations: Opuntia (phylloclade), CAM (water conservation), Kangaroo rat (metabolic water), Pneumatophores (aeration)."),

        # 29. Statement I & II: Ecology
        ("Environmental Issues / Ecosystem", "Biochemical Oxygen Demand (BOD) and Eutrophication", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Discharge of untreated municipal sewage rich in biodegradable organic matter into a river causes a sharp rise in Biochemical Oxygen Demand (BOD).\n\n"
         "**Statement II:** A high BOD value is accompanied by a dramatic increase in dissolved oxygen (DO), resulting in rapid proliferation and flourishing of fish populations.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Microorganisms consume dissolved oxygen to decompose biodegradable organic matter, causing BOD to surge (Statement I is correct).\n2. Because microbes consume the dissolved oxygen, DO drops catastrophically, suffocating and killing fishes and other aquatic organisms (Statement II is incorrect).\n3. Therefore, Statement I is correct but Statement II is incorrect.",
         "Distractors claim DO increases with rising BOD.", "Discharge of sewage causes a sharp rise in BOD accompanied by a catastrophic drop in dissolved oxygen."),

        # 30. Direct MCQ: Environmental Issues (11/29)
        ("Environmental Issues / Ecosystem", "Biomagnification of DDT in Aquatic Food Chain", "Direct MCQ",
         "Biomagnification refers to increase in concentration of a persistent toxicant at successive trophic levels. In an aquatic food chain contaminated with DDT, the highest concentration of DDT ($25\\text{ ppm}$) is found in:",
         ["Fish-eating birds (Top carnivores)", "Large predatory fishes", "Small fishes", "Phytoplankton"], 0,
         "1. DDT cannot be metabolized or excreted by organisms, so it accumulates in fat tissue.\n2. Progressive biomagnification levels:\n   - Water: $0.003\\text{ ppb}$\n   - Zooplankton: $0.04\\text{ ppm}$\n   - Small fish: $0.5\\text{ ppm}$\n   - Large fish: $2\\text{ ppm}$\n   - Fish-eating birds: $25\\text{ ppm}$ (ten-million-fold magnification!).\n3. High DDT disturbs calcium metabolism in birds, causing premature thinning of eggshells and bird population decline.",
         "Phytoplankton have the lowest concentration; fish-eating birds have the highest.", "Biomagnification concentrates DDT up to $25\\text{ ppm}$ in top trophic consumers (fish-eating birds)."),

        # 31. Direct MCQ: Cell Biology (12/29)
        ("Cell: The Unit of Life", "Chloroplast Thylakoid Stacking", "Direct MCQ",
         "In eukaryotic chloroplasts, flattened membranous sacs called thylakoids are arranged in stacks like piles of coins called grana. The connecting membranous tubules between adjacent grana are termed:",
         ["Stroma lamellae (fret membranes)", "Cristae", "Cisternae", "Mesosomes"], 0,
         "1. Thylakoids are arranged in stacks called grana (granum singular).\n2. Flat membranous tubules called stroma lamellae interconnect the thylakoids of different grana.\n3. Cristae are folds in mitochondria; cisternae are flattened Golgi sacs; mesosomes are prokaryotic infoldings.",
         "Cristae belong to mitochondria; cisternae belong to Golgi.", "Stroma lamellae connect thylakoids of adjacent grana in the chloroplast."),

        # 32. Direct MCQ: Cell Division (13/29)
        ("Cell Cycle and Cell Division", "Anaphase Centromere Splitting", "Direct MCQ",
         "The key landmark event of mitotic anaphase that ensures equal distribution of genetic material to daughter cells is:",
         ["Simultaneous splitting of the centromere of each chromosome and separation of sister chromatids",
          "Condensation of chromatin fibres into distinct chromosomes",
          "Alignment of chromosomes at the equatorial spindle plate",
          "Reformation of nuclear envelope and nucleolus"], 0,
         "1. In Metaphase, chromosomes align at equatorial plate held by spindle fibres attached to kinetochores.\n2. At the onset of Anaphase, each chromosome's centromere splits simultaneously.\n3. Sister chromatids separate and become daughter chromosomes of the future daughter nuclei, moving towards opposite poles by spindle shortening.",
         "Alignment is metaphase; reformation of envelope is telophase.", "Anaphase is demarcated by centromere splitting and poleward migration of sister chromatids."),

        # 33. Match List: Plant Physiology (7/7)
        ("Plant Growth and Development", "Phytohormones and Physiological Responses", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Plant Growth Regulator) | List-II (Specific Physiological Function) |\n"
         "| :--- | :--- |\n"
         "| **A.** Auxin (IAA) | **I.** Apical dominance, initiation of rooting in stem cuttings, and prevention of premature fruit drop |\n"
         "| **B.** Gibberellin (GA3) | **II.** Bolting in rosette plants, elongation of sugarcane internodes, and speeding up malting process |\n"
         "| **C.** Cytokinin (Zeatin) | **III.** Overcoming apical dominance, delay of leaf senescence, and lateral shoot growth |\n"
         "| **D.** Abscisic acid (ABA) | **IV.** Stomatal closure during water stress, induction of seed dormancy, and general growth inhibitor |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV", "A-II, B-I, C-III, D-IV", "A-I, B-II, C-IV, D-III", "A-III, B-II, C-I, D-IV"], 0,
         "1. Auxin (IAA): Induces apical dominance, rooting, parthenocarpy in tomatoes $\\to$ I.\n2. Gibberellin (GA3): Promotes bolting (internode elongation before flowering in beet/cabbage) and malting in brewing $\\to$ II.\n3. Cytokinin: Promotes cell division, counteracts apical dominance, delays senescence (Richmond-Lang effect) $\\to$ III.\n4. Abscisic acid (ABA): Acts as stress hormone, triggers stomatal closure, induces seed dormancy $\\to$ IV.",
         "Distractors swap auxin (apical dominance) and cytokinin (counteracts apical dominance).", "Phytohormone roles: Auxin (apical dominance), GA (bolting/malting), Cytokinin (delays senescence), ABA (stress/stomatal closure)."),

        # 34. Direct MCQ: Photosynthesis (14/29)
        ("Photosynthesis in Higher Plants", "Kranz Anatomy Dimorphic Chloroplasts", "Direct MCQ",
         "In $C_4$ plants displaying Kranz anatomy, the bundle sheath cells possess chloroplasts that are characteristically:",
         ["Agranic (lacking grana), large in size, with thick impermeable walls and no intercellular spaces",
          "Granic with active PS-II and thin walls",
          "Small, rudimentary with no starch grains",
          "Identical in ultrastructure to mesophyll chloroplasts"], 0,
         "1. $C_4$ plants have dimorphic chloroplasts:\n   - Mesophyll cells: Small chloroplasts with well-developed grana (active PS-II).\n   - Bundle sheath cells: Large, agranic chloroplasts (lacking grana, only stroma thylakoids) containing high levels of RuBisCO and starch grains.\n2. Bundle sheath cells have thick walls impervious to gaseous exchange and lack intercellular spaces to prevent oxygen entry.",
         "Bundle sheath chloroplasts lack grana; mesophyll chloroplasts possess grana.", "Bundle sheath chloroplasts in $C_4$ plants are large, agranic (lacking grana), and specialized for the Calvin cycle."),

        # 35. Direct MCQ: Respiration (15/29)
        ("Respiration in Plants", "Terminal Electron Acceptor in Aerobic Respiration", "Direct MCQ",
         "In mitochondrial oxidative phosphorylation, the ultimate terminal acceptor of electrons at the end of the electron transport chain (Complex IV) is:",
         ["Molecular oxygen ($\\text{O}_2$), which is reduced to water",
          "Cytochrome c",
          "$\\text{NAD}^+$",
          "Ubiquinone"], 0,
         "1. Electrons from NADH and $\\text{FADH}_2$ travel through Complexes I, II, III, and IV.\n2. At Complex IV (cytochrome $c$ oxidase), electrons are transferred to molecular oxygen:\n   $$\\frac{1}{2}\\text{O}_2 + 2\\text{H}^+ + 2e^- \\to \\text{H}_2\\text{O}$$.\n3. Oxygen acts as the final terminal electron and proton acceptor, driving the entire respiratory electron flow.",
         "$\\text{NAD}^+$ is an electron carrier; $\\text{O}_2$ is the terminal electron acceptor.", "Molecular oxygen ($\\text{O}_2$) is the terminal electron acceptor in aerobic respiration, forming water."),

        # 36. Direct MCQ: Reproduction (16/29)
        ("Sexual Reproduction in Flowering Plants", "Apomixis and Polyembryony in Citrus", "Direct MCQ",
         "In *Citrus* and mango varieties, multiple embryos are frequently observed in a single seed (polyembryony). These maternal embryos arise from:",
         ["Nucellar cells surrounding the embryo sac protruding into it and developing into embryos without fertilization",
          "Multiple pollen tubes fertilizing several egg cells simultaneously",
          "Cleavage of a single diploid zygote into multiple blastomeres",
          "Synergids and antipodals undergoing syngamy"], 0,
         "1. Apomixis is a form of asexual reproduction that mimics sexual reproduction, producing seeds without fertilization.\n2. In *Citrus*, adventive embryony occurs: diploid cells of the maternal nucellus surrounding the embryo sac start dividing, protrude into the embryo sac, and develop into mature embryos.\n3. In such species, each ovule contains many embryos (polyembryony) of maternal genotype.",
         "Distractors suggest multiple pollen tubes or zygotic cleavage.", "Nucellar adventive polyembryony in *Citrus* produces maternal embryos without fertilization."),

        # 37. Direct MCQ: Genetics (17/29)
        ("Principles of Inheritance and Variation", "Test Cross Utility in Genetics", "Direct MCQ",
         "A genetic test cross is performed by crossing an organism exhibiting a dominant phenotype with an organism of known:",
         ["Homozygous recessive genotype ($aa$)",
          "Homozygous dominant genotype ($AA$)",
          "Heterozygous genotype ($Aa$)",
          "Wild-type parent of either sex"], 0,
         "1. An organism showing dominant phenotype could be homozygous ($AA$) or heterozygous ($Aa$).\n2. To determine its unknown genotype, it is crossed with a homozygous recessive tester parent ($aa$).\n3. If unknown is $AA$, all progeny show dominant phenotype ($100\\%$).\n4. If unknown is $Aa$, progeny show a $1:1$ ratio of dominant to recessive.",
         "Crossing with dominant ($AA$) would mask recessive alleles entirely.", "A test cross crosses an individual of dominant phenotype with a homozygous recessive parent ($aa$) to reveal genotype."),

        # 38. Direct MCQ: Molecular Basis (18/29)
        ("Molecular Basis of Inheritance", "Function of Histone H1", "Direct MCQ",
         "In the eukaryotic chromatin nucleosome core particle, which histone protein is NOT part of the central octamer, but binds to the linker DNA sealing the entering and exiting DNA turns?",
         ["Histone H1", "Histone H2A", "Histone H2B", "Histone H3"], 0,
         "1. The nucleosome core octamer consists of two molecules each of four core histones: H2A, H2B, H3, and H4 ($2 \\times 4 = 8$ proteins).\n2. Histone H1 (linker histone) binds outside the core octamer at the site where DNA enters and leaves the nucleosome, stabilizing the 30-nm solenoid chromatin fibre.",
         "H2A, H2B, H3, and H4 form the internal octamer.", "Histone H1 binds to the outside of the nucleosome, locking the DNA wrapped around the core octamer."),

        # 39. Direct MCQ: Molecular Basis (19/29)
        ("Molecular Basis of Inheritance", "Rho and Sigma Factors in Transcription", "Direct MCQ",
         "In prokaryotic transcription by RNA polymerase, initiation and termination of RNA chain synthesis are directed respectively by transient association with:",
         ["Sigma factor ($\\sigma$) for initiation AND Rho factor ($\\rho$) for termination",
          "Rho factor ($\\rho$) for initiation AND Sigma factor ($\\sigma$) for termination",
          "TATA-binding protein for initiation AND Poly-A polymerase for termination",
          "Ribozyme for initiation AND Spliceosome for termination"], 0,
         "1. Prokaryotic RNA polymerase core enzyme ($\\alpha_2 \\beta \\beta' \\omega$) is capable of elongation but cannot recognize promoters alone.\n2. Association with the initiation factor sigma ($\\sigma$) confers sequence specificity, enabling binding to promoter consensus sequences ($-10$ and $-35$ boxes).\n3. After elongation, association with the termination factor rho ($\\rho$) unwinds RNA-DNA hybrid, terminating transcription.",
         "Distractors swap sigma (initiation) and rho (termination).", "Sigma factor ($\\sigma$) initiates transcription; Rho factor ($\\rho$) terminates transcription in prokaryotes."),

        # 40. Direct MCQ: Biotechnology (20/29)
        ("Biotechnology - Principles and Processes", "Elution in Agarose Gel Electrophoresis", "Direct MCQ",
         "In recombinant DNA technology, the process of cutting out the separated band of DNA from an agarose gel and extracting the DNA from the gel piece is termed:",
         ["Elution", "Spooling", "Transformation", "Downstream processing"], 0,
         "1. After DNA fragments separate by electrophoresis and are visualized under UV light with ethidium bromide, the desired band is cut out from the agarose gel.\n2. The extraction and purification of DNA from this excised gel slice is called elution.\n3. Spooling is the collection of precipitated DNA on a glass rod after adding chilled ethanol.",
         "Spooling refers to winding precipitated DNA on a glass rod.", "Cutting out the DNA band from agarose gel and extracting it is called elution."),

        # 41. Direct MCQ: Biotechnology (21/29)
        ("Biotechnology and Its Applications", "Golden Rice Beta-Carotene Enrichment", "Direct MCQ",
         "Golden Rice is a genetically modified biofortified crop developed to alleviate malnutrition and childhood blindness in developing nations by engineering it to synthesize:",
         ["$\\beta$-carotene (provitamin A precursor)",
          "Vitamin C (ascorbic acid)",
          "Iron and zinc minerals only",
          "Essential amino acid lysine"], 0,
         "1. Golden Rice (*Oryza sativa*) was genetically engineered by Ingo Potrykus and Peter Beyer.\n2. Genes encoding phytoene synthase and phytoene desaturase were introduced into the rice genome.\n3. This enables biosynthesis of yellow-orange $\\beta$-carotene (provitamin A) in the edible rice endosperm.\n4. In the human body, $\\beta$-carotene is cleaved into active vitamin A (retinol), preventing night blindness and xerophthalmia.",
         "Distractors name Vitamin C or minerals.", "Golden Rice is a genetically engineered transgenic crop enriched in $\\beta$-carotene (provitamin A)."),

        # 42. Direct MCQ: Ecology (22/29)
        ("Organisms and Populations", "Commensalism Ecological Interactions", "Direct MCQ",
         "Which of the following biological pairs represents an ecological interaction of COMMENSALISM ($+/0$), where one species benefits while the other is neither harmed nor benefited?",
         ["An orchid growing as an epiphyte on the branch of a mango tree",
          "Lichen composed of a fungus and an alga",
          "Cuckoo bird laying eggs in the nest of a crow (brood parasitism)",
          "*Cuscuta* growing on a hedge plant"], 0,
         "1. Commensalism ($+/0$): Epiphytic orchid gains structural support, light, and canopy moisture without absorbing sap from the host mango tree (mango is unaffected $0$).\n2. Other examples: Barnacles on whale back, cattle egret foraging near grazing cattle, sea anemone and clownfish.\n3. Lichen is mutualism ($+/+$); Brood parasitism and *Cuscuta* are parasitism ($+/-$).",
         "Lichen is mutualism; *Cuscuta* is a parasitic plant that absorbs nutrients.", "An orchid epiphyte on a mango tree represents commensalism ($+/0$)."),

        # 43. Direct MCQ: Ecosystem (23/29)
        ("Ecosystem", "Ten Percent Law and Trophic Transfer", "Direct MCQ",
         "Lindeman's 10 percent law of energy transfer across trophic levels in an ecosystem states that only $10\\%$ of the energy of organic food is transferred to the next higher level. The remaining $90\\%$ is primarily:",
         ["Dissipated as heat during respiration, metabolism, and lost as unconsumed waste/feces",
          "Stored permanently as indestructible biomass",
          "Absorbed by decomposers instantly without heat emission",
          "Radiated into space as visible photons"], 0,
         "1. According to Raymond Lindeman (1942), only about $10\\%$ of energy entering a trophic level is incorporated into new biomass available to the next consumer.\n2. The bulk ($~90\\%$) is consumed in basal cellular respiration, physical locomotion, thermoregulation, and dissipated irreversibly into the environment as low-grade heat, or lost in excretory feces.",
         "Distractors claim energy is stored permanently without respiratory dissipation.", "Only ~10% of energy is passed to the next trophic level; ~90% is dissipated as metabolic heat and waste."),

        # 44. Statement I & II: Ecology (7/7)
        ("Organisms and Populations", "Mutualism between Fig and Blastophaga Wasp", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** The mutualistic association between the fig tree (*Ficus*) and the pollinator wasp (*Blastophaga*) is a tight co-evolutionary obligate relationship.\n\n"
         "**Statement II:** The female wasp pollinates the fig inflorescence while ovipositing her eggs inside the unfertilized ovaries, and the developing wasp larvae feed on some of the developing seeds.\n\n"
         "In the light of the above statements, choose the most appropriate answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. A given fig species can be pollinated ONLY by its specific partner wasp species, and no other wasp.\n2. The female wasp searches for suitable egg-laying (oviposition) sites in the syconium inflorescence and pollinates the flowers.\n3. In return, the fig provides oviposition sites and a portion of developing seeds as nourishment for the grubs.\n4. Both statements are accurate NCERT textbook assertions.",
         "Distractors claim any wasp can pollinate any fig, which violates obligate specificity.", "Fig and wasp exhibit tight mutualistic co-evolution: pollination in exchange for oviposition and seed food."),

        # 45. Direct MCQ: Ecosystem (24/29)
        ("Ecosystem", "Stratification in Forest Ecosystem", "Direct MCQ",
         "The vertical distribution of different species occupying different physical levels in a forest ecosystem (e.g. trees occupy top vertical strata, shrubs the middle, and herbs/grasses the bottom) is termed:",
         ["Stratification", "Standing crop", "Ecological succession", "Trophic level"], 0,
         "1. Vertical distribution of different species occupying different levels in an ecosystem is called stratification.\n2. In a forest, tall canopy trees occupy the top vertical tier, shrubs the second layer, and herbs and grasses occupy the bottom ground layer.\n3. Standing crop is the amount of living biomass at a given time.",
         "Standing crop is biomass; succession is temporal change over time.", "Stratification is the vertical layering of species occupying different structural tiers in an ecosystem."),

        # 46. Direct MCQ: Biodiversity (25/29)
        ("Biodiversity and Conservation", "Ramsar Convention on Wetlands", "Direct MCQ",
         "The Ramsar Convention (signed in Ramsar, Iran in 1971) is an international intergovernmental treaty dedicated specifically to the conservation and sustainable utilization of:",
         ["Wetlands of international ecological importance",
          "Ozone-depleting substances",
          "Hazardous waste transboundary movement",
          "Endangered migratory birds exclusively"], 0,
         "1. The Convention on Wetlands was adopted in the Iranian city of Ramsar in 1971.\n2. It provides the framework for national action and international cooperation for the conservation and wise use of wetlands and their resources.\n3. Montreal Protocol governs ozone; Basel Convention governs hazardous waste.",
         "Montreal Protocol protects ozone; Basel Convention regulates hazardous waste.", "The Ramsar Convention is an international treaty dedicated to the conservation of wetlands."),

        # 47. Direct MCQ: Morphology (26/29)
        ("Morphology of Flowering Plants", "Edible Part of Coconut Fruit", "Direct MCQ",
         "The fruit of coconut (*Cocos nucifera*) is a drupe developing from a monocarpellary superior ovary. The edible white kernel and tender coconut water represent:",
         ["Endosperm (cellular endosperm and free-nuclear liquid endosperm)",
          "Mesocarp",
          "Endocarp",
          "Perisperm"], 0,
         "1. Coconut fruit is a fibrous drupe with a membranous epicarp, fibrous mesocarp (yielding coir), and stony hard endocarp.\n2. Inside the endocarp, the seed contains a vast endosperm:\n   - The tender coconut water is free-nuclear liquid endosperm.\n   - The surrounding white coconut meat/kernel is cellular endosperm.\n3. The embryo is small and embedded within the endosperm.",
         "Mesocarp of coconut is fibrous (coir), not edible.", "In coconut drupe, the edible meat and water represent cellular and free-nuclear endosperm."),

        # 48. Direct MCQ: Cell Biology (27/29)
        ("Cell: The Unit of Life", "Centrosome Structure and Microtubule Triplet Triplet", "Direct MCQ",
         "In eukaryotic centrosomes, the two cylindrical centrioles lie perpendicular to each other and possess a cartwheel organization composed of nine evenly spaced peripheral triplets of:",
         ["Tubulin protein fibrils arranged in a '9 + 0' pattern with an absence of central microtubules",
          "Actin microfilaments in a '9 + 2' pattern",
          "Dynein motor proteins in a '9 + 2' pattern",
          "Keratin intermediate filaments"], 0,
         "1. Centrioles consist of nine evenly spaced peripheral triplets of tubulin fibrils arranged radially like a cartwheel.\n2. Unlike cilia and flagella (which have a $9+2$ doublet arrangement with two central singlet microtubules), centrioles have a '9 + 0' pattern because central microtubules are completely absent.\n3. The central hub is proteinaceous and connected to peripheral triplets by radial spokes.",
         "Cilia and flagella have a $9+2$ doublet pattern; centrioles have a $9+0$ triplet pattern.", "Centrioles possess a cartwheel structure with nine peripheral tubulin triplets in a '9 + 0' pattern."),

        # 49. Direct MCQ: Biodiversity (28/29)
        ("Biodiversity and Conservation", "Rivet Popper Hypothesis", "Direct MCQ",
         "In Paul Ehrlich's 'Rivet Popper Hypothesis' comparing an ecosystem to an airplane, the rivets on the wings of the airplane represent:",
         ["Key species that drive major ecosystem functions, whose loss poses a serious threat to ecosystem safety",
          "Extinct non-functional species",
          "Pioneer species during primary succession",
          "Invasive weeds"], 0,
         "1. Stanford ecologist Paul Ehrlich used the rivet popper analogy:\n   - Airplane = Ecosystem\n   - Rivets = Species\n   - Popping a rivet = Causing a species to become extinct\n2. Removing rivets from seats may not endanger flight safety initially, but removing 'rivets on the wings' (key species driving fundamental processes) directly jeopardizes flight safety.",
         "Seats represent minor species; wing rivets represent keystone species.", "In the Rivet Popper hypothesis, wing rivets represent keystone species vital to ecosystem integrity."),

        # 50. Direct MCQ: Environmental Issues (29/29)
        ("Environmental Issues / Ecosystem", "Electrostatic Precipitator Particulate Removal", "Direct MCQ",
         "The most widely used thermal power plant technology capable of removing over $99\\%$ of particulate matter from industrial chimney exhaust is the:",
         ["Electrostatic Precipitator (ESP)", "Scrubber using lime spray", "Catalytic Converter", "Incinerator"], 0,
         "1. Electrostatic precipitators have electrode wires maintained at several thousand volts, creating a corona discharge that releases electrons.\n2. Electrons attach to dust particles, giving them a net negative charge.\n3. Collecting plates are grounded and attract the negatively charged dust particles, removing over $99\\%$ of particulate matter.\n4. Scrubbers remove gaseous pollutants like $\\text{SO}_2$.",
         "Scrubbers remove $\\text{SO}_2$ gas; catalytic converters treat automobile exhaust.", "Electrostatic precipitators remove $>99\\%$ of particulate matter from thermal power plant exhaust.")
    ]

    all_topics = botany_topics + more_botany
    assert len(all_topics) == 50, f"Expected 50 moderate botany topics, got {len(all_topics)}"

    # Dynamic rotation per mock
    shift = (mock_num * 13) % len(all_topics)
    rotated_topics = all_topics[shift:] + all_topics[:shift]

    for i, item in enumerate(rotated_topics):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 101  # 101 to 150
        sec = "Section A" if (q_num - 100) <= 35 else "Section B"
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
