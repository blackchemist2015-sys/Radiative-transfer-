# Radiative Transfer and Stellar Atmospheres: Two Graduated Courses for Pre-Master Students

Two self-contained, illustrated, **concept-based** courses for students preparing for an **Astrophysics master's programme**:

| Course | Lectures | PDF |
|---|---|---|
| **A. Radiative Transfer**: how radiation moves through matter | RT1–RT6, exam RT7, formula sheet RT8 | [`Radiative_Transfer_Course.pdf`](Radiative_Transfer_Course.pdf) |
| **B. Stellar Atmospheres**: the state of the gas, opacity, rates and non-LTE, gray atmospheres and lines, model atmospheres | SA1–SA5, exam SA6, formula sheet SA7 | [`Stellar_Atmospheres_Course.pdf`](Stellar_Atmospheres_Course.pdf) |

Take Course A first; Course B uses its results. Every lecture follows the same structure:

1. **Concept map**: a one-page picture of how the ideas of the lecture connect
2. **Learning goals**
3. **The big ideas in plain words**: each idea explained physically, with everyday analogies, before any mathematics
4. **Theory**, with an illustration for each section
5. **2–4 worked numerical examples**
6. **Common misconceptions**: the mistakes students most often make
7. **Lecture summary**
8. **4 exam questions with complete answers**

## Course A — Radiative Transfer ([`courses/radiative-transfer/`](courses/radiative-transfer))

| # | Lecture | Highlights |
|---|---|---|
| RT1 | [Radiation and how we describe it](courses/radiative-transfer/RT1_radiation_and_its_description.md) | photon bookkeeping; $I_\nu$ vs flux; conservation of intensity; $J$, $F$, $K$; optical depth; RTE preview |
| RT2 | [Black bodies and light–matter interaction](courses/radiative-transfer/RT2_blackbodies_and_interactions.md) | Planck, Wien, Stefan–Boltzmann; the four interactions; Einstein relations; masers; $S = \varepsilon B + (1-\varepsilon)J$; random walk |
| RT3 | [The transfer equation: where it comes from and how to solve it](courses/radiative-transfer/RT3_transfer_equation.md) | Boltzmann equation → RTE → special forms; formal solution; contribution function; MIT thin cloud, two-layer star, thermal inversion |
| RT4 | [Atmospheres: plane-parallel layers, moments and scattering](courses/radiative-transfer/RT4_atmospheres_moments_scattering.md) | Eddington–Barbier, limb darkening → $T(\tau)$; radiative equilibrium; Eddington closure; Rosseland mean; $S(0) = \sqrt\varepsilon B$; Λ-iteration |
| RT5 | [Polarized light](courses/radiative-transfer/RT5_polarized_light.md) | Stokes parameters, vector RTE, 11.7 % limb polarization, Zeeman and Hanle effects |
| RT6 | [How the problem was solved: a history](courses/radiative-transfer/RT6_history.md) | Schuster, Schwarzschild, Eddington, Milne, Hopf, Chandrasekhar → ALI, 3D |
| RT7 | [Final exam with complete solutions](courses/radiative-transfer/RT7_final_exam.md) | short answers, 8 problems, 3 further-topic questions, essay |
| RT8 | [Formula sheet](courses/radiative-transfer/RT8_formula_sheet.md) | |

## Course B — Stellar Atmospheres ([`courses/stellar-atmospheres/`](courses/stellar-atmospheres))

