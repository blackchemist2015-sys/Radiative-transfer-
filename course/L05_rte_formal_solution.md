# Lecture 5 — The Radiative Transfer Equation and Its Formal Solution

> **Sources:** MIT 8.901 Lec. 7 §§7.1–7.3 (RTE built up in three steps, constant-$S$ solution, formal solution, Kirchhoff's law for thick and thin lumps, thin H cloud, two-layer stellar atmosphere, thermal inversions); Hu Set 1 (optical depth, source function, formal solution, interpretation); Collins §9.2c–d (source function and its meaning).

## Learning goals

1. Write the RTE in terms of $\tau_\nu$ and $S_\nu$ and explain why "$I_\nu$ relaxes toward $S_\nu$".
2. Derive the formal solution with an integrating factor.
3. Solve the uniform slab, including its optically thin and thick limits.
4. Explain Kirchhoff's three laws of spectroscopy with RT, including MIT's two-layer star and thermal inversions.


## Key concepts in plain words

**The RTE is a tug of war.** Along a beam, two effects compete: the gas removes a fraction of the light (absorption), and the gas adds its own light (emission). If the beam is brighter than the gas's source function $S_\nu$, absorption wins and the beam fades toward $S_\nu$. If the beam is fainter, emission wins and the beam brightens toward $S_\nu$. Either way, after about one optical depth the beam "forgets" where it came from and approaches $S_\nu$.

**The formal solution — looking down a foggy street of lamps.** Imagine looking down a long, foggy street lined with lamps. The light reaching your eye is the sum of the light from every lamp, each one dimmed by the fog between it and you. Nearby lamps contribute strongly; distant lamps contribute only a little, because their light is attenuated by a factor $e^{-\tau}$. That is exactly the formal solution: $I = I_0e^{-\tau}+\int S\,e^{-(\tau-t)}dt$. It also explains why we "see" only about one optical depth into any medium.

**Optically thin versus optically thick.** A *thin* medium ($\tau\ll1$) is like a light mist: you see the background through it, and its own glow is weak and proportional to how much gas there is (each atom contributes independently). A *thick* medium ($\tau\gg1$) is like a wall: you see only its surface layer, and its brightness is $S_\nu$, independent of how much more gas lies behind.

**Why lines appear — Kirchhoff's three laws explained.** Atoms absorb strongly only at certain frequencies (the spectral lines). At those frequencies the gas is "thicker", so we see less deeply into it. If the background (or the deeper gas) is brighter than the gas in front, the line frequencies look darker: an *absorption line*. If there is no bright background, the gas glows mostly at the line frequencies: *emission lines*. If the gas is thick at all frequencies and at one temperature, we see a smooth continuum.

**The MIT two-layer star.** The simplest star that shows lines is a hot, thick base with a cooler, thin layer on top. In the continuum we see through the cool layer to the hot base; at the lines the cool layer blocks the view and we see its lower brightness. If the upper layer is *hotter* than the base (a **thermal inversion**), the same lines appear in emission. Thus line spectra are, at heart, thermometers of how temperature changes with height.

---

## 5.1 The equation, built up in three steps (MIT 8.901 §7.1)

![MIT 8.901 build-up of the RTE](../figures/L05_mit_rte_panels.png)

*Figure 5.0 — After MIT 8.901 Lecture 7, Fig. 9: radiation through (left) vacuum, $dI_\nu/ds = 0$; (centre) a purely absorbing medium, $dI_\nu/ds = -\alpha_\nu I_\nu$, so $I = I_0e^{-\tau}$; (right) a medium that absorbs and emits, $dI_\nu/ds = j_\nu-\alpha_\nu I_\nu$.*

MIT's notation: $\alpha_\nu = n\sigma_\nu = \rho\kappa_\nu$ (extinction coefficient, m$^{-1}$) and $j_\nu$ (emissivity, W m$^{-3}$ Hz$^{-1}$ sr$^{-1}$). Note that $j_\nu$ and $I_\nu$ have different units; their ratio $S_\nu = j_\nu/\alpha_\nu$ has the units of intensity. Combining Lecture 4's gains and losses:
$$\frac{dI_\nu}{ds} = -\alpha_\nu I_\nu + j_\nu .$$
Divide by $\alpha_\nu$ and use $d\tau_\nu = \alpha_\nu\,ds$ (optical depth measured **along the beam**) and $S_\nu = j_\nu/\alpha_\nu$:
$$\boxed{\;\frac{dI_\nu}{d\tau_\nu} = S_\nu - I_\nu\;}$$

**Physical meaning.** If $I_\nu > S_\nu$, then $dI_\nu/d\tau_\nu<0$: intensity decreases. If $I_\nu < S_\nu$, it increases. **The intensity always relaxes toward the local source function, on a scale of one optical depth.** $S_\nu$ is the intensity the medium "wants" to have.

## 5.2 Formal solution

Multiply by the integrating factor $e^{\tau_\nu}$ (MIT eq. 82–85):
$$\frac{d}{d\tau_\nu}\left(I_\nu e^{\tau_\nu}\right) = S_\nu e^{\tau_\nu}.$$
Integrate from $0$ to $\tau_\nu$:
$$\boxed{\;I_\nu(\tau_\nu) = I_\nu(0)\,e^{-\tau_\nu} + \int_0^{\tau_\nu}S_\nu(t)\,e^{-(\tau_\nu-t)}\,dt\;}$$

**Interpretation** (Hu): what arrives at $\tau_\nu$ is (i) the initial intensity attenuated by the whole column, plus (ii) the emission $S_\nu\,dt$ from every layer $t$, attenuated by the material between $t$ and the observer, $e^{-(\tau_\nu-t)}$.

The solution is "formal" because $S_\nu$ may depend on $I_\nu$ itself (scattering, NLTE). It is then an integral equation, not an explicit answer. In **LTE without scattering**, $S_\nu = B_\nu(T)$ is known once $T(\tau)$ is known, and the formal solution **is** the solution.

## 5.3 The uniform (isothermal) slab

If $S_\nu$ is constant:
$$\boxed{\;I_\nu = I_\nu(0)\,e^{-\tau_\nu} + S_\nu\left(1-e^{-\tau_\nu}\right)\;}$$

![Slab solution and line formation](../figures/L05_slab.png)

*Figure 5.1 — Left: whatever the incident intensity, $I_\nu\to S_\nu$ after a few optical depths. Right: a slab with optical depth larger at line centre than in the wings produces an absorption line when the background is brighter than $S$, and an emission line when it is fainter.*

| Limit | Result | Meaning |
|---|---|---|
| $\tau_\nu\ll1$ (optically thin) | $I_\nu\approx I_\nu(0)(1-\tau_\nu) + \tau_\nu S_\nu$ | background passes; emission $\propto$ column density ($\tau S = j\,L$) |
| $\tau_\nu\gg1$ (optically thick) | $I_\nu\to S_\nu$ | memory of the background lost; we see the medium itself |
| thick, LTE | $I_\nu = B_\nu(T)$ | an optically thick isothermal LTE body radiates as a black body |

> Even in LTE, $I_\nu = B_\nu$ only inside an **optically thick, isothermal** body. A real star is not isothermal, so its emergent spectrum is not exactly Planckian.

### Kirchhoff's laws of spectroscopy, explained

Write $\tau_\nu = \tau_c + \tau_0\phi(\nu)$, with a weak continuum $\tau_c$ plus a line. Then:

1. **Hot, opaque body** ($\tau_\nu\gg1$ at all $\nu$): $I_\nu = B_\nu(T)$, a continuous spectrum.
2. **Hot, thin gas, no background** ($I_\nu(0) = 0$): $I_\nu = B_\nu(1-e^{-\tau_\nu})$ is largest where $\tau_\nu$ is largest, so we see **emission lines**.
3. **Cooler gas in front of a hotter continuum** ($I_\nu(0) > S_\nu$): where $\tau_\nu$ is large, $I_\nu$ is pulled *down* toward $S_\nu$, giving **absorption lines**.

The real criterion is $I_{\rm background}$ versus $S_\nu$, not "cool versus hot" by itself. This idea carries over to stellar atmospheres in Lecture 10.

## 5.4 MIT 8.901 §7.3: thin clouds, two-layer stars and thermal inversions

MIT's form of **Kirchhoff's law** says that a thermally emitting object in equilibrium has $S_\nu = B_\nu(T)$, but this does **not** mean that it emits a black-body spectrum. What emerges depends on $\tau_\nu$. Take two lumps of matter at the same $T$, with nothing behind them ($I_\nu(0) = 0$):

| Lump | Emergent intensity | Spectrum |
|---|---|---|
| optically thick, $\tau_\nu\gg1$ | $I_\nu = S_\nu = B_\nu(T)$ | black body |
| optically thin, $\tau_\nu\ll1$ | $I_\nu = S_\nu\left[1-(1-\tau_\nu)\right] = \tau_\nu B_\nu(T) = \alpha_\nu s\,B_\nu(T)$ | black body × $\tau_\nu$: bright only where $\alpha_\nu$ is large |

**(a) A hot, thin hydrogen cloud on a dark sky.** $\alpha_\nu$ is large only at the hydrogen lines, whose wavelengths follow the Rydberg formula
$$\frac{1}{\lambda_{\rm vac}} = R_{\rm H}\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right),\qquad R_{\rm H} = 1.0968\times10^{7}\ {\rm m^{-1}}$$
($n_1 = 1, 2, 3, 4$: Lyman, Balmer, Paschen, Brackett). Since $I_\nu = \tau_\nu B_\nu$, we see an **emission-line spectrum** (Figure 5.2a).

