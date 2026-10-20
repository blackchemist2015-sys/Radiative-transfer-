# Lecture RT4 — Emission, Absorption and Scattering

> **Sources:** Hu Set 1 (spontaneous emission, absorption, cross-section, scattering, random walk, multiple processes); MIT 8.901 Lec. 7 ($\alpha_\nu = n\sigma_\nu = \rho\kappa_\nu$); Collins §9.2c (creation rate, redistribution function); Chandrasekhar Ch. I §§7–11.

## Learning goals

1. Define $j_\nu$, $\alpha_\nu$, $\kappa_\nu$, $\sigma_\nu$ and the mean free path.
2. Derive the Einstein relations and the correction for stimulated emission.
3. Describe scattering as absorption followed by re-emission, and write the mixed source function.
4. Use the random walk to estimate photon escape times.


## Key concepts in plain words

**Absorption coefficient — probability per metre.** $\alpha_\nu$ is the probability that a photon is removed from the beam per unit length travelled. If $\alpha_\nu = 0.01$ m$^{-1}$, a photon has a 1 % chance of being stopped in each metre. Its inverse, the **mean free path** $\ell = 1/\alpha_\nu$, is the typical distance a photon travels before something happens to it; it plays the role of "visibility" in fog.

**Cross-section — the effective size of a target.** Each atom or electron acts like a little target of area $\sigma_\nu$ that photons can hit. This area is not a physical size: an electron has no measurable size, yet it has a Thomson cross-section of $6.65\times10^{-29}$ m$^2$. Multiply the target area by the number of targets per volume and you get $\alpha_\nu = n\sigma_\nu$. Many tiny targets can make a medium very opaque.

**Opacity — absorption per kilogram.** Writing $\alpha_\nu = \rho\kappa_\nu$ separates "how much stuff there is" ($\rho$) from "how good each kilogram is at stopping light" ($\kappa_\nu$, the opacity). Opacity depends strongly on temperature, composition and frequency, and that frequency dependence is what produces spectral features.

**Emission coefficient.** $j_\nu$ is the energy that matter emits per unit volume, time, frequency and solid angle. It does not depend on how much light is already present: hot, excited atoms emit spontaneously anyway.

**Stimulated emission — photon cloning.** A photon passing an excited atom can trigger it to emit a second photon identical to the first (same frequency, direction and phase). Because this process grows with the light already present, it acts like *negative absorption*. If more atoms are in the upper level than in the lower one (a population inversion), light is amplified instead of absorbed: this is a laser in the lab and a **maser** in space.

**Absorption versus scattering — sponge versus pinball.** In *true absorption* the photon's energy is given to the gas (it becomes heat) and the photon disappears; the gas may later emit a different photon according to its temperature. In *scattering* the photon only bounces off in a new direction, like a pinball, keeping its energy. Scattering does not heat the gas and does not "know" the gas temperature; it only redistributes the light that is already there. The number $\varepsilon$ is the probability that an interaction is a true absorption (photon destroyed) rather than a scattering.

**Random walk — why light leaves stars slowly.** A photon in a scattering medium moves like a drunk person who takes steps in random directions: after $N$ steps it is typically only $\sqrt N$ steps from the start. To escape from an optical depth $\tau$ it needs about $\tau^2$ scatterings. Light that would cross the Sun in 2 seconds takes thousands of years to diffuse out.

---

## 4.1 The four radiative processes

![Radiative processes in a two-level atom](../../figures/L04_processes.png)

*Figure 4.1 — Absorption, spontaneous emission, stimulated emission and scattering. Stimulated emission produces a photon identical to the incoming one (same frequency, direction and polarisation), so mathematically it behaves like **negative absorption**.*

## 4.2 Emission coefficient

Let matter emit power $P_\nu\,d\nu$ per unit volume. If it emits isotropically, the energy into $d\Omega$ is
$$dE = j_\nu\,dV\,d\Omega\,d\nu\,dt,\qquad j_\nu = \frac{P_\nu}{4\pi}.$$
Along a path $ds$ through a cylinder of cross-section $dA$ ($dV = dA\,ds$), the beam gains $dI_\nu = j_\nu\,ds$. With emission only:
$$\frac{dI_\nu}{ds} = j_\nu\quad\Rightarrow\quad I_\nu(s) = I_\nu(s_0) + \int_{s_0}^s j_\nu\,ds'.$$
The emissivity per unit mass is $\epsilon_\nu = 4\pi j_\nu/\rho$ (Hu).

