# Lecture 6 — Thermodynamic Equilibrium and Local Thermodynamic Equilibrium (LTE)

> **Sources:** Collins §9.1a–d (breakdown of STE, assumption of LTE, the five assumptions of normal stellar atmospheres), §9.2c (Kirchhoff's law $j_\nu = \kappa_\nu B_\nu$, eq. 9.2.22), §9.2d ($S_\nu = B_\nu$, eq. 9.2.28); MIT 8.901 §7.3 (Kirchhoff's law for thick and thin lumps); Hu Set 1; Carroll & Ostlie Ch. 8 (Saha–Boltzmann example).

## Learning goals

1. State what is in equilibrium in TE and in LTE.
2. Derive Kirchhoff's law $j_\nu = \alpha_\nu B_\nu(T)$ and the LTE result $S_\nu = B_\nu(T)$.
3. Use the Boltzmann and Saha equations; explain the strength of the Balmer lines along the spectral sequence.
4. Derive the two-level-atom source function and the condition for LTE to be valid.

---

## 6.1 Strict (full) thermodynamic equilibrium

In TE at temperature $T$, **every** distribution is the equilibrium one:

| Distribution | Law |
|---|---|
| particle velocities | Maxwell: $f(v)\propto v^2e^{-mv^2/2kT}$ |
| excitation | Boltzmann: $\dfrac{n_j}{n_i} = \dfrac{g_j}{g_i}e^{-(E_j-E_i)/kT}$ |
| ionisation | Saha (below) |
| radiation | Planck: $I_\nu = B_\nu(T)$, isotropic |

Deep in a star this holds extremely well. The photon mean free path ($\sim$ cm) is tiny compared with the temperature scale height ($\sim R_\odot\sim10^{11}$ cm), so every photon sees an isothermal enclosure.

## 6.2 Why TE fails near the surface

Collins (§9.1a) identifies the key asymmetry: **photons have much longer mean free paths than particles**. Approaching the surface:

1. Photons begin to **escape** into space, so $I_\nu$ becomes anisotropic and departs from $B_\nu$. The radiation field "feels" the boundary first.
2. A photon at a given point was emitted in regions with different $T$; the radiation field is **non-local**.
3. Particles, with short mean free paths, still collide often enough to keep Maxwell, Boltzmann and Saha distributions at the **local** $T$.

![Regimes from interior to the outer atmosphere](../figures/L06_regimes.png)

*Figure 6.1 — From STE in the interior, through LTE in the deep atmosphere, to NLTE in the upper layers. LTE fails first for strong lines and at low density.*

## 6.3 Local thermodynamic equilibrium

> **Definition.** In **LTE** the *matter* at each point is in thermodynamic equilibrium at the local temperature $T(\mathbf r)$: velocities are Maxwellian, populations follow Boltzmann and Saha. The radiation field $I_\nu$ is **not** required to be Planckian.

### Kirchhoff's law

In a closed cavity in TE, $I_\nu = B_\nu$ is homogeneous and isotropic, so $dI_\nu/ds = 0$. The RTE then gives $0 = -\alpha_\nu B_\nu + j_\nu$:
$$\boxed{\;j_\nu = \alpha_\nu B_\nu(T)\;}\qquad\text{(Kirchhoff's law)}$$
Both $j_\nu$ and $\alpha_\nu$ depend only on the **state of the matter** (populations and velocity distribution). In LTE that state is the TE state at the local $T$, so Kirchhoff's law still holds, even though $I_\nu\neq B_\nu$. Hence:
$$\boxed{\;S_\nu^{\rm LTE} = \frac{j_\nu}{\alpha_\nu} = B_\nu(T)\;}$$

MIT 8.901 (§7.3) stresses the other half of this statement: $S_\nu = B_\nu$ does **not** mean the object emits a black-body spectrum. An optically thick lump emits $B_\nu(T)$, but an optically thin lump at the same $T$ emits only $\tau_\nu B_\nu(T)$, which is bright only at the frequencies where $\alpha_\nu$ is large (see Lecture 5, §5.4).

Collins (eq. 9.2.28) notes that $S_\nu = B_\nu$ is **sufficient** for LTE but not necessary in general: with electron scattering present, $S_\nu = \varepsilon B_\nu + (1-\varepsilon)J_\nu$, yet the populations may still be in LTE.

### LTE written with Einstein coefficients

With Boltzmann populations, $g_1n_2/(g_2n_1) = e^{-h\nu/kT}$, the formulas of Lecture 4 give
$$\alpha_\nu = \frac{h\nu}{4\pi}n_1B_{12}\phi(\nu)\left(1-e^{-h\nu/kT}\right),\qquad
\frac{j_\nu}{\alpha_\nu} = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/kT}-1} = B_\nu(T).\ \checkmark$$
The factor $(1-e^{-h\nu/kT})$ is the **LTE stimulated-emission correction**; it multiplies every LTE opacity.

### What LTE does and does not say

