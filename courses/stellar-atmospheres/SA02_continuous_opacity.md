# Lecture SA2 — Physical Processes I: Continuous Opacity

> **Sources:** D. Mihalas, *Stellar Atmospheres* (1978), absorption cross-sections (bound–free, free–free, H$^-$, scattering); D. F. Gray, *The Observation and Analysis of Stellar Photospheres* (2005), Ch. 8 "The continuous absorption coefficient"; Rybicki & Lightman (1979), Chs. 5 (bremsstrahlung) and 10 (atomic structure); Wildt (1939) for H$^-$; Collins Ch. 9.
> **Prerequisites:** RT4 (absorption coefficient, cross-section, stimulated emission), SA1 (Saha–Boltzmann populations).

## Learning goals

1. List the physical processes that make up the continuous opacity of a stellar atmosphere and say where each one dominates.
2. Use Kramers' hydrogenic bound–free cross-section and the free–free formula with LTE populations.
3. Explain why H$^-$ is the dominant opacity source in the Sun and why its strength depends on metallicity.
4. Explain the Balmer jump, and combine the processes into a total opacity and a mean opacity.

---

## Key concepts in plain words

**Opacity is a menu of processes.** A photon in a stellar atmosphere can be stopped in four basic ways: (1) it lifts a bound electron to a higher bound level (*bound–bound*: spectral lines, SA4); (2) it frees a bound electron (*bound–free*: photo-ionisation); (3) a free electron absorbs it while passing an ion (*free–free*: inverse bremsstrahlung); (4) it is redirected without being destroyed (*scattering*). Processes 2–4 vary smoothly with frequency and make the **continuous opacity**, which sets the overall shape of the spectrum and the depth scale of the atmosphere.

**Edges are the fingerprints of bound–free absorption.** A photon can ionise an atom from level $n$ only if its energy exceeds the binding energy of that level. Each level therefore contributes absorption that starts abruptly at a threshold frequency (an *edge*) and fades toward higher frequency roughly as $\nu^{-3}$. For hydrogen the edges are at 91.2 nm (Lyman), 364.7 nm (Balmer) and 820.6 nm (Paschen).

**The opacity depends on the populations.** A process can absorb only if there are atoms in the right state. In LTE these populations come from Saha and Boltzmann (SA1), so the opacity changes dramatically with temperature: at 6000 K almost no hydrogen atoms are in level 2, while at 9000 K many more are.

**H$^-$: a fragile ion with a big effect.** A neutral hydrogen atom can hold a second electron, but only with 0.754 eV of binding. In the Sun only about one hydrogen atom in $10^8$ is H$^-$. That is enough to dominate the visible and infrared opacity, because it can be ionised by any photon with $\lambda<1.64$ µm, while ordinary hydrogen in cool gas is almost all in the ground state and absorbs only below 91 nm. The extra electrons come from easily ionised metals, so H$^-$ opacity grows with metallicity.

---

## 2.1 The four kinds of continuous and line processes

| Process | Photon is | Frequency dependence | Dominant in |
|---|---|---|---|
| bound–bound | absorbed (line) | narrow profiles (SA4) | lines in all stars |
| bound–free | absorbed (ionisation) | edges, $\propto\nu^{-3}$ above each edge | H I in A–B stars; He in O–B; metals in the UV; H$^-$ in F–K |
| free–free | absorbed (inverse bremsstrahlung) | $\propto\nu^{-3}$ (optical), $\nu^{-2}$ (radio) | hot stars (IR, radio); H$^-$ free–free in cool stars beyond 1.6 µm |
| electron scattering | scattered (Thomson) | gray | O stars, stellar interiors |
| Rayleigh scattering | scattered by atoms or molecules | $\propto\lambda^{-4}$ | blue and UV of cool giants |

## 2.2 Hydrogenic bound–free absorption