**(b) The simplest stellar atmosphere** (MIT Fig. 10): an optically thick interior at $T_H$ under a cooler, thin layer at $T_C<T_H$. The thick base supplies $I_\nu(0) = B_\nu(T_H)$, and the layer gives
$$I_\nu = B_\nu(T_H)e^{-\tau_\nu} + B_\nu(T_C)\left(1-e^{-\tau_\nu}\right)\ \overset{\tau_\nu\ll1}{\approx}\ B_\nu(T_H) - \tau_\nu\left[B_\nu(T_H)-B_\nu(T_C)\right].$$
The **continuum** (small $\alpha_\nu$) shows $B_\nu(T_H)$ from deep down. At the **lines** (large $\alpha_\nu$) we see only down to $\tau_\nu\sim1$, i.e. the cool layer, so $I_\nu\to B_\nu(T_C)$: **absorption lines** (Figure 5.2b). An isothermal atmosphere gives a pure black body whatever $\alpha_\nu$ is.

**(c) Thermal inversion.** If $T$ *increases* outward ($T_{\rm top}>T_{\rm base}$), every argument reverses and the same lines appear in **emission** above the continuum (Figure 5.2c). MIT notes that inversions are ubiquitous: the solar chromosphere, Solar System planets (stratospheres) and hot-Jupiter exoplanets.

