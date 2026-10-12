# Radiative Transfer: a Graduated Course for Pre-Master Students (with LTE Solutions)

A self-contained, illustrated course in **radiative transfer** for students preparing for an **Astrophysics master's programme**. It is built in 10 lectures that go from the definition of specific intensity to the full solution of the **gray LTE stellar atmosphere** and **LTE line formation**. Every lecture contains derivations, figures, worked numerical examples, and **3–4 exam questions with complete answers**. A final exam with full solutions and a formula sheet close the course.

📘 **Read the whole course as one PDF:** [`Radiative_Transfer_Course.pdf`](Radiative_Transfer_Course.pdf)

## Contents

| # | Lecture | Highlights |
|---|---|---|
| 1 | [Introduction: how the RTE is used in astrophysics](course/L01_introduction.md) | RTE, TE vs LTE vs NLTE, applications |
| 2 | [Describing the radiation field](course/L02_radiation_field.md) | $I_\nu$, $J_\nu$, $F_\nu$, $K_\nu$; conservation of intensity; solar constant |
| 3 | [Black-body radiation](course/L03_blackbody.md) | Planck derivation, Wien, Stefan–Boltzmann, brightness temperature, CMB |
| 4 | [Emission, absorption, scattering](course/L04_emission_absorption.md) | $\alpha_\nu = n\sigma = \rho\kappa$, Einstein relations, masers, random walk |
| 5 | [The RTE and its formal solution](course/L05_rte_formal_solution.md) | slab solution; **MIT 8.901 toy models**: thin H cloud (Rydberg emission lines), two-layer star, thermal inversion; H II regions |
| 6 | [Thermodynamic equilibrium and **LTE**](course/L06_LTE.md) | Kirchhoff's law, $S_\nu = B_\nu$, Saha–Boltzmann, two-level atom |
| 7 | [Plane-parallel atmospheres](course/L07_plane_parallel.md) | Schwarzschild–Milne, $E_n$, Eddington–Barbier, limb-darkening inversion |
| 8 | [Moments, diffusion and scattering](course/L08_moments_diffusion_scattering.md) | Eddington approximation, Rosseland mean, $S(0) = \sqrt\varepsilon B$, Λ-iteration |
| 9 | [**The gray LTE atmosphere — complete solution**](course/L09_gray_LTE_atmosphere.md) | $T^4 = \tfrac34T_{\rm eff}^4(\tau+q)$, Hopf function, $H$-function, emergent spectrum |
| 10 | [**LTE spectral lines** and the limits of LTE](course/L10_LTE_lines_and_beyond.md) | Milne–Eddington, curve of growth, abundances, NLTE |
| 11 | [Final exam with complete solutions](course/L11_final_exam_solutions.md) | 15 short questions, 12 problems, 2 essays |
| 12 | [Formula sheet](course/L12_formula_sheet.md) | all key results on 2 pages |

## How to study

1. Read each lecture in order; the difficulty increases gradually.
2. Re-derive every boxed equation yourself.
3. Redo each worked example without looking at the solution.
4. Answer the exam questions at the end of each lecture, then check the answers.
5. Finish with the final exam under exam conditions (3 hours).

## Code: numerical LTE solutions

All figures and all numbers in the worked examples are produced by the Python scripts in [`scripts/`](scripts):

| Script | What it does |
|---|---|
| [`lte_solvers.py`](scripts/lte_solvers.py) | Planck functions; the **Λ operator** as a matrix; exact solution of $S = \varepsilon B+(1-\varepsilon)J$; Λ-iteration; **exact gray LTE atmosphere** (Hopf function); Chandrasekhar $H$-function; Milne–Eddington line profiles and curves of growth; Saha–Boltzmann for hydrogen |
| [`make_figures.py`](scripts/make_figures.py) | regenerates every figure in [`figures/`](figures) |
| [`worked_examples.py`](scripts/worked_examples.py) | prints every numerical answer quoted in the lectures |
| [`build_pdf.sh`](scripts/build_pdf.sh) | builds the PDF (pandoc + KaTeX + headless Chromium) |

```bash
pip install numpy scipy matplotlib
python3 scripts/lte_solvers.py        # self-test against known exact results
python3 scripts/make_figures.py       # regenerate all figures
python3 scripts/worked_examples.py    # reproduce all numbers
```

The solvers reproduce known exact results: $q(0) = 1/\sqrt3$, $q(\infty) = 0.7104$, $H(1) = 2.9078$, the limb-darkening ratio $I(0)/I(1) = 0.3439$ (Chandrasekhar 1950, Table), and $S(0) = \sqrt\varepsilon\,B$.

## References used

1. A670 *Advanced Astrophysics*, Lecture 1: *Introduction — How is the RTE used in astrophysics?*
2. W. Hu, *Astro 305 Lecture Notes, Set 1: Radiative Transfer*, University of Chicago.
3. MIT 8.901 *Astrophysics I* (Spring 2019), Lecture 7: *Radiative Transfer*. Its three-step build-up of the RTE, Kirchhoff's law for thick and thin objects, the thin hydrogen cloud, the two-layer stellar atmosphere and thermal inversions are reproduced (with computed figures) in Lecture 5, and cross-referenced in Lectures 6 and 10.
4. G. W. Collins II, *The Fundamentals of Stellar Astrophysics* (2003), Part II, Ch. 9: *The Flow of Radiation Through the Atmosphere*.
5. S. Chandrasekhar, *Radiative Transfer* (Oxford 1950; Dover 1960), Chs. I, III, V, XII.

Further reading: Rybicki & Lightman, *Radiative Processes in Astrophysics*; Mihalas, *Stellar Atmospheres*; Gray, *The Observation and Analysis of Stellar Photospheres*; Hubeny & Mihalas, *Theory of Stellar Atmospheres*.
