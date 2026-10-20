# Lecture SA3 — Physical Processes II: Transition Rates and Statistical Equilibrium

> **Sources:** D. Mihalas, *Stellar Atmospheres* (1978), the equations of statistical equilibrium and transition rates; Hubeny & Mihalas, *Theory of Stellar Atmospheres* (2014); Osterbrock & Ferland, *Astrophysics of Gaseous Nebulae* (2006) for collision strengths and critical densities; van Regemorter (1962), Seaton (1962) for collisional rate approximations.
> **Prerequisites:** RT4 (Einstein coefficients), SA1 (Saha–Boltzmann, two-level atom), SA2 (photo-ionisation cross-sections).

## Learning goals

1. Write every radiative and collisional rate between bound levels and between a level and the continuum.
2. Derive the relations between forward and inverse rates (Einstein, Milne, Klein–Rosseland) from detailed balance.
3. Set up the statistical-equilibrium equations and recover LTE as a limit.
4. Use the **coronal** and **nebular** approximations, and compute critical densities from collision strengths.

---

## Key concepts in plain words

**A level population is a balance between traffic in and traffic out.** Picture each atomic level as a room with doors to every other room and to the "continuum" (the ion plus a free electron). Every second, atoms leave a room by absorbing a photon, by emitting one, or by being hit by an electron. They enter it by the inverse processes. In a steady state, traffic in equals traffic out for every room: this is **statistical equilibrium**.

**Two kinds of traffic.** *Radiative* transitions depend on the radiation field ($J_\nu$), which may come from far away and may not match the local temperature. *Collisional* transitions depend on the local electron density and temperature. Collisions push the populations toward LTE; radiation pushes them toward whatever the radiation field dictates.

**Every process has an inverse, and they are linked.** The probability of a process and of its inverse are related by atomic physics alone, independent of the environment. This is found by imagining the gas in full thermodynamic equilibrium, where each process must exactly balance its inverse (detailed balance). The Einstein relations (RT4) are one example; the same reasoning links photo-ionisation to recombination (Milne relation) and collisional excitation to collisional de-excitation (Klein–Rosseland relation).

**Two simple limits.** In very thin hot gas (the solar corona) collisions excite atoms but every excited atom decays by emitting a photon that escapes: the **coronal approximation**. In a nebula around a hot star, photo-ionisation by diluted starlight is balanced by recombination: the **nebular approximation**. Between these limits and LTE lies the full NLTE problem (SA7).

---

## 3.1 Inventory of rates

Number of transitions per unit volume per second from level $i$ to level $j$: $n_iP_{ij}$, with $P_{ij} = R_{ij}+C_{ij}$.

| Transition | Rate per atom | Inverse | Link (detailed balance) |
|---|---|---|---|
| radiative excitation $l\to u$ | $R_{lu} = B_{lu}\bar J$ | spontaneous + stimulated emission, $R_{ul} = A_{ul}+B_{ul}\bar J$ | Einstein: $g_lB_{lu} = g_uB_{ul}$, $A_{ul} = \frac{2h\nu^3}{c^2}B_{ul}$ |
| photo-ionisation $i\to\kappa$ | $R_{i\kappa} = 4\pi\displaystyle\int_{\nu_i}^\infty\frac{\sigma_i(\nu)}{h\nu}J_\nu\,d\nu$ | radiative recombination (spontaneous + stimulated) | Milne relation (below) |
| collisional excitation | $C_{lu} = n_eq_{lu}(T)$ | collisional de-excitation $C_{ul} = n_eq_{ul}$ | Klein–Rosseland: $\frac{q_{lu}}{q_{ul}} = \frac{g_u}{g_l}e^{-h\nu/kT}$ |
| collisional ionisation | $C_{i\kappa} = n_eq_{i\kappa}(T)$ | three-body recombination ($\propto n_e^2$) | Saha: $C_{\kappa i} = (n_i/n_\kappa)^*C_{i\kappa}$ |
| — | — | dielectronic recombination | important in hot plasmas (corona, nebulae) |
| charge exchange | e.g. O$^+$ + H ⇄ O + H$^+$ | inverse reaction | detailed balance at $T$ |

