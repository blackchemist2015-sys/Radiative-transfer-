# Lecture 9 — The Gray LTE Atmosphere: Complete Solution

> **This is the central lecture of the course.** We solve, step by step and then exactly, the simplest self-consistent model of a stellar atmosphere in LTE.
> **Sources:** Collins §9.1d (assumptions), §9.4 (radiative equilibrium; Eddington approximation, eq. 9.4.12–9.4.13); Chandrasekhar Ch. III §25 (Milne problem by discrete ordinates: $J(\tau) = \tfrac34F[\tau+q(\tau)]$, eq. 45; $H$-function law of darkening, eq. 61; Hopf–Bronstein relation $J(0) = \tfrac{\sqrt3}{4}F$, eq. 64) and Ch. V (exact tables); Hu Set 1; MIT 8.901.

## Learning goals

1. List the assumptions of the gray LTE atmosphere and explain each.
2. Derive $T^4(\tau) = \tfrac34T_{\rm eff}^4\left(\tau+\tfrac23\right)$ in the Eddington approximation.
3. Know the exact solution (Hopf function $q(\tau)$, Chandrasekhar's $H$-function) and its numerical values.
4. Compute the emergent intensity, limb darkening, spectrum and pressure structure of a gray LTE model.

---

## 9.1 The problem

**Assumptions**

1. **Plane-parallel, static** atmosphere; $\tau$ measured inward.
2. **LTE:** $S_\nu = B_\nu(T)$ (pure absorption; scattering can be added and changes nothing for the gray case, since it cancels in radiative equilibrium).
3. **Gray:** $\kappa_\nu = \kappa$ is independent of frequency, so $\tau_\nu = \tau$ for all $\nu$. (In practice we use the Rosseland mean: Lecture 8.)
4. **Radiative equilibrium:** constant flux $F = \sigma T_{\rm eff}^4$, with no convection and no energy sources.

**Frequency-integrated equations.** Integrating $\mu\,dI_\nu/d\tau = I_\nu - B_\nu$ over $\nu$ (allowed because $\tau$ does not depend on $\nu$):
$$\mu\frac{dI}{d\tau} = I - B,\qquad B = \frac{\sigma T^4}{\pi}.$$

## 9.2 Step-by-step solution in the Eddington approximation

**Step 1 — Radiative equilibrium gives $J = B$.** Radiative equilibrium, $\int\kappa_\nu(J_\nu - B_\nu)d\nu = 0$, becomes for a gray atmosphere $\kappa(J - B) = 0$:
$$\boxed{\;J(\tau) = B(\tau) = S(\tau)\;}$$
In a gray LTE atmosphere the source function equals the mean intensity. This is mathematically identical to a **pure-scattering** atmosphere (the Milne problem), which is why Chandrasekhar treats both together.

**Step 2 — The flux is constant.** The zeroth moment gives $dH/d\tau = J - B = 0$, so
$$H = \text{const} = \frac{F}{4\pi} = \frac{\sigma T_{\rm eff}^4}{4\pi}.$$

**Step 3 — $K$ is linear in $\tau$ (exactly).** The first moment, $dK/d\tau = H$, gives
$$K(\tau) = H\tau + \text{const}.$$
No approximation has been made so far.

**Step 4 — Eddington closure.** With $K = J/3$:
$$J(\tau) = 3H\,(\tau + C).$$

**Step 5 — Surface boundary condition.** With $J(0) = 2H(0)$ (Lecture 8): $3HC = 2H$, so $C = 2/3$:
$$J(\tau) = 3H\left(\tau+\frac23\right) = \frac{3\sigma T_{\rm eff}^4}{4\pi}\left(\tau+\frac23\right).$$

**Step 6 — Temperature.** Since $J = B = \sigma T^4/\pi$:
$$\boxed{\;T^4(\tau) = \frac34\,T_{\rm eff}^4\left(\tau+\frac23\right)\;}$$

**Step 7 — Consequences.**

| Quantity | Value | Meaning |
|---|---|---|
| $T(\tau = 2/3)$ | $T_{\rm eff}$ | the "photosphere": the effective temperature is the actual temperature at $\tau = 2/3$ (Eddington–Barbier) |
| $T(0)$ | $2^{-1/4}T_{\rm eff} = 0.841\,T_{\rm eff}$ | **boundary temperature**; the atmosphere does not cool to zero |
| $\tau\gg1$ | $T^4\approx\tfrac34T_{\rm eff}^4\tau$ | diffusion regime, $F = \frac{4\pi}{3}\frac{dB}{d\tau}$ ✓ |

## 9.3 Emergent intensity and limb darkening

Since $S(\tau) = \frac{3F}{4\pi}\left(\tau+\frac23\right)$ is **linear**, Eddington–Barbier is exact:
$$I(0,\mu) = S(\tau = \mu) = \frac{3F}{4\pi}\left(\mu+\frac23\right)
\qquad\Rightarrow\qquad
\boxed{\;\frac{I(0,\mu)}{I(0,1)} = \frac{2+3\mu}{5} = \frac25\left(1+\frac32\mu\right)\;}$$

**Self-consistency check.** The flux computed from the emergent intensity is
$$2\pi\int_0^1 I(0,\mu)\,\mu\,d\mu = 2\pi\cdot\frac{3F}{4\pi}\left(\frac13+\frac13\right) = F.\ \checkmark$$

## 9.4 The exact solution (Milne, Hopf, Chandrasekhar)

Without the Eddington approximation, Step 1 combined with the Schwarzschild–Milne equation (Lecture 7) gives **Milne's integral equation**
$$J(\tau) = \Lambda_\tau[J] = \frac12\int_0^\infty J(t)\,E_1|t-\tau|\,dt .$$
Its solution, normalised to flux $F$, is written (Chandrasekhar eq. 45)
$$\boxed{\;J(\tau) = \frac{3F}{4\pi}\left[\tau + q(\tau)\right],\qquad T^4 = \frac34T_{\rm eff}^4\left[\tau+q(\tau)\right]\;}$$
where $q(\tau)$ is the **Hopf function**:

| $\tau$ | 0 | 0.01 | 0.1 | 0.5 | 1 | 2 | $\infty$ |
|---|---|---|---|---|---|---|---|
| $q(\tau)$ (our solver) | 0.5773 | 0.5882 | 0.6279 | 0.6802 | 0.6985 | 0.7078 | 0.7104 |
| exact | $1/\sqrt3 = 0.57735$ | | | | | | 0.710446 |

- $q(0) = 1/\sqrt3$ is the **Hopf–Bronstein relation** $J(0) = \sqrt3\,H$ (Chandrasekhar eq. 64), an exact result.
- Exact boundary temperature: $T(0) = (\sqrt3/4)^{1/4}T_{\rm eff} = 0.8114\,T_{\rm eff}$, against Eddington's $0.8409$ (a 3.6 % error).
- $q(\infty) = 0.7104$ against Eddington's $2/3$: the deep structure is shifted by $\Delta\tau = 0.044$.

**Exact emergent intensity** (Chandrasekhar eq. 61): $I(0,\mu) = \dfrac{\sqrt3}{4}\dfrac{F}{\pi}H(\mu)$, where $H(\mu)$ solves
$$\frac1{H(\mu)} = \int_0^1\frac{\mu'H(\mu')}{2(\mu+\mu')}d\mu',\qquad H(0) = 1,\ H(1) = 2.9078.$$

| $\mu$ | 0 | 0.1 | 0.2 | 0.5 | 1 |
|---|---|---|---|---|---|
| exact $I(\mu)/I(1)$ (Chandrasekhar Table; our solver) | 0.3439 | 0.4290 | 0.4988 | 0.6922 | 1 |
| Eddington $(2+3\mu)/5$ | 0.400 | 0.460 | 0.520 | 0.700 | 1 |

![Gray atmosphere: T(tau), Hopf function, limb darkening](../figures/L09_gray_atmosphere.png)

*Figure 9.1 — Left: temperature structure, Eddington versus exact. They differ only for $\tau\lesssim1$. Centre: the Hopf function from our numerical solution of Milne's equation. Right: bolometric limb darkening. The exact $H$-function law (dashed) agrees with Chandrasekhar's 1950 table (dots) to 4 decimals; the Eddington law (solid) is too bright at the limb.*

## 9.5 Numerical solution of the gray LTE problem

`scripts/lte_solvers.py → hopf_function()` solves Milne's equation directly:

1. Grid $\tau_i$ from 0 to 30 (logarithmic).
2. Build the $\Lambda$ matrix analytically (piecewise-linear $S$; Lecture 8).
3. Below $\tau_{\max}$, attach the known asymptotic form $S = \tfrac34(\tau+q_\infty)$ and treat its contribution as a known right-hand side.
4. Solve $(\mathbf1-\mathbf\Lambda)\mathbf S = \mathbf b$; then $q = \tfrac43S - \tau$.

**Results:** $q(0) = 0.5773$ (exact 0.57735), $q(1) = 0.6985$. The emergent flux, integrated over all wavelengths with $T(\tau)$ from this solution and the LTE formal solution $F_\lambda = 2\pi\int_0^\infty B_\lambda(T(\tau))E_2(\tau)d\tau$, equals $\sigma T_{\rm eff}^4$ to **0.007 %**, confirming radiative equilibrium.

## 9.6 Monochromatic properties: the spectrum of a gray LTE star

Although $\kappa$ is gray, the **spectrum is not a black body**, because each frequency samples $B_\nu(T(\tau))$ with $T$ varying with depth:
$$I_\nu(0,\mu) = \int_0^\infty B_\nu\big(T(\tau)\big)\,e^{-\tau/\mu}\frac{d\tau}{\mu},\qquad
F_\nu(0) = 2\pi\int_0^\infty B_\nu\big(T(\tau)\big)E_2(\tau)\,d\tau .$$

![Gray atmosphere spectrum and monochromatic limb darkening](../figures/L09_gray_spectrum.png)

*Figure 9.2 — Left: emergent flux of the exact gray LTE atmosphere with $T_{\rm eff} = 5772$ K compared with $\pi B_\lambda(T_{\rm eff})$. The UV excess comes from hot deep layers that shine through. Right: limb darkening is much stronger in the blue, because $B_\lambda$ is more sensitive to $T$ in the Wien regime (Lecture 3).*

| $\lambda$ | $I(0.1)/I(1)$ | $I(0.5)/I(1)$ |
|---|---|---|
| 400 nm | 0.242 | 0.569 |
| 550 nm | 0.372 | 0.672 |
| 800 nm | 0.510 | 0.761 |

## 9.7 Adding hydrostatic equilibrium: a complete model

With $dP/dz = -\rho g$ and $d\tau = -\kappa\rho\,dz$:
$$\frac{dP}{d\tau} = \frac g\kappa\quad\Rightarrow\quad P(\tau) = \frac{g}{\kappa}\tau\quad(\kappa\ \text{constant}).$$
Then $\rho = P\mu m_H/(kT)$. Together with $T(\tau)$ this gives a full **gray LTE model atmosphere**: $T(\tau)$, $P(\tau)$, $\rho(\tau)$, as functions of only $T_{\rm eff}$, $g$ and $\kappa$ (i.e. composition), exactly as Collins' five assumptions promised (Lecture 6).

**Real (non-gray) atmospheres** need iteration: guess $T(\tau)$ → Saha–Boltzmann gives $\kappa_\nu$ → solve the RTE at all $\nu$ → check $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$ and flux constancy → correct $T$ (Unsöld–Lucy correction) → repeat. The gray solution is the standard **starting model**.

---

## Worked example 9.1 — The Sun as a gray LTE atmosphere

*$T_{\rm eff} = 5772$ K. Find $T$ at $\tau = 0, 2/3, 1, 2, 10$ (Eddington), and the exact surface temperature.*

| $\tau$ | 0 | 2/3 | 1 | 2 | 10 |
|---|---|---|---|---|---|
| $T$ (Eddington) [K] | 4854 | 5772 | 6103 | 6864 | 9707 |

Exact $T(0) = 0.8114\times5772 = 4682$ K. The observed solar temperature minimum is about 4400 K (it then rises in the chromosphere, which a radiative-equilibrium model cannot reproduce). Compare Lecture 7: the limb-darkening inversion at 500 nm gave 5155 K at $\tau_{500} = 0$ and 6300 K at $\tau_{500} = 1$. The gray model is the right order of magnitude, with differences due to non-grayness (H$^-$ opacity varies with $\lambda$).

## Worked example 9.2 — Pressure at the solar photosphere

*Take $g_\odot = 274$ m s$^{-2}$ and a mean opacity $\kappa\approx0.03$ m$^2$ kg$^{-1}$. Estimate $P$ and $\rho$ at $\tau = 2/3$.*

$P = g\tau/\kappa = 274\times0.667/0.03 = 6.1\times10^3$ Pa (about 0.06 atm). With $\mu\approx1.3$ (neutral gas) and $T = 5772$ K:
$\rho = P\mu m_H/(kT) = 6.1\times10^3\times1.3\times1.67\times10^{-27}/(1.38\times10^{-23}\times5772) = 1.7\times10^{-4}$ kg m$^{-3}$.
Detailed solar models give $\rho\approx2.5\times10^{-4}$ kg m$^{-3}$ at $\tau_{500} = 1$, so the gray estimate is good to a factor of order unity.

## Worked example 9.3 — Verifying Step 1 directly

*Show that if $S = J$ and $H$ = const, then $\int_0^\infty J(t)E_2(t)dt = 2H$ (the flux from the Schwarzschild–Milne equation at $\tau = 0$), and check it for the Eddington solution.*

$F(0) = 2\pi\int_0^\infty S(t)E_2(t)dt = 4\pi H\Rightarrow\int_0^\infty SE_2\,dt = 2H$. Eddington: $S = 3H(t+2/3)$, and $\int_0^\infty tE_2dt = 1/3$, $\int_0^\infty E_2dt = E_3(0) = 1/2$. So $\int SE_2 = 3H(1/3+1/3) = 2H$ ✓. The Eddington solution satisfies the **surface** flux condition exactly, but not Milne's equation at every depth. The exact $q(\tau)$ corrects that.

---

## Exam questions and answers — Lecture 9

**Q1.** State the assumptions of the gray LTE atmosphere and derive $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$. Indicate clearly where the Eddington approximation enters.

> **A1.** Assumptions: plane-parallel, static, LTE ($S = B$), gray ($\kappa_\nu = \kappa$), radiative equilibrium with $F = \sigma T_{\rm eff}^4$. Derivation: (i) RE with gray opacity gives $J = B$; (ii) $dH/d\tau = J - B = 0\Rightarrow H = F/4\pi$; (iii) $dK/d\tau = H\Rightarrow K = H\tau + c$ (exact). **(iv) Eddington:** $K = J/3\Rightarrow J = 3H(\tau + C)$. **(v) Eddington boundary condition** $J(0) = 2H$ gives $C = 2/3$. (vi) $J = B = \sigma T^4/\pi$ and $H = \sigma T_{\rm eff}^4/4\pi$ give $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$.

**Q2.** Derive the limb-darkening law $I(\mu)/I(1) = \frac25(1+\frac32\mu)$ and verify that it gives the correct flux.

> **A2.** $S = 3H(\tau + 2/3)$ is linear, so $I(0,\mu) = S(\mu) = 3H(\mu+2/3)$, and $I(\mu)/I(1) = (\mu + 2/3)/(5/3) = (2+3\mu)/5$. Flux: $2\pi\int_0^1 3H(\mu+\frac23)\mu\,d\mu = 6\pi H(\frac13+\frac13) = 4\pi H = F$ ✓.

**Q3.** What is the Hopf function? Give $q(0)$ and $q(\infty)$, and explain how the Eddington solution approximates it.

> **A3.** The exact solution of Milne's equation is $J = 3H[\tau+q(\tau)]$, where $q$ increases monotonically from $q(0) = 1/\sqrt3 = 0.577$ (Hopf–Bronstein) to $q(\infty) = 0.7104$. Eddington replaces it by the constant $2/3 = 0.667$, which lies between the two limits; the maximum error in $T$ is 3.6 %, at the surface.

**Q4.** Explain why the emergent spectrum of a gray LTE atmosphere is not a black body at $T_{\rm eff}$, and why it shows an excess in the UV.

> **A4.** $F_\nu = 2\pi\int B_\nu(T(\tau))E_2(\tau)d\tau$ is a weighted average of Planck functions over a range of temperatures. Because $B_\nu$ is a convex, steep function of $T$ in the Wien (UV) regime, the hotter layers contribute disproportionately there, so the UV flux exceeds $\pi B_\nu(T_{\rm eff})$. Energy conservation then requires a slight deficit elsewhere. The total $\int F_\nu d\nu$ equals $\sigma T_{\rm eff}^4$ exactly.