## 4.3 Absorption coefficient, cross-section and opacity

A beam loses a fraction $\alpha_\nu\,ds$ of its intensity over $ds$:
$$\frac{dI_\nu}{ds} = -\alpha_\nu I_\nu\quad\Rightarrow\quad I_\nu(s) = I_\nu(0)\,e^{-\int\alpha_\nu ds} = I_\nu(0)e^{-\tau_\nu}.$$

**Particle picture** (Hu). Absorbers of number density $n$ each present a cross-section $\sigma_\nu$. In a slab $dA\times ds$ they block an area $\sigma_\nu n\,dA\,ds$, so the fraction removed is $n\sigma_\nu ds$:
$$\boxed{\;\alpha_\nu = n\sigma_\nu = \rho\kappa_\nu\;}\qquad\text{mean free path } \ell_\nu = \frac1{\alpha_\nu}.$$
An optical depth $\tau_\nu$ therefore equals the number of mean free paths along the path.

**Main opacity sources in stars**

| Process | Name | Frequency dependence | Where it matters |
|---|---|---|---|
| bound–bound | line absorption | narrow profile $\phi(\nu)$ | spectral lines |
| bound–free | photo-ionisation | edges, $\propto\nu^{-3}$ above each edge | Balmer/Lyman jumps; H$^-$ in the Sun |
| free–free | bremsstrahlung | $\propto\nu^{-3}$ (optical), $\nu^{-2}$ (radio) | hot stars, H II regions |
| electron scattering | Thomson | grey: $\sigma_T = 6.652\times10^{-29}$ m$^2$ | O stars, interiors, accretion disks |
| H$^-$ | b-f + f-f of the negative H ion | broad | **dominant continuum opacity in the solar photosphere** |

For fully ionised gas, $\kappa_{\rm es} = \sigma_T/(\mu_em_H) = 0.020(1+X)$ m$^2$ kg$^{-1}$ $= 0.2(1+X)$ cm$^2$ g$^{-1}$.

## 4.4 Einstein coefficients

Consider a transition $1\leftrightarrow2$ with energy $h\nu_0 = E_2 - E_1$, statistical weights $g_1, g_2$, and line profile $\phi(\nu)$ normalised to $\int\phi\,d\nu = 1$. Let $\bar J = \int J_\nu\phi(\nu)\,d\nu$.

| Process | Rate per unit volume |
|---|---|
| spontaneous emission | $n_2A_{21}$ |
| absorption | $n_1B_{12}\bar J$ |
| stimulated emission | $n_2B_{21}\bar J$ |

**Relations.** In TE, $J_\nu = B_\nu(T)$, detailed balance holds ($n_1B_{12}\bar J = n_2A_{21} + n_2B_{21}\bar J$), and the populations follow Boltzmann, $n_2/n_1 = (g_2/g_1)e^{-h\nu/kT}$. Solving for $\bar J$:
$$\bar J = \frac{A_{21}/B_{21}}{(g_1B_{12}/g_2B_{21})e^{h\nu/kT}-1}.$$
For this to equal $B_\nu(T)$ at **every** $T$ we need
$$\boxed{\;g_1B_{12} = g_2B_{21},\qquad A_{21} = \frac{2h\nu^3}{c^2}B_{21}\;}$$
These are **atomic** properties, so they hold whether or not the gas is in equilibrium.

**Macroscopic coefficients.** Each transition moves energy $h\nu$, spread over $4\pi$ sr and over the profile:
$$j_\nu = \frac{h\nu}{4\pi}n_2A_{21}\phi(\nu),\qquad
\alpha_\nu = \frac{h\nu}{4\pi}\left(n_1B_{12} - n_2B_{21}\right)\phi(\nu) = \frac{h\nu}{4\pi}n_1B_{12}\left(1-\frac{g_1n_2}{g_2n_1}\right)\phi(\nu).$$
The bracket is the **correction for stimulated emission**. If $g_1n_2/g_2n_1 > 1$ (a population inversion), then $\alpha_\nu<0$ and the beam grows exponentially: a **maser**.

**Line source function** (any populations):
$$S_\nu = \frac{j_\nu}{\alpha_\nu} = \frac{2h\nu^3}{c^2}\,\frac{1}{\dfrac{g_2n_1}{g_1n_2}-1}.$$
With Boltzmann populations at $T$ this becomes exactly $B_\nu(T)$. This is the key LTE result of Lecture SA1.