**Radiative recombination rate** (the Milne relation in rate form). With $(n_i/n_\kappa)^*$ the LTE (Saha) ratio at the actual $n_e$ and $T$:
$$n_\kappa R_{\kappa i} = n_\kappa\left(\frac{n_i}{n_\kappa}\right)^*4\pi\int_{\nu_i}^\infty\frac{\sigma_i(\nu)}{h\nu}\left(\frac{2h\nu^3}{c^2}+J_\nu\right)e^{-h\nu/kT}d\nu .$$
If $J_\nu = B_\nu$ this exactly balances photo-ionisation, as detailed balance requires.

## 3.2 Collisional rates

Collisional rate coefficients are written with the dimensionless **collision strength** $\Omega_{lu}$ (Maxwell-averaged), symmetric in $l$ and $u$:
$$q_{ul} = \frac{8.629\times10^{-6}}{g_u\sqrt T}\,\Omega_{lu}\ \text{cm}^3\,\text{s}^{-1},\qquad
q_{lu} = \frac{g_u}{g_l}q_{ul}\,e^{-\Delta E/kT} = \frac{8.629\times10^{-6}}{g_l\sqrt T}\,\Omega_{lu}\,e^{-\Delta E/kT}.$$
(In SI multiply by $10^{-6}$: $8.629\times10^{-12}$ m$^3$ s$^{-1}$.) The relation between $q_{lu}$ and $q_{ul}$ is the **Klein–Rosseland relation**, the collisional analogue of the Einstein relations.

When no measured or computed $\Omega$ is available, approximations are used: **van Regemorter (1962)** for allowed transitions (relating $\Omega$ to the oscillator strength), **Seaton (1962)** for collisional ionisation, and **Drawin's formula** for collisions with neutral hydrogen in cool stars (often scaled by an empirical factor, now replaced by quantum calculations).

## 3.3 Statistical-equilibrium equations

For every level $i$ (including the ground states of each ion):
$$\boxed{\;n_i\sum_{j\ne i}\left(R_{ij}+C_{ij}\right) = \sum_{j\ne i}n_j\left(R_{ji}+C_{ji}\right)\;}$$
Together with **particle conservation** ($\sum_in_i = N_{\rm element}$) and **charge conservation** ($n_e = \sum$ ion charges), this is a linear system for the populations *if* $J_\nu$ is known. It is written as a matrix equation $\mathsf A\,\mathbf n = \mathbf b$. The coupling with the RTE through $J_\nu$ makes the full problem non-linear (SA7).

**LTE as a limit.** If $C_{ij}\gg R_{ij}$ for all transitions, the equations reduce to collisional detailed balance, whose solution is Saha–Boltzmann at the local $T$. If $J_\nu = B_\nu(T)$, the radiative rates also balance pairwise. In both cases the populations are the LTE ones.

![Rate processes and the coronal-to-LTE transition](../../figures/SA3_rates.png)

*Figure 3.1 — Left: the radiative and collisional processes connecting bound levels and the continuum. Right: for an optically thin two-level atom with no radiation field ($T = 10^4$ K, $\Delta E = 2.48$ eV), the upper-level population relative to its LTE value rises $\propto n_e$ (coronal regime) and saturates at the Boltzmann value above the critical density (dotted). A forbidden line ($A = 0.027$ s$^{-1}$) is in LTE above $\sim7\times10^{11}$ m$^{-3}$; an allowed line ($A = 10^8$ s$^{-1}$) needs $\sim6\times10^{20}$ m$^{-3}$.*

## 3.4 Two classical limits

**Coronal approximation** (hot, very low density, optically thin, weak radiation field; e.g. the solar corona, supernova remnants):

- excitation: $n_ln_eq_{lu} = n_uA_{ul}$, so $\dfrac{n_u}{n_l} = \dfrac{n_eq_{lu}}{A_{ul}}\ll$ Boltzmann, and the line emissivity $\propto n_en_lq_{lu}$ (every collision gives one photon);
- ionisation: collisional ionisation = radiative + dielectronic recombination, so $\dfrac{n_{i+1}}{n_i} = \dfrac{q_{\rm ion}(T)}{\alpha_{\rm rec}(T)}$ is **independent of density** and depends on $T$ only. This is why Fe IX–Fe XVI lines are coronal thermometers.

