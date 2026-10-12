# Lecture 10 — Spectral Lines in LTE, and the Limits of LTE

> **Sources:** Collins §9.1c (continuum and spectral lines), §9.2e (redistribution: coherent, complete, isotropic); Chandrasekhar Ch. XII §83–84 (line formation; Milne–Eddington model, residual intensities); MIT 8.901 Lec. 7 §7.3 (two-layer atmosphere, thermal inversions); Hu Set 1 ("photons escape through the channel of lowest opacity, so lines are dark"); Lectures 4, 6, 7, 9 of this course.

## Learning goals

1. Write the line absorption coefficient, the line profile (Doppler, Lorentz, Voigt) and the Doppler width.
2. Explain with Eddington–Barbier why LTE atmospheres with outward-decreasing $T$ show absorption lines.
3. Derive the Milne–Eddington residual-flux profile exactly in LTE.
4. Explain the curve of growth and use the weak-line formula to measure abundances.
5. Recognise when LTE fails for lines, and what NLTE changes.

---

## 10.1 Line opacity

For a bound–bound transition $l\to u$ with oscillator strength $f_{lu}$:
$$\alpha^{\rm line}_\nu = \frac{\pi e^2}{4\pi\varepsilon_0m_ec}\,f_{lu}\,n_l\,\phi(\nu)\left(1-e^{-h\nu/kT}\right)
= \pi r_e c\,f_{lu}\,n_l\,\phi(\nu)\left(1-e^{-h\nu/kT}\right)\quad\text{[LTE]},$$
with $r_e = 2.818\times10^{-15}$ m, so $\pi r_ec = 2.654\times10^{-6}$ m$^2$ Hz. The level population $n_l$ comes from **Saha–Boltzmann** at the local $T$ and $P_e$ (Lecture 6). The factor $(1-e^{-h\nu/kT})$ is the LTE stimulated-emission correction.

**Profiles** ($\int\phi\,d\nu = 1$):

| Broadening | Profile | Width |
|---|---|---|
| thermal + microturbulent Doppler | Gaussian: $\phi = \dfrac{1}{\sqrt\pi\Delta\nu_D}e^{-v^2}$, $v = (\nu-\nu_0)/\Delta\nu_D$ | $\Delta\nu_D = \dfrac{\nu_0}{c}\sqrt{\dfrac{2kT}{m}+\xi^2}$ |
| natural, collisional (pressure), Stark | Lorentzian: $\phi = \dfrac{\gamma/4\pi^2}{(\nu-\nu_0)^2+(\gamma/4\pi)^2}$ | $\gamma = \gamma_{\rm rad}+\gamma_{\rm coll}$ |
| both | **Voigt**: $\phi = \dfrac{H(a,v)}{\sqrt\pi\Delta\nu_D}$, $a = \dfrac{\gamma}{4\pi\Delta\nu_D}$ | Gaussian core + Lorentzian ("damping") wings |

## 10.2 Why lines are dark: LTE and Eddington–Barbier

In LTE with pure absorption, both the continuum and the line emit thermally:
$$S_\nu = \frac{\kappa_cB_\nu + \kappa_lB_\nu}{\kappa_c+\kappa_l} = B_\nu(T).$$
The difference lies only in the **depth scale**. With $\eta_\nu\equiv\kappa_l\phi/\kappa_c$, $d\tau_\nu = (1+\eta_\nu)d\tau_c$. By Eddington–Barbier, $F_\nu\approx\pi B_\nu\big(T(\tau_\nu = 2/3)\big)$:

- In the **continuum**, $\tau_\nu = 2/3$ at $\tau_c = 2/3$: deep and hot.
- At **line centre**, $\tau_\nu = 2/3$ at $\tau_c = \frac{2/3}{1+\eta}$: high and cool.

So $F_{\rm line} < F_{\rm cont}$ when $T$ decreases outward. This is the continuous version of MIT 8.901's two-layer toy star (Lecture 5, §5.4), where the continuum shows $B_\nu(T_H)$ and the lines show $B_\nu(T_C)$. **An LTE absorption line is a map of the temperature gradient.** If $T$ increases outward (a chromosphere), the same physics gives emission lines.

![LTE line formation: Milne-Eddington](../figures/L10_lines.png)

*Figure 10.1 — Left: line photons escape from higher layers, where $S = B$ is smaller. Centre: Milne–Eddington LTE profiles for increasing line strength $\eta_0$. The core saturates at a finite depth (dotted line), set by the surface value of $B$. Right: the curve of growth. The equivalent width grows linearly, then flattens (saturation), then rises again as $\sqrt{\eta_0}$ when damping wings become optically thick.*

## 10.3 The Milne–Eddington model: an exact LTE line solution

**Assumptions:** LTE ($S_\nu = B_\nu$); $B_\nu$ linear in continuum optical depth, $B_\nu = B_0(1+\beta\tau_c)$; and $\eta_\nu$ = constant with depth (the same ratio of line to continuum opacity at all depths).