## 4.5 Scattering

Scattering is absorption immediately followed by re-emission into a new direction (Hu). For **coherent** (same frequency), **isotropic** scattering with coefficient $\alpha^{\rm sc}_\nu$, the energy removed from all directions is redistributed evenly over $4\pi$:
$$j^{\rm sc}_\nu = \alpha^{\rm sc}_\nu\oint I_\nu\frac{d\Omega}{4\pi} = \alpha^{\rm sc}_\nu J_\nu\quad\Rightarrow\quad S^{\rm sc}_\nu = J_\nu .$$
The RTE then becomes an **integro-differential equation**, because $J_\nu$ depends on $I_\nu$ in all directions:
$$\frac{dI_\nu}{ds} = -\alpha^{\rm sc}_\nu\left(I_\nu - \oint I_\nu\frac{d\Omega}{4\pi}\right).$$
Collins (eq. 9.2.27) gives the general form with a redistribution function $R(\nu',\nu,\Omega',\Omega)$, describing how photons are moved in frequency and angle.

### Absorption plus scattering

The coefficients add (Hu): $\alpha_\nu = \alpha^{a}_\nu+\alpha^{\rm sc}_\nu$. The combined source function is
$$S_\nu = \frac{\alpha^{a}_\nu B_\nu + \alpha^{\rm sc}_\nu J_\nu}{\alpha^{a}_\nu+\alpha^{\rm sc}_\nu} = \varepsilon_\nu B_\nu + (1-\varepsilon_\nu)J_\nu,\qquad
\varepsilon_\nu = \frac{\alpha^a_\nu}{\alpha^a_\nu+\alpha^{\rm sc}_\nu},$$
where $1-\varepsilon_\nu$ is the **single-scattering albedo** (the probability that an interaction is a scattering). This equation is the heart of Lecture RT8.

## 4.6 Random walk

![Random walk of photons](../../figures/L04_random_walk.png)

*Figure 4.2 — Left: photon paths with unit steps; the dashed circle has radius $\sqrt N\ell$. Right: a 3D simulation confirms $R_{\rm rms} = \sqrt N\,\ell$.*

With steps $\mathbf r_i$ of length $\ell$ in random directions, $\mathbf R = \sum\mathbf r_i$ and $\langle\mathbf r_i\cdot\mathbf r_j\rangle = \ell^2\delta_{ij}$, so
$$\langle R^2\rangle = N\ell^2 .$$
To escape from optical depth $\tau = R/\ell$ takes $N\approx\tau^2$ steps when $\tau\gg1$. When $\tau\ll1$, only a fraction $\tau$ of photons interact at all. A useful estimate is $N\approx\max(\tau,\tau^2)$ (Hu).

**Thermalisation.** If each interaction is an absorption with probability $\varepsilon$, a photon survives $N\approx1/\varepsilon$ interactions before it is destroyed, travelling a net optical distance $\tau_{\rm th}\approx\sqrt N = 1/\sqrt\varepsilon$: the **thermalisation depth** (Lecture RT8).

---

## Worked example 4.1 — How long does light take to leave the Sun?

*Assume a uniform Sun of mean density $\bar\rho$, fully ionised with $X = 0.7$, and only Thomson scattering.*

1. $\bar\rho = M_\odot/(\tfrac43\pi R_\odot^3) = 1410$ kg m$^{-3}$.
2. $\mu_e = 2/(1+X) = 1.18$, so $n_e = \bar\rho/(\mu_em_H) = 7.2\times10^{29}$ m$^{-3}$.
3. $\ell = 1/(n_e\sigma_T) = 2.1$ cm.
4. $\tau = R_\odot/\ell = 3.3\times10^{10}$, so $N = \tau^2 = 1.1\times10^{21}$ scatterings.
5. Total path $N\ell = R^2/\ell$; time $t = R_\odot^2/(\ell c) = 7.7\times10^{10}$ s $\approx$ **2400 yr**, compared with a light-crossing time of 2.3 s.

The real Sun is denser in the core and has higher (bound-free) opacity, so realistic estimates are $10^4$–$10^5$ yr. The method is the point.

## Worked example 4.2 — Stimulated emission at radio wavelengths

*Evaluate $1-e^{-h\nu/kT}$ (the LTE correction factor) for the 21-cm line at $T = 100$ K and for H$\alpha$ in the Sun.*