**Nebular approximation** (photo-ionised gas around a hot star, e.g. H II regions and planetary nebulae):

- the stellar radiation is diluted, $J_\nu\approx W\,B_\nu(T_*)$, with the dilution factor $W\approx\frac14(R_*/r)^2\ll1$;
- ionisation balance: photo-ionisation from the ground state = recombination to all levels;
- excited levels are populated mainly by recombination cascades and collisions, and forbidden lines are collisionally excited with $n_e\ll n_{\rm crit}$ (SA7).

---

## Worked example 3.1 — Collisional de-excitation from detailed balance

*Starting from $n_lC_{lu} = n_uC_{ul}$ in TE, derive the Klein–Rosseland relation.*

In TE the populations are Boltzmann, $n_u/n_l = (g_u/g_l)e^{-\Delta E/kT}$, and the electrons are Maxwellian at the same $T$. Collisional excitation must be exactly balanced by collisional de-excitation: $n_ln_eq_{lu} = n_un_eq_{ul}$. So $q_{lu}/q_{ul} = n_u/n_l = (g_u/g_l)e^{-\Delta E/kT}$. Because $q$ depends only on atomic physics and on the Maxwellian at $T$, the relation holds in any gas with Maxwellian electrons, even far from TE.

## Worked example 3.2 — Critical density of [O III] 500.7 nm

*The $^1D_2$ level of O$^{2+}$ ($g_u = 5$) has total radiative decay rate $A\approx0.027$ s$^{-1}$, and the collision strength to the ground term is $\Omega\approx2.29$. Compute $q_{ul}$ and $n_{\rm crit}$ at $T = 10^4$ K.*

$q_{ul} = 8.629\times10^{-12}\times2.29/(5\times100) = 3.95\times10^{-14}$ m$^3$ s$^{-1}$; $n_{\rm crit} = A/q_{ul} = 6.8\times10^{11}$ m$^{-3}$ ($6.8\times10^5$ cm$^{-3}$). Figure 3.1 confirms that the upper level reaches 59 % of its LTE population at $n_e = 10^{12}$ m$^{-3}$ but only 1.4 % at $10^{10}$ m$^{-3}$ (typical of planetary nebulae).

## Worked example 3.3 — An allowed line in the coronal regime

*An allowed line with $A = 10^8$ s$^{-1}$, $\Omega = 10$, $g_l = g_u = 5$, $\Delta E = 2.48$ eV at $T = 10^4$ K. Compute $n_{\rm crit}$ and $(n_u/n_l)/(n_u/n_l)_{\rm LTE}$ at $n_e = 10^{15}$ m$^{-3}$ (solar transition region) and $10^{20}$ m$^{-3}$ (deep photosphere).*

$q_{ul} = 8.629\times10^{-12}\times10/500 = 1.73\times10^{-13}$ m$^3$ s$^{-1}$, so $n_{\rm crit} = 10^8/1.73\times10^{-13} = 5.8\times10^{20}$ m$^{-3}$. Below $n_{\rm crit}$ the ratio is $\approx n_e/n_{\rm crit}$: $1.7\times10^{-6}$ at $10^{15}$ m$^{-3}$ (extreme NLTE, coronal) and $0.15$ at $10^{20}$ m$^{-3}$. Even in a photosphere, strong allowed lines are not collisionally thermalised without help from photon trapping, which reduces the effective $A$ by the escape probability (SA7).

---

## Common misconceptions

1. **"Detailed-balance relations only apply in TE."** They are derived in TE but involve only atomic properties (and the Maxwellian electrons), so they hold in any environment.
2. **"High temperature means LTE."** The solar corona is very hot but far from LTE, because its density is tiny; what matters is the ratio of collisional to radiative rates.
3. **"Recombination is just the reverse arrow of photo-ionisation at the same rate."** Only in LTE; in a nebula photo-ionisation is driven by diluted starlight while recombination proceeds at the local $T_e$, and the two balance at very different populations from Saha.
4. **"Coronal ionisation depends on density."** In the coronal limit both ionisation and recombination are $\propto n_e$, so the ionisation balance depends on $T$ alone.

