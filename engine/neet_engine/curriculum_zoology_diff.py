# -*- coding: utf-8 -*-
"""
NEET Mock Generation Engine - Difficult Curriculum (Zoology)
Strictly calibrated to NTA NEET-UG standards (2023-2027 Predictive Rigor).
Difficult conceptual and analytical depth: nerve impulse kinetics,
renal countercurrent multiplier, hormonal feedback loops, gametogenesis arrest points,
recombinant vector insertional inactivation, Hardy-Weinberg math, and animal taxonomy exceptions.
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

def get_zoology_diff_questions(mock_num):
    questions = []
    shift = (mock_num - 41) * 3

    topics_data = [
        # 1. Human Physiology - Nerve Impulse Kinetics
        ("Neural Control and Coordination", "Action Potential Generation and Ion Channel Gating", "Direct MCQ",
         "During the generation of an action potential along an unmyelinated axon, the rapid depolarization phase of the axonal membrane is primarily caused by:",
         ["Rapid influx of $\\text{Na}^+$ ions through voltage-gated sodium channels down their electrochemical gradient",
          "Rapid efflux of $\\text{K}^+$ ions through voltage-gated potassium channels",
          "Active transport of $3\\text{ Na}^+$ outward and $2\\text{ K}^+$ inward by the sodium-potassium pump",
          "Influx of $\\text{Cl}^-$ ions into the axoplasm causing membrane hyperpolarization"], 0,
         "1. At resting state, the axonal membrane is polarized ($-70\\text{ mV}$) due to high resting permeability to $\\text{K}^+$ and activity of the $\\text{Na}^+/\\text{K}^+$ ATPase pump ($3\\text{ Na}^+$ out, $2\\text{ K}^+$ in).\n2. When a threshold stimulus reaches the axon hillock, voltage-gated $\\text{Na}^+$ channels open rapidly.\n3. $\\text{Na}^+$ ions rush into the axoplasm driven by both chemical concentration gradient and electrical attraction.\n4. This rapid influx reverses the membrane polarity from $-70\\text{ mV}$ to $+30\\text{ mV}$ (depolarization / action potential spike).\n5. Repolarization follows as $\\text{Na}^+$ channels inactivate and voltage-gated $\\text{K}^+$ channels open, allowing $\\text{K}^+$ efflux.",
         "Active $\\text{Na}^+/\\text{K}^+$ pump maintains the resting potential; the action potential spike is driven by passive influx through voltage-gated sodium channels.",
         "Depolarization is caused by rapid passive $\\text{Na}^+$ influx; Repolarization is caused by rapid passive $\\text{K}^+$ efflux."),

        # 2. Human Physiology - Sliding Filament Theory (Statement I & II)
        ("Locomotion and Movement", "Sliding Filament Mechanism Calcium Ion Role in Muscle Contraction", "Statement I & II",
         "Given below are two statements regarding skeletal muscle contraction:\n\n"
         "Statement I: Calcium ions ($Ca^{2+}$) released from the sarcoplasmic reticulum bind to troponin C on actin filaments, causing a conformational change that moves tropomyosin away to expose the myosin-binding sites on actin.\n\n"
         "Statement II: During sarcomere contraction, the length of the dark A-band remains constant while the light I-band and central H-zone shorten.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. At rest, tropomyosin physically masks the active myosin-binding sites on actin thin filaments. When an action potential depolarizes the sarcolemma and T-tubules, $Ca^{2+}$ is released from sarcoplasmic reticulum cisterna. $Ca^{2+}$ binds troponin C, pulling tropomyosin aside and exposing the binding sites for myosin cross-bridge formation. Statement I is correct.\n2. According to the sliding filament theory, actin filaments slide past thick myosin filaments toward the M-line. The length of the thick filaments (A-band) does not change, while the I-band narrows and the H-zone (central region without thin filament overlap) disappears/shortens. Statement II is correct.",
         "Students often incorrectly think the A-band shortens; only the I-band and H-zone shorten.",
         "During muscle contraction: A-band length is invariant; I-band and H-zone shorten as actin slides toward sarcomere center."),

        # 3. Excretion - Countercurrent Mechanism
        ("Excretory Products and Their Elimination", "Henle Loop Countercurrent Multiplier and Medullary Hyperosmolarity", "Direct MCQ",
         "In the mammalian kidney, the high osmolarity gradient ($300\\text{ mOsmol/L}$ in cortex to $1200\\text{ mOsmol/L}$ in inner medulla) is maintained primarily by:",
         ["Active transport of $\\text{NaCl}$ by thick ascending limb of Henle\'s loop and urea recycling by collecting duct",
          "Active transport of water from ascending limb of Henle\'s loop into interstitial fluid",
          "High hydrostatic blood pressure inside peritubular capillaries",
          "Continuous active secretion of potassium and hydrogen ions in proximal convoluted tubule"], 0,
         "1. The countercurrent mechanism operates between the two limbs of Henle\'s loop and the two limbs of the vasa recta.\n2. The descending limb of Henle\'s loop is permeable to water but virtually impermeable to electrolytes; water leaves by osmosis, concentrating the tubular fluid to $1200\\text{ mOsmol/L}$ at the hairpin bend.\n3. The ascending limb is impermeable to water but actively transports $\\text{NaCl}$ into the medullary interstitium in its thick segment.\n4. Urea diffuses out from the lower medullary collecting duct into the interstitium and enters the thin ascending limb, recycling to preserve hypertonicity.\n5. Vasa recta preserves this gradient by countercurrent exchange without washing away medullary solutes.",
         "Water is never actively transported; it moves strictly passively by osmosis.",
         "Medullary hyperosmolarity is generated by active $\\text{NaCl}$ transport in thick ascending limb and maintained by urea recycling and vasa recta."),

        # 4. Excretion - RAAS vs ANF (Assertion & Reason)
        ("Excretory Products and Their Elimination", "Renin-Angiotensin-Aldosterone System vs Atrial Natriuretic Factor", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): Atrial Natriuretic Factor (ANF) acts as an antagonist and natural check on the Renin-Angiotensin-Aldosterone System (RAAS).\n"
         "Reason (R): In response to an increase in blood pressure and atrial blood flow, the heart atria secrete ANF which causes systemic vasodilation and increased excretion of sodium ($\\text{Na}^+$) in urine.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. When GFR or blood pressure falls, the juxtaglomerular apparatus (JGA) releases renin, producing Angiotensin II (a potent vasoconstrictor) which stimulates aldosterone secretion from the adrenal cortex, reabsorbing $\\text{Na}^+$ and water to raise blood pressure.\n2. Conversely, when blood pressure or venous return to the heart increases, atrial stretch triggers secretion of Atrial Natriuretic Factor (ANF). Assertion is TRUE.\n3. ANF induces dilation of renal blood vessels, inhibits renin and aldosterone release, and increases urinary excretion of sodium (natriuresis) and water, effectively reducing blood volume and blood pressure. Thus, ANF directly checks RAAS. Reason is TRUE and explains Assertion.",
         "RAAS increases blood pressure (vasoconstriction + sodium reabsorption); ANF decreases blood pressure (vasodilation + natriuresis).",
         "ANF acts antagonistically to RAAS by causing vasodilation and promoting sodium excretion (natriuresis)."),

        # 5. Endocrine - Hormone Mechanism of Action (Match List)
        ("Chemical Coordination and Integration", "Membrane-bound vs Intracellular Hormone Receptors", "Match List",
         "Match List-I with List-II for hormones and their primary cellular mechanism of action and secondary messengers:\n\n"
         "| List-I (Hormone) | List-II (Receptor Type & Signal Transduction Mechanism) |\n"
         "| :--- | :--- |\n"
         "| **A.** Epinephrine (Adrenaline) | **I.** Membrane-bound receptor; generates cAMP as secondary messenger |\n"
         "| **B.** Follicle Stimulating Hormone (FSH) | **II.** Membrane-bound receptor; generates $IP_3$, $DAG$, and $Ca^{2+}$ |\n"
         "| **C.** Estrogen | **III.** Intracellular nuclear receptor; regulates gene expression at chromosome |\n"
         "| **D.** Thyroxine ($T_4$) | **IV.** Intracellular receptor; directly alters DNA transcription and basal metabolism |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Epinephrine binds adrenergic cell-surface receptors, activating G-protein and adenylate cyclase to produce cyclic AMP (cAMP) $\\to$ I.\n2. Peptide hormones like FSH bind membrane receptors and activate secondary messenger cascades ($cAMP, Ca^{2+}, IP_3$) $\\to$ II.\n3. Steroid hormones (Estrogen, Progesterone, Testosterone, Cortisol) are lipid-soluble, cross the plasma membrane, and bind intracellular nuclear receptors to modulate chromatin transcription $\\to$ III.\n4. Thyroid hormones ($T_3, T_4$) are iodinated amino acids that enter cells and bind nuclear hormone receptors directly on target DNA genes $\\to$ IV.",
         "Steroid and thyroid hormones do NOT need secondary messengers; they pass through lipid membranes directly.",
         "Peptide/protein hormones bind membrane receptors generating secondary messengers; steroid/thyroid hormones bind intracellular nuclear receptors."),

        # 6. Endocrine - Pituitary-Ovarian Feedback
        ("Chemical Coordination and Integration", "Negative and Positive Feedback in Human Menstrual Hormones", "Direct MCQ",
         "During the normal human menstrual cycle, the mid-cycle LH surge that triggers ovulation is induced by:",
         ["A sustained positive feedback surge of high estrogen concentration secreted by the mature Graafian follicle",
          "A sudden sharp drop in progesterone concentration from the corpus luteum",
          "Inhibin secretion by ovarian stroma stimulating the anterior pituitary",
          "Direct negative feedback inhibition of GnRH by progesterone"], 0,
         "1. During the early follicular phase, low estrogen levels exert negative feedback on LH and FSH secretion from the anterior pituitary.\n2. As the Graafian follicle matures, its granulosa and theca cells secrete progressively increasing quantities of estrogen.\n3. When estrogen reaches and maintains an elevated threshold concentration for over 36 hours, it switches from negative feedback to positive feedback on the hypothalamus and anterior pituitary gonadotrophs.\n4. This triggers a massive release of luteinizing hormone (LH surge) around day 14, causing rupture of the mature Graafian follicle and release of the secondary oocyte (ovulation).",
         "Low estrogen causes negative feedback; high sustained estrogen triggers POSITIVE feedback causing the LH surge.",
         "The mid-cycle LH surge triggering ovulation is caused by a positive feedback switch induced by peak estrogen levels."),

        # 7. Reproduction - Meiotic Arrests in Oogenesis (Statement I & II)
        ("Human Reproduction", "Gametogenesis Developmental Milestones and Meiotic Arrest Stages", "Statement I & II",
         "Given below are two statements regarding human oogenesis:\n\n"
         "Statement I: Primary oocytes are formed during embryonic development and remain arrested in the diplotene stage of meiotic Prophase I from birth until puberty.\n\n"
         "Statement II: The secondary oocyte completes meiosis II only upon the entry of a fertilizing sperm into the ovum cytoplasm.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Oogenesis initiates during embryonic gestation; no new oogonia are formed after birth. Oogonia enter meiotic division and become arrested at the diplotene stage of Prophase I as primary oocytes enclosed in primary follicles. This meiotic arrest persists until puberty when individual follicles resume maturation under gonadotropin influence. Statement I is correct.\n2. Following the first meiotic division at ovulation, the secondary oocyte enters meiosis II but arrests at metaphase II. It completes meiosis II only when the fertilizing sperm penetrates the zona pellucida and vitelline membrane, triggering degradation of maturation-promoting factor (MPF) and extruding the second polar body. Statement II is correct.",
         "Confusing primary oocyte arrest (Prophase I diplotene) with secondary oocyte arrest (Metaphase II).",
         "Primary oocyte arrests at Prophase I (diplotene); Secondary oocyte arrests at Metaphase II until sperm fertilization."),

        # 8. Reproduction - Menstrual Cycle Hormonal Coordinates (Match List)
        ("Human Reproduction", "Phases of Menstrual Cycle and Dominant Endocrine Organs", "Match List",
         "Match List-I with List-II for phases of the human menstrual cycle and their physiological features:\n\n"
         "| List-I (Cycle Phase) | List-II (Endocrine Profile and Endometrial State) |\n"
         "| :--- | :--- |\n"
         "| **A.** Menstrual phase (Days $1-5$) | **I.** Breakdown of endometrial lining due to progesterone withdrawal |\n"
         "| **B.** Follicular / Proliferative phase (Days $6-13$) | **II.** Regeneration of endometrium driven by ovarian estrogen |\n"
         "| **C.** Ovulatory phase (Day $14$) | **III.** LH surge triggers rupture of Graafian follicle and oocyte release |\n"
         "| **D.** Luteal / Secretory phase (Days $15-28$) | **IV.** Corpus luteum secretes high progesterone for implantation readiness |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Menstruation occurs when progesterone drops sharply following regression of the corpus luteum into corpus albicans $\\to$ I.\n2. Follicular phase: growing ovarian follicles secrete estrogen which proliferates and thickens the endometrium $\\to$ II.\n3. Ovulatory phase: peak LH surge induces follicular rupture and ovulation $\\to$ III.\n4. Luteal phase: corpus luteum develops and secretes high progesterone, making endometrium highly vascular and secretory for blastocyst implantation $\\to$ IV.",
         "Distractors swap proliferative phase (estrogen-dominant) with secretory phase (progesterone-dominant).",
         "Proliferative phase is driven by estrogen; Secretory phase is maintained by progesterone from the corpus luteum."),

        # 9. Reproduction - Placental Exclusive Hormones
        ("Human Reproduction", "Hormones Secreted Exclusively by Human Placenta During Pregnancy", "Direct MCQ",
         "Which group of hormones is secreted exclusively during pregnancy and is absent in non-pregnant human females?",
         ["Human chorionic gonadotropin (hCG), Human placental lactogen (hPL), and Relaxin",
          "Estrogen, Progesterone, and Prolactin",
          "Oxytocin, Vasopressin, and Aldosterone",
          "Luteinizing Hormone (LH), Follicle Stimulating Hormone (FSH), and Progesterone"], 0,
         "1. During pregnancy, the placenta acts as a transient endocrine organ.\n2. Hormones produced exclusively in pregnant females:\n   - Human chorionic gonadotropin (hCG): maintains corpus luteum and basis of urine pregnancy test kits,\n   - Human placental lactogen (hPL): alters maternal metabolism to ensure fetal nutrition,\n   - Relaxin: secreted by the ovary and placenta to soften pelvic ligaments for parturition.\n3. Other hormones such as estrogens, progesterone, cortisol, prolactin, and thyroxine are also elevated several-fold during pregnancy, but they are also normally present in non-pregnant females.",
         "Progesterone and estrogen are present in non-pregnant females during the normal menstrual cycle; hCG and hPL are unique to pregnancy.",
         "hCG, hPL, and relaxin are produced in women only during pregnancy."),

        # 10. Reproductive Health - ART Techniques
        ("Reproductive Health", "Assisted Reproductive Technologies Clinical Indications", "Direct MCQ",
         "A specialized Assisted Reproductive Technology (ART) procedure in which a single sperm is directly microinjected into the cytoplasm of an ovum in the laboratory to form an embryo is:",
         ["Intra-Cytoplasmic Sperm Injection (ICSI)", "Zygote Intra-Fallopian Transfer (ZIFT)", "Gamete Intra-Fallopian Transfer (GIFT)", "Intra-Uterine Insemination (IUI)"], 0,
         "1. ZIFT: embryo at zygote or up to 8 blastomeres is placed in the fallopian tube $\\to$ I.\n2. IUT: embryo with more than 8 blastomeres (e.g. morula/blastocyst) is transferred into uterus $\\to$ II.\n3. GIFT: used for females who cannot produce ova but can provide suitable environment for fertilization and development; ovum is transferred into fallopian tube $\\to$ III.\n4. ICSI: laboratory procedure where a single sperm is directly injected into the cytoplasm of an ovum $\\to$ IV.",
         "Confusing ZIFT (up to 8 blastomeres into fallopian tube) with IUT (>8 blastomeres into uterus).",
         "Embryo $\\le 8$ blastomeres $\\implies$ ZIFT (fallopian tube); Embryo $> 8$ blastomeres $\\implies$ IUT (uterus)."),

        # 11. Reproductive Health - Contraceptive Mechanisms (Multi-Statement)
        ("Reproductive Health", "Mechanisms of Action of Modern Contraceptive Methods", "Multi-Statement",
         "Consider the contraceptive mechanisms of various family planning methods:\n\n"
         "A. Copper-releasing IUDs (e.g. CuT, Multiload 375) release copper ions that suppress sperm motility and fertilizing capacity.\n"
         "B. Hormone-releasing IUDs (e.g. Progestasert, LNG-20) make the uterus unsuitable for implantation and the cervix hostile to sperms.\n"
         "C. 'Saheli' is a once-a-week non-steroidal oral contraceptive pill developed by CDRI Lucknow with minimal side effects.\n"
         "D. Tubectomy and vasectomy are barrier methods of contraception that prevent gamete production.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Copper ions ($Cu^{2+}$) suppress sperm motility and inhibit sperm fertilizing enzyme capacity. Statement A is TRUE.\n2. Hormone IUDs release levonorgestrel (progestin), thickening cervical mucus to block sperm entry and thinning endometrium to prevent implantation. Statement B is TRUE.\n3. Saheli contains centchroman (a non-steroidal selective estrogen receptor modulator); taken once weekly. Statement C is TRUE.\n4. Tubectomy and vasectomy are surgical sterilization methods (terminal methods). They block gamete transport through the fallopian tubes or vas deferens, but do NOT stop gamete production (gametogenesis) or hormone synthesis. Statement D is FALSE.",
         "Surgical sterilization blocks gamete transport; it does not stop spermatogenesis or oogenesis.",
         "Cu-IUDs suppress sperm motility; Hormone-IUDs prevent implantation and thicken cervical mucus; Surgical methods block gamete transport."),

        # 12. Genetics - Pedigree Analysis Trait Identification
        ("Principles of Inheritance and Variation", "Pedigree Chart Pattern of Inheritance Diagnostic Rules", "Direct MCQ",
         "In a human family pedigree, an inherited disease affects both males and females equally. Affected offspring always have at least one affected parent, and the trait never skips generations. Unaffected parents never have affected children. This pedigree chart represents which mode of inheritance?",
         ["Autosomal dominant (e.g. Myotonic dystrophy)",
          "Autosomal recessive (e.g. Sickle cell anemia)",
          "X-linked recessive (e.g. Hemophilia)",
          "Y-linked (holandric)"], 0,
         "1. Diagnostic rules for pedigree analysis:\n   - Autosomal dominant: Trait appears in every generation without skipping; affected individuals must have at least one affected parent; males and females affected with equal frequency; unaffected parents ($aa \\times aa$) can only have unaffected children ($aa$). Examples: Myotonic dystrophy, Huntington\'s chorea.\n   - Autosomal recessive: Trait frequently skips generations; unaffected carrier parents ($Aa \\times Aa$) can have affected children ($aa$). Examples: Sickle cell anemia, Cystic fibrosis.\n   - X-linked recessive: Skips generations; predominantly affects males; father never passes trait to son (criss-cross inheritance). Examples: Hemophilia, Color blindness.",
         "Autosomal recessive traits skip generations and can appear in children of unaffected carrier parents.",
         "Autosomal dominant traits appear in every generation, affect both sexes equally, and never arise from unaffected parents."),

        # 13. Genetics - Human Chromosomal Syndromes
        ("Principles of Inheritance and Variation", "Aneuploidy Syndromes Karyotypes and Phenotypes", "Direct MCQ",
         "A sterile male individual having 47 chromosomes with karyotype $47, \\text{XXY}$, tall stature, overall masculine development but exhibiting feminine breast development (gynaecomastia) suffers from:",
         ["Klinefelter syndrome", "Down syndrome", "Turner syndrome", "Edward syndrome"], 0,
         "1. Klinefelter syndrome is caused by the presence of an extra X chromosome in males due to non-disjunction of sex chromosomes during gametogenesis, resulting in karyotype $47, \\text{XXY}$.\n2. Affected individuals are phenotypic males with overall masculine development, but possess feminine features including gynaecomastia (breast development), high-pitched voice, sparse body hair, small testes, and azoospermia (sterility).\n3. Turner syndrome: $45, \\text{X0}$ (female with rudimentary ovaries, webbed neck, sterile).\n4. Down syndrome: Trisomy 21 ($47, \\text{XX}+21$ or $47, \\text{XY}+21$), mental retardation, furrowed tongue, palm crease.",
         "Turner syndrome is $45, X0$ in females; Klinefelter syndrome is $47, XXY$ in males.",
         "Klinefelter syndrome ($47, \\text{XXY}$) results in sterile males with gynaecomastia."),

        # 14. Evolution - Hardy-Weinberg Allele Frequencies
        ("Evolution", "Hardy-Weinberg Equilibrium Allele Frequency Mathematical Calculation", "Direct MCQ",
         "In a randomly mating diploid population in Hardy-Weinberg equilibrium consisting of $1000$ individuals, $160$ individuals exhibit the recessive albino phenotype ($aa$). The frequency of the dominant allele $A$ and the expected number of heterozygous carrier individuals ($Aa$) in this population are respectively:",
         ["$p = 0.6$ and $480\\text{ individuals}$",
          "$p = 0.4$ and $480\\text{ individuals}$",
          "$p = 0.84$ and $320\\text{ individuals}$",
          "$p = 0.6$ and $360\\text{ individuals}$"], 0,
         "1. By Hardy-Weinberg principle: $p^2 + 2pq + q^2 = 1$, where $p = \\text{freq}(A)$ and $q = \\text{freq}(a)$.\n2. Genotypic frequency of homozygous recessive individuals ($aa$):\n   $$q^2 = \\frac{160}{1000} = 0.16 \\implies q = \\sqrt{0.16} = 0.40$$.\n3. Since $p + q = 1$:\n   $$p = 1 - q = 1 - 0.40 = 0.60$$.\n4. Frequency of heterozygous genotype ($Aa$):\n   $$2pq = 2 \\times (0.60) \\times (0.40) = 0.48$$.\n5. Expected number of heterozygous carriers in population of 1000:\n   $$\\text{Number of } Aa = 0.48 \\times 1000 = 480\\text{ individuals}$$.\n6. (Check: homozygous dominant $p^2 = (0.6)^2 = 0.36 \\implies 360$ individuals. Total: $360 + 480 + 160 = 1000$).",
         "Forgetting that 160 is $q^2$ (not $q$) is the most frequent calculation error.",
         "Hardy-Weinberg equilibrium: $q = \\sqrt{\\text{recessive fraction}}$, $p = 1 - q$, carriers $= 2pq \\times N$."),

        # 15. Evolution - Modes of Natural Selection
        ("Evolution", "Stabilizing Directional and Disruptive Natural Selection Curves", "Direct MCQ",
         "In a study of human birth weight, infants weighing between $3\\text{ kg}$ and $3.5\\text{ kg}$ have significantly higher survival rates than infants with very low birth weights ($<2\\text{ kg}$) or very high birth weights ($>4.5\\text{ kg}$). This evolutionary pattern is a classic example of:",
         ["Stabilizing selection (favors mean intermediate phenotype)",
          "Directional selection (favors one extreme phenotype)",
          "Disruptive selection (favors both extreme phenotypes)",
          "Genetic drift (Sewall Wright effect)"], 0,
         "1. Natural selection can lead to three distinct phenotypic distribution shifts:\n   - Stabilizing selection: favors the intermediate (mean) phenotype and eliminates extreme variants. The phenotypic distribution curve becomes narrower and taller. Human infant birth weight is the classic textbook example where intermediate weight ($3-3.5\\text{ kg}$) is selected for, while extremes face high neonatal mortality.\n   - Directional selection: favors individuals at one extreme of the phenotypic range, shifting the peak in one direction (e.g. industrial melanism in peppered moth Biston betularia, evolution of antibiotic resistance in bacteria).\n   - Disruptive selection: favors both extreme phenotypes over intermediate forms, splitting the population curve into two separate peaks.",
         "Directional selection shifts the peak; stabilizing selection narrows the peak around the intermediate mean.",
         "Stabilizing selection favors intermediate phenotypes and reduces variation (e.g. human birth weight)."),

        # 16. Evolution - Homologous vs Analogous Organs (Statement I & II)
        ("Evolution", "Divergent vs Convergent Evolution Anatomical Homologies", "Statement I & II",
         "Given below are two statements regarding comparative anatomy in evolution:\n\n"
         "Statement I: The forelimbs of whales, bats, cheetahs, and humans share similar anatomical bone structures (humerus, radius, ulna, carpals) but perform different functions, representing divergent evolution through homology.\n\n"
         "Statement II: The eye of an octopus and the eye of a mammal have different embryonic origins and structural designs but perform similar visual functions, representing convergent evolution through analogy.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Homology indicates common ancestry: identical basic anatomical design and developmental origin adapted to different functional niches (divergent evolution). Vertebrate forelimbs share identical skeletal architecture modified for swimming (whale), flying (bat), running (cheetah), and grasping (human). Statement I is correct.\n2. Analogy indicates convergent evolution: structures that are not anatomically similar and have different embryonic origins evolving independently to serve identical functional roles due to similar ecological pressures. The cephalopod (octopus) eye develops from epidermal invagination, whereas the vertebrate eye develops as an outgrowth of the diencephalic brain. Statement II is correct.",
         "Homology = common ancestry + divergent evolution; Analogy = different origin + convergent evolution.",
         "Homologous structures arise by divergent evolution; Analogous structures arise by convergent evolution."),

        # 17. Evolution - Human Ancestral Chronology (Match List)
        ("Evolution", "Fossil Hominid Chronology and Brain Cranial Capacities", "Match List",
         "Match List-I with List-II for prehistoric human ancestors and their diagnostic brain cranial capacities and tool cultures:\n\n"
         "| List-I (Human Ancestor) | List-II (Cranial Capacity & Diagnostic Characteristic) |\n"
         "| :--- | :--- |\n"
         "| **A.** $Homo \\, habilis$ | **I.** $650 - 800\\text{ cc}$; first handy toolmaker, did not eat meat |\n"
         "| **B.** $Homo \\, erectus$ | **II.** $900\\text{ cc}$; fossils found in Java (1891), ate meat |\n"
         "| **C.** Neanderthal man | **III.** $1400\\text{ cc}$; lived in near-East/Central Asia, buried their dead |\n"
         "| **D.** Australopithecus | **IV.** Walked erect in East African grasslands ($2\\text{ mya}$), hunted with stone |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Homo habilis ('handy man'): brain capacity 650-800 cc, first hominid tool maker, vegetarian $\\to$ I.\n2. Homo erectus (1.5 mya, Java man): brain capacity 900 cc, large brain, probably ate meat $\\to$ II.\n3. Neanderthal man (100,000 - 40,000 years ago): brain capacity 1400 cc, used hides, buried dead with rituals $\\to$ III.\n4. Australopithecines (2 mya): brain capacity 400-500 cc, bipedal hominids in East Africa grasslands $\\to$ IV.",
         "Distractors swap Homo erectus (900 cc) with Homo habilis (650-800 cc).",
         "Human brain capacities: Homo habilis = 650-800 cc; Homo erectus = 900 cc; Neanderthal man = 1400 cc; Modern Homo sapiens = 1350-1450 cc."),

        # 18. Biotechnology - pBR322 Insertional Inactivation
        ("Biotechnology: Principles and Processes", "Selectable Markers and Insertional Inactivation in pBR322", "Direct MCQ",
         "In plasmid vector pBR322, if a foreign DNA fragment is inserted at the $Bam\\text{HI}$ recognition site located within the tetracycline resistance gene ($tet^R$), the recombinant transformants will exhibit:",
         ["Resistance to ampicillin but sensitivity to tetracycline",
          "Resistance to tetracycline but sensitivity to ampicillin",
          "Resistance to both ampicillin and tetracycline",
          "Sensitivity to both ampicillin and tetracycline"], 0,
         "1. Plasmid pBR322 carries two selectable antibiotic resistance marker genes: $amp^R$ (ampicillin resistance) and $tet^R$ (tetracycline resistance).\n2. The $Bam\\text{HI}$ restriction site is located within the coding sequence of the $tet^R$ gene.\n3. Ligation of foreign DNA at the $Bam\\text{HI}$ site disrupts the reading frame of $tet^R$, causing insertional inactivation of tetracycline resistance.\n4. Recombinant plasmids lose resistance to tetracycline but retain an intact, functional $amp^R$ gene.\n5. Transformants grow on ampicillin plates, but when replica-plated onto tetracycline-containing media, recombinants fail to grow.",
         "Inserting into $tet^R$ inactivates tetracycline resistance, leaving ampicillin resistance intact.",
         "Insertional inactivation of a selectable marker allows distinction of recombinant transformants from non-recombinants."),

        # 19. Biotechnology - Gel Electrophoresis (Statement I & II)
        ("Biotechnology: Principles and Processes", "Agarose Gel Electrophoresis Separation and UV Staining", "Statement I & II",
         "Given below are two statements regarding agarose gel electrophoresis:\n\n"
         "Statement I: DNA fragments are negatively charged molecules that migrate toward the anode (positive electrode) under an electric field, separating according to size through the sieving effect of the agarose gel.\n\n"
         "Statement II: Separated DNA bands can be visualized directly under visible white light without any chemical staining.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. DNA carries net negative charge on its phosphate backbone ($PO_4^{3-}$). When an electric field is applied, DNA fragments move toward the positive electrode (anode). Smaller DNA fragments move faster and farther through the agarose matrix (sieving effect). Statement I is correct.\n2. Pure DNA bands cannot be seen under ordinary visible white light. They can only be visualized after staining with ethidium bromide ($EtBr$) followed by exposure to ultraviolet (UV) light, which reveals bright orange fluorescent bands. Statement II is incorrect.",
         "DNA is invisible under visible light; it requires ethidium bromide staining and UV illumination.",
         "DNA migrates toward the anode (+); visualization requires ethidium bromide staining under UV light."),

        # 20. Biotechnology - Transgenic Animals and Bioreactors
        ("Biotechnology and Its Applications", "Therapeutic Proteins Transgenic Animals (Rosie and Alpha-1-Antitrypsin)", "Direct MCQ",
         "Transgenic animals are engineered to produce human therapeutic proteins in their milk. The first transgenic cow, Rosie (produced in 1997), produced human protein-enriched milk ($2.4\\text{ g/L}$) containing which vital human protein?",
         ["Human alpha-lactalbumin", "Alpha-1-antitrypsin", "Human insulin", "Tissue plasminogen activator (tPA)"], 0,
         "1. Rosie was the first transgenic cow produced in 1997.\n2. Her milk contained the human gene for alpha-lactalbumin at a concentration of $2.4\\text{ grams per liter}$.\n3. This milk was nutritionally much more balanced for human babies than natural cow milk.\n4. Note: Alpha-1-antitrypsin is a human protein produced by transgenic animals used in the medical treatment of emphysema.\n5. Transgenic mice are used to test the safety of polio vaccines before human trials.",
         "Alpha-1-antitrypsin is used for treating emphysema; Rosie produced human alpha-lactalbumin.",
         "Rosie the transgenic cow produced human alpha-lactalbumin enriched milk ($2.4\\text{ g/L}$)."),

        # 21. Immunology - Immunoglobulin Classes (Match List)
        ("Human Health and Disease", "Antibody Isotypes Structural Features and Biological Roles", "Match List",
         "Match List-I with List-II for human immunoglobulin (antibody) classes and their primary immunological roles:\n\n"
         "| List-I (Antibody Class) | List-II (Diagnostic Biological Role & Structure) |\n"
         "| :--- | :--- |\n"
         "| **A.** IgG | **I.** Most abundant ($75-80%$), crosses placenta providing natural passive immunity |\n"
         "| **B.** IgA | **II.** Dimeric secretory antibody present in colostrum, saliva, and tears |\n"
         "| **C.** IgM | **III.** Pentameric heavy antibody with $10$ antigen-binding sites; first responder |\n"
         "| **D.** IgE | **IV.** Mediates allergic responses; binds Fc receptors on mast cells and basophils |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. IgG: monomeric, most abundant serum antibody, only isotype that readily crosses maternal placenta to protect fetus $\\to$ I.\n2. IgA: dimer joined by J-chain with secretory component; abundant in colostrum protecting newborn gastrointestinal tract $\\to$ II.\n3. IgM: pentamer with 10 antigen-binding sites, synthesized first in primary immune response $\\to$ III.\n4. IgE: triggers mast cell degranulation releasing histamine and serotonin in Type I hypersensitivity (allergic reactions) $\\to$ IV.",
         "IgG crosses placenta; IgA is in colostrum; IgM is pentamer; IgE is allergy.",
         "IgG crosses the placenta; IgA protects mucosal surfaces (colostrum); IgE mediates allergic responses."),

        # 22. Immunology - Active vs Passive Immunity
        ("Human Health and Disease", "Artificial vs Natural Active and Passive Immunization", "Direct MCQ",
         "A patient bitten by a venomous cobra is immediately injected with antivenom at the hospital emergency ward. This clinical intervention is an example of:",
         ["Artificially acquired passive immunity",
          "Naturally acquired active immunity",
          "Artificially acquired active immunity",
          "Naturally acquired passive immunity"], 0,
         "1. Active immunity: host body produces its own antibodies in response to antigen exposure (slow, long-lasting memory).\n2. Passive immunity: preformed antibodies are directly administered into the recipient from outside (immediate protection, no immunological memory).\n3. Naturally acquired passive immunity: maternal antibodies transferred across placenta (IgG) or in colostrum (IgA) to infant.\n4. Artificially acquired passive immunity: injection of pre-formed antibodies (antivenom for snake bites, anti-tetanus serum ATS for tetanus) providing instant neutralization of lethal toxins.",
         "Vaccination (e.g. Polio, MMR) is artificially acquired ACTIVE immunity; antivenom injection is artificially acquired PASSIVE immunity.",
         "Snake antivenom and tetanus antitoxin contain preformed antibodies, providing artificially acquired passive immunity."),

        # 23. Human Health - Malaria Life Cycle in Host and Vector
        ("Human Health and Disease", "Plasmodium Life Cycle Toxin Release and Chills Mechanism", "Direct MCQ",
         "In the life cycle of $Plasmodium vivax$, the characteristic recurring bouts of high fever with shivering chills every 3 to 4 days are caused by:",
         ["Rupture of erythrocytic schizonts releasing toxic hemozoin granules into the bloodstream",
          "Invasion of human liver hepatocytes by motile sporozoites",
          "Fertilization of gametocytes inside the mosquito stomach",
          "Accumulation of sporozoites in the mosquito salivary glands"], 0,
         "1. Female Anopheles mosquito injects motile infectious sporozoites into human blood during a bite.\n2. Sporozoites migrate to the liver, reproducing asexually inside hepatocytes (hepatic schizogony).\n3. Merozoites emerge from the liver and invade circulating erythrocytes (RBCs), undergoing erythrocytic schizogony.\n4. Inside RBCs, parasites consume hemoglobin, converting toxic free heme into insoluble crystalline pigment called hemozoin.\n5. When RBCs burst synchronously, millions of merozoites and toxic hemozoin granules are released into the blood plasma.\n6. Hemozoin triggers macrophages to release pyrogenic cytokines ($IL-1$ and $TNF$), inducing sudden shivering chills and spike in body temperature.",
         "Liver stage (exoerythrocytic) does not release hemozoin and causes no fever symptoms; fever occurs when RBCs burst.",
         "Malarial fever and chills coincide with the rupture of RBCs releasing hemozoin toxin."),

        # 24. Human Health - Cancer Hallmarks (Multi-Statement)
        ("Human Health and Disease", "Cancer Cell Biological Characteristics and Oncogenic Transformation", "Multi-Statement",
         "Consider the distinctive biological properties of cancerous neoplastic cells:\n\n"
         "A. Normal cells show contact inhibition (inhibition of uncontrolled division by contact with neighboring cells), a property that cancer cells completely lose.\n"
         "B. Metastasis is the most feared characteristic of malignant tumors, where detached cells travel via blood and lymph to establish secondary tumors.\n"
         "C. Proto-oncogenes present in normal cellular genomes can be activated into active oncogenes by mutations or retroviral insertion.\n"
         "D. Benign tumors invade surrounding tissues and spread throughout the body.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Normal cells contact neighbors and arrest division; malignant cancer cells fail to arrest upon contact, forming heaps of unorganized tumor masses. Statement A is TRUE.\n2. Metastasis: malignant cells shed into circulatory and lymphatic vessels, invading distant vital organs to seed secondary tumors. Statement B is TRUE.\n3. Normal cells contain cellular oncogenes (c-onc or proto-oncogenes) that regulate normal cell division; carcinogenic mutagens (ionizing radiation, chemical mutagens) activate them into oncogenes. Statement C is TRUE.\n4. Benign tumors remain strictly localized to their original anatomical site, are encapsulated, and do NOT invade distant organs. Statement D is FALSE.",
         "Benign tumors do not metastasize; malignant tumors exhibit invasive metastasis.",
         "Hallmarks of cancer: loss of contact inhibition, autonomous proliferation, metastasis, and activation of proto-oncogenes."),

        # 25. Circulation - Cardiac Cycle Dynamics and ECG
        ("Body Fluids and Circulation", "ECG Waves Cardiac Output and Stroke Volume Calculation", "Direct MCQ",
         "In a clinical ECG recording of a healthy resting human with a heart rate of $75\\text{ beats per minute}$, the end-diastolic volume (EDV) is $120\\text{ mL}$ and end-systolic volume (ESV) is $50\\text{ mL}$. The stroke volume and total cardiac output are respectively:",
         ["$70\\text{ mL}$ and $5.25\\text{ L/min}$",
          "$50\\text{ mL}$ and $3.75\\text{ L/min}$",
          "$120\\text{ mL}$ and $9.0\\text{ L/min}$",
          "$70\\text{ mL}$ and $7.0\\text{ L/min}$"], 0,
         "1. Stroke Volume ($SV$) is the volume of blood pumped out by each ventricle during one cardiac cycle:\n   $$SV = \\text{EDV} - \\text{ESV} = 120\\text{ mL} - 50\\text{ mL} = 70\\text{ mL}$$.\n2. Cardiac Output ($CO$) is the total volume of blood pumped out by each ventricle per minute:\n   $$CO = SV \\times \\text{Heart Rate} = 70\\text{ mL/beat} \\times 75\\text{ beats/min} = 5250\\text{ mL/min} = 5.25\\text{ L/min}$$.\n3. In ECG: P-wave represents atrial depolarization; QRS complex represents ventricular depolarization; T-wave represents ventricular repolarization.",
         "Confusing stroke volume (70 mL) with end-systolic volume (50 mL).",
         "Stroke volume $SV = \\text{EDV} - \\text{ESV} = 70\\text{ mL}$; Cardiac output $CO = SV \\times \\text{HR} \\approx 5\\text{ L/min}$."),

        # 26. Circulation - Erythroblastosis Foetalis (Assertion & Reason)
        ("Body Fluids and Circulation", "Rh Incompatibility and Erythroblastosis Foetalis Pathology", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): Erythroblastosis foetalis (hemolytic disease of the newborn) can develop in a second child when an $\\text{Rh}^-$ mother carries an $\\text{Rh}^+$ foetus.\n"
         "Reason (R): During the delivery of the first $\\text{Rh}^+$ child, maternal exposure to fetal $\\text{Rh}$ antigens induces the production of anti-$\\text{Rh}$ IgG antibodies which cross the placenta during subsequent pregnancies to destroy fetal red blood cells.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. Rh incompatibility occurs between an $\\text{Rh}^-$ mother and an $\\text{Rh}^+$ fetus. During first pregnancy, fetal and maternal blood are separated by placental barrier and the first baby is born safely. Assertion is TRUE.\n2. During first delivery, disruption of placental barrier allows fetal $\\text{Rh}^+$ RBCs into maternal blood, sensitizing the mother to produce anti-$\\text{Rh}$ antibodies (IgG class).\n3. In subsequent pregnancies with an $\\text{Rh}^+$ fetus, maternal anti-$\\text{Rh}$ IgG antibodies cross the placenta into fetal circulation, hemolyzing fetal RBCs and leading to severe hemolytic anemia, jaundice, and potential fetal hydrops (erythroblastosis foetalis). Administering anti-$\\text{Rh}$ antibodies (RhoGAM) immediately after first delivery prevents sensitization. Reason is TRUE and explains Assertion.",
         "The condition requires Rh- mother and Rh+ fetus (NOT Rh+ mother and Rh- fetus).",
         "Erythroblastosis foetalis occurs when maternal anti-Rh IgG crosses placenta, destroying fetal $\\text{Rh}^+$ erythrocytes."),

        # 27. Respiration - Oxygen Dissociation Curve Shifts
        ("Breathing and Exchange of Gases", "Oxygen-Hemoglobin Dissociation Curve Bohr Effect Factors", "Direct MCQ",
         "The oxygen-hemoglobin dissociation curve exhibits a sigmoid shape. Which set of physiological conditions in active metabolizing tissues promotes the unloading of oxygen from oxyhemoglobin by shifting the curve to the right (Bohr effect)?",
         ["High $p\\text{CO}_2$, High $[\\text{H}^+]$ (Low $pH$), High temperature, and High 2,3-BPG",
          "Low $p\\text{CO}_2$, Low $[\\text{H}^+]$ (High $pH$), Low temperature",
          "High $p\\text{O}_2$, Low $p\\text{CO}_2$, and Low temperature",
          "High $pH$, Low $p\\text{CO}_2$, and High fetal hemoglobin"], 0,
         "1. In active tissues, cellular respiration consumes $O_2$ and produces $CO_2$, heat, and lactic acid.\n2. Conditions at active tissue level:\n   - High $pCO_2$,\n   - High $[H^+]$ (acidic, low pH),\n   - Higher local temperature,\n   - Increased 2,3-bisphosphoglycerate (2,3-BPG).\n3. These factors stabilize the deoxygenated T-state of hemoglobin, lowering its affinity for oxygen and shifting the sigmoid curve to the RIGHT (Bohr effect).\n4. A right shift means hemoglobin releases $O_2$ more readily to active muscle fibers.\n5. Conversely, in pulmonary alveoli (high $pO_2$, low $pCO_2$, low $[H^+]$, lower temperature), the curve shifts to the LEFT to favor oxygen loading.",
         "Shift to right = lower affinity, oxygen UNLOADING (tissue conditions); Shift to left = higher affinity, oxygen LOADING (lung conditions).",
         "Bohr effect shifts curve RIGHT: High $pCO_2$, low $pH$, high temperature promote oxygen delivery to tissues."),

        # 28. Respiration - Respiratory Volumes & Capacities
        ("Breathing and Exchange of Gases", "Spirometric Respiratory Volumes and Vital Capacity", "Match List",
         "Match List-I with List-II for spirometric respiratory volumes and capacities in a healthy adult human:\n\n"
         "| List-I (Respiratory Volume / Capacity) | List-II (Average Volume in mL) |\n"
         "| :--- | :--- |\n"
         "| **A.** Tidal Volume (TV) | **I.** $500\\text{ mL}$ (normal resting breath) |\n"
         "| **B.** Inspiratory Reserve Volume (IRV) | **II.** $2500 - 3000\\text{ mL}$ |\n"
         "| **C.** Expiratory Reserve Volume (ERV) | **III.** $1000 - 1100\\text{ mL}$ |\n"
         "| **D.** Residual Volume (RV) | **IV.** $1100 - 1200\\text{ mL}$ (cannot be measured by simple spirometer) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Tidal Volume: volume inspired or expired during normal quiet breathing $= 500\\text{ mL} \\to$ I.\n2. Inspiratory Reserve Volume: extra volume of air that can be inspired by maximum forced effort above tidal volume $= 2500 - 3000\\text{ mL} \\to$ II.\n3. Expiratory Reserve Volume: additional volume that can be expired by forceful exhalation after normal tidal expiration $= 1000 - 1100\\text{ mL} \\to$ III.\n4. Residual Volume: volume of air remaining in lungs even after maximal forceful expiration $= 1100 - 1200\\text{ mL}$. Residual volume cannot be measured by a standard spirometer $\\to$ IV.\n5. Vital Capacity $VC = ERV + TV + IRV \\approx 4000 - 4600\\text{ mL}$.",
         "Residual volume cannot be emptied from lungs and cannot be recorded directly on a spirometer.",
         "Vital Capacity $VC = TV + IRV + ERV$; Total Lung Capacity $TLC = VC + RV$."),

        # 29. Digestion & Biomolecules - Enzyme Michaelis-Menten
        ("Biomolecules - Animal Physiology", "Competitive Inhibition of Succinate Dehydrogenase by Malonate", "Direct MCQ",
         "The catalytic conversion of succinate to fumarate by the enzyme succinate dehydrogenase in the Krebs cycle is competitively inhibited by malonate because:",
         ["Malonate closely mimics the molecular substrate structure of succinate and competes for the active catalytic site",
          "Malonate binds to an allosteric regulatory site altering the tertiary enzyme conformation",
          "Malonate irreversibly denatures the protein structure of the enzyme",
          "Malonate phosphorylates the coenzyme FAD, preventing electron transfer"], 0,
         "1. Competitive inhibition occurs when an inhibitor compound possesses a chemical structure very similar to the natural substrate.\n2. Succinate is a 4-carbon dicarboxylic acid: $HOOC-CH_2-CH_2-COOH$.\n3. Malonate is a 3-carbon dicarboxylic acid: $HOOC-CH_2-COOH$.\n4. Because of its structural similarity, malonate fits into the active site pocket of succinate dehydrogenase, blocking succinate from binding.\n5. However, the enzyme cannot dehydrogenate malonate, so no product forms.\n6. Increasing substrate (succinate) concentration outcompetes malonate, restoring enzyme activity (reversible competitive inhibition).",
         "Binding to allosteric sites is non-competitive; malonate binds directly to the active catalytic site.",
         "Competitive inhibition is reversible: inhibitor closely resembles substrate and competes for the active site."),

        # 30. Animal Kingdom - Excretory Organs in Invertebrates (Match List)
        ("Animal Kingdom", "Excretory and Osmoregulatory Organs Across Invertebrate Phyla", "Match List",
         "Match List-I with List-II for invertebrate animals and their specialized excretory and osmoregulatory structures:\n\n"
         "| List-I (Animal / Phylum) | List-II (Specialized Excretory Structure) |\n"
         "| :--- | :--- |\n"
         "| **A.** Planaria (Platyhelminthes) | **I.** Flame cells (solenocytes / protonephridia) |\n"
         "| **B.** Earthworm (Annelida) | **II.** Nephridia (septal, integumentary, pharyngeal) |\n"
         "| **C.** Prawn (Crustacean Arthropod) | **III.** Antennal glands (green glands) |\n"
         "| **D.** Cockroach (Insecta) | **IV.** Malpighian tubules |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Platyhelminthes (Planaria, tapeworm): flame cells (protonephridia) for osmoregulation and excretion $\\to$ I.\n2. Annelida (Earthworm): nephridia $\\to$ II.\n3. Crustaceans (Prawns): antennal glands or green glands $\\to$ III.\n4. Insects (Cockroach): Malpighian tubules located at the junction of midgut and hindgut $\\to$ IV.",
         "Distractors swap green glands (prawn) with Malpighian tubules (cockroach).",
         "Planaria = flame cells; Earthworm = nephridia; Prawn = green glands; Cockroach = Malpighian tubules."),

        # 31. Animal Kingdom - Chordates vs Non-chordates (Statement I & II)
        ("Animal Kingdom", "Fundamental Defining Hallmarks of Phylum Chordata", "Statement I & II",
         "Given below are two statements regarding fundamental animal body plans:\n\n"
         "Statement I: All chordates possess a dorsal, hollow, single nerve cord, a solid notochord, paired pharyngeal gill slits, and a post-anal tail at some stage of their life cycle.\n\n"
         "Statement II: In non-chordates, the central nervous system is ventral, solid, and double, while pharyngeal gill slits and post-anal tails are strictly absent.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Chordata fundamental diagnostic criteria: (1) Notochord present, (2) Central nervous system is dorsal, hollow, and single, (3) Pharynx perforated by gill slits, (4) Post-anal tail present, (5) Ventral heart. Statement I is correct.\n2. Non-chordates: Notochord absent; central nervous system is ventral, solid, and double (with paired nerve cords and segmental ganglia); gill slits absent; heart (if present) is dorsal; post-anal tail absent. Statement II is correct.",
         "Confusing nervous system orientation: Chordates have DORSAL hollow nerve cord; Non-chordates have VENTRAL solid nerve cord.",
         "Chordates: dorsal hollow single nerve cord + ventral heart; Non-chordates: ventral solid double nerve cord + dorsal heart."),

        # 32. Animal Kingdom - Monotremes and Marsupials
        ("Animal Kingdom", "Mammalian Classes Viviparity and Oviparous Exceptions", "Direct MCQ",
         "Which of the following mammals is unique in being oviparous (egg-laying), possessing a cloaca and mammary glands lacking true teats?",
         ["Ornithorhynchus (Duck-billed Platypus)", "Macropus (Kangaroo)", "Pteropus (Flying Fox)", "Balaenoptera (Blue Whale)"], 0,
         "1. Class Mammalia is characterized by mammary glands, hair, muscular diaphragm, and 7 cervical vertebrae.\n2. Almost all mammals are viviparous (giving birth to live young).\n3. The subclass Prototheria (monotremes) represents the most primitive living mammals, which are oviparous (egg-laying).\n4. Examples: Ornithorhynchus (Duck-billed platypus) and Tachyglossus (Echidna / spiny anteater).\n5. Macropus (Kangaroo) is a marsupial (pouched viviparous mammal); Pteropus (bat) and Balaenoptera (whale) are placental eutherian viviparous mammals.",
         "Platypus and Echidna are the ONLY egg-laying mammals; kangaroos give birth to immature live young.",
         "Ornithorhynchus (platypus) is an oviparous (egg-laying) mammal."),

        # 33. Structural Organisation - Epithelial Tissues
        ("Structural Organisation in Animals", "Epithelial Tissue Types Locations and Cellular Junctions", "Direct MCQ",
         "Ciliated columnar epithelium consisting of column-like cells bearing cilia on their free apical surfaces is found lining the inner lumen of which human anatomical organs?",
         ["Fallopian tubes (oviducts) and bronchioles",
          "Stomach and intestinal mucosa",
          "Blood vessels and alveoli of lungs",
          "Proximal convoluted tubule (PCT) of nephron"], 0,
         "1. Ciliated epithelium has cilia on free surface that beat rhythmically to move particles, mucus, or gametes in a specific direction.\n2. Found specifically in: inner lining of fallopian tubes (moves ovum towards uterus) and bronchioles of respiratory tract (moves trapped dust particles and mucus outward).\n3. Simple squamous: alveoli and capillary endothelium (diffusion).\n4. Simple cuboidal with brush border microvilli: PCT of nephron (absorption).\n5. Simple columnar with goblet cells: stomach and intestinal mucosa (secretion and absorption).",
         "PCT has microvilli brush border (non-motile for absorption), NOT cilia; fallopian tubes have true motile cilia.",
         "Ciliated epithelium lines the lumen of fallopian tubes and bronchioles to direct fluid and particles."),

        # 34. Cockroach Morphology - Diagnostic Features (Multi-Statement)
        ("Structural Organisation in Animals", "Periplaneta americana Anatomy and Sexual Dimorphism", "Multi-Statement",
         "Consider the morphological and anatomical characteristics of the common cockroach ($Periplaneta americana$):\n\n"
         "A. Sexual dimorphism is evident: male cockroaches bear a pair of short, unjointed anal styles on the 9th sternum, which are absent in females.\n"
         "B. Both male and female cockroaches possess a pair of jointed filamentous anal cerci on the 10th segment.\n"
         "C. The circulatory system is open with a 13-chambered contractile heart situated dorsally.\n"
         "D. Excretion is carried out by green glands located at the junction of foregut and midgut.\n\n"
         "Choose the correct answer from the options given below:",
         ["A, B, and C only", "A and B only", "B, C, and D only", "A, B, C, and D"], 0,
         "1. Male cockroaches possess anal styles on the 9th sternum which are strictly absent in females. Statement A is TRUE.\n2. Both sexes bear jointed, sensitive anal cerci on the 10th tergum. Statement B is TRUE.\n3. Open circulatory system consists of poorly developed vessels and a 13-chambered dorsal heart with ostia. Statement C is TRUE.\n4. Excretion in cockroaches is performed by Malpighian tubules (100-150 yellow fine tubules) located at the junction of midgut and hindgut, NOT green glands (which belong to crustaceans like prawns). Statement D is FALSE.",
         "Anal styles are present ONLY in males; anal cerci are present in BOTH males and females.",
         "Male cockroaches have anal styles on 9th sternum; both sexes have anal cerci on 10th segment; excretion is by Malpighian tubules."),

        # 35. Locomotion - Types of Synovial Joints (Match List)
        ("Locomotion and Movement", "Classification of Synovial Joints and Anatomical Locations", "Match List",
         "Match List-I with List-II for human skeletal joints and their anatomical joint classifications:\n\n"
         "| List-I (Anatomical Skeletal Joint) | List-II (Synovial Joint Classification) |\n"
         "| :--- | :--- |\n"
         "| **A.** Shoulder joint and Hip joint | **I.** Ball and socket joint (multi-axial rotation) |\n"
         "| **B.** Knee joint and Elbow joint | **II.** Hinge joint (uni-axial flexion and extension) |\n"
         "| **C.** Joint between Atlas ($C_1$) and Axis ($C_2$) | **III.** Pivot joint (rotational movement around odontoid process) |\n"
         "| **D.** Joint between Carpal and Metacarpal of Thumb | **IV.** Saddle joint (biaxial movement) |\n\n"
         "Choose the correct answer from the options given below:",
         ["A-I, B-II, C-III, D-IV",
          "A-II, B-I, C-III, D-IV",
          "A-I, B-II, C-IV, D-III",
          "A-III, B-I, C-II, D-IV"], 0,
         "1. Shoulder and hip: head of humerus/femur into glenoid cavity/acetabulum $\\to$ Ball and socket joint $\\to$ I.\n2. Knee and elbow: movement in single plane $\\to$ Hinge joint $\\to$ II.\n3. Atlas-Axis: allows side-to-side head shaking $\\to$ Pivot joint $\\to$ III.\n4. Carpal and metacarpal of thumb: saddle joint giving human opposable thumb dexterity $\\to$ IV.\n5. Gliding joint: between carpal bones.",
         "Distractors swap Pivot joint (Atlas-Axis) with Saddle joint (thumb).",
         "Atlas-Axis = Pivot joint; Thumb carpal-metacarpal = Saddle joint; Shoulder = Ball and socket; Knee = Hinge joint."),

        # 36. Locomotion - Muscular Disorders (Statement I & II)
        ("Locomotion and Movement", "Pathophysiology of Myasthenia Gravis vs Tetany", "Statement I & II",
         "Given below are two statements regarding muscular disorders:\n\n"
         "Statement I: Myasthenia gravis is an autoimmune disorder in which autoantibodies attack nicotinic acetylcholine receptors at the neuromuscular junction, leading to progressive muscle weakness and paralysis.\n\n"
         "Statement II: Tetany is characterized by rapid, violent muscle spasms (cramps) caused by low calcium ($Ca^{2+}$) levels in extracellular body fluids.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is correct but Statement II is incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Myasthenia gravis is an autoimmune disease where circulating antibodies target and destroy acetylcholine receptors on the motor end plate of skeletal muscle fibers. With fewer functional receptors, muscle stimulation declines, causing fatigue, drooping eyelids (ptosis), and eventual respiratory failure. Statement I is correct.\n2. Tetany involves hypocalcemia (low serum $Ca^{2+}$), often due to hypoparathyroidism. Low extracellular calcium increases sodium permeability of nerve and muscle membranes, lowering depolarization thresholds and causing spontaneous, repetitive firings manifest as painful tetanic muscle spasms. Statement II is correct.",
         "Confusing Tetany (hypocalcemic spasms) with Tetanus (bacterial infection by Clostridium tetani).",
         "Myasthenia gravis is an autoimmune disorder against neuromuscular ACh receptors; Tetany is caused by hypocalcemia."),

        # 37. Neural - Ear Equilibrium Receptors
        ("Neural Control and Coordination", "Crista Ampullaris vs Macula in Rotational and Linear Equilibrium", "Direct MCQ",
         "In the human inner ear, which sensory receptors are responsible for dynamic equilibrium (sensing rotational and angular acceleration of the head)?",
         ["Crista ampullaris located in the ampullae of semicircular canals",
          "Maculae located in the utricle and saccule",
          "Organ of Corti on the basilar membrane",
          "Tectorial membrane in the scala media"], 0,
         "1. The inner ear vestibular apparatus consists of three semicircular canals and the otolith organ (utricle and saccule).\n2. Semicircular canals lie at right angles to each other in three planes. The base of each canal is swollen into an ampulla containing the crista ampullaris.\n3. The crista ampullaris bears sensory hair cells embedded in a gelatinous cupula. Endolymph movement during rotational/angular head acceleration displaces the cupula, stimulating hair cells (dynamic rotational equilibrium).\n4. The utricle and saccule contain the macula with otoliths (calcium carbonate stones) that detect static equilibrium and linear acceleration (gravity and head tilt).",
         "Maculae detect linear acceleration and gravity; Crista ampullaris detects rotational angular acceleration.",
         "Rotational / dynamic equilibrium = Crista ampullaris; Linear equilibrium / gravity = Maculae of utricle and saccule."),

        # 38. Neural - Retinal Photoreceptors and Fovea
        ("Neural Control and Coordination", "Rods vs Cones Distribution and Fovea Centralis High Resolution", "Direct MCQ",
         "The fovea centralis of the human retina is the point of greatest visual acuity (resolution) because:",
         ["It is a thinned-out area containing exclusively densely packed cones and zero rods",
          "It contains an equal mixture of rods and cones with thick overlying nerve fibers",
          "It is the exit point of the optic nerve containing no photoreceptors",
          "It contains exclusively rods sensitized by high concentrations of rhodopsin"], 0,
         "1. The macula lutea is a yellowish central area of the retina with a central pit called the fovea centralis.\n2. In the fovea, the ganglion cell and bipolar cell layers are shifted aside, allowing light to strike photoreceptors directly with minimal scattering.\n3. The fovea contains exclusively densely packed cones; rods are completely absent in the fovea.\n4. Each cone in the fovea has a private one-to-one connection to a single ganglion cell, providing maximum daylight photopic color vision and highest resolving power.\n5. The blind spot is where optic nerve fibers exit and retinal blood vessels enter; it lacks all photoreceptors.",
         "The blind spot lacks photoreceptors; the fovea centralis has exclusively CONES for maximum resolution.",
         "Fovea centralis has maximum visual acuity because it contains exclusively densely packed cones with zero rods."),

        # 39. Animal Kingdom - Chondrichthyes vs Osteichthyes
        ("Animal Kingdom", "Diagnostic Features of Cartilaginous vs Bony Fishes", "Direct MCQ",
         "Which combination of features correctly characterizes cartilaginous fishes (Class Chondrichthyes, e.g. $Scoliodon$) in contrast to bony fishes (Class Osteichthyes)?",
         ["Ventral mouth, placoid scales, absence of air bladder (must swim continuously), and pelvic claspers in males",
          "Terminal mouth, cycloid scales, presence of swim bladder, and external fertilization",
          "Ventral mouth, operculum covering gills, and viviparous reproduction",
          "Terminal mouth, placoid scales, air bladder, and pelvic claspers"], 0,
         "1. Chondrichthyes (cartilaginous fishes: sharks, dogfish, rays):\n   - Mouth located ventrally,\n   - Skin covered with microscopic tooth-like placoid scales,\n   - Gills lack an operculum (gill cover) except chimaeras,\n   - Air bladder (swim bladder) is ABSENT; they must swim constantly to avoid sinking,\n   - Internal fertilization with male pelvic fins bearing claspers for copulation.\n2. Osteichthyes (bony fishes: rohu, catla, seahorse): terminal mouth, cycloid/ctenoid scales, operculum present, air bladder present for buoyancy regulation.",
         "Bony fish have swim bladders and terminal mouths; cartilaginous fish have ventral mouths and lack swim bladders.",
         "Chondrichthyes: ventral mouth, placoid scales, lack air bladder (swim continuously), male pelvic claspers."),

        # 40. Animal Kingdom - Cnidaria Metagenesis
        ("Animal Kingdom", "Alternation of Generations (Metagenesis) in Obelia", "Direct MCQ",
         "In cnidarians such as $Obelia$, metagenesis refers to:",
         ["Alternation of generations between asexual sessile polyp forms and sexual free-swimming medusa forms",
          "Metamorphosis from a free-swimming larva to a parasitic adult",
          "Alternation between diploid and haploid multicellular individuals",
          "Regenerative budding of hydranth tentacles"], 0,
         "1. Cnidarians exhibit two basic body forms: sessile, cylindrical Polyps (e.g. Hydra, Adamsia) and umbrella-shaped, free-swimming Medusae (e.g. Aurelia / jellyfish).\n2. Species like Obelia exhibit metagenesis (alternation of generations within diploid phase):\n   - Polyps reproduce asexually by budding to produce free-swimming medusae,\n   - Medusae produce gametes sexually; fertilization yields a ciliated planula larva that settles to develop into a new polyp.\n3. Note: this is different from plant alternation of generations because both polyp and medusa are diploid ($2n$).",
         "Plant metagenesis alternates haploid ($n$) and diploid ($2n$); Cnidarian metagenesis alternates asexual polyp with sexual medusa (both $2n$).",
         "In Obelia: Polyps reproduce asexually to form medusae; Medusae reproduce sexually to form polyps."),

        # 41. Immunology - HIV Pathogenesis (Assertion & Reason)
        ("Human Health and Disease", "Retrovirus HIV Infection Mechanism and Macrophage Factory", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): During HIV infection, the virus uses macrophages as an 'HIV factory' while progressively depleting helper T-lymphocytes ($T_H$ cells), causing severe immunocompromise.\n"
         "Reason (R): In macrophages, viral RNA genome is transcribed into viral DNA by reverse transcriptase and integrated into host DNA, continuously producing new viral progeny without destroying the macrophage.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. HIV is an enveloped retrovirus containing two copies of single-stranded RNA and reverse transcriptase. It binds CD4 receptors on macrophages and helper T-cells ($CD4^+ T_H$).\n2. Upon entry into macrophages, viral reverse transcriptase converts viral RNA into double-stranded complementary DNA. Viral DNA integrates into host chromosomes (provirus), directing synthesis of new viral particles.\n3. Macrophages survive infection and continually shed new virions into blood, serving as an ongoing 'HIV factory'. Assertion is TRUE.\n4. Simultaneously, HIV enters helper T-lymphocytes ($T_H$), replicates, and lyses them. Progressive decline in $T_H$ count below $200\\text{ cells/}\\mu\\text{L}$ impairs both cell-mediated and humoral immunity, rendering patient vulnerable to opportunistic pathogens like Mycobacterium, Toxoplasma, and cytomegalovirus. Reason is TRUE and explains Assertion.",
         "Macrophages act as a continuous factory because the virus buds out without immediately lysing the macrophage, unlike helper T-cells.",
         "Macrophages serve as HIV factories producing virions continually; progressive destruction of helper T-lymphocytes causes AIDS."),

        # 42. Human Health - Drug Abuse Classifications
        ("Human Health and Disease", "Opioids Cannabinoids and Cocaine Neurotransmitter Receptors", "Direct MCQ",
         "Which addictive drug is a central nervous system depressant that slows down body functions, is chemically diacetylmorphine, and binds to specific opioid receptors in the CNS and gastrointestinal tract?",
         ["Heroin (Smack)", "Cocaine (Crack)", "Charas (Cannabinoid)", "LSD (Lysergic acid diethylamide)"], 0,
         "1. Opioids bind to specific opioid receptors in the central nervous system and gastrointestinal tract.\n2. Morphine is extracted from the latex of the opium poppy ($Papaver somniferum$).\n3. Acetylation of morphine (reaction with acetic anhydride) yields diacetylmorphine, commonly known as heroin or smack.\n4. Heroin is a white, odorless, bitter crystalline compound taken by snorting or injection.\n5. It acts as a depressant, slowing down nervous and physiological functions.\n6. Cocaine is a stimulant that interferes with dopamine reuptake; Cannabinoids interact with cannabinoid receptors affecting the cardiovascular system.",
         "Cocaine is a stimulant; Heroin (diacetylmorphine) is a depressant.",
         "Heroin (smack) is diacetylmorphine, an opioid that acts as a central nervous system depressant."),

        # 43. Biotechnology - ADA Gene Therapy
        ("Biotechnology and Its Applications", "First Clinical Gene Therapy for Adenosine Deaminase Deficiency", "Direct MCQ",
         "The first clinical gene therapy was administered in 1990 to a 4-year-old girl suffering from Severe Combined Immunodeficiency (SCID) caused by a deficiency of which enzyme, and what was the delivery vector used?",
         ["Adenosine deaminase (ADA) using a retroviral vector to introduce functional cDNA into patient lymphocytes",
          "Alpha-1-antitrypsin using Agrobacterium tumefaciens",
          "Insulin using a bacteriophage lambda vector",
          "Beta-galactosidase using a plasmid vector into bone marrow stem cells"], 0,
         "1. Severe Combined Immunodeficiency (SCID) is caused by deletion or mutation of the gene coding for adenosine deaminase (ADA), an enzyme vital for purine metabolism and immune lymphocyte function.\n2. In the 1990 clinical gene therapy, lymphocytes were isolated from the patient\'s blood and grown in culture in vitro.\n3. A functional human ADA complementary DNA (cDNA) was introduced into these lymphocytes using a disarmed retroviral vector.\n4. The genetically engineered lymphocytes were infused back into the patient, temporarily restoring immune function.\n5. Because mature lymphocytes have a finite lifespan, periodic re-infusions are required; a permanent cure requires introducing the gene into bone marrow stem cells at an early embryonic stage.",
         "Agrobacterium is for plants; retroviral vectors are used for animal human gene therapy.",
         "First clinical gene therapy (1990) treated ADA deficiency by introducing functional ADA cDNA via retroviral vectors into lymphocytes."),

        # 44. Human Physiology - Gas Transport Mechanisms (Assertion & Reason)
        ("Breathing and Exchange of Gases", "Carbon Dioxide Transport as Bicarbonate and Chloride Shift", "Assertion & Reason",
         "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R):\n\n"
         "Assertion (A): During carbon dioxide transport in blood, chloride ions ($\\text{Cl}^-$) diffuse from plasma into erythrocytes at tissue capillaries (Chloride Shift or Hamburger phenomenon).\n"
         "Reason (R): In tissue capillaries, hydration of $\\text{CO}_2$ by carbonic anhydrase produces bicarbonate ions ($\\text{HCO}_3^-$) which diffuse out into plasma, requiring $\\text{Cl}^-$ influx to maintain electrical neutrality.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
          "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
          "(A) is true but (R) is false",
          "(A) is false but (R) is true"], 0,
         "1. $\\approx 70%$ of $CO_2$ is transported as bicarbonate ($HCO_3^-$) in plasma.\n2. In tissue capillaries, $CO_2$ diffuses into RBCs where carbonic anhydrase catalyzes: $CO_2 + H_2O \\rightleftharpoons H_2CO_3 \\rightleftharpoons H^+ + HCO_3^-$.\n3. Accumulation of $HCO_3^-$ creates a concentration gradient, causing $HCO_3^-$ to diffuse out of RBCs into blood plasma through an anion exchanger protein (AE1).\n4. To maintain electrical neutrality across the erythrocyte membrane, chloride ions ($Cl^-$) diffuse from plasma into the RBC. This is the Hamburger phenomenon (Chloride Shift). Assertion is TRUE.\n5. In pulmonary capillaries, the process reverses: $Cl^-$ moves out and $HCO_3^-$ moves in to be converted back to $CO_2$ and exhaled. Reason is TRUE and explains Assertion.",
         "Chloride moves INTO RBCs at tissues; chloride moves OUT of RBCs at lungs.",
         "Chloride shift (Hamburger phenomenon): $Cl^-$ enters RBCs in tissue capillaries to balance $HCO_3^-$ efflux into plasma."),

        # 45. Human Physiology - Glomerular Filtration Rate Math
        ("Excretory Products and Their Elimination", "Net Filtration Pressure and GFR Regulation", "Direct MCQ",
         "In human kidneys, if glomerular hydrostatic pressure is $GHP = 60\\text{ mmHg}$, blood colloid osmotic pressure is $BCOP = 32\\text{ mmHg}$, and capsular hydrostatic pressure is $CHP = 18\\text{ mmHg}$, the net effective filtration pressure (NFP) driving glomerular filtration is:",
         ["$10\\text{ mmHg}$", "$20\\text{ mmHg}$", "$42\\text{ mmHg}$", "$28\\text{ mmHg}$"], 0,
         "1. Net Filtration Pressure ($NFP$) is the net driving pressure across the glomerular filtration membrane.\n2. Outward driving force favoring filtration: Glomerular Hydrostatic Pressure ($GHP = 60\\text{ mmHg}$).\n3. Inward opposing forces resisting filtration:\n   - Blood Colloid Osmotic Pressure due to plasma proteins ($BCOP = 32\\text{ mmHg}$),\n   - Capsular Hydrostatic Pressure in Bowman\'s space ($CHP = 18\\text{ mmHg}$).\n4. Net Filtration Pressure formula:\n   $$NFP = GHP - (BCOP + CHP) = 60\\text{ mmHg} - (32 + 18)\\text{ mmHg} = 60 - 50 = 10\\text{ mmHg}$$.\n5. This positive net pressure of $10\\text{ mmHg}$ drives a normal GFR of $125\\text{ mL/min}$ ($180\\text{ L/day}$).",
         "Adding opposing pressures: 32 + 18 = 50 mmHg; subtracting from 60 gives 10 mmHg.",
         "Net filtration pressure: $NFP = GHP - (BCOP + CHP) = 60 - (32 + 18) = 10\\text{ mmHg}$."),

        # 46. Reproduction - Cleavage and Blastocyst Hatching (Statement I & II)
        ("Human Reproduction", "Zygotic Cleavage Divisions and Blastocyst Implantation Stages", "Statement I & II",
         "Given below are two statements regarding human embryonic development:\n\n"
         "Statement I: Cleavage divisions in the human zygote are holoblastic, rotational, and asynchronous, leading to a solid multicellular morula ($16$ cells) that enters the uterine cavity.\n\n"
         "Statement II: The blastocyst implants into the maternal endometrium via its inner cell mass while the zona pellucida remains intact around the embryo.\n\n"
         "In the light of the above statements, choose the correct answer from the options given below:",
         ["Statement I is correct but Statement II is incorrect",
          "Both Statement I and Statement II are correct",
          "Both Statement I and Statement II are incorrect",
          "Statement I is incorrect but Statement II is correct"], 0,
         "1. Human cleavage is holoblastic (entire zygote divides) and unequal/rotational, without any intervening growth phase between divisions. By day 3-4, a solid mulberry-like ball of 16-32 cells (morula) is formed which moves through the isthmus into the uterus. Statement I is correct.\n2. The morula develops into a hollow blastocyst with an outer layer of trophoblast cells and an inner cell mass. The blastocyst MUST shed its thick acellular glycoprotein coat (zona pellucida) in a process called 'hatching' before implantation. Implantation occurs when the bare trophoblast cells attach and invade the uterine endometrium (day 6-7). Statement II is incorrect because the zona pellucida must shed, and attachment occurs via trophoblast, not inner cell mass.",
         "Zona pellucida prevents ectopic implantation in the fallopian tube and MUST shed ('hatch') before uterine implantation.",
         "Implantation occurs via outer trophoblast cells after shedding the zona pellucida (blastocyst hatching)."),

        # 47. Endocrine - Endocrine Disorders
        ("Chemical Coordination and Integration", "Endocrine Hypersecretion and Hyposecretion Clinical Syndromes", "Direct MCQ",
         "A patient diagnosed with hypersecretion of cortisol from the adrenal cortex presenting with central obesity, 'moon face', 'buffalo hump', hypertension, and persistent hyperglycemia suffers from:",
         ["Cushing\'s syndrome", "Addison\'s disease", "Graves\' disease", "Acromegaly"], 0,
         "1. Addison\'s disease: deficiency of glucocorticoids and mineralocorticoids due to adrenal cortex destruction; causes extreme fatigue, weakness, bronze skin pigmentation, hypotension $\\to$ I.\n2. Cushing\'s syndrome: excess cortisol hypersecretion $\\to$ II.\n3. Graves\' disease: autoimmune hyperthyroidism where autoantibodies stimulate TSH receptors, causing enlarged thyroid, bulging eyes (exophthalmos), weight loss $\\to$ III.\n4. Acromegaly: excess GH after epiphyseal plate closure in adults causing enlargement of hands, feet, and facial bones $\\to$ IV.",
         "Distractors swap Addison\'s disease (hypoadrenalism) with Cushing\'s syndrome (hyperadrenalism).",
         "Addison = hypoadrenalism; Cushing = hypercortisolism; Graves = hyperthyroidism; Acromegaly = adult GH excess."),

        # 48. Animal Classification - Coelom Types
        ("Animal Kingdom", "Body Cavity (Coelom) Classifications Across Metazoan Phyla", "Direct MCQ",
         "Which phylum consists of triploblastic, bilaterally symmetrical animals that possess a pseudocoelom (false body cavity where mesoderm is scattered as pouches between ectoderm and endoderm)?",
         ["Aschelminthes (Nematoda, e.g. $Ascaris$)",
          "Platyhelminthes (Flatworms, e.g. $Taenia$)",
          "Annelida (Segmented worms, e.g. $Nereis$)",
          "Echinodermata (Spiny-skinned animals, e.g. $Asterias$)"], 0,
         "1. Acoelomates: no body cavity; space between gut and body wall filled with mesodermal parenchyma (Platyhelminthes / Flatworms).\n2. Pseudocoelomates: body cavity is not lined by continuous mesodermal peritoneum; instead, mesoderm exists as scattered patches/pouches between ectoderm and endoderm. This condition is uniquely diagnostic of Phylum Aschelminthes (roundworms like Ascaris, Wuchereria, Ancylostoma).\n3. Eucoelomates (True coelomates): body cavity completely lined by mesodermal peritoneum (Annelids, Arthropods, Molluscs, Echinoderms, Hemichordates, Chordates).",
         "Platyhelminthes are acoelomate; Aschelminthes are pseudocoelomate; Annelids are true coelomates.",
         "Aschelminthes (roundworms) are the ONLY pseudocoelomate animal phylum in the animal kingdom."),

        # 49. Animal Physiology - Synaptic Transmission Blockers
        ("Neural Control and Coordination", "Neurotransmitter Release and Pharmacological Receptor Antagonists", "Direct MCQ",
         "Curare is a plant toxin historically used on arrow tips. It causes flaccid muscle paralysis and death by asphyxiation by acting as a competitive antagonist that blocks:",
         ["Nicotinic acetylcholine receptors on the motor end plate",
          "Voltage-gated calcium channels on the presynaptic terminal",
          "Acetylcholinesterase enzyme in the synaptic cleft",
          "Sodium-potassium ATPase pump in axonal membranes"], 0,
         "1. At the neuromuscular junction, motor axon terminals release the neurotransmitter acetylcholine (ACh) into the synaptic cleft.\n2. ACh binds nicotinic acetylcholine receptors ($nAChR$) on the skeletal muscle motor end plate, opening cation channels that depolarize the muscle fiber (end plate potential).\n3. Curare (specifically d-tubocurarine) binds competitively to nicotinic ACh receptors without opening the ion channel, preventing acetylcholine from binding.\n4. Without receptor activation, skeletal muscles (including the diaphragm and intercostal respiratory muscles) cannot contract, causing flaccid paralysis and death from respiratory failure.\n5. Note: Botulinum toxin inhibits ACh release; Organophosphates inhibit acetylcholinesterase.",
         "Organophosphate nerve agents inhibit acetylcholinesterase; Curare blocks the nicotinic acetylcholine receptor.",
         "Curare causes flaccid paralysis by competitively blocking nicotinic acetylcholine receptors at the motor end plate."),

        # 50. Biotechnology - PCR Stages and Primer Annealing
        ("Biotechnology: Principles and Processes", "Polymerase Chain Reaction Thermocycling and Primer Design", "Direct MCQ",
         "In the Polymerase Chain Reaction (PCR), chemically synthesized oligonucleotide primers anneal specifically to which region of the separated single-stranded template DNA molecules during the annealing step?",
         ["To the $3\'$ ends of both template strands in antiparallel orientation",
          "To the $5\'$ ends of both template strands",
          "To the center of the gene of interest",
          "Exclusively to the lagging strand template"], 0,
         "1. PCR consists of three sequential steps repeated over 30 cycles:\n   - Step 1: Denaturation at $94-96^\\circ\\text{C}$ (breaks hydrogen bonds, producing single-stranded DNA templates),\n   - Step 2: Annealing at $50-60^\\circ\\text{C}$ (short forward and reverse primers hybridize to complementary sequences),\n   - Step 3: Extension at $72^\\circ\\text{C}$ (thermostable Taq DNA polymerase adds dNTPs from $5\'$ to $3\'$).\n2. DNA polymerases can only add nucleotides to an existing $3\'$ hydroxyl ($-OH$) group.\n3. Therefore, primers must anneal to the $3\'$ ends of the template strands so that polymerization proceeds in the $5\' \\to 3\'$ direction along both strands.",
         "DNA synthesis proceeds $5' \\to 3'$; therefore, primers anneal to the $3'$ ends of the template strands.",
         "In PCR, primers anneal to the $3'$ ends of template DNA strands; Taq polymerase extends in the $5' \\to 3'$ direction.")
    ]

    assert len(topics_data) == 50, f"Expected 50 Zoology topics, got {len(topics_data)}"

    # Dynamic rotation across Mocks 41 to 60 so each mock starts with a distinct chapter sequence
    rotated = topics_data[shift % 50:] + topics_data[:shift % 50]

    for i, item in enumerate(rotated):
        chapter, topic, q_type, text, options, correct_idx, solution_steps, distractor_analysis, takeaway = item
        q_num = i + 1  # 1 to 50
        sec = "Section A" if q_num <= 35 else "Section B"
        q = NeetQuestion(
            q_num=q_num,
            subject="Zoology",
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