**Kramers' cross-section** for photo-ionisation from level $n$ of a hydrogen-like ion of charge $Z$ (semi-classical, corrected by a Gaunt factor $g_{\rm bf}\approx1$):
$$\boxed{\;\sigma_{\rm bf}(n,\nu) = \frac{64\pi^4m_ee^{10}}{3\sqrt3\,ch^6}\frac{Z^4}{n^5\nu^3}\,g_{\rm bf} = 2.815\times10^{29}\frac{Z^4g_{\rm bf}}{n^5\nu^3}\ \text{cm}^2\quad(\nu\ge\nu_n)\;}$$
(in SI: $2.815\times10^{25}$ m$^2$ Hz$^3$; first formula in Gaussian units). The thresholds are $\nu_n = 3.288\times10^{15}Z^2/n^2$ Hz, i.e. $\lambda_n = 91.13\,n^2/Z^2$ nm.

**Absorption coefficient in LTE.** Sum over levels with Boltzmann populations, $N_n = N_{\rm H\,I}\,2n^2e^{-E_n/kT}/U$, and include stimulated emission:
$$\alpha_\nu^{\rm bf} = \sum_n N_n\,\sigma_{\rm bf}(n,\nu)\left(1-e^{-h\nu/kT}\right).$$

![Continuous opacity of hydrogen](../../figures/SA2_continuous_opacity.png)

*Figure 2.1 — Left: hydrogen continuous cross-section per neutral H atom (bound–free + free–free + electron scattering) in LTE at $P_e = 20$ Pa, computed with `scripts/sa_physics.py`. The jumps at the Lyman, Balmer and Paschen edges grow dramatically with temperature, because the excited-level populations follow Boltzmann. Right: Kramers cross-sections of the first four levels. Each level absorbs only blueward of its edge.*

## 2.3 Free–free absorption

A free electron passing an ion can absorb a photon (the inverse of bremsstrahlung). For a hydrogen-like ion in LTE (Rybicki & Lightman eq. 5.18b, Gaussian units, $n$ in cm$^{-3}$):
$$\alpha_\nu^{\rm ff} = 3.69\times10^8\,\frac{Z^2n_en_i}{T^{1/2}\nu^3}\,g_{\rm ff}\left(1-e^{-h\nu/kT}\right)\ \text{cm}^{-1}.$$
It rises toward low frequency, dominates the infrared and radio emission of hot ionised gas (H II regions, RT5), and in cool stars appears as H$^-$ free–free (an electron passing a *neutral* H atom).

## 2.4 The negative hydrogen ion H$^-$

- **Binding energy** 0.754 eV, so the bound–free threshold is at $\lambda = 1.64$ µm. The cross-section peaks near 850 nm at about $4\times10^{-21}$ m$^2$ ($4\times10^{-17}$ cm$^2$).
- **Free–free** H$^-$ (electron + neutral H) dominates beyond about 1.6 µm. The minimum of the total H$^-$ opacity near 1.6 µm makes the solar continuum at that wavelength come from the deepest visible layers.
- **Abundance** from the Saha equation (H$^-$ has $U = 1$, H I has $U = 2$, one electron added):
$$\frac{n({\rm H^-})}{n({\rm H\,I})\,n_e} = \frac{1}{4}\left(\frac{h^2}{2\pi m_ekT}\right)^{3/2}e^{+0.754\,{\rm eV}/kT}.$$

- **Electron donors.** In the solar photosphere hydrogen is nearly neutral; the electrons come mainly from easily ionised metals (Na, Mg, Al, Si, Ca, Fe; ionisation energies 5–8 eV). The H$^-$ opacity is therefore roughly proportional to the metal abundance: metal-poor stars are more transparent, and we see deeper and hotter layers in them.
- **History:** Wildt (1939) identified H$^-$ as the main solar opacity; Chandrasekhar computed its cross-sections in the 1940s.

## 2.5 Scattering and other sources

- **Electron (Thomson) scattering**, $\sigma_T = 6.652\times10^{-29}$ m$^2$, gray. $\kappa_{\rm es} = 0.020(1+X)$ m$^2$ kg$^{-1}$ for fully ionised gas. It dominates in O stars and enters the source function as $S = \varepsilon B+(1-\varepsilon)J$ (RT8).
- **Rayleigh scattering** by H I and H$_2$, $\propto\lambda^{-4}$ far from resonance. Important in the blue and UV of cool giants.
- **He I and He II bound–free** (edges at 50.4 and 22.8 nm, plus excited-level edges) in hot stars; **metal bound–free** edges (Mg, Si, Fe, Al, C) in the UV of solar-type stars.
- **Molecules** (TiO, H$_2$O, CO, CH$_4$) and **dust** in M, L and T dwarfs.