## Lecture summary

- Rates: radiative (bound–bound, bound–free) depend on $J_\nu$; collisional depend on $n_e$ and $T$.
- Detailed balance links each process to its inverse: Einstein (bound–bound radiative), Milne (bound–free radiative), Klein–Rosseland (collisional), Saha (collisional ionisation and three-body recombination).
- Statistical equilibrium: $n_i\sum_j P_{ij} = \sum_jn_jP_{ji}$ with particle and charge conservation; LTE when collisions dominate or $J = B$.
- Coronal limit: $n_u/n_l = n_eq_{lu}/A_{ul}$ and $T$-only ionisation balance. Nebular limit: diluted photo-ionisation balanced by recombination.
- Critical density $n_{\rm crit} = A/q_{ul}$, with $q_{ul} = 8.629\times10^{-6}\,\Omega/(g_u\sqrt T)$ cm$^3$ s$^{-1}$.

---

## Exam questions and answers — Lecture SA3

**Q1.** List the radiative and collisional processes that populate and depopulate a bound level, and give the detailed-balance relation for each pair.

> **A1.** Radiative excitation $B_{lu}\bar J$ ↔ spontaneous + stimulated emission $A_{ul}+B_{ul}\bar J$ (Einstein: $g_lB_{lu} = g_uB_{ul}$, $A_{ul} = 2h\nu^3B_{ul}/c^2$). Photo-ionisation ↔ radiative recombination (Milne relation). Collisional excitation $n_eq_{lu}$ ↔ de-excitation $n_eq_{ul}$ (Klein–Rosseland: $q_{lu}/q_{ul} = (g_u/g_l)e^{-\Delta E/kT}$). Collisional ionisation ↔ three-body recombination (Saha ratio). Plus dielectronic recombination and charge exchange.

**Q2.** Derive the Klein–Rosseland relation and explain why it holds outside TE.

> **A2.** In TE, detailed balance gives $n_lq_{lu} = n_uq_{ul}$ with Boltzmann populations, so $q_{lu}/q_{ul} = (g_u/g_l)e^{-\Delta E/kT}$. The rate coefficients depend only on the cross-section and on the electron velocity distribution. As long as the electrons are Maxwellian at $T$, the relation holds whatever the radiation field or the level populations.

**Q3.** Describe the coronal approximation. Show that the ionisation balance is independent of density, and give one application.

> **A3.** Low density, optically thin gas with a weak radiation field: collisional excitations are balanced by spontaneous radiative decays ($n_ln_eq_{lu} = n_uA_{ul}$), and collisional ionisation by radiative and dielectronic recombination. Both ionisation and recombination rates per ion are $\propto n_e$: $n_in_eq_{\rm ion} = n_{i+1}n_e\alpha_{\rm rec}$, so $n_{i+1}/n_i = q_{\rm ion}(T)/\alpha_{\rm rec}(T)$, independent of $n_e$. Application: Fe ion ratios (e.g. Fe IX–Fe XVI) measure coronal temperatures of 1–3 MK.

**Q4.** A forbidden line has $A = 0.02$ s$^{-1}$, $g_u = 5$ and $\Omega = 2$ at $T = 10^4$ K. Compute its critical density and state whether it is in LTE in a nebula with $n_e = 10^{9}$ m$^{-3}$.

> **A4.** $q_{ul} = 8.629\times10^{-12}\times2/(5\times100) = 3.45\times10^{-14}$ m$^3$ s$^{-1}$; $n_{\rm crit} = 0.02/3.45\times10^{-14} = 5.8\times10^{11}$ m$^{-3}$. With $n_e = 10^9$ m$^{-3}\approx2\times10^{-3}n_{\rm crit}$, the line is far from LTE: every collisional excitation produces a photon, and the upper level is underpopulated by a factor of about 600 relative to Boltzmann.