![MIT toy models](../figures/L05_mit_two_layer.png)

*Figure 5.2 — The MIT 8.901 toy models, computed exactly with $I = I_0e^{-\tau}+B(1-e^{-\tau})$ for Balmer and Paschen lines placed by the Rydberg formula (line widths exaggerated for visibility). (a) Thin 8000 K cloud: emission lines. (b) 6500 K base under a 4500 K layer: absorption lines. (c) Inverted case: emission lines.*

## 5.5 Radio spectrum of an H II region

For free–free absorption, $\tau_\nu\propto T_e^{-1.35}\nu^{-2.1}\int n_e^2\,ds$ (the integral is the emission measure). In the RJ limit, $I_\nu\propto T_b$:
$$T_b = T_e\left(1-e^{-\tau_\nu}\right).$$
At low $\nu$, $\tau\gg1$, so $T_b = T_e$ and the flux $S_\nu\propto\nu^2T_e$ (black body). At high $\nu$, $\tau\ll1$, so $T_b = T_e\tau_\nu\propto\nu^{-2.1}$ and the flux is $\propto\nu^{-0.1}$ (almost flat). The turnover at $\tau_\nu\approx1$ measures the emission measure.

---

## Worked example 5.1 — H II region brightness temperatures

*$T_e = 8000$ K. Find $T_b$ for $\tau = 0.01, 0.1, 1, 3, 10$.*