Then $\tau_\nu = (1+\eta_\nu)\tau_c$, so $B_\nu = B_0\left(1+\dfrac{\beta}{1+\eta_\nu}\tau_\nu\right)$ is linear in $\tau_\nu$, and Eddington–Barbier is **exact**:
$$F_\nu = \pi B_0\left(1+\frac{2}{3}\frac{\beta}{1+\eta_\nu}\right),\qquad F_c = \pi B_0\left(1+\frac{2\beta}{3}\right),$$
$$\boxed{\;r_\nu\equiv\frac{F_\nu}{F_c} = \frac{1+\dfrac{2\beta}{3(1+\eta_\nu)}}{1+\dfrac{2\beta}{3}}\;}$$

- Weak line ($\eta\ll1$): $1 - r_\nu\approx\dfrac{2\beta/3}{1+2\beta/3}\,\eta_\nu\propto\eta_\nu\propto N f$.
- Saturated core ($\eta\to\infty$): $r\to\dfrac{1}{1+2\beta/3}$. The maximum depth is set by the temperature gradient $\beta$. A steeper gradient gives deeper lines; an isothermal atmosphere ($\beta = 0$) gives **no lines at all** in LTE.
- For the gray atmosphere, bolometrically $B\propto\tau+2/3$, i.e. $\beta = 3/2$, and the maximum depth is $1-1/2 = 0.5$. At optical wavelengths $\beta$ is larger (Wien sensitivity), so lines can be deeper.

## 10.4 Equivalent width and the curve of growth

The **equivalent width** is the width of a rectangle of zero flux with the same area as the line:
$$W_\nu = \int\left(1-\frac{F_\nu}{F_c}\right)d\nu,\qquad W_\lambda = \frac{\lambda^2}{c}W_\nu .$$

**Weak-line (optically thin) limit.** For an absorbing column $N_l$ in front of a continuum (the slab of Lecture 5 with $S\ll I_0$), $1-F/F_c\approx\tau_\nu$, so
$$\boxed{\;W_\lambda = \pi r_e\,\lambda^2\,N_lf\;}\qquad\text{(independent of the profile and of the broadening)}$$
In SI: $W_\lambda[{\rm m}] = 8.853\times10^{-15}\,\lambda^2[{\rm m^2}]\,N_lf\,[{\rm m^{-2}}]$.

**Three regimes:**

| Regime | Condition | $W$ depends on | Use |
|---|---|---|---|
| linear | $\tau_0\lesssim1$ | $W\propto Nf$ | **abundances** (best) |
| flat (saturated) | $1\lesssim\tau_0\lesssim10^{3\text{–}4}$ | $W\propto\Delta\nu_D\sqrt{\ln\tau_0}$ | **microturbulence** $\xi$, temperature |
| damping (square-root) | wings opaque | $W\propto\sqrt{Nf\gamma}$ | gravity (pressure broadening) |

## 10.5 Beyond LTE

From Lecture 6, the line source function of a two-level atom is
$$S^{\rm line} = (1-\varepsilon)\bar J + \varepsilon B,\qquad \varepsilon\approx\frac{C_{21}}{C_{21}+A_{21}}.$$
For strong lines in low-density layers, $\varepsilon\ll1$. Then, from Lecture 8:

- $S^{\rm line}(0)\approx\sqrt\varepsilon\,B$, well below $B$, so **NLTE line cores are darker than LTE cores** (e.g. Na I D, Mg I b, Ca II H & K, H$\alpha$ cores in the Sun).
- Thermalisation occurs only at $\tau_{\rm line}\sim1/\sqrt\varepsilon$, which can be deep in the photosphere.

**Departure coefficients** $b_i = n_i/n_i^{\rm LTE}$ give
$$S^{\rm line} = \frac{2h\nu^3}{c^2}\,\frac{1}{\dfrac{b_l}{b_u}e^{h\nu/kT}-1},\qquad S^{\rm line}\approx\frac{b_u}{b_l}B_\nu\quad(\text{Wien}).$$

**When to expect NLTE:** low density (giants, supergiants, upper atmospheres); hot stars with intense UV radiation (photo-ionisation dominates); low metallicity (fewer free electrons, so fewer collisions); strong resonance lines; nebulae and the ISM (always NLTE).

| | LTE | NLTE |
|---|---|---|
| populations | Saha–Boltzmann($T$, $n_e$) | rate equations, coupled to $J_\nu$ |
| $S^{\rm line}$ | $B_\nu(T)$ | $(1-\varepsilon)\bar J+\varepsilon B$, or via $b_i$ |
| locality | local | non-local (photons couple distant layers) |
| computational cost | small | large (ALI, multi-level, many frequencies) |
| where valid | deep photospheres, weak lines, high density | strong lines, chromospheres, hot or low-density stars |

---

## Worked example 10.1 — Doppler widths

*Compute the thermal Doppler width for (a) H$\alpha$ (656.28 nm) at 5772 K, (b) an Fe I line at 500 nm at 5772 K.*

