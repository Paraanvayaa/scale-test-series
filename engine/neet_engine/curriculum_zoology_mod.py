# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Moderate Curriculum (Zoology)
Strictly calibrated to NTA NEET-UG standards (2023-2026).
Moderate analytical depth: multi-concept physiological mechanisms, 
hormonal regulation cascades, genetic crosses, and anatomical structures.
No JEE material; strictly NCERT-aligned.

Proportions for 50 Questions:
- Direct MCQ: 29
- Statement I & II: 7
- Match List: 7
- Assertion & Reason: 4
- Multi-Statement: 3
Total: 50
"""
from neet_models import NeetQuestion

def get_zoology_mod_questions(mock_num):
    questions = []
    
    # 50 moderate topics covering class 11 and class 12 Zoology syllabus
    topics_data = [
        # 1. Animal Kingdom - Non-chordates
        ("Animal Kingdom", "Canal System in Porifera", "Direct MCQ",
         "The correct sequence of water flow through the canal system (syconoid type) of a sponge is:",
         ["Ostia -> Prosopyles -> Radial canals -> Internal ostia -> Spongocoel -> Osculum",
          "Osculum -> Spongocoel -> Radial canals -> Ostia",
          "Ostia -> Spongocoel -> Incurrent canal -> Osculum",
          "Osculum -> Radial canals -> Prosopyles -> Ostia"], 0,
         "In sponges, water enters through ostia, passes through prosopyles into flagellated radial canals lined with choanocytes, exits via apopyles into the central spongocoel, and finally discharges through the osculum.",
         "Distractors reverse entry and exit or omit radial canals.",
         "Spongocoel water exit occurs strictly via osculum, driven by beating choanocyte flagella."),

        # 2. Animal Kingdom - Coelenterata & Ctenophora
        ("Animal Kingdom", "Metagenesis in Cnidaria", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** In *Obelia*, the polyp form produces medusae asexually, and medusae produce polyps sexually.\n\n"
         "**Statement II:** Both polyp and medusa stages in cnidarians are diploid ($2n$) multicellular body forms.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In *Obelia* exhibiting metagenesis, polyps reproduce asexually by budding to yield free-swimming medusae. Medusae produce gametes sexually to form polyps via a planula larva.\n2. Unlike plant alternation of generations, both polyp and medusa are diploid multicellular structures; only gametes are haploid.",
         "Statement II is often mistaken for haplo-diplontic plant alternation.",
         "Metagenesis in cnidarians represents alternation of generations between two diploid body forms."),

        # 3. Animal Kingdom - Platyhelminthes & Aschelminthes
        ("Animal Kingdom", "Parasitic Adaptations in Helminths", "Multi-Statement",
         "Which of the following morphological and physiological adaptations are characteristic of parasitic platyhelminths (*Taenia* and *Fasciola*)?\n\n"
         "A. Presence of hooks and suckers for adhesion to host intestinal mucosa.\n"
         "B. Thick protective tegument resistant to host digestive enzymes.\n"
         "C. Highly developed sensory organs and locomotory cilia.\n"
         "D. Absence of digestive system with direct absorption of nutrients through body surface.\n"
         "E. Complex reproductive system with high fecundity (prolific egg production).\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, D and E only",
          "A, B and C only",
          "B, C, D and E only",
          "A, C and D only"], 0,
         "Parasitic helminths show degeneration/absence of sensory organs and locomotory structures (making statement C incorrect). Statements A, B, D, and E represent well-documented parasitic adaptations.",
         "Statement C is false because endoparasites do not need specialized sensory organs in host gut.",
         "Endoparasites maximize reproductive output while simplifying digestive and sensory systems."),

        # 4. Animal Kingdom - Annelida & Arthropoda
        ("Animal Kingdom", "Excretory and Respiratory Organs in Invertebrates", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** The king crab (*Limulus*) respires by means of book gills, whereas scorpions and spiders respire via book lungs.\n\n"
         "**Reason (R):** *Limulus* is an aquatic chelicerate merostome, while scorpions and spiders are terrestrial arachnids adapted to aerial breathing.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Both statements are scientifically accurate: *Limulus* (living fossil) is an aquatic chelicerate that possesses 5 pairs of book gills for aquatic gas exchange, whereas terrestrial arachnids evolved internal book lungs to breathe atmospheric air. Reason explains Assertion.",
         "King crab (*Limulus*) uses book gills, whereas arachnids use book lungs.",
         "Book gills are characteristic of aquatic merostomes (*Limulus*); book lungs of terrestrial arachnids."),

        # 5. Animal Kingdom - Mollusca & Echinodermata
        ("Animal Kingdom", "Water Vascular System of Asterias", "Direct MCQ",
         "In *Asterias* (starfish), the water vascular system (ambulacral system) performs all of the following vital functions EXCEPT:",
         ["Excretion of nitrogenous wastes via specialized flame cells",
          "Locomotion across the substratum",
          "Capture and transport of food to the mouth",
          "Gaseous exchange (respiration)"], 0,
         "Echinoderms lack specialized excretory organs; nitrogenous wastes (ammonia) diffuse through tube feet and dermal branchiae. Flame cells are found in Platyhelminthes.",
         "Distractors confuse excretory structures across phyla.",
         "Water vascular system assists locomotion, food capture, and respiration, but echinoderms lack an excretory system."),

        # 6. Animal Kingdom - Chordata Classification
        ("Animal Kingdom", "Chondrichthyes vs Osteichthyes", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** Cartilaginous fishes (Chondrichthyes) must swim constantly in water to avoid sinking.\n\n"
         "**Reason (R):** Chondrichthyes lack an air bladder (swim bladder) to regulate hydrostatic buoyancy.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "Chondrichthyes (sharks, rays) do not have an air bladder; therefore, they lack hydrostatic equilibrium and must constantly swim forward to generate hydrodynamic lift and avoid sinking. Both statements are true and Reason directly explains Assertion.",
         "Osteichthyes possess air bladders which provide neutral buoyancy without constant swimming.",
         "Air bladder in bony fishes provides buoyancy; its absence in Chondrichthyes necessitates constant active swimming."),

        # 7. Animal Kingdom - Mammalian Characteristics
        ("Animal Kingdom", "Prototheria vs Metatheria vs Eutheria", "Direct MCQ",
         "Which of the following mammals is oviparous (egg-laying), possesses mammary glands lacking nipples, and lacks a corpus callosum in its brain?",
         ["*Ornithorhynchus* (Duck-billed platypus)",
          "*Macropus* (Kangaroo)",
          "*Pteropus* (Flying fox)",
          "*Balaenoptera* (Blue whale)"], 0,
         "*Ornithorhynchus* (Platypus) and *Echidna* (Spiny anteater) are monotremes (Prototheria): oviparous mammals whose mammary glands open onto skin patches rather than teats/nipples.",
         "*Macropus* is viviparous with a marsupial pouch. *Pteropus* and *Balaenoptera* are placental eutherians.",
         "Monotremes are the only egg-laying mammals; they retain cloaca and lack teats."),

        # 8. Structural Organisation in Animals - Epithelial Tissue
        ("Structural Organisation in Animals", "Cell Junctions and Epithelial Classification", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Epithelial Type / Junction) | List-II (Location / Primary Function) |\n"
         "| :--- | :--- |\n"
         "| **A.** Tight junctions | **I.** Prevent leaking of substances across a tissue |\n"
         "| **B.** Adhering junctions | **II.** Rapid ionic transfer and communication between cells |\n"
         "| **C.** Gap junctions | **III.** Cementing neighboring cells together |\n"
         "| **D.** Ciliated columnar epithelium | **IV.** Inner lining of bronchioles and fallopian tubes |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-III, C-II, D-IV",
          "A-III, B-I, C-II, D-IV",
          "A-I, B-II, C-III, D-IV",
          "A-IV, B-III, C-II, D-I"], 0,
         "Tight junctions stop substances from leaking (A-I). Adhering junctions perform cementing to keep cells together (B-III). Gap junctions facilitate communication via cytoplasm channels (C-II). Ciliated columnar epithelium moves particles in bronchioles and oviducts (D-IV).",
         "Confusing tight (leakage prevention) with adhering (cementing) is a classic mistake.",
         "Tight junctions seal, adhering junctions anchor, and gap junctions communicate."),

        # 9. Structural Organisation in Animals - Connective Tissue
        ("Structural Organisation in Animals", "Cartilage vs Bone Matrix", "Direct MCQ",
         "The intercellular material of cartilage differs from that of bone in being:",
         ["Solid, pliable, and resistant to compression due to chondroitin salts",
          "Hard and non-pliable due to calcium phosphate and collagen fibers",
          "Fluid and non-pliable due to lack of collagen fibers",
          "Vascular and highly mineralized with haversian systems"], 0,
         "Cartilage matrix is solid, pliable, and resists compression due to chondroitin sulfate proteoglycans. Bone matrix is hard, non-pliable, rich in calcium salts and collagen fibers, organized around Haversian canals.",
         "Hard, non-pliable matrix describes bone, not cartilage.",
         "Cartilage is pliable due to chondroitin salts; bone is non-pliable due to calcium hydroxyapatite."),

        # 10. Structural Organisation in Animals - Cockroach Anatomy
        ("Structural Organisation in Animals", "Cockroach Reproductive System", "Direct MCQ",
         "In male cockroach (*Periplaneta americana*), the sperms stored in seminal vesicles are glued together into bundles called:",
         ["Spermatophores",
          "Oothecae",
          "Pseudopenis",
          "Conglobate masses"], 0,
         "Sperms discharged from testes are stored in the seminal vesicles and glued together into bundles called spermatophores, which are discharged during copulation.",
         "Ootheca is the egg capsule formed in females. Conglobate gland is an accessory male gland.",
         "Spermatophore is the sperm-containing capsule transferred to the female genital chamber."),

        # 11. Breathing and Exchange of Gases - Pulmonary Volumes
        ("Breathing and Exchange of Gases", "Alveolar Ventilation Rate Calculation", "Direct MCQ",
         f"A healthy student has a tidal volume ($TV$) of 500 mL, an anatomical dead space of 150 mL, and a resting respiratory rate of {12 + mock_num % 4} breaths per minute. The alveolar ventilation rate per minute is:",
         [f"{(500 - 150) * (12 + mock_num % 4)} mL/min",
          f"{500 * (12 + mock_num % 4)} mL/min",
          f"{150 * (12 + mock_num % 4)} mL/min",
          f"{(500 + 150) * (12 + mock_num % 4)} mL/min"], 0,
         f"Alveolar ventilation rate = $(TV - \\text{{dead space}}) \\times \\text{{breathing rate}} = (500 - 150) \\times {12 + mock_num % 4} = 350 \\times {12 + mock_num % 4} = {(500 - 150) * (12 + mock_num % 4)}\\text{{ mL/min}}$. Total pulmonary ventilation would be $500 \\times {12 + mock_num % 4}$.",
         "Pulmonary ventilation ($TV \\times RR$) ignores dead space and is an incorrect overestimation.",
         "Alveolar ventilation represents the fresh gas volume reaching gas-exchange surfaces per minute."),

        # 12. Breathing and Exchange of Gases - Transport of Gases
        ("Breathing and Exchange of Gases", "Oxygen-Hemoglobin Dissociation Curve Shifts", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** A rightward shift of the oxygen-hemoglobin dissociation curve implies a decrease in hemoglobin's affinity for oxygen, facilitating oxygen unloading at tissues.\n\n"
         "**Statement II:** Factors causing a rightward shift (Bohr effect) include increased $p\\text{CO}_2$, increased $[\\text{H}^+]$ (decreased pH), elevated temperature, and increased 2,3-BPG.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. A shift to the right means a higher $p\\text{O}_2$ is required for $50\\%$ saturation ($P_{50}$ increases), which signifies lower affinity and enhanced delivery to tissues.\n2. In active tissues, high $p\\text{CO}_2$, high $[\\text{H}^+]$ (acidosis), high temperature, and 2,3-BPG promote right shift. Both statements are accurate.",
         "A right shift does not mean increased affinity; it means decreased affinity (Bohr effect).",
         "Right shift = higher $P_{50}$ = lower affinity = greater tissue oxygen delivery."),

        # 13. Breathing and Exchange of Gases - Regulation
        ("Breathing and Exchange of Gases", "Respiratory Rhythm Center and Chemosensitive Area", "Direct MCQ",
         "The primary physiological chemical stimulus for the central chemosensitive area adjacent to the respiratory rhythm center in the medulla oblongata is:",
         ["Increase in $\\text{CO}_2$ concentration and $[\\text{H}^+]$ ions in cerebrospinal fluid",
          "Decrease in arterial $p\\text{O}_2$ below 60 mmHg",
          "Decrease in arterial $p\\text{CO}_2$ and rise in blood pH",
          "Increase in hemoglobin saturation with oxygen"], 0,
         "The central chemoreceptors located in the medulla are highly sensitive to $\\text{CO}_2$ and $\\text{H}^+$ concentration in CSF. Arterial $p\\text{O}_2$ has very little direct effect on the respiratory rhythm center.",
         "Role of oxygen in the regulation of respiratory rhythm is quite insignificant.",
         "Carbon dioxide and hydrogen ions are the primary chemical regulators of human respiration."),

        # 14. Body Fluids and Circulation - Cardiac Cycle
        ("Body Fluids and Circulation", "Ventricular Pressure and Heart Sounds", "Direct MCQ",
         "The first heart sound ('LUB') and second heart sound ('DUB') are produced respectively by the closure of:",
         ["Atrioventricular (bicuspid and tricuspid) valves, followed by Semilunar valves",
          "Semilunar valves, followed by Atrioventricular valves",
          "Bicuspid valve only, followed by Tricuspid valve only",
          "Opening of semilunar valves, followed by opening of AV valves"], 0,
         "First heart sound (lub) is associated with closure of the tricuspid and bicuspid (mitral) valves at the onset of ventricular systole. Second heart sound (dub) is associated with closure of the semilunar valves at the onset of ventricular diastole.",
         "Heart sounds are caused by valve CLOSURE, not valve opening.",
         "Lub = AV valves close (ventricular systole start); Dub = semilunar valves close (diastole start)."),

        # 15. Body Fluids and Circulation - Blood Clotting
        ("Body Fluids and Circulation", "Blood Coagulation Cascade", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Coagulation Step) | List-II (Catalytic Enzyme / Factor) |\n"
         "| :--- | :--- |\n"
         "| **A.** Inactive prothrombin -> Active thrombin | **I.** Thrombokinase (Prothrombinase) |\n"
         "| **B.** Soluble fibrinogen -> Insoluble fibrin mesh | **II.** Thrombin |\n"
         "| **C.** Critical mineral ion required for clotting | **III.** $\\text{Ca}^{2+}$ (Factor IV) |\n"
         "| **D.** Clot dissolution enzyme | **IV.** Plasmin (Fibrinolysin) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "Thrombokinase converts prothrombin into thrombin (A-I). Thrombin converts fibrinogen into insoluble fibrin (B-II). Calcium ions are essential for multiple cascade stages (C-III). Plasmin hydrolyzes fibrin clots (D-IV).",
         "Calcium is Factor IV and is mandatory for clot formation.",
         "Prothrombinase activates thrombin; thrombin cleaves fibrinogen to form fibrin polymer."),

        # 16. Body Fluids and Circulation - ECG
        ("Body Fluids and Circulation", "Standard Electrocardiogram (ECG) Deflections", "Direct MCQ",
         "In a standard clinical electrocardiogram (ECG), the ventricular repolarization (return of ventricles from excited to normal state) and the end of ventricular systole are represented respectively by:",
         ["T-wave, and the end of the T-wave",
          "QRS complex, and the S-T segment",
          "P-wave, and the beginning of the QRS complex",
          "Q-wave, and the end of the T-wave"], 0,
         "1. P-wave represents electrical excitation (depolarization) of atria.\n2. QRS complex represents depolarization of ventricles, initiating ventricular contraction.\n3. T-wave represents the return of ventricles from excited to normal state (repolarization).\n4. The end of the T-wave marks the end of mechanical ventricular systole.",
         "QRS is ventricular depolarization, while T-wave is ventricular repolarization.",
         "P = Atrial depolarization, QRS = Ventricular depolarization, T = Ventricular repolarization."),

        # 17. Excretory Products and Their Elimination - Nephron Function
        ("Excretory Products and Their Elimination", "Counter-Current Mechanism in Loop of Henle and Vasa Recta", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** The descending limb of the loop of Henle concentrates the tubular fluid as it descends into the renal medulla.\n\n"
         "**Reason (R):** The descending limb is permeable to water but almost impermeable to electrolytes, allowing water to exit by osmosis into the hypertonic medullary interstitium.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "The descending limb of loop of Henle is permeable to water and impermeable to salts. As it travels down into the hyperosmolar medulla (up to 1200 mOsmol/L), water flows out into the interstitium, concentrating the urine up to 1200 mOsmol/L. Reason correctly explains Assertion.",
         "Ascending limb is the opposite: impermeable to water and permeable/active for NaCl.",
         "Descending limb loses water (concentrating); ascending limb extrudes NaCl (diluting)."),

        # 18. Excretory Products and Their Elimination - Regulation
        ("Excretory Products and Their Elimination", "Renin-Angiotensin-Aldosterone System (RAAS)", "Direct MCQ",
         "When glomerular blood flow or GFR drops, juxtaglomerular (JG) cells release renin. Renin directly catalyses the conversion of:",
         ["Angiotensinogen to Angiotensin I",
          "Angiotensin I to Angiotensin II",
          "Angiotensin II to Aldosterone",
          "Prorenin to Angiotensinogen"], 0,
         "Renin is an aspartyl protease released by JG cells that cleaves liver-synthesized angiotensinogen into the decapeptide angiotensin I. Angiotensin Converting Enzyme (ACE) in lung endothelium then converts Ang I to Ang II.",
         "ACE converts Ang I to Ang II; renin converts Angiotensinogen to Ang I.",
         "Renin cleaves Angiotensinogen -> Ang I; ACE cleaves Ang I -> Ang II."),

        # 19. Excretory Products and Their Elimination - ANF
        ("Excretory Products and Their Elimination", "Antagonistic Actions of ANF vs RAAS", "Direct MCQ",
         "Atrial Natriuretic Factor (ANF) acts as a physiological check on the RAAS mechanism by:",
         ["Causing vasodilation of blood vessels and increasing renal excretion of $\\text{Na}^+$ and water",
          "Causing powerful vasoconstriction and stimulating aldosterone release",
          "Stimulating renin secretion from juxtaglomerular cells",
          "Increasing tubular reabsorption of sodium in the distal tubule"], 0,
         "An increase in blood flow to the atria causes release of ANF. ANF causes vasodilation (reducing systemic vascular resistance and blood pressure) and promotes natriuresis (excretion of $\\text{Na}^+$), directly antagonizing renin and aldosterone.",
         "ANF lowers blood pressure, unlike Angiotensin II which raises it.",
         "ANF is a vasodilator and natriuretic peptide that counters RAAS to decrease blood pressure."),

        # 20. Locomotion and Movement - Muscle Contraction
        ("Locomotion and Movement", "Cross-Bridge Cycle in Skeletal Muscle", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Stage of Contraction) | List-II (Molecular Event) |\n"
         "| :--- | :--- |\n"
         "| **A.** Binding of $\\text{Ca}^{2+}$ to troponin C | **I.** Unmasking of myosin-binding sites on actin |\n"
         "| **B.** Hydrolysis of ATP by myosin ATPase | **II.** Energizing myosin head into high-energy cocked state |\n"
         "| **C.** Release of ADP and inorganic phosphate (Pi) | **III.** Power stroke pulling actin thin filaments toward M-line |\n"
         "| **D.** Binding of a new ATP molecule to myosin | **IV.** Detachment of cross-bridge from actin |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-IV, B-II, C-III, D-I"], 0,
         "Ca2+ binds troponin C to unmask active sites (A-I). ATP hydrolysis cocks myosin head (B-II). Release of ADP and Pi triggers the power stroke (C-III). New ATP binding causes cross-bridge detachment (D-IV; absence causes rigor mortis).",
         "Rigor mortis occurs because lack of ATP prevents detachment of cross-bridges.",
         "ATP hydrolysis cocks the head; Pi release drives the power stroke; new ATP causes detachment."),

        # 21. Locomotion and Movement - Muscle Fibers
        ("Locomotion and Movement", "Red (Slow Oxidative) vs White (Fast Glycolytic) Muscle Fibers", "Multi-Statement",
         "Which of the following statements correctly describe Red muscle fibers as compared to White muscle fibers?\n\n"
         "A. They possess high myoglobin content, giving them a characteristic reddish sheen.\n"
         "B. They contain a very large number of mitochondria for aerobic ATP generation.\n"
         "C. They possess a high amount of sarcoplasmic reticulum for rapid calcium release.\n"
         "D. They can sustain prolonged contraction without rapid fatigue.\n"
         "E. They depend primarily on anaerobic glycolysis for quick bursts of energy.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B and D only",
          "A, B, C and D only",
          "C and E only",
          "B, C and E only"], 0,
         "Statements A, B, and D are true of Red (slow-twitch) fibers: high myoglobin, abundant mitochondria, highly vascularized, fatigue-resistant aerobic engines. Statements C and E describe White muscle fibers (extensive SR, low myoglobin, fast fatigue, anaerobic glycolysis).",
         "White fibers have abundant SR and rely on glycolysis; red fibers rely on aerobic respiration.",
         "Red muscle = slow-twitch, high myoglobin, high mitochondria, fatigue-resistant."),

        # 22. Locomotion and Movement - Joints and Disorders
        ("Locomotion and Movement", "Musculoskeletal Disorders", "Direct MCQ",
         "Match the disorder with its primary underlying pathological mechanism:\n"
         "1. Myasthenia gravis: Autoimmune attack against acetylcholine receptors at neuromuscular junctions.\n"
         "2. Tetany: Rapid spasms in muscle due to low calcium ($[\\text{Ca}^{2+}]$) in body fluids.\n"
         "3. Gout: Inflammation of joints due to accumulation of uric acid crystals.\n"
         "4. Muscular dystrophy: Progressive genetic degeneration of skeletal muscle.\n\n"
         "Which of the statements above is/are correct?",
         ["All 1, 2, 3, and 4",
          "1 and 3 only",
          "1, 2 and 3 only",
          "2 and 4 only"], 0,
         "All four definitions are precise NCERT facts: Myasthenia gravis is autoimmune; Tetany is hypocalcemic spasticity; Gout is hyperuricemic crystal deposition; Muscular dystrophy is an X-linked recessive genetic degeneration.",
         "Tetany is due to LOW calcium (hypocalcemia), not hypercalcemia.",
         "Myasthenia gravis = autoimmune; Tetany = low Ca2+; Gout = uric acid; Muscular dystrophy = genetic."),

        # 23. Neural Control and Coordination - Action Potential
        ("Neural Control and Coordination", "Ionic Basis of Nerve Impulse Conduction", "Direct MCQ",
         "During the depolarization phase of an axonal membrane action potential, there is a rapid inward movement of:",
         ["$\\text{Na}^+$ ions down their electrochemical gradient via voltage-gated channels",
          "$\\text{K}^+$ ions out of the axoplasm into extracellular fluid",
          "$\\text{Ca}^{2+}$ ions into the synaptic knob",
          "$\\text{Cl}^-$ ions into the axoplasm maintaining negative potential"], 0,
         "Depolarization is driven by the opening of voltage-gated Na+ channels, allowing rapid influx of Na+ along its concentration and electrical gradient, reversing polarity from -70 mV to +30 mV. Repolarization is driven by K+ efflux.",
         "K+ efflux causes repolarization; Na+ influx causes depolarization.",
         "Depolarization = rapid Na+ influx; Repolarization = rapid K+ efflux."),

        # 24. Neural Control and Coordination - Synaptic Transmission
        ("Neural Control and Coordination", "Chemical vs Electrical Synapse", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** At a chemical synapse, the membranes of pre- and post-synaptic neurons are separated by a fluid-filled space called the synaptic cleft.\n\n"
         "**Statement II:** Electrical synapses allow bidirectional and faster transmission of impulses across gap junctions compared to chemical synapses.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Chemical synapses use neurotransmitters across a 20 nm synaptic cleft, requiring vesicular exocytosis and post-synaptic receptor binding.\n2. Electrical synapses have pre- and post-synaptic membranes in physical contact via gap junction connexons, allowing instantaneous ionic current flow in either direction. Both statements are correct.",
         "Electrical synapses are rare in human system but allow much faster transmission.",
         "Chemical synapses have a synaptic cleft; electrical synapses communicate directly via gap junctions."),

        # 25. Neural Control and Coordination - Human Brain
        ("Neural Control and Coordination", "Functional Localization in Human Brain", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Brain Region) | List-II (Key Function) |\n"
         "| :--- | :--- |\n"
         "| **A.** Hypothalamus | **I.** Thermoregulation, hunger, thirst, and neurosecretion |\n"
         "| **B.** Cerebellum | **II.** Precision of voluntary movements and body posture/balance |\n"
         "| **C.** Corpora quadrigemina | **III.** Visual and auditory reflex coordination centers |\n"
         "| **D.** Medulla oblongata | **IV.** Control of cardiovascular reflexes, respiration, and vomiting |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-IV, D-III",
          "A-I, B-III, C-II, D-IV",
          "A-IV, B-II, C-III, D-I"], 0,
         "Hypothalamus governs homeostasis and endocrine release (A-I). Cerebellum coordinates motor activity and balance (B-II). Corpora quadrigemina (four colliculi of midbrain) integrate visual and acoustic reflexes (C-III). Medulla controls autonomous vital centers (D-IV).",
         "Cerebrum initiates voluntary action; cerebellum fine-tunes precision and balance.",
         "Hypothalamus = homeostasis; Cerebellum = balance; Medulla = vital vegetative centers."),

        # 26. Chemical Coordination and Integration - Hormonal Mechanisms
        ("Chemical Coordination and Integration", "Mechanism of Hormone Action", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Peptide, polypeptide, and protein hormones (e.g., insulin, glucagon, epinephrine) bind to membrane-bound extracellular receptors and generate second messengers such as $\\text{cAMP}, \\text{IP}_3$, or $\\text{Ca}^{2+}$.\n\n"
         "**Statement II:** Steroid hormones (e.g., estrogen, progesterone, cortisol) and thyroid hormones easily cross cell membranes and interact with intracellular receptors to regulate gene expression.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Water-soluble peptide hormones cannot cross the lipid bilayer; they bind surface receptors to activate adenylate cyclase or phospholipase C, producing second messengers.\n2. Lipid-soluble steroids and iodothyronines diffuse through the membrane and bind nuclear receptors, acting as transcription factors to modulate mRNA synthesis. Both statements are accurate.",
         "Peptides do not enter target cells directly; they act via second messengers.",
         "Peptide hormones = membrane receptors & second messengers; Steroids = intracellular receptors & gene transcription."),

        # 27. Chemical Coordination and Integration - Endocrine Disorders
        ("Chemical Coordination and Integration", "Endocrine Gland Pathology", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Disorder) | List-II (Underlying Hormonal Abnormality) |\n"
         "| :--- | :--- |\n"
         "| **A.** Diabetes insipidus | **I.** Hyposecretion of ADH (Vasopressin) from posterior pituitary |\n"
         "| **B.** Graves' disease (Exophthalmic goitre) | **II.** Hyperthyroidism with protrusion of eyeballs and elevated BMR |\n"
         "| **C.** Addison's disease | **III.** Hyposecretion of adrenal cortex hormones (glucocorticoids & mineralocorticoids) |\n"
         "| **D.** Cushing's syndrome | **IV.** Hypersecretion of cortisol from adrenal cortex |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-III, B-II, C-I, D-IV"], 0,
         "Diabetes insipidus is caused by lack of ADH, leading to polyuria without glycosuria (A-I). Graves' disease is autoantibody-driven hyperthyroidism (A-II). Addison's disease is adrenal cortical insufficiency (A-III). Cushing's syndrome is cortisol excess (A-IV).",
         "Diabetes mellitus is insulin deficiency; diabetes insipidus is ADH deficiency.",
         "Diabetes insipidus = low ADH; Graves = hyperthyroid; Addison = low adrenal cortical hormones."),

        # 28. Chemical Coordination and Integration - Non-Endocrine Hormones
        ("Chemical Coordination and Integration", "Gastrointestinal and Renal Hormones", "Direct MCQ",
         "Which gastrointestinal peptide hormone stimulates the exocrine pancreas to secrete water and bicarbonate ions, neutralizing acidic chyme in the duodenum?",
         ["Secretin",
          "Cholecystokinin (CCK)",
          "Gastrin",
          "Gastric Inhibitory Peptide (GIP)"], 0,
         "Secretin acts on the exocrine pancreas to stimulate secretion of water and bicarbonate ions. CCK stimulates secretion of pancreatic digestive enzymes and contraction of gall bladder to release bile.",
         "CCK stimulates pancreatic enzymes and bile release; Secretin stimulates bicarbonate and water.",
         "Secretin = pancreatic water and bicarbonate; CCK = pancreatic enzymes and bile."),

        # 29. Human Reproduction - Spermatogenesis
        ("Human Reproduction", "Spermatogenesis Chromosome Numbers and Sequence", "Direct MCQ",
         "During human spermatogenesis, the transition from primary spermatocyte to secondary spermatocyte involves:",
         ["Reduction division (Meiosis I) resulting in two haploid ($n = 23$) cells",
          "Equational division (Meiosis II) resulting in four haploid cells",
          "Mitotic multiplication of diploid spermatogonia",
          "Spermiogenesis of round spermatids into spermatozoa"], 0,
         "Primary spermatocytes ($2n = 46$) undergo the first meiotic division (reductional division) to produce two equal, haploid secondary spermatocytes ($n = 23$). Secondary spermatocytes then undergo Meiosis II to yield four haploid spermatids.",
         "Meiosis I reduces chromosome number from 46 to 23.",
         "Primary spermatocyte ($2n$) -> Meiosis I -> Secondary spermatocyte ($n$) -> Meiosis II -> Spermatid ($n$)."),

        # 30. Human Reproduction - Oogenesis
        ("Human Reproduction", "Meiotic Arrest Stages in Human Oogenesis", "Direct MCQ",
         "In human females, oogenesis is arrested at two distinct developmental milestones. These arrest stages are:",
         ["Diplotene of Prophase I (before birth) and Metaphase II (until fertilization)",
          "Pachytene of Prophase I and Anaphase II",
          "Leptotene of Prophase I and Metaphase I",
          "Telophase I and Metaphase II"], 0,
         "Primary oocytes enter Prophase I during embryonic fetal life and remain arrested at the diplotene stage until puberty. Secondary oocyte arrests at Metaphase II after ovulating, and only completes Meiosis II upon penetration by a sperm.",
         "Arrest at birth is Diplotene; arrest after ovulation is Metaphase II.",
         "First arrest = Diplotene of Prophase I; Second arrest = Metaphase II of Meiosis II."),

        # 31. Human Reproduction - Menstrual Cycle
        ("Human Reproduction", "Hormonal Regulation of Menstrual Cycle", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Cycle Phase / Event) | List-II (Dominant Hormonal Profile) |\n"
         "| :--- | :--- |\n"
         "| **A.** Follicular (Proliferative) phase | **I.** Rising estrogen secreted by growing ovarian follicles |\n"
         "| **B.** Ovulation (Day 14) | **II.** LH surge triggered by positive feedback of high estrogen |\n"
         "| **C.** Luteal (Secretory) phase | **III.** High progesterone secreted by corpus luteum |\n"
         "| **D.** Menstruation | **IV.** Abrupt decline in progesterone and estrogen levels |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-III, B-II, C-I, D-IV"], 0,
         "Proliferative phase is driven by follicular estrogen (A-I). Ovulation requires LH peak/surge (B-II). Luteal phase is sustained by corpus luteum progesterone (C-III). Menstruation occurs when corpus luteum degenerates, causing drop in progesterone (D-IV).",
         "Progesterone withdrawal triggers menstrual breakdown of endometrium.",
         "Follicular = Estrogen; Ovulation = LH surge; Luteal = Progesterone; Menses = Progesterone withdrawal."),

        # 32. Human Reproduction - Fertilization and Cleavage
        ("Human Reproduction", "Cortical Reaction and Block to Polyspermy", "Assertion & Reason",
         "Given below are two statements: one is labelled as **Assertion (A)** and the other is labelled as **Reason (R)**.\n\n"
         "**Assertion (A):** Entry of a single sperm into the ovum induces changes in the zona pellucida that block the entry of additional sperms.\n\n"
         "**Reason (R):** Fusion of sperm with the oolemma triggers the cortical granules to release enzymes into the perivitelline space, hardening the zona pellucida (zona reaction).\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "When a sperm binds to ZP3 receptors and fuses with the egg plasma membrane, intracellular Ca2+ wave triggers exocytosis of cortical granules (cortical reaction). The enzymes destroy ZP3 receptors and harden the zona pellucida, establishing the slow block to polyspermy. Both statements are true and Reason directly explains Assertion.",
         "Without cortical reaction, polyspermy occurs leading to non-viable polyploidy.",
         "Cortical granule exocytosis hardens zona pellucida to ensure monospermy."),

        # 33. Human Reproduction - Blastocyst and Implantation
        ("Human Reproduction", "Inner Cell Mass and Trophoblast", "Direct MCQ",
         "In a human blastocyst, the outer layer of cells that attaches to the endometrium and later contributes to the placenta is the:",
         ["Trophoblast",
          "Inner cell mass (Embryoblast)",
          "Zona pellucida",
          "Corona radiata"], 0,
         "The blastocyst consists of an outer cell layer called trophoblast, which attaches to the endometrium and forms the chorionic villi, and an inner group of cells attached to one side called inner cell mass (embryoblast), which gives rise to the embryo.",
         "Inner cell mass forms the embryo proper; trophoblast forms extra-embryonic tissues.",
         "Trophoblast attaches to endometrium and forms placenta; inner cell mass forms the embryo."),

        # 34. Reproductive Health - Contraceptive Methods
        ("Reproductive Health", "Mode of Action of IUDs", "Multi-Statement",
         "Which of the following statements correctly describe the mechanisms by which Intrauterine Devices (IUDs) prevent conception?\n\n"
         "A. Non-medicated IUDs (e.g., Lippes loop) increase phagocytosis of sperms within the uterus.\n"
         "B. Copper-releasing IUDs (e.g., CuT, Cu7, Multiload 375) suppress sperm motility and fertilizing capacity.\n"
         "C. Hormone-releasing IUDs (e.g., Progestasert, LNG-20) make the uterus unsuitable for implantation.\n"
         "D. Hormone-releasing IUDs render the cervix hostile to sperms by thickening cervical mucus.\n"
         "E. Copper ions prevent the occurrence of ovulation during the ovarian cycle.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, C and D only",
          "A, B and E only",
          "B, C, D and E only",
          "C, D and E only"], 0,
         "Statements A, B, C, and D are authentic NCERT facts regarding IUD mechanisms. Statement E is incorrect because copper ions do NOT inhibit ovulation; their primary action is suppressing sperm motility and fertilizing ability.",
         "Copper-T suppresses sperm motility, not ovulation.",
         "Non-medicated = phagocytosis; Cu-IUD = reduces motility; Hormone IUD = prevents implantation & thickens mucus."),

        # 35. Reproductive Health - Assisted Reproductive Technologies
        ("Reproductive Health", "ART Procedures: ZIFT vs GIFT vs ICSI", "Direct MCQ",
         "A couple is infertile because the female partner has blocked fallopian tubes bilaterally, but her ovaries produce normal ova and her uterus is fully receptive. The most suitable ART technique for this couple is:",
         ["IVF followed by ZIFT (if <= 8 blastomeres) or IUT (if > 8 blastomeres)",
          "Gamete Intra-Fallopian Transfer (GIFT)",
          "Intra-Uterine Insemination (IUI)",
          "Artificial Insemination (AI)"], 0,
         "Because both fallopian tubes are blocked, fertilization cannot occur in vivo. GIFT is impossible because GIFT requires at least one healthy patent fallopian tube for fertilization. Therefore, in vitro fertilization (IVF) followed by embryo transfer (ZIFT or IUT) is necessary.",
         "GIFT requires functional fallopian tubes because fertilization occurs inside the tube.",
         "Blocked fallopian tubes rule out GIFT; they necessitate in vitro fertilization (IVF-ET)."),

        # 36. Principles of Inheritance - Mendelian Dihybrid Cross
        ("Principles of Inheritance and Variation", "Dihybrid Test Cross Ratio", "Direct MCQ",
         "A test cross of a heterozygous dihybrid individual ($AaBb \\times aabb$) for two independently assorting unlinked genes yields a phenotypic ratio of:",
         ["1 : 1 : 1 : 1",
          "9 : 3 : 3 : 1",
          "3 : 1",
          "9 : 7"], 0,
         "A dihybrid test cross between $AaBb$ and the double recessive parent $aabb$ produces four phenotypic classes in equal proportions: $1/4 AaBb : 1/4 Aabb : 1/4 aaBb : 1/4 aabb$ = $1 : 1 : 1 : 1$.",
         "9:3:3:1 is the selfing phenotypic ratio of $AaBb \\times AaBb$, not a test cross.",
         "Dihybrid test cross ratio for unlinked genes is strictly 1:1:1:1."),

        # 37. Principles of Inheritance - Sex Determination
        ("Principles of Inheritance and Variation", "Haplodiploidy in Honeybees", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** In honeybees, drones (males) develop parthenogenetically from unfertilized eggs and are haploid ($n = 16$).\n\n"
         "**Statement II:** Drone honeybees produce sperms by mitosis and therefore have a grandfather and grandsons, but cannot have a father or sons.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Female honeybees (queen/workers) develop from fertilized eggs ($2n = 32$), while males (drones) develop parthenogenetically from unfertilized eggs ($n = 16$).\n2. Because drones are haploid, they produce gametes by mitosis. A drone has no father (mother was virgin queen) and cannot directly produce sons (his sperm fertilized an egg yields a female). Both statements are accurate NCERT facts.",
         "Drones produce sperms by mitosis because they are already haploid.",
         "Honeybee haplodiploidy: Males are haploid ($n$), develop parthenogenetically, and produce gametes by mitosis."),

        # 38. Principles of Inheritance - Pedigree Analysis
        ("Principles of Inheritance and Variation", "Mode of Inheritance from Pedigree", "Direct MCQ",
         "A rare genetic disorder affects both males and females equally. Affected offspring always have at least one affected parent. Unaffected individuals do not transmit the trait to their offspring. This pedigree pattern is characteristic of:",
         ["Autosomal dominant inheritance",
          "Autosomal recessive inheritance",
          "X-linked recessive inheritance",
          "Y-linked (holandric) inheritance"], 0,
         "In autosomal dominant traits, affected individuals appear in every generation without skipping; unaffected individuals cannot pass the trait because they lack the dominant disease allele ($aa$).",
         "Autosomal recessive traits characteristically skip generations and appear from unaffected carriers.",
         "Autosomal dominant: no generation skipping, affected child has at least one affected parent."),

        # 39. Molecular Basis of Inheritance - Human Genome Project
        ("Molecular Basis of Inheritance", "Key Findings of Human Genome Project", "Direct MCQ",
         "According to the Human Genome Project (HGP), the human genome contains approximately $3.1647 \\times 10^9$ base pairs. What percentage of the genome codes for proteins?",
         ["Less than 2%",
          "Around 25%",
          "Approximately 50%",
          "Over 80%"], 0,
         "A major surprise of the HGP was that less than $2\\%$ of the human genome codes for functional proteins; repeated sequences make up a very large portion of the human genome.",
         "Over 98% of human DNA is non-coding (introns, regulatory sequences, repetitive elements).",
         "Less than 2% of human genome codes for proteins."),

        # 40. Molecular Basis of Inheritance - DNA Fingerprinting
        ("Molecular Basis of Inheritance", "VNTRs and Southern Blotting", "Direct MCQ",
         "In DNA fingerprinting, the probe hybridized to the nitrocellulose membrane to detect genetic polymorphism consists of:",
         ["Radio-labelled single-stranded Variable Number of Tandem Repeats (VNTR)",
          "Double-stranded total genomic DNA",
          "Fluorescently labelled ribosomal RNA",
          "Bacterial plasmid DNA vectors"], 0,
         "DNA fingerprinting uses satellite DNA as probe that shows very high degree of polymorphism (VNTR, a type of minisatellite). The radioactive or fluorescent ssDNA VNTR probe hybridizes specifically to complementary tandem repeat bands on the membrane.",
         "VNTRs belong to minisatellite class of repetitive DNA.",
         "DNA fingerprinting probe is a labelled VNTR showing high individual polymorphism."),

        # 41. Evolution - Origin of Life & Miller's Experiment
        ("Evolution", "Miller-Urey Spark Discharge Experiment", "Direct MCQ",
         "In S.L. Miller's 1953 electric discharge experiment simulating primitive prebiotic Earth conditions, what gas mixture and temperature were maintained inside the closed flask?",
         ["$\\text{CH}_4, \\text{H}_2, \\text{NH}_3$, and water vapour at $800^\\circ\\text{C}$",
          "$\\text{CO}_2, \\text{O}_2, \\text{N}_2$, and water vapour at $100^\\circ\\text{C}$",
          "$\\text{CH}_4, \\text{O}_2, \\text{NH}_3$, and hydrogen at $500^\\circ\\text{C}$",
          "$\\text{CO}, \\text{NH}_3, \\text{H}_2\\text{S}$, and water at $1200^\\circ\\text{C}$"], 0,
         "Miller circulated methane (CH4), hydrogen (H2), ammonia (NH3), and water vapour in a closed glass flask with tungsten electrodes creating sparks at 800 deg C, observing synthesis of amino acids (glycine, alanine, aspartic acid).",
         "Oxygen was absent in the primitive reducing atmosphere.",
         "Miller used $\\text{CH}_4, \\text{H}_2, \\text{NH}_3$, and $\\text{H}_2\\text{O}$ at $800^\\circ\\text{C}$ in a reducing environment."),

        # 42. Evolution - Evidences for Evolution
        ("Evolution", "Homologous vs Analogous Organs", "Direct MCQ",
         "Which of the following pairs of anatomical structures exemplifies analogous evolution resulting from convergent natural selection?",
         ["Wings of butterfly and wings of birds",
          "Forelimbs of cheetah and flippers of whale",
          "Thorns of *Bougainvillea* and tendrils of *Cucurbita*",
          "Heart of crocodile and heart of mammal"], 0,
         "Wings of butterfly (membranous chitin) and wings of birds (feathered bones) perform the same function (flight) but have completely different structural origins, demonstrating convergent evolution (analogy). Other options represent divergent evolution (homology).",
         "Cheetah limb and whale flipper share common pentadactyl bone structure (homology).",
         "Analogous = different origin, same function (convergent); Homologous = same origin (divergent)."),

        # 43. Evolution - Natural Selection Types
        ("Evolution", "Stabilizing vs Directional vs Disruptive Selection", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Stabilizing natural selection favours intermediate phenotypes and eliminates individuals with extreme peripheral traits at both ends of the distribution curve.\n\n"
         "**Statement II:** Disruptive selection favours both peripheral character values simultaneously, leading to two distinct peaks in the population curve and potentially driving sympatric speciation.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. In stabilizing selection (e.g., human infant birth weight), the curve becomes taller and narrower around the mean.\n2. In disruptive selection, individuals at both extremes have higher fitness than intermediate variants, generating a bimodal distribution with two peaks. Both statements are accurate.",
         "Directional selection shifts the peak in one particular direction.",
         "Stabilizing = narrow mean peak; Directional = peak shifts one way; Disruptive = two peripheral peaks."),

        # 44. Evolution - Hardy-Weinberg Principle
        ("Evolution", "Hardy-Weinberg Equilibrium Mathematical Analysis", "Direct MCQ",
         f"In a population in Hardy-Weinberg equilibrium, the frequency of homozygous recessive individuals ($q^2$) for an autosomal trait is {0.04 + (mock_num % 5)*0.01:.2f}. The percentage of heterozygous individuals ($2pq$) in this population is:",
         [f"{2 * (1 - (0.04 + (mock_num % 5)*0.01)**0.5) * ((0.04 + (mock_num % 5)*0.01)**0.5) * 100:.1f}%",
          f"{(0.04 + (mock_num % 5)*0.01)*100:.1f}%",
          f"{(1 - (0.04 + (mock_num % 5)*0.01)**0.5)*100:.1f}%",
          f"{((0.04 + (mock_num % 5)*0.01)**0.5)*100:.1f}%"], 0,
         f"1. $q^2 = {0.04 + (mock_num % 5)*0.01:.2f} \\implies q = \\sqrt{{{0.04 + (mock_num % 5)*0.01:.2f}}} = {(0.04 + (mock_num % 5)*0.01)**0.5:.2f}$.\n"
         f"2. $p = 1 - q = {1 - (0.04 + (mock_num % 5)*0.01)**0.5:.2f}$.\n"
         f"3. Heterozygous frequency $2pq = 2 \\times ({1 - (0.04 + (mock_num % 5)*0.01)**0.5:.2f}) \\times ({(0.04 + (mock_num % 5)*0.01)**0.5:.2f}) = {2 * (1 - (0.04 + (mock_num % 5)*0.01)**0.5) * ((0.04 + (mock_num % 5)*0.01)**0.5) * 100:.1f}\\%$.",
         "Confusing $q^2$ with $q$ or reporting $p^2$ instead of $2pq$ are common errors.",
         "In Hardy-Weinberg equilibrium: $p^2 + 2pq + q^2 = 1$ and $p + q = 1$."),

        # 45. Evolution - Human Evolution
        ("Evolution", "Cranial Capacities of Hominid Ancestors", "Match List",
         "Match List-I with List-II:\n\n"
         "| List-I (Hominid Species) | List-II (Average Cranial Capacity / Feature) |\n"
         "| :--- | :--- |\n"
         "| **A.** *Homo habilis* | **I.** 650 - 800 cc, first tool maker, probably did not eat meat |\n"
         "| **B.** *Homo erectus* | **II.** 900 cc, fossils found in Java (1891), definitely ate meat |\n"
         "| **C.** *Neanderthal man* | **III.** 1400 cc, used hides to protect body and buried their dead |\n"
         "| **D.** *Australopithecus* | **IV.** ~500 cc, lived in East African grasslands, hunted with stone weapons |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-III, C-II, D-IV",
          "A-III, B-II, C-I, D-IV"], 0,
         "Homo habilis: 650-800 cc (A-I). Homo erectus: 900 cc (B-II). Neanderthal man: 1400 cc (C-III). Australopithecines: ~500 cc, hunted with stones and ate fruit (D-IV).",
         "Neanderthal had 1400 cc cranial capacity and buried their dead.",
         "Cranial capacities: *H. habilis* (650-800 cc) < *H. erectus* (900 cc) < Neanderthal (1400 cc)."),

        # 46. Human Health and Disease - Immunity
        ("Human Health and Disease", "Active vs Passive Immunity", "Direct MCQ",
         "Which of the following medical interventions confers immediate passive artificial immunity to a patient?",
         ["Administration of Anti-Tetanus Serum (ATS) containing preformed antibodies",
          "Inoculation with attenuated measles vaccine",
          "Transfer of secretory IgA antibodies through mother's colostrum",
          "Recovery from natural infection of chickenpox virus"], 0,
         "Administration of pre-formed antibodies (ATS, Anti-Snake Venom, anti-rabies antibodies) gives immediate passive artificial immunity. Colostrum provides passive natural immunity. Vaccines stimulate active artificial immunity.",
         "Colostrum is natural passive; ATS is artificial passive; vaccines are artificial active.",
         "Preformed antibodies injected directly constitute artificial passive immunity."),

        # 47. Human Health and Disease - AIDS & Cancer
        ("Human Health and Disease", "HIV Replication Cycle and Cellular Targets", "Direct MCQ",
         "HIV preferentially attacks and destroys which host immune cells, causing progressive collapse of cell-mediated immunity?",
         ["Helper T-lymphocytes ($T_H$ cells carrying CD4 coreceptors)",
          "Cytotoxic T-lymphocytes ($T_C$ cells carrying CD8 receptors)",
          "B-lymphocytes producing circulating antibodies",
          "Erythrocytes and megakaryocytes in red bone marrow"], 0,
         "HIV viral envelope glycoprotein gp120 binds to CD4 receptors on helper T cells and macrophages. The virus replicates inside T-helper cells, lyses them, and progressively depletes $T_H$ cell count, crippling both humoral and cell-mediated immunity.",
         "HIV targets CD4+ helper T-cells, not CD8+ cytotoxic T-cells.",
         "Progressive decrease in CD4+ T-helper lymphocyte count is the hallmark of AIDS."),

        # 48. Human Health and Disease - Drug Abuse
        ("Human Health and Disease", "Opioids, Cannabinoids, and Cocaine", "Direct MCQ",
         "Match the psychoactive drug with its primary biological source and receptor target:\n"
         "1. Morphine: Extracted from latex of *Papaver somniferum*; binds specific opioid receptors in CNS and GI tract.\n"
         "2. Cannabinoids: Obtained from *Cannabis sativa*; interact with cannabinoid receptors principally in the brain, affecting cardiovascular system.\n"
         "3. Cocaine: Alkaloid from *Erythroxylum coca*; interferes with transport and reuptake of the neurotransmitter dopamine.\n\n"
         "Which of the statements given above are correct?",
         ["1, 2, and 3",
          "1 and 2 only",
          "2 and 3 only",
          "1 and 3 only"], 0,
         "All three statements represent exact NCERT facts: Morphine is an opioid from poppy latex; Cannabinoids interact with brain cannabinoid receptors and alter cardiovascular function; Cocaine blocks dopamine reuptake.",
         "Cocaine directly interferes with the reuptake of dopamine.",
         "Morphine = opioid receptors; Cannabinoids = cannabinoid receptors; Cocaine = dopamine transport blocker."),

        # 49. Biotechnology and Its Applications - Transgenic Animals & Gene Therapy
        ("Biotechnology and Its Applications", "Adenosine Deaminase (ADA) Deficiency Gene Therapy", "Direct MCQ",
         "The first clinical gene therapy was given in 1990 to a 4-year-old girl suffering from SCID due to Adenosine Deaminase (ADA) deficiency. The permanent cure for this genetic condition would be:",
         ["Introducing functional ADA cDNA into bone marrow cells at early embryonic stages",
          "Periodic infusion of genetically engineered lymphocytes from patient's blood",
          "Enzyme replacement therapy via periodic intravenous ADA injection",
          "Bone marrow transplantation during adulthood"], 0,
         "Periodic infusion of genetically engineered lymphocytes is not permanent because lymphocytes have a finite lifespan. A permanent cure is possible only if the gene isolated from marrow cells producing ADA is introduced into cells at early embryonic stages.",
         "Lymphocyte infusion is therapeutic but non-permanent due to cell turnover.",
         "Permanent cure for ADA deficiency requires introducing functional cDNA into early embryonic cells."),

        # 50. Biotechnology and Its Applications - Recombinant Insulin & Transgenics
        ("Biotechnology and Its Applications", "Genetically Engineered Human Insulin (Humulin)", "Statement I & II",
         "Given below are two statements:\n\n"
         "**Statement I:** Human pro-insulin contains an extra polypeptide called C-peptide, which is excised during maturation into active insulin.\n\n"
         "**Statement II:** In 1983, Eli Lilly prepared two DNA sequences corresponding to A and B chains of human insulin, introduced them into *E. coli* plasmids, produced chains separately, and combined them by creating disulfide bonds.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Pro-insulin synthesized by pancreatic beta cells contains an extra stretch of amino acids called the C-peptide (33 amino acids), absent in mature active insulin.\n2. In 1983, Eli Lilly synthesized A and B chains separately in *E. coli* and joined them via disulfide bridges in vitro. Both statements are accurate.",
         "Mature insulin does NOT contain the C-peptide.",
         "Human insulin consists of A and B chains linked by disulfide bridges; C-peptide is removed during processing.")
    ]
    
    assert len(topics_data) == 50, f"Expected 50 Zoology topics, got {len(topics_data)}"
    
    for i, item in enumerate(topics_data):
        q_num = 151 + i
        section = "Section A" if i < 35 else "Section B"
        chapter, topic, q_type, text, options, correct_idx, sol_steps, distractor, takeaway = item
        
        q = NeetQuestion(
            q_num=q_num,
            subject="Zoology",
            section=section,
            chapter=chapter,
            topic=topic,
            q_type=q_type,
            text=text,
            options=options,
            correct_idx=correct_idx,
            solution_steps=sol_steps,
            distractor_analysis=distractor,
            takeaway=takeaway
        )
        questions.append(q)
        
    return questions