| $\tau$ | 0.01 | 0.1 | 1 | 3 | 10 |
|---|---|---|---|---|---|
| $T_b = T_e(1-e^{-\tau})$ [K] | 80 | 761 | 5057 | 7602 | 8000 |

**Lesson:** the brightness temperature equals the physical temperature only when the source is optically thick.

## Worked example 5.2 — Absorption by a foreground cloud

*A star with continuum intensity $I_0$ is seen through a cloud with $S = 0.3I_0$. At line centre $\tau = 5$, in the wings $\tau = 0.1$. Find the line profile values and the central depth.*

$I = I_0e^{-\tau}+S(1-e^{-\tau})$:

- wings ($\tau = 0.1$): $I = 0.933\,I_0$;
- $\tau = 1$: $I = 0.558\,I_0$;
- centre ($\tau = 5$): $I = 0.305\,I_0\approx S$.

The line core is **saturated**: it cannot go below $S$, however large $\tau$ becomes. The central depth is $1-0.305/0.933 = 0.67$ relative to the local continuum.

## Worked example 5.3 — Formal solution with a linearly increasing source function

*Let $S(t) = a + bt$ along a path of total optical depth $\tau$, with $I(0) = 0$. Find $I(\tau)$ and its thick limit.*

$$I(\tau) = \int_0^\tau(a+bt)e^{-(\tau-t)}dt.$$
Put $u = \tau-t$: $I = \int_0^\tau[a+b(\tau-u)]e^{-u}du = (a+b\tau)(1-e^{-\tau}) - b\left[1-(1+\tau)e^{-\tau}\right]$.
For $\tau\to\infty$: $I\to a + b\tau - b = S(\tau-1)$.

**The emerging intensity equals the source function one optical depth back from the observer.** This is the seed of the Eddington–Barbier relation (Lecture 7).

---

## Worked example 5.4 — The MIT two-layer star at H$\alpha$

*Base $T_H = 6500$ K, upper layer $T_C = 4500$ K. At $\lambda = 656.3$ nm the layer has $\tau_c = 0.02$ in the continuum and $\tau = 2.02$ at the centre of H$\alpha$. (a) Find the line depth. (b) Compare with the linearised MIT formula, and say when the formula fails. (c) What is the deepest the line could ever be?*

$B_\lambda(6500\ {\rm K}) = 3.474\times10^{13}$ and $B_\lambda(4500\ {\rm K}) = 7.551\times10^{12}$ W m$^{-3}$ sr$^{-1}$.

**(a)** Continuum: $I_c = B_He^{-0.02}+B_C(1-e^{-0.02}) = 0.9845\,B_H$. Line: $I_l = B_He^{-2.02}+B_C(1-e^{-2.02}) = 0.321\,B_H$. Depth $= 1 - I_l/I_c = 0.67$.

**(b)** The linearised form $B_H-\tau(B_H-B_C)$ gives $0.984\,B_H$ for $\tau = 0.02$ (correct to 0.02 %) but $-0.57\,B_H$ for $\tau = 2$: **negative and meaningless**. The linear form holds only for $\tau_\nu\ll1$; strong lines need the full exponential.

**(c)** For $\tau\to\infty$, $I_l\to B_C$, so the maximum depth is $1-B_C/I_c = 0.78$. **The depth of a saturated line measures the temperature contrast of the atmosphere**, which is the same conclusion as the Milne–Eddington model of Lecture 10.

---

## Common misconceptions