(a) $v_{\rm th} = \sqrt{2kT/m_H} = 9.76$ km s$^{-1}$, so $\Delta\lambda_D = \lambda v/c = 0.0214$ nm $= 214$ mÅ.
(b) $m = 55.85\,m_u$: $v_{\rm th} = 1.31$ km s$^{-1}$, so $\Delta\lambda_D = 21.9$ mÅ.
Iron lines are about 10 times narrower than hydrogen lines. In the Sun the microturbulence $\xi\approx1$ km s$^{-1}$ is comparable to $v_{\rm th}$(Fe), so it matters for metal lines.

## Worked example 10.2 — An abundance from a weak line

*A weak Fe I line at 500 nm has $W_\lambda = 22$ mÅ and $f = 0.1$. Assume it is on the linear part of the curve of growth and treat the atmosphere as an absorbing column. Find the column density $N_l$ of absorbing atoms.*

$$N_l = \frac{W_\lambda}{\pi r_e\lambda^2f} = \frac{2.2\times10^{-12}}{8.853\times10^{-15}\times(5\times10^{-7})^2\times0.1} = 1.0\times10^{16}\ {\rm m^{-2}}.$$
The total iron abundance follows from Saha–Boltzmann (fraction of Fe in the lower level of Fe I) and the column of hydrogen above $\tau\approx2/3$, roughly $P/(g\mu m_H)$ from Lecture 9. **LTE enters at the Saha–Boltzmann step.**

## Worked example 10.3 — Milne–Eddington line depths

*With $\beta = 1.5$, find the central residual flux for $\eta_0 = 1$, $10$ and $\infty$.*

$r = \dfrac{1+1/(1+\eta)}{2}$: for $\eta = 1$, $r = 0.75$; for $\eta = 10$, $r = 0.545$; for $\eta\to\infty$, $r = 0.5$. Increasing $\eta$ from 10 to $\infty$ barely changes the core: the line is **saturated**, and further growth of $W$ happens only in the wings.

## Worked example 10.4 — LTE emission lines from a chromosphere

*Suppose that above the temperature minimum $T$ rises outward, so that near the surface $B = B_0(1-\beta'\tau_c)$ with $\beta'>0$ for $\tau_c<0.1$. What does LTE predict for a strong line formed at $\tau_c\approx0.01$?*

The strong line's $\tau_\nu = 2/3$ falls at $\tau_c\approx0.01$, where $B$ is larger than at $\tau_c\approx0.1$ (the temperature minimum), so the core shows an **emission reversal** inside the broad absorption profile. This is seen in the Ca II H & K lines (the K$_2$ peaks). In reality NLTE decoupling ($S<B$) makes the emission weaker than LTE predicts.

---

## Exam questions and answers — Lecture 10

**Q1.** Explain, using the Eddington–Barbier relation, why the solar spectrum shows absorption lines. What would an LTE isothermal atmosphere show?

> **A1.** $F_\nu\approx\pi S_\nu(\tau_\nu = 2/3)$, and in LTE $S_\nu = B_\nu(T)$. Line opacity raises $\tau_\nu$, so $\tau_\nu = 2/3$ is reached higher up, where $T$ (hence $B_\nu$) is lower, and the flux is lower. If the atmosphere were isothermal, $B_\nu$ would be the same at all depths and $F_\nu = F_c$: no lines, whatever the opacity.

**Q2.** Derive the Milne–Eddington residual flux and its saturation limit.

> **A2.** See §10.3. $B = B_0(1+\beta\tau_c)$ and $\tau_\nu = (1+\eta)\tau_c$ give $B = B_0(1+\beta\tau_\nu/(1+\eta))$, which is linear in $\tau_\nu$. Then $F = \pi B(\tau_\nu = 2/3) = \pi B_0(1+\frac{2\beta}{3(1+\eta)})$. Divide by $F_c$ ($\eta = 0$). As $\eta\to\infty$, $r\to1/(1+2\beta/3)$.

**Q3.** Sketch the curve of growth and explain the physics of each of its three parts. Which part is best for abundance determination and why?

> **A3.** Linear: the line is optically thin; every atom removes photons independently, so $W\propto Nf$. Flat: the core is saturated ($r\to r_{\min}$), and $W$ grows only as the Doppler core broadens in frequency where $\tau_\nu>1$, i.e. $W\propto\Delta\nu_D\sqrt{\ln\tau_0}$. Square-root: the Lorentzian damping wings ($\propto\gamma/\Delta\nu^2$) become optically thick, giving $W\propto\sqrt{Nf\gamma}$. The linear part is best for abundances because $W$ is insensitive to the poorly known broadening parameters ($\xi$, $\gamma$).

**Q4.** Why are the cores of strong resonance lines in the Sun deeper than LTE models predict?

> **A4.** In the low-density upper photosphere and chromosphere, $C_{21}\ll A_{21}$, so $\varepsilon\ll1$ and $S^{\rm line} = (1-\varepsilon)\bar J+\varepsilon B$. Photons escape from the line core ($\bar J<B$) and the source function drops to $\sim\sqrt\varepsilon\,B$ at the surface. The core intensity $\approx S(\tau_\nu\approx1)$ is therefore lower than $B(T)$, and the line is darker than in LTE.
