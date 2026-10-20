# Lecture SA0 — Course Overview: Stellar Atmospheres

> **Course B of two.** Course A, *Radiative Transfer* (lectures RT1–RT10), provides the transfer theory. This course applies it to stars and adds the **physical processes and transition rates** that determine opacities, emissivities and level populations, following the structure of Mihalas, *Stellar Atmospheres* (2nd ed., 1978): radiation field and transfer → absorption cross-sections → statistical equilibrium and rates → line broadening → LTE and NLTE model atmospheres and line formation.
> **Main sources:** D. Mihalas, *Stellar Atmospheres* (1978); G. W. Collins II, *Fundamentals of Stellar Astrophysics* (2003), Part II; D. F. Gray, *The Observation and Analysis of Stellar Photospheres* (2005); I. Hubeny & D. Mihalas, *Theory of Stellar Atmospheres* (2014); Rybicki & Lightman (1979).

## What is a stellar atmosphere?

The **atmosphere** is the thin outer layer of a star from which photons escape into space: from optical depth $\tau\approx10$–$100$ (where the gas is still opaque) out to $\tau\ll1$. It is less than 0.1 % of the radius of a Sun-like star, yet it produces the entire observed spectrum. Collins (§9.1) stresses that it is defined by *the failure of the assumptions that work in the interior*: near the surface the photons begin to escape, the radiation field stops being Planckian, and the physics of the transfer of radiation becomes global instead of local.

## The questions this course answers

1. **What is the state of the gas?** Temperature, pressure, ionisation and excitation (SA1, SA7).
2. **How does matter absorb and emit?** Bound–bound, bound–free, free–free and scattering processes: the opacity and emissivity (SA2, SA4).
3. **What sets the level populations?** Collisions versus radiation: transition rates and statistical equilibrium (SA3, SA7).
4. **What structure results?** Radiative equilibrium plus hydrostatic equilibrium: the model atmosphere (SA5, SA8).
5. **What spectrum emerges?** Continuum, limb darkening and spectral lines (SA5, SA6).

## Prerequisites from Course A

| You need | From |
|---|---|
| specific intensity, flux, moments | RT2 |
| Planck function | RT3 |
| $\alpha_\nu$, $j_\nu$, Einstein coefficients, scattering source function | RT4 |
| formal solution; MIT two-layer star | RT5 |
| plane-parallel RTE, Eddington–Barbier | RT7 |
| moments, Eddington approximation, Rosseland mean, thermalisation | RT8 |

## Course map

| # | Lecture | Key content |
|---|---|---|
| SA0 | Overview (this page) | what an atmosphere is; course plan |
| SA1 | Thermodynamic state: LTE, Saha–Boltzmann, Kirchhoff | populations in LTE, two-level atom |
| SA2 | **Physical processes I: continuous opacity** | hydrogenic bound–free and free–free, H$^-$, scattering, opacity tables |
| SA3 | **Physical processes II: transition rates and statistical equilibrium** | radiative and collisional rates, detailed balance, Milne relations, coronal and nebular limits |
| SA4 | **Line absorption and broadening** | oscillator strengths, natural, Doppler, Stark, van der Waals broadening, Voigt profile, rotation |
| SA5 | The gray LTE atmosphere: complete solution | $T^4 = \frac34T_{\rm eff}^4(\tau+q)$, Hopf function, limb darkening, spectrum |
| SA6 | LTE spectral lines | Milne–Eddington, curve of growth, abundances |
| SA7 | TE, LTE and non-LTE | definitions with examples, rate equations, NLTE mechanisms and methods |
| SA8 | Model atmospheres and the solar atmosphere | structure equations, blanketing, convection, solar layers, grids, diagnostics |
| SA9 | Final exam with full solutions | |
| SA10 | Formula sheet | |

## Collins' five assumptions of "normal" stellar atmospheres

1. **LTE**: all material properties follow from the local $T$ and $\rho$.
2. The structure is set by the **continuum** opacity.
3. **Plane-parallel** geometry: thickness much smaller than the radius.
4. **Constant gravity** $g$, with hydrostatic equilibrium $dP/dz = -\rho g$.
5. **Radiative equilibrium**, with no energy sources: $F = \sigma T_{\rm eff}^4$ = constant.

Under these assumptions only $T_{\rm eff}$, $\log g$ and the chemical composition specify the atmosphere. Lectures SA5–SA6 work entirely inside these assumptions. SA7–SA8 show where each one fails and what replaces it.