## 2.6 Total and mean opacity

$$\kappa_\nu^{\rm tot}\rho = \sum_{\rm species}\left(\alpha_\nu^{\rm bf}+\alpha_\nu^{\rm ff}\right)(1-e^{-h\nu/kT}) + \alpha_\nu^{\rm es} + \alpha_\nu^{\rm Ray} + \alpha_\nu^{\rm lines}$$
(the stimulated-emission factor applies to true absorption only, not to scattering).

- Structure calculations need mean opacities: the **Rosseland mean** (harmonic, for the flux, RT8) and the **Planck mean** (arithmetic, for emission and absorption balance).
- **Opacity tables:** OPAL (Iglesias & Rogers 1996), the Opacity Project (Seaton et al. 1994), and low-temperature molecular and dust tables (e.g. Ferguson et al. 2005).
- In stellar interiors the bound–free and free–free opacities combine into **Kramers' law**, $\bar\kappa\propto\rho\,T^{-3.5}$.

---

## Worked example 2.1 — The size of a bound–free cross-section

*Evaluate Kramers' formula at the Lyman and Balmer edges of hydrogen ($g_{\rm bf} = 1$).*

Lyman ($n = 1$, $\nu_1 = 3.288\times10^{15}$ Hz): $\sigma = 2.815\times10^{25}/(3.288\times10^{15})^3 = 7.9\times10^{-22}$ m$^2$ (the exact quantum value, with $g_{\rm bf} = 0.80$, is $6.3\times10^{-22}$ m$^2$).
Balmer ($n = 2$, $\nu_2 = \nu_1/4$): $\sigma = 2.815\times10^{25}/(2^5(\nu_1/4)^3) = 7.9\times10^{-22}\times64/32 = 1.6\times10^{-21}$ m$^2$.
**Note:** the edge cross-section *grows* with $n$ (as $n$), because the $\nu^{-3}$ factor wins over $n^{-5}$. Excited levels are excellent absorbers, if they are populated.

## Worked example 2.2 — Why H$^-$ dominates the solar opacity at 500 nm

*At $T = 6000$ K and $n_e = 10^{19}$ m$^{-3}$, compare the H$^-$ bound–free cross-section per H atom with the hydrogen $n = 3$ (Paschen) bound–free cross-section per H atom at 500 nm.*

1. **H$^-$:** $n({\rm H^-})/n({\rm H\,I}) = n_e\big/\left[4\,(2\pi m_ekT/h^2)^{3/2}e^{-0.754/kT}\right]$. Here $(2\pi m_ekT/h^2)^{3/2} = 1.12\times10^{27}$ m$^{-3}$ and $e^{-0.754/0.517} = 0.233$, so the ratio is $10^{19}/(4\times1.12\times10^{27}\times0.233) = 9.6\times10^{-9}$. Times $\sigma\approx4\times10^{-21}$ m$^2$: $3.8\times10^{-29}$ m$^2$ per H atom.
2. **H I, $n = 3$:** $N_3/N_{\rm H\,I} = 9e^{-12.09/0.517} = 6.3\times10^{-10}$; $\sigma_3(500\,{\rm nm}) = 5.4\times10^{-22}$ m$^2$. Product: $3.4\times10^{-31}$ m$^2$ per H atom.
3. **Ratio** ≈ 110. A tiny fraction of fragile negative ions out-absorbs the excited neutral hydrogen by two orders of magnitude.

## Worked example 2.3 — The Balmer jump across the spectral sequence

*From the computation behind Figure 2.1 ($P_e = 20$ Pa), the hydrogen opacity just blueward of the Balmer edge exceeds that just redward of it by factors of 106 (6000 K), 26 (9000 K) and 12 (12 000 K). Why is the observed Balmer jump largest in late B and A stars, not in the Sun?*

In the Sun hydrogen bound–free is not the main opacity: H$^-$ is about 100 times larger (Worked example 2.2), and it has no edge at 364.7 nm. The hydrogen jump is diluted and the observed solar Balmer jump is small. Near 9000–10 000 K hydrogen dominates the continuum, so its jump appears fully in the spectrum: blueward of the edge the opacity is much higher, we see higher and cooler layers (Eddington–Barbier), and the flux drops. At higher $T$ the jump shrinks (12 at 12 000 K) as electron scattering and ionisation take over. The Balmer jump therefore measures temperature in B stars and gravity (through $P_e$) in A and F stars.