21 cm: $h\nu/kT = 6.8\times10^{-4}$, so the factor is $6.8\times10^{-4}$. Stimulated emission cancels **99.93 %** of the absorption, and the net opacity $\propto1/T$. That is why 21-cm absorption measures the spin temperature.
H$\alpha$ (656 nm, 5772 K): $h\nu/kT = 3.8$, so the factor is $0.98$; stimulated emission is a 2 % correction.

## Worked example 4.3 — Source function of a two-level atom

*Show that if the level populations are Boltzmann at temperature $T_{\rm ex}$, then $S_\nu = B_\nu(T_{\rm ex})$.*

Insert $g_2n_1/(g_1n_2) = e^{h\nu/kT_{\rm ex}}$ into $S_\nu = (2h\nu^3/c^2)/[g_2n_1/(g_1n_2)-1]$ to get $S_\nu = B_\nu(T_{\rm ex})$. **The line source function only measures the excitation temperature.** LTE is the special case $T_{\rm ex} = T_{\rm kin}$.

---

## Common misconceptions

1. **"Scattering removes energy from the radiation."** It removes photons from one beam but puts them into others; the total energy is conserved.
2. **"Stimulated emission is a small correction that can always be ignored."** At radio wavelengths ($h\nu\ll kT$) it cancels almost all of the absorption.
3. **"Opacity is a fixed property of a material."** It depends on temperature, density (through ionisation and excitation) and, above all, frequency.
4. **"A photon from the Sun's core reaches us directly."** The energy random-walks out over thousands of years, being absorbed and re-emitted many times on the way.

## Lecture summary

- $\alpha_\nu = n\sigma_\nu = \rho\kappa_\nu$; mean free path $\ell = 1/\alpha_\nu$.
- Einstein relations link absorption, spontaneous and stimulated emission; they are atomic properties.
- Stimulated emission is negative absorption; population inversion gives masers.
- Scattering gives $S = J$; absorption plus scattering gives $S = \varepsilon B+(1-\varepsilon)J$.
- Random walk: $N\approx\tau^2$ scatterings to escape from optical depth $\tau$.

---

## Exam questions and answers — Lecture RT4

**Q1.** Derive the Einstein relations. Explain why they hold even when the gas is not in TE.

> **A1.** See §4.4. Detailed balance plus Boltzmann populations, required to reproduce $B_\nu(T)$ for all $T$, gives $g_1B_{12} = g_2B_{21}$ (high-$T$ limit) and $A_{21} = (2h\nu^3/c^2)B_{21}$. The coefficients depend only on the atomic wavefunctions (matrix elements), not on the environment, so once found in TE they apply everywhere.

**Q2.** Write $\alpha_\nu$ including stimulated emission. What happens physically when $n_2/g_2 > n_1/g_1$? Give an astrophysical example.

> **A2.** $\alpha_\nu = \frac{h\nu}{4\pi}\phi(\nu)(n_1B_{12} - n_2B_{21}) = \frac{h\nu}{4\pi}\phi\,n_1B_{12}(1-\frac{g_1n_2}{g_2n_1})$. With an inversion, $\alpha_\nu<0$ and $\tau_\nu<0$, so $I_\nu$ grows as $e^{|\tau|}$: maser amplification. Examples: OH (1665/1667 MHz) and H$_2$O (22 GHz) masers in star-forming regions and the envelopes of AGB stars.

**Q3.** Derive $S_\nu = \varepsilon B_\nu + (1-\varepsilon)J_\nu$ and give the meaning of $\varepsilon$.

> **A3.** $j = \alpha^aB + \alpha^{\rm sc}J$ (thermal emission by Kirchhoff, plus scattering) and $\alpha = \alpha^a+\alpha^{\rm sc}$. Divide to get $S = \varepsilon B + (1-\varepsilon)J$ with $\varepsilon = \alpha^a/(\alpha^a+\alpha^{\rm sc})$, the probability that an interaction destroys the photon (converts it into thermal energy of the gas).

**Q4.** A cloud has $\tau = 100$ for pure scattering. Roughly how many scatterings does a photon undergo before escaping, and how far does it travel in total?

> **A4.** $N\approx\tau^2 = 10^4$; total path $N\ell = \tau^2\ell = 100\,L$, where $L = \tau\ell$ is the size of the cloud. So the photon travels 100 times the cloud size, and the escape time is $100\,L/c$.