| True in LTE | Not implied by LTE |
|---|---|
| $S_\nu = B_\nu(T_{\rm local})$ | $I_\nu = B_\nu$ |
| populations from Saha–Boltzmann at $T_{\rm local}$ | $J_\nu = B_\nu$ (it fails near the surface) |
| opacity and emissivity are functions of $(T,\rho)$ only | isotropic radiation |
| once $T(\tau)$ is known, the formal solution gives $I_\nu$ directly | zero flux |

## 6.4 Boltzmann and Saha equations

**Boltzmann** (excitation within one ionisation stage):
$$\frac{N_j}{N_i} = \frac{g_j}{g_i}\,e^{-(E_j-E_i)/kT},\qquad
\frac{N_j}{N} = \frac{g_j\,e^{-E_j/kT}}{U(T)},\quad U = \sum_i g_ie^{-E_i/kT}.$$
For hydrogen, $g_n = 2n^2$ and $E_n = -13.6\ {\rm eV}/n^2$.

**Saha** (ionisation $r\to r+1$):
$$\boxed{\;\frac{N_{r+1}\,n_e}{N_r} = \frac{2U_{r+1}}{U_r}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi_r/kT}\;}$$
with $(2\pi m_ek/h^2)^{3/2} = 2.415\times10^{21}$ m$^{-3}$ K$^{-3/2}$. Using $P_e = n_ekT$:
$$\frac{N_{r+1}}{N_r} = \frac{2kT\,U_{r+1}}{P_e\,U_r}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi_r/kT}.$$
The factor $2$ is the spin degeneracy of the free electron. The $T^{3/2}$ counts the free-electron phase space, and that large number is why gases ionise at $kT\ll\chi$.

![Saha-Boltzmann for hydrogen](../figures/L06_saha_boltzmann.png)

*Figure 6.2 — Hydrogen in LTE at $P_e = 20$ N m$^{-2}$. The $n=2$ population, which produces the Balmer lines, rises with $T$ (Boltzmann) and then collapses as H ionises (Saha). Its peak at $T\approx9900$ K explains why Balmer lines are strongest in A0 stars.*

## 6.5 When is LTE valid? The two-level atom

