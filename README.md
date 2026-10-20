# Radiative Transfer and Stellar Atmospheres: Two Graduated Courses for Pre-Master Students

Two self-contained, illustrated courses for students preparing for an **Astrophysics master's programme**:

| Course | Lectures | PDF |
|---|---|---|
| **A. Radiative Transfer**: the theory of how radiation moves through matter | RT1–RT10, exam RT11, formula sheet RT12 | [`Radiative_Transfer_Course.pdf`](Radiative_Transfer_Course.pdf) |
| **B. Stellar Atmospheres**: physical processes, transition rates (after Mihalas), LTE and non-LTE, model atmospheres | SA0–SA8, exam SA9, formula sheet SA10 | [`Stellar_Atmospheres_Course.pdf`](Stellar_Atmospheres_Course.pdf) |

Take Course A first; Course B uses its results. Every lecture follows the same structure:

1. **Learning goals**
2. **Key concepts in plain words**: each idea explained physically, with everyday analogies, before any mathematics
3. **Theory and derivations** with figures
4. **Worked numerical examples**
5. **Common misconceptions**: the mistakes students most often make
6. **Lecture summary**
7. **3–4 exam questions with complete answers**

## Course A — Radiative Transfer ([`courses/radiative-transfer/`](courses/radiative-transfer))

| # | Lecture | Highlights |
|---|---|---|
| RT1 | [Introduction: how the RTE is used in astrophysics](courses/radiative-transfer/RT01_introduction.md) | RTE, TE vs LTE vs NLTE, applications |
| RT2 | [Describing the radiation field](courses/radiative-transfer/RT02_radiation_field.md) | $I_\nu$, $J_\nu$, $F_\nu$, $K_\nu$; conservation of intensity; solar constant |
| RT3 | [Black-body radiation](courses/radiative-transfer/RT03_blackbody.md) | Planck derivation, Wien, Stefan–Boltzmann, brightness temperature, CMB |
| RT4 | [Emission, absorption, scattering](courses/radiative-transfer/RT04_emission_absorption.md) | $\alpha_\nu = n\sigma = \rho\kappa$, Einstein relations, masers, random walk |
| RT5 | [The RTE and its formal solution](courses/radiative-transfer/RT05_rte_formal_solution.md) | slab solution; MIT 8.901 toy models (thin H cloud, two-layer star, thermal inversion); H II regions |
| RT6 | [How the radiative transfer equation is formed](courses/radiative-transfer/RT06_forming_the_RTE.md) | Boltzmann equation → general RTE → special forms; energy and momentum moments |
| RT7 | [Plane-parallel atmospheres](courses/radiative-transfer/RT07_plane_parallel.md) | Schwarzschild–Milne, $E_n$, Eddington–Barbier, limb-darkening inversion |
| RT8 | [Moments, diffusion and scattering](courses/radiative-transfer/RT08_moments_diffusion_scattering.md) | Eddington approximation, Rosseland mean, $S(0) = \sqrt\varepsilon B$, Λ-iteration |
| RT9 | [Polarized light](courses/radiative-transfer/RT09_polarized_light.md) | Stokes parameters, polarized RTE, 11.7 % limb polarization, Zeeman and Hanle effects |
| RT10 | [Historical context of approximations and solutions](courses/radiative-transfer/RT10_history_of_approximations.md) | Schuster, Schwarzschild, Eddington, Milne, Hopf, Chandrasekhar → ALI, 3D |
| RT11 | [Final exam with complete solutions](courses/radiative-transfer/RT11_final_exam.md) | short answers, 8 problems, 3 further-topic questions, essay |
| RT12 | [Formula sheet](courses/radiative-transfer/RT12_formula_sheet.md) | |

## Course B — Stellar Atmospheres ([`courses/stellar-atmospheres/`](courses/stellar-atmospheres))

| # | Lecture | Highlights |
|---|---|---|
| SA0 | [Course overview](courses/stellar-atmospheres/SA00_overview.md) | what an atmosphere is, prerequisites, Collins' five assumptions |
| SA1 | [Thermodynamic state: LTE, Saha–Boltzmann, Kirchhoff](courses/stellar-atmospheres/SA01_LTE_thermodynamics.md) | Kirchhoff's law, $S_\nu = B_\nu$, Balmer-line strength, two-level atom |
| SA2 | [**Physical processes I: continuous opacity**](courses/stellar-atmospheres/SA02_continuous_opacity.md) | Kramers bound–free, free–free, H$^-$, scattering, Balmer jump |
| SA3 | [**Physical processes II: transition rates and statistical equilibrium**](courses/stellar-atmospheres/SA03_transition_rates.md) | radiative and collisional rates, Einstein/Milne/Klein–Rosseland relations, coronal and nebular limits, critical density |
| SA4 | [**Physical processes III: line absorption and broadening**](courses/stellar-atmospheres/SA04_line_broadening.md) | oscillator strengths, natural, Doppler, Stark, van der Waals, Voigt, rotation |
| SA5 | [The gray LTE atmosphere: complete solution](courses/stellar-atmospheres/SA05_gray_LTE_atmosphere.md) | $T^4 = \tfrac34T_{\rm eff}^4(\tau+q)$, Hopf function, $H$-function, emergent spectrum |
| SA6 | [LTE spectral lines](courses/stellar-atmospheres/SA06_LTE_lines.md) | Milne–Eddington, curve of growth, abundances, NLTE line cores |
| SA7 | [TE, LTE and non-LTE: definitions, examples, methods](courses/stellar-atmospheres/SA07_TE_LTE_NLTE.md) | side-by-side definitions with examples, rate equations, NLTE mechanisms, solution methods (names) |
| SA8 | [Model atmospheres and the solar atmosphere](courses/stellar-atmospheres/SA08_model_atmospheres.md) | structure equations, blanketing, convection, solar layers, grids, diagnostics |
| SA9 | [Final exam with complete solutions](courses/stellar-atmospheres/SA09_final_exam.md) | 10 short answers, 8 problems, 2 essays, classification |
| SA10 | [Formula sheet](courses/stellar-atmospheres/SA10_formula_sheet.md) | |