| # | Lecture | Highlights |
|---|---|---|
| SA1 | [The state of the gas: TE, LTE and non-LTE; Saha and Boltzmann](courses/stellar-atmospheres/SA1_state_of_the_gas.md) | definitions with examples, Kirchhoff's law, Balmer-line strength, Collins' five assumptions |
| SA2 | [Where opacity comes from: continuous absorption and line broadening](courses/stellar-atmospheres/SA2_opacity_and_line_broadening.md) | Kramers bound–free, free–free, H$^-$, Balmer jump; natural, Doppler, pressure broadening; Voigt |
| SA3 | [Transition rates, statistical equilibrium and non-LTE](courses/stellar-atmospheres/SA3_rates_and_nonLTE.md) | Einstein, Milne, Klein–Rosseland; two-level atom; critical density; coronal and nebular limits; NLTE mechanisms; methods (names) |
| SA4 | [The gray LTE atmosphere and how spectral lines form](courses/stellar-atmospheres/SA4_gray_atmosphere_and_LTE_lines.md) | $T^4 = \tfrac34T_{\rm eff}^4(\tau+q)$, Hopf and $H$-functions; where lines form; Milne–Eddington; curve of growth |
| SA5 | [Real model atmospheres and the Sun](courses/stellar-atmospheres/SA5_model_atmospheres.md) | structure equations; **a solar model built by hand (after Novotny, Ch. 9)**; blanketing; convection; solar layers; codes and diagnostics |
| SA6 | [Final exam with complete solutions](courses/stellar-atmospheres/SA6_final_exam.md) | short answers, 8 problems, essays, classification |
| SA7 | [Formula sheet](courses/stellar-atmospheres/SA7_formula_sheet.md) | |

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
| RT1 | Intensity vs flux | T_eff, radius, distance (presets: Sun from Earth/Mars/Neptune, Sirius) |
| RT2 | Planck function | temperature; Rayleigh–Jeans and Wien limits; Wien peak; σT⁴ |
| RT2 | Random walk | cloud optical depth, destruction probability ε (live photon paths in the web app) |
| RT3 | Slab & MIT two-layer star | I₀/S and τ; T_base, T_top, line strength (thin cloud, absorption, thermal inversion) |
| SA1 | Saha–Boltzmann | temperature and electron pressure → ionisation and Balmer (n = 2) population |
| RT4 | Eddington–Barbier | S(τ) = a + bτ + cτ², viewing angle μ → limb-darkened disk |
| RT4 | Scattering atmosphere | ε and the number of Λ-iterations (exact Λ-matrix solution in the web app); Rosseland mean |
| SA4 | Gray LTE atmosphere | T_eff, wavelength, log g, κ → exact T(τ), limb darkening, emergent spectrum, pressure |
| SA4 | LTE spectral lines | β, η₀, damping a, temperature, mass, microturbulence → profile and curve of growth |

- **Web app** ([`app/index.html`](app/index.html)): sliders, live plots with hover readouts, and the equation with your values substituted. It opens in any browser on a computer or phone, and needs no installation. Source: `app/src.html` (page) and `app/rtmath.js` (physics, checked against scipy). Rebuild with `node app/build.js`.
- **Spreadsheet** ([`Radiative_Transfer_Lab.xlsx`](Radiative_Transfer_Lab.xlsx)): one sheet per lecture. Type a value into a yellow cell and all formulas, tables and charts update. It works in Excel, LibreOffice and Google Sheets. Generated by `scripts/make_excel.py`.

## Code: numerical LTE solutions

All figures and all numbers in the worked examples are produced by the Python scripts in [`scripts/`](scripts):

| Script | What it does |
|---|---|
| [`lte_solvers.py`](scripts/lte_solvers.py) | Planck functions; the **Λ operator** as a matrix; exact solution of $S = \varepsilon B+(1-\varepsilon)J$; Λ-iteration; **exact gray LTE atmosphere** (Hopf function); Chandrasekhar $H$-function; Milne–Eddington line profiles and curves of growth; Saha–Boltzmann for hydrogen |
| [`sa_physics.py`](scripts/sa_physics.py) | Stellar Atmospheres physics: Kramers bound–free and free–free opacity, H$^-$ abundance, collisional rates and critical densities, Voigt and rotational profiles, Novotny's hand-built solar model and the Schwarzschild convection test |
| [`make_figures.py`](scripts/make_figures.py) | regenerates every figure in [`figures/`](figures) (`--part2`, `--sa` and `--concepts` build subsets; `--concepts` draws the concept maps and concept illustrations) |
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
3. MIT 8.901 *Astrophysics I* (Spring 2019), Lecture 7: *Radiative Transfer*. Its three-step build-up of the RTE, Kirchhoff's law for thick and thin objects, the thin hydrogen cloud, the two-layer stellar atmosphere and thermal inversions are reproduced (with computed figures) in Lecture RT3.
4. G. W. Collins II, *The Fundamentals of Stellar Astrophysics* (2003), Part II, Ch. 9: *The Flow of Radiation Through the Atmosphere*.
5. S. Chandrasekhar, *Radiative Transfer* (Oxford 1950; Dover 1960), Chs. I, III, V, X, XII.
6. D. Mihalas, *Stellar Atmospheres*, 2nd ed. (Freeman 1978): absorption cross-sections, statistical equilibrium and transition rates, line broadening (structure of Course B).
7. E. Novotny, *Introduction to Stellar Atmospheres and Interiors* (Oxford University Press 1973), Chs. 2–5 and 9: transfer of radiation, absorption coefficients, model atmospheres, line formation, and the step-by-step model solar atmosphere reproduced in Lecture SA5.

Further reading: Rybicki & Lightman, *Radiative Processes in Astrophysics*; Mihalas, *Stellar Atmospheres*; Gray, *The Observation and Analysis of Stellar Photospheres*; Hubeny & Mihalas, *Theory of Stellar Atmospheres*.