Consider the line $1\leftrightarrow2$ with collisional rates $C_{12}, C_{21}$ (per atom per second; $C_{21} = n_eq_{21}$). Detailed balance for collisions gives $C_{12}/C_{21} = (g_2/g_1)e^{-h\nu/kT}$. Statistical equilibrium:
$$n_1\left(B_{12}\bar J + C_{12}\right) = n_2\left(A_{21}+B_{21}\bar J + C_{21}\right).$$
Insert this into $S = (2h\nu^3/c^2)/[g_2n_1/(g_1n_2)-1]$ and use the Einstein relations. After some algebra (Exam Q4):
$$\boxed{\;S_\nu^{\rm line} = (1-\varepsilon)\bar J + \varepsilon B_\nu(T),\qquad
\varepsilon = \frac{\varepsilon'}{1+\varepsilon'},\quad \varepsilon' = \frac{C_{21}}{A_{21}}\left(1-e^{-h\nu/kT}\right)}$$

- **Collisions dominate** ($C_{21}\gg A_{21}$, high density): $\varepsilon\to1$, $S\to B$: **LTE**.
- **Radiation dominates** (low density): $\varepsilon\ll1$, $S\approx\bar J$: scattering-like, **NLTE**.

The **critical density** $n_{\rm crit} = A_{21}/q_{21}$ separates the two. The line source function has exactly the form found for continuum scattering in Lecture 4, so the methods of Lecture 8 apply.

### Collins' five assumptions of "normal" stellar atmospheres (§9.1d)

1. LTE prevails: all material properties follow from the local $T$ and $\rho$.
2. The atmospheric structure is set by the continuum opacity.
3. The geometry is a plane-parallel slab (thickness $\ll R$).
4. Gravity $g$ is constant through the atmosphere: $dP/dz = -g\rho$.
5. All energy is carried by radiation, with no sources: $F = \sigma T_{\rm eff}^4$ = constant.

Then **only $T_{\rm eff}$, $g$ and the composition** specify the atmosphere. This is the basis of Lectures 7–10.

---

## Worked example 6.1 — Why are the Balmer lines weak in the Sun?

*At $T = 5772$ K, compute $N_2/N_1$ for hydrogen.*
$kT = 0.4974$ eV, so $N_2/N_1 = (8/2)e^{-10.20/0.4974} = 4e^{-20.51} = 5.0\times10^{-9}$.
Only five atoms in a billion can absorb a Balmer photon. The Balmer lines are still visible because hydrogen is so abundant.
At 9900 K: $N_2/N_1 = 4e^{-11.96} = 2.6\times10^{-5}$, about 5000 times larger.

## Worked example 6.2 — Saha ionisation at 9900 K

*Hydrogen at $T = 9900$ K, $P_e = 20$ Pa. Find $N_{\rm II}/N_{\rm I}$. Take $U_{\rm I} = 2$, $U_{\rm II} = 1$.*

1. $n_e = P_e/kT = 20/(1.381\times10^{-23}\times9900) = 1.46\times10^{20}$ m$^{-3}$.
2. $(2\pi m_ekT/h^2)^{3/2} = 2.415\times10^{21}\times9900^{3/2} = 2.38\times10^{27}$ m$^{-3}$.
3. $e^{-13.6/0.8531} = e^{-15.94} = 1.19\times10^{-7}$.
4. $N_{\rm II}/N_{\rm I} = \dfrac{2\times1}{2}\times\dfrac{2.38\times10^{27}\times1.19\times10^{-7}}{1.46\times10^{20}} = 1.94$.

The ionised fraction is $1.94/2.94 = 0.66$. Then $N_2/N_{\rm tot} = (2.6\times10^{-5}/1.000026)\times(1/2.94)\approx8.7\times10^{-6}$, which is the peak in Figure 6.2.

## Worked example 6.3 — Is the H I 21-cm line in LTE in the ISM?

*$A_{21} = 2.9\times10^{-15}$ s$^{-1}$, and the collisional de-excitation rate coefficient is $q_{21}\approx10^{-16}$ m$^3$ s$^{-1}$ (H–H collisions at 100 K). Is the line in LTE at $n_{\rm H} = 10^6$ m$^{-3}$ (1 cm$^{-3}$)?*

$n_{\rm crit} = A_{21}/q_{21}\approx29$ m$^{-3}$ $\ll10^6$ m$^{-3}$. Collisions dominate, so the spin temperature is close to the kinetic temperature (the populations are thermalised). By contrast, optical forbidden lines such as [O III] have $A\sim10^{-2}$ s$^{-1}$ and $n_{\rm crit}\sim10^{11}$–$10^{12}$ m$^{-3}$, above nebular densities, so they are strongly NLTE.

---

## Exam questions and answers — Lecture 6

**Q1.** Define LTE precisely. Explain why LTE can hold even though the radiation field near a stellar surface is very far from a black body.

> **A1.** LTE: at each point the matter (velocity, excitation and ionisation distributions) is in TE at the local temperature $T(\mathbf r)$. It can hold because particle–particle collisions, which set the material distributions, are frequent (short particle mean free path). Photons have long mean free paths and escape, so $I_\nu\neq B_\nu$, but as long as collisional rates dominate the radiative rates in setting the populations, the matter does not "notice" the anomalous radiation field.

**Q2.** Derive Kirchhoff's law and show that it implies $S_\nu = B_\nu$ in LTE.

> **A2.** In a TE cavity, $I_\nu = B_\nu$ is uniform and isotropic, so $dI_\nu/ds = 0 = j_\nu-\alpha_\nu B_\nu$, giving $j_\nu = \alpha_\nu B_\nu(T)$. Because $j_\nu$ and $\alpha_\nu$ are properties of the matter only, the relation holds whenever the matter is in its TE state at the local $T$, i.e. in LTE. Then $S_\nu = j_\nu/\alpha_\nu = B_\nu(T)$.

**Q3.** Explain, with Saha and Boltzmann, why Balmer lines peak in strength for A0 stars ($T\approx10^4$ K) and are weaker in both cooler and hotter stars.

> **A3.** The Balmer opacity $\propto N_2$. In cool stars, $N_2/N_1\propto e^{-10.2\,{\rm eV}/kT}$ is tiny (e.g. $5\times10^{-9}$ at 5800 K). Above about $10^4$ K, Saha ionisation removes neutral H: $N_{\rm I}/N_{\rm tot}\to0$. The product $N_2/N_{\rm tot}$ therefore peaks near 9900 K (for $P_e = 20$ Pa).

**Q4.** For a two-level atom with collisions, derive $S = (1-\varepsilon)\bar J+\varepsilon B$. When does the line form in LTE?

> **A4.** From statistical equilibrium, $\frac{n_1}{n_2} = \frac{A_{21}+B_{21}\bar J + C_{21}}{B_{12}\bar J + C_{12}}$. Then
> $\frac{g_2n_1}{g_1n_2}-1 = \frac{A_{21}+C_{21}(1-e^{-h\nu/kT})}{B_{21}\bar J + C_{21}e^{-h\nu/kT}}$ (using $g_2B_{21} = g_1B_{12}$ and $g_2C_{21}e^{-h\nu/kT} = g_1C_{12}$). So
> $S = \frac{2h\nu^3}{c^2}\frac{B_{21}\bar J + C_{21}e^{-h\nu/kT}}{A_{21}+C_{21}(1-e^{-h\nu/kT})}$. With $A_{21} = (2h\nu^3/c^2)B_{21}$ and $\varepsilon' = C_{21}(1-e^{-h\nu/kT})/A_{21}$:
> $S = \frac{\bar J + \varepsilon'B_\nu}{1+\varepsilon'}$, because $\frac{2h\nu^3}{c^2}\frac{e^{-h\nu/kT}}{1-e^{-h\nu/kT}} = B_\nu$. Writing $\varepsilon = \varepsilon'/(1+\varepsilon')$ gives the result. LTE holds when $C_{21}\gg A_{21}$, i.e. $n_e\gg n_{\rm crit}$, but **also** only at depths $\gtrsim1/\sqrt\varepsilon$ (Lecture 8).