## How to study

1. Read each lecture in order; the difficulty increases gradually.
2. Re-derive every boxed equation yourself.
3. Redo each worked example without looking at the solution.
4. Answer the exam questions at the end of each lecture, then check the answers.
5. Finish with the final exam under exam conditions (3 hours).

## Interactive tools: change the values and watch the physics

Two companions let you change every input and see the equations respond. They cover ten experiments, labelled with the lecture they belong to (RT = Radiative Transfer, SA = Stellar Atmospheres):

| # | Experiment | What you can change |
|---|---|---|
| RT1 | Optical depth | absorption coefficient, path length → τ, transmission, extinction in magnitudes |
| RT2 | Intensity vs flux | T_eff, radius, distance (presets: Sun from Earth/Mars/Neptune, Sirius) |
| RT3 | Planck function | temperature; Rayleigh–Jeans and Wien limits; Wien peak; σT⁴ |
| RT4 | Random walk | cloud optical depth, destruction probability ε (live photon paths in the web app) |
| RT5 | Slab & MIT two-layer star | I₀/S and τ; T_base, T_top, line strength (thin cloud, absorption, thermal inversion) |
| SA1 | Saha–Boltzmann | temperature and electron pressure → ionisation and Balmer (n = 2) population |
| RT7 | Eddington–Barbier | S(τ) = a + bτ + cτ², viewing angle μ → limb-darkened disk |
| RT8 | Scattering atmosphere | ε and the number of Λ-iterations (exact Λ-matrix solution in the web app); Rosseland mean |
| SA5 | Gray LTE atmosphere | T_eff, wavelength, log g, κ → exact T(τ), limb darkening, emergent spectrum, pressure |
| SA6 | LTE spectral lines | β, η₀, damping a, temperature, mass, microturbulence → profile and curve of growth |

- **Web app** ([`app/index.html`](app/index.html)): sliders, live plots with hover readouts, and the equation with your values substituted. It opens in any browser on a computer or phone, and needs no installation. Source: `app/src.html` (page) and `app/rtmath.js` (physics, checked against scipy). Rebuild with `node app/build.js`.
- **Spreadsheet** ([`Radiative_Transfer_Lab.xlsx`](Radiative_Transfer_Lab.xlsx)): one sheet per lecture. Type a value into a yellow cell and all formulas, tables and charts update. It works in Excel, LibreOffice and Google Sheets. Generated by `scripts/make_excel.py`.

## Code: numerical LTE solutions

All figures and all numbers in the worked examples are produced by the Python scripts in [`scripts/`](scripts):

| Script | What it does |
|---|---|
| [`lte_solvers.py`](scripts/lte_solvers.py) | Planck functions; the **Λ operator** as a matrix; exact solution of $S = \varepsilon B+(1-\varepsilon)J$; Λ-iteration; **exact gray LTE atmosphere** (Hopf function); Chandrasekhar $H$-function; Milne–Eddington line profiles and curves of growth; Saha–Boltzmann for hydrogen |
| [`sa_physics.py`](scripts/sa_physics.py) | Stellar Atmospheres physics: Kramers bound–free and free–free opacity, H$^-$ abundance, collisional rates and critical densities, Voigt and rotational profiles |
| [`make_figures.py`](scripts/make_figures.py) | regenerates every figure in [`figures/`](figures) (`--part2` and `--sa` build subsets) |
| [`worked_examples.py`](scripts/worked_examples.py) | prints every numerical answer quoted in the lectures |
| [`build_pdf.sh`](scripts/build_pdf.sh) | builds both course PDFs (pandoc + KaTeX + headless Chromium) |

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
5. S. Chandrasekhar, *Radiative Transfer* (Oxford 1950; Dover 1960), Chs. I, III, V, X, XII.
6. D. Mihalas, *Stellar Atmospheres*, 2nd ed. (Freeman 1978): absorption cross-sections, statistical equilibrium and transition rates, line broadening (structure of Course B).

Further reading: Rybicki & Lightman, *Radiative Processes in Astrophysics*; Mihalas, *Stellar Atmospheres*; Gray, *The Observation and Analysis of Stellar Photospheres*; Hubeny & Mihalas, *Theory of Stellar Atmospheres*.