---

## Common misconceptions

1. **"The most abundant atom gives the most opacity."** What matters is how many particles are in an absorbing state at the relevant frequency. A $10^{-8}$ fraction of H$^-$ beats neutral hydrogen in the Sun.
2. **"Bound–free absorption occurs only at the edge."** It occurs at all frequencies *above* the edge, falling roughly as $\nu^{-3}$.
3. **"Electron scattering is absorption."** It redirects photons without destroying them; it adds to the extinction but enters the source function as $J$, not $B$.
4. **"Metals are too rare to matter for the continuum."** They supply the electrons that make H$^-$, and their bound–free edges dominate the UV of cool stars.

## Lecture summary

- Continuous opacity = bound–free + free–free + scattering (plus H$^-$, molecules, dust); lines are added separately (SA4).
- Kramers: $\sigma_{\rm bf} = 2.815\times10^{29}Z^4g/(n^5\nu^3)$ cm$^2$ above $\nu_n = 3.29\times10^{15}Z^2/n^2$ Hz.
- Free–free: $\alpha_{\rm ff}\propto Z^2n_en_iT^{-1/2}\nu^{-3}$.
- H$^-$ (0.754 eV, threshold 1.64 µm) dominates F–K photospheres; its strength scales with $n_e$, i.e. with metallicity.
- Edges produce the Balmer and Paschen jumps; the opacity changes enormously with $T$ through Saha–Boltzmann.

---

## Exam questions and answers — Lecture SA2

**Q1.** Write Kramers' bound–free cross-section and show that, at the edge, the cross-section of level $n$ is proportional to $n$.

> **A1.** $\sigma_{\rm bf}(n,\nu) = 2.815\times10^{29}Z^4g_{\rm bf}/(n^5\nu^3)$ cm$^2$ for $\nu\ge\nu_n = \nu_1/n^2$. At the edge, $\nu_n^3 = \nu_1^3/n^6$, so $\sigma(n,\nu_n) = 2.815\times10^{29}Z^4g\,n^6/(n^5\nu_1^3)\propto n$.

**Q2.** Explain why H$^-$ is the main continuous opacity in the solar photosphere, and why metal-poor stars are more transparent.

> **A2.** In the Sun hydrogen is mostly neutral and in the ground state, which absorbs only below 91 nm. Excited levels are very weakly populated ($N_3/N_1\sim10^{-9}$). H$^-$, though rare ($\sim10^{-8}$ of H), can be ionised by any photon below 1.64 µm with a large cross-section, so it dominates the visible and near-IR. Its abundance $\propto n_e$, and in the photosphere the electrons come from metals; fewer metals means fewer electrons, less H$^-$, lower opacity, so we see deeper layers.

**Q3.** Write the LTE bound–free absorption coefficient of hydrogen, including stimulated emission. Which quantities depend on temperature?

> **A3.** $\alpha^{\rm bf}_\nu = \sum_nN_n\sigma_{\rm bf}(n,\nu)(1-e^{-h\nu/kT})$, with $N_n = N_{\rm H\,I}\,2n^2e^{-E_n/kT}/U(T)$ and $N_{\rm H\,I}$ from the Saha equation. Temperature enters through the Boltzmann factor of each level, the Saha ionisation balance (through $T^{3/2}e^{-\chi/kT}/n_e$) and the stimulated-emission factor. The cross-sections themselves do not depend on $T$.

**Q4.** Rank the dominant continuous opacity in an O star, an A0 star, the Sun and an M dwarf, and say which produces a Balmer jump.

> **A4.** O star: electron scattering, with He bound–free. A0: H I bound–free and free–free. Sun: H$^-$ bound–free (and free–free in the IR). M dwarf: H$^-$ plus molecules. A strong Balmer jump appears where H I bound–free dominates, i.e. in late B, A and early F stars. It is weak in the Sun (H$^-$ dominates) and in O stars (hydrogen ionised, electron scattering dominates).