1. **"The formal solution solves the transfer problem."** Only if $S_\nu$ is known in advance (e.g. LTE with known $T$). With scattering, $S$ depends on $I$, and the formal solution becomes an integral equation.
2. **"An optically thick object always emits a black-body spectrum."** Only if it is also isothermal and $S = B$. A real star is thick but not isothermal.
3. **"Emission lines require a hot gas."** They require gas whose $S_\nu$ is larger than the background intensity, e.g. thin gas on a dark sky, or a temperature that rises outward.
4. **"The linearised two-layer formula works for every line."** It assumes $\tau\ll1$; for strong lines it can even give negative intensities.

## Lecture summary

- $dI_\nu/d\tau_\nu = S_\nu - I_\nu$: intensity relaxes toward the source function.
- Formal solution: background dimmed by $e^{-\tau}$ plus emission from each layer, each dimmed by the gas in front.
- Constant $S$: $I = I_0e^{-\tau}+S(1-e^{-\tau})$; thin ⇒ $I\approx I_0+\tau(S-I_0)$, thick ⇒ $I\to S$.
- Absorption lines need background brighter than $S$; emission lines need the opposite.
- MIT toy models: thin cloud (emission lines), two-layer star (absorption lines), inversion (emission lines).

---

## Exam questions and answers — Lecture 5

**Q1.** Starting from $dI_\nu/ds = -\alpha_\nu I_\nu+j_\nu$, derive the formal solution.

> **A1.** With $d\tau = \alpha\,ds$ and $S = j/\alpha$: $dI/d\tau + I = S$. Multiply by $e^\tau$: $d(Ie^\tau)/d\tau = Se^\tau$. Integrate: $I(\tau)e^\tau - I(0) = \int_0^\tau S(t)e^tdt$, so $I(\tau) = I(0)e^{-\tau}+\int_0^\tau S(t)e^{-(\tau-t)}dt$.

**Q2.** For a uniform slab with $S$ constant, derive $I = I_0e^{-\tau}+S(1-e^{-\tau})$ and discuss the thin and thick limits.

> **A2.** Take $S$ out of the integral: $\int_0^\tau e^{-(\tau-t)}dt = 1-e^{-\tau}$. Thin: $I\approx I_0+\tau(S-I_0)$, so the change is linear in $\tau$ (the column density). Thick: $I\to S$, independent of $I_0$.

**Q3.** "Absorption lines form because the gas in a stellar atmosphere is cooler than the gas below it." Rephrase this precisely using $I_\nu$ and $S_\nu$.

> **A3.** At line frequencies $\tau_\nu$ is large, so the emergent intensity is set by $S_\nu$ in higher layers. If $S_\nu$ decreases outward (in LTE, $S_\nu = B_\nu(T)$ with $T$ decreasing outward), then line photons come from layers with smaller $S_\nu$ than continuum photons, and an absorption line results. If $S_\nu$ increases outward (a chromosphere, or NLTE effects), the line appears in emission.

**Q4.** (MIT 8.901 two-layer model.) A star has an optically thick base at $T_H$ and a thin upper layer at $T_C$. Show that $I_\nu\approx B_\nu(T_H)-\tau_\nu[B_\nu(T_H)-B_\nu(T_C)]$ for $\tau_\nu\ll1$. Explain why the spectrum shows absorption lines, and what changes in a thermal inversion.

> **A4.** The base is thick, so $I_\nu(0) = B_\nu(T_H)$. The layer has $S_\nu = B_\nu(T_C)$ (LTE), so $I_\nu = B_\nu(T_H)e^{-\tau_\nu}+B_\nu(T_C)(1-e^{-\tau_\nu})$, and expanding $e^{-\tau}\approx1-\tau$ gives the result. Where $\alpha_\nu$ is large (lines), $\tau_\nu$ is large and the intensity drops toward $B_\nu(T_C)<B_\nu(T_H)$: absorption lines. In a thermal inversion $T_C>T_H$, so $B_\nu(T_C)>B_\nu(T_H)$ and the same lines appear in emission (solar chromosphere, planetary stratospheres). For strong lines the linear form fails (it can even go negative), and the full exponential must be used (Worked example 5.4).
