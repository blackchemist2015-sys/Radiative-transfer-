# Final Examination — Radiative Transfer (with complete solutions)

> **Format suggestion:** 3 hours. Part A (30 %): short answers. Part B (70 %): problems; answer any 8 of the 12. The solutions follow each question. All numbers were checked with `scripts/worked_examples.py` and the solvers in `scripts/lte_solvers.py`.
> Constants: $h = 6.626\times10^{-34}$ J s, $k = 1.381\times10^{-23}$ J K$^{-1}$, $c = 2.998\times10^8$ m s$^{-1}$, $\sigma = 5.670\times10^{-8}$ W m$^{-2}$ K$^{-4}$, $m_e = 9.109\times10^{-31}$ kg, $m_H = 1.674\times10^{-27}$ kg, $r_e = 2.818\times10^{-15}$ m, $\sigma_T = 6.652\times10^{-29}$ m$^2$, $R_\odot = 6.957\times10^8$ m, 1 pc $= 3.086\times10^{16}$ m, 1 eV $= 1.602\times10^{-19}$ J.
> $\int_0^\infty E_n(t)\,dt = \dfrac1n$, $\int_0^\infty t\,E_n(t)\,dt = \dfrac{1}{n+1}$, $E_n(0) = \dfrac1{n-1}$.

---

## Part A — Short answers (2 marks each)

**A1.** True or false: "In LTE the specific intensity equals the Planck function."
> **False.** In LTE the **source function** equals $B_\nu(T)$. $I_\nu = B_\nu$ only in full TE, or deep inside an optically thick, isothermal region.

**A2.** What is conserved along a ray in vacuum: $F_\nu$, $I_\nu$ or $J_\nu$?
> $I_\nu$ (more generally $I_\nu/\nu^3$).

**A3.** Give the source function for coherent isotropic scattering plus thermal absorption.
> $S_\nu = \varepsilon B_\nu + (1-\varepsilon)J_\nu$, with $\varepsilon = \kappa^a/(\kappa^a+\sigma^{\rm sc})$.

**A4.** At what optical depth does the emergent flux "originate" according to Eddington–Barbier?
> $\tau_\nu = 2/3$: $F_\nu(0)\approx\pi S_\nu(2/3)$.

**A5.** Why is the Rosseland mean a harmonic mean?
> The flux in each frequency band is $\propto1/\kappa_\nu$ (like conductances in parallel), so the total is dominated by low-opacity windows.

**A6.** Write the Eddington closure and the Eddington surface condition.
> $K = J/3$; $J(0) = 2H(0)$.

**A7.** What does the factor $1-e^{-h\nu/kT}$ represent?
> The LTE correction for stimulated emission (negative absorption).

**A8.** For an isothermal scattering atmosphere, what is $S(0)/B$ exactly?
> $\sqrt\varepsilon$.

**A9.** What is the exact boundary temperature of a gray atmosphere in units of $T_{\rm eff}$?
> $(\sqrt3/4)^{1/4} = 0.811$.

**A10.** Why do Balmer lines peak in A stars?
> Boltzmann excitation into $n = 2$ increases with $T$, while Saha ionisation removes neutral H above about $10^4$ K. The product peaks near 9900 K.

**A11.** What is an optically thin source's brightness temperature in terms of $T$ and $\tau$?
> $T_b = T(1-e^{-\tau})\approx T\tau$ (RJ, no background).

**A12.** Name the integral equation of the gray LTE atmosphere.
> Milne's equation, $J(\tau) = \Lambda_\tau[J] = \frac12\int_0^\infty J(t)E_1|t-\tau|dt$.

**A13.** Two stars with equal $T_{\rm eff}$ but different radii: which quantity is the same, the flux at Earth or the surface brightness?
> The surface brightness.

**A14.** Why are NLTE effects strongest in strong resonance lines?
> They form in high, low-density layers where $C\ll A$ ($\varepsilon\ll1$), and the thermalisation depth $1/\sqrt\varepsilon$ is very large.

**A15.** What does a positive $\beta$ in $B = B_0(1+\beta\tau)$ imply for limb darkening and for line formation in LTE?
> Temperature increasing inward: limb darkening, and absorption lines.

---

## Part B — Problems

### B1. Intensity and flux (8 marks)

An A-type star has $R = 1.7R_\odot$ and $T_{\rm eff} = 9900$ K and lies at $d = 2.64$ pc. (a) Find its surface flux and luminosity in $L_\odot$ ($L_\odot = 3.828\times10^{26}$ W). (b) Find the bolometric flux at Earth. (c) Show that its mean surface brightness is the same at the star and at Earth.

> **Solution.** (a) $F_s = \sigma T^4 = 5.67\times10^{-8}\times(9900)^4 = 5.45\times10^8$ W m$^{-2}$; $L = 4\pi R^2F_s = 25\,L_\odot$.
> (b) $F_\oplus = F_s(R/d)^2$, with $R = 1.18\times10^9$ m and $d = 8.15\times10^{16}$ m, so $(R/d)^2 = 2.1\times10^{-16}$ and $F_\oplus = 1.15\times10^{-7}$ W m$^{-2}$.
> (c) The mean intensity is $\bar I = F_s/\pi$. At Earth, $\bar I = F_\oplus/\Omega$ with $\Omega = \pi(R/d)^2$, giving $F_s(R/d)^2/(\pi(R/d)^2) = F_s/\pi$, the same. Intensity is conserved along rays.

### B2. Planck function (8 marks)

(a) Show that in the RJ limit $I_\nu = (2k\nu^2/c^2)T_b$. (b) A compact source has $I_\nu = 10^{-18}$ W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$ at 5 GHz. Find $T_b$. (c) If the source is an H II region with $T_e = 10^4$ K, what is its optical depth at 5 GHz? (d) Is it thick or thin at 0.5 GHz if $\tau\propto\nu^{-2.1}$?

> **Solution.** (a) $e^x-1\approx x$ gives $B_\nu\approx2h\nu^3/(c^2x) = 2\nu^2kT/c^2$; define $T_b$ by $I_\nu = B_\nu(T_b)$.
> (b) $T_b = c^2I_\nu/(2k\nu^2) = (8.99\times10^{16}\times10^{-18})/(2\times1.381\times10^{-23}\times2.5\times10^{19}) = 130$ K.
> (c) $T_b = T_e(1-e^{-\tau})\Rightarrow1-e^{-\tau} = 0.013\Rightarrow\tau = 0.013$.
> (d) $\tau(0.5\ {\rm GHz}) = 0.013\times10^{2.1} = 1.6$: marginally thick, so $T_b = 10^4(1-e^{-1.6}) = 8000$ K.

### B3. Kirchhoff's law and LTE (8 marks)

(a) Using the Einstein coefficients, write $j_\nu$ and $\alpha_\nu$ for a line. (b) Show that if the level populations obey Boltzmann's law at temperature $T$, then $S_\nu = B_\nu(T)$. (c) Explain why this result does not require $I_\nu = B_\nu$.

> **Solution.** (a) $j_\nu = \frac{h\nu}{4\pi}n_2A_{21}\phi$, $\alpha_\nu = \frac{h\nu}{4\pi}\phi(n_1B_{12}-n_2B_{21})$.
> (b) $S = \frac{n_2A_{21}}{n_1B_{12}-n_2B_{21}} = \frac{A_{21}/B_{21}}{\frac{n_1g_2}{n_2g_1}-1}$ (using $g_1B_{12} = g_2B_{21}$). Boltzmann gives $\frac{n_1g_2}{n_2g_1} = e^{h\nu/kT}$, and $A_{21}/B_{21} = 2h\nu^3/c^2$, so $S = B_\nu(T)$.
> (c) Only the **populations** (a property of the matter, set by collisions) were used. The radiation field does not appear, so $S = B$ holds whenever the matter is in LTE, whatever $I_\nu$ is.

### B4. Saha equation (8 marks)

Pure hydrogen has $n_e = 10^{20}$ m$^{-3}$. Find the ionised fraction at (a) $T = 6000$ K and (b) $T = 8000$ K. ($U_{\rm I} = 2$, $U_{\rm II} = 1$, $\chi = 13.6$ eV.)

> **Solution.** $\frac{N_{\rm II}}{N_{\rm I}} = \frac{1}{n_e}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$ (the factor $2U_{\rm II}/U_{\rm I} = 1$).
> (a) $T = 6000$ K: $(\dots)^{3/2} = 2.415\times10^{21}\times6000^{1.5} = 1.12\times10^{27}$ m$^{-3}$; $\chi/kT = 26.3$, so $e^{-26.3} = 3.8\times10^{-12}$. Ratio $= 1.12\times10^{27}\times3.8\times10^{-12}/10^{20} = 4.2\times10^{-5}$: essentially neutral.
> (b) $T = 8000$ K: $(\dots)^{3/2} = 1.73\times10^{27}$; $\chi/kT = 19.7$, so $e^{-19.7} = 2.7\times10^{-9}$. Ratio $= 0.047$; ionised fraction $= 0.045$.
> A 33 % rise in $T$ increases ionisation by a factor of about 1000: Saha ionisation is extremely sensitive to temperature.

### B5. Formal solution in a plane-parallel atmosphere (8 marks)

$S(\tau) = a + b\tau + c\tau^2$ in a semi-infinite atmosphere. (a) Find $I(0,\mu)$. (b) Find $F(0)$. (c) Compare with the Eddington–Barbier values and state when they are exact.

> **Solution.** (a) $I(0,\mu) = \int_0^\infty(a+bt+ct^2)e^{-t/\mu}dt/\mu = a+b\mu+2c\mu^2$.
> (b) $F = 2\pi\int_0^1(a+b\mu+2c\mu^2)\mu\,d\mu = 2\pi(a/2+b/3+c/2) = \pi(a+\frac23b+c)$.
> (c) E–B: $I\approx S(\mu) = a+b\mu+c\mu^2$ (error $c\mu^2$); $F\approx\pi S(2/3) = \pi(a+\frac23b+\frac49c)$ (error $\frac59\pi c$). Both are exact when $c = 0$ (linear $S$).

### B6. The gray LTE atmosphere — full derivation (12 marks)

(a) Starting from the plane-parallel RTE with $S = B$ and gray opacity, show that radiative equilibrium implies $J = B$ and $H$ = constant. (b) Using the Eddington approximation, derive $T(\tau)$. (c) For $T_{\rm eff} = 10\,000$ K, tabulate $T$ at $\tau = 0, 2/3, 1, 4$. (d) Derive the emergent intensity $I(0,\mu)$ and the limb-darkening law. (e) The exact surface temperature is $0.811\,T_{\rm eff}$. What is the percentage error of the Eddington value?

> **Solution.** (a) RE: $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$, which with $\kappa_\nu = \kappa$ gives $J = B$. The zeroth moment $dH/d\tau = J - S = J - B = 0$ gives $H$ = const $= \sigma T_{\rm eff}^4/4\pi$.
> (b) $dK/d\tau = H\Rightarrow K = H\tau+$const; $K = J/3\Rightarrow J = 3H(\tau+C)$; $J(0) = 2H\Rightarrow C = 2/3$. $J = B = \sigma T^4/\pi$ gives $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$.
> (c) $T(0) = 8409$ K, $T(2/3) = 10\,000$ K, $T(1) = 10\,574$ K, $T(4) = 13\,678$ K.
> (d) $S = 3H(\tau+2/3)$ is linear, so $I(0,\mu) = 3H(\mu+2/3) = \frac{3\sigma T_{\rm eff}^4}{4\pi}(\mu+\frac23)$, and $I(\mu)/I(1) = (2+3\mu)/5$.
> (e) $(0.841-0.811)/0.811 = 3.7\,\%$.

### B7. Testing the Eddington solution with the $\Lambda$ operator (8 marks)

For the Eddington gray solution $S(\tau) = 3H(\tau+\frac23)$, compute $J(0) = \Lambda_0[S] = \frac12\int_0^\infty S(t)E_1(t)dt$. Compare with $S(0)$ and with the exact (Hopf–Bronstein) value $J(0) = \sqrt3H$. What does this tell you?

> **Solution.** $J(0) = \frac{3H}{2}\left[\int_0^\infty tE_1dt+\frac23\int_0^\infty E_1dt\right] = \frac{3H}{2}\left[\frac12+\frac23\right] = \frac74H = 1.750\,H$. But $S(0) = 2H$, so $\Lambda[S]\neq S$: the Eddington solution does **not** satisfy Milne's equation exactly ($J\neq S$ at the surface). The exact value $\sqrt3H = 1.732H$ is close to the result of one $\Lambda$-iteration (1.750H), which shows that $\Lambda$-iteration improves the solution near the surface, where it couples to the boundary.

### B8. Two-stream (Schuster–Schwarzschild) gray atmosphere (10 marks)

Represent the radiation field by two streams, $I^+$ at $\mu = +1/\sqrt3$ and $I^-$ at $\mu = -1/\sqrt3$, so that $J = \frac12(I^++I^-)$, $H = \frac{1}{2\sqrt3}(I^+-I^-)$, $K = \frac16(I^++I^-)$. (a) Show that $K = J/3$ exactly. (b) With $I^-(0) = 0$, show $J(0) = \sqrt3H$. (c) Hence derive $T^4 = \frac34T_{\rm eff}^4(\tau+1/\sqrt3)$ and compare $T(0)$ with the exact result.

> **Solution.** (a) $K = \frac12\sum\mu_i^2I_i = \frac12\cdot\frac13(I^++I^-) = J/3$.
> (b) $J(0) = I^+/2$ and $H(0) = I^+/(2\sqrt3)$, so $J(0) = \sqrt3H(0)$.
> (c) As in B6: $J = 3H(\tau+C)$ with $3HC = \sqrt3H\Rightarrow C = 1/\sqrt3$. So $T^4 = \frac34T_{\rm eff}^4(\tau+0.577)$ and $T(0) = (\sqrt3/4)^{1/4}T_{\rm eff} = 0.811\,T_{\rm eff}$, which is **exactly the true surface value**. This is Chandrasekhar's "first approximation" of the discrete-ordinate method; it gives $J(0)$ exactly in every order (Chandrasekhar eq. 64), while $q(\infty)$ improves with the order.

### B9. Limb darkening and LTE temperature structure (8 marks)

At $\lambda = 500$ nm, the observed solar limb darkening is $I(\mu) = I(1)(0.36+0.64\mu)$ with $I(1) = 4.0\times10^{13}$ W m$^{-3}$ sr$^{-1}$. Assuming LTE and the Eddington–Barbier relation, find $T(\tau_{500} = 0)$ and $T(\tau_{500} = 1)$. Comment.

> **Solution.** $S(\tau) = I(1)(0.36+0.64\tau)$, and LTE gives $S = B_\lambda(T)$, so $T = (hc/\lambda k)/\ln(1+2hc^2/(\lambda^5B))$, with $hc/\lambda k = 28\,776$ K and $2hc^2/\lambda^5 = 3.811\times10^{15}$. $\tau = 0$: $B = 1.44\times10^{13}$, so $T = 28776/\ln(265.7) = 5155$ K. $\tau = 1$: $B = 4.0\times10^{13}$, so $T = 28776/\ln(96.3) = 6300$ K. The temperature rises inward by about 1100 K per unit optical depth, which is why the Sun shows limb darkening and absorption lines. The values bracket $T_{\rm eff} = 5772$ K, consistent with the gray model (Lecture 9).

### B10. Scattering and thermalisation (10 marks)

An isothermal atmosphere has $S = \varepsilon B+(1-\varepsilon)J$. (a) In the Eddington approximation, derive the differential equation for $J$ and solve it with the appropriate boundary conditions. (b) For $\varepsilon = 10^{-2}$, find $S(0)/B$ (Eddington) and compare with the exact value. (c) Estimate the thermalisation depth and the number of scatterings a photon undergoes before destruction. (d) Why does $\Lambda$-iteration starting from $S = B$ converge so slowly?

> **Solution.** (a) $dH/d\tau = J - S = \varepsilon(J-B)$ and $H = \frac13dJ/d\tau$, so $\frac13J'' = \varepsilon(J-B)$. Then $J = B+Ce^{-\sqrt{3\varepsilon}\tau}$; with $J(0) = \frac23J'(0)$, $C = -B/(1+2\sqrt{\varepsilon/3})$.
> (b) $\sqrt{\varepsilon/3} = 0.0577$, so $J(0)/B = 1-1/1.1155 = 0.1035$ and $S(0)/B = 0.01+0.99\times0.1035 = 0.1125$. The exact value is $\sqrt\varepsilon = 0.100$; Eddington overestimates by 12 %.
> (c) $\tau_{\rm th}\sim1/\sqrt\varepsilon = 10$ (Eddington: $1/\sqrt{3\varepsilon} = 5.8$); $N\sim1/\varepsilon = 100$ scatterings.
> (d) Each iteration transmits information only about $\Delta\tau\sim1$, and the error decreases by a factor $(1-\varepsilon) = 0.99$ per step, so hundreds of iterations are needed (see Figure 8.1). Our solver gives $S(0)$ errors of 95 % after 10 iterations, 17 % after 50, 5 % after 100 and 0.9 % after 200; yet beyond 100 iterations each step changes $S(0)$ by less than 0.1 %, so a naive convergence test would stop far too early.

### B11. Milne–Eddington line in LTE (10 marks)

In an LTE atmosphere $B_\nu = B_0(1+\beta\tau_c)$, and a line has a constant ratio $\eta_\nu = \eta_0e^{-v^2}$ of line to continuum opacity. (a) Derive $F_\nu/F_c$. (b) For $\beta = 3$, find the central depth for $\eta_0 = 0.1$, $1$, $\infty$. (c) Show that for weak lines the equivalent width is proportional to $\eta_0$, and find the constant (in units of $\Delta\nu_D$).

> **Solution.** (a) $\tau_\nu = (1+\eta_\nu)\tau_c$, so $B$ is linear in $\tau_\nu$ and E–B is exact: $r = \frac{1+2\beta/[3(1+\eta)]}{1+2\beta/3}$.
> (b) $\beta = 3$: $1+2\beta/3 = 3$. $\eta_0 = 0.1$: $r = (1+2/1.1)/3 = 0.939$, depth 0.061. $\eta_0 = 1$: $r = 2/3$, depth 0.333. $\eta_0\to\infty$: $r = 1/3$, depth 0.667.
> (c) For $\eta\ll1$: $1-r\approx\frac{2\beta/3}{1+2\beta/3}\eta_\nu$, so $W/\Delta\nu_D = \int(1-r)dv = \frac{2\beta/3}{1+2\beta/3}\eta_0\sqrt\pi$. For $\beta = 3$: $W/\Delta\nu_D = \frac23\sqrt\pi\,\eta_0 = 1.18\,\eta_0$.

### B12. Diffusion and Rosseland mean (8 marks)

(a) From $I\approx B+\mu\,dB/d\tau$, derive $F = \frac{4\pi}{3}\frac{dB}{d\tau}$. (b) A gas has three frequency bands carrying 50 %, 30 % and 20 % of $\partial B/\partial T$, with $\kappa = 1$, $10$ and $1000$ (arbitrary units). Find the Rosseland and Planck means. (c) Which mean controls the energy flux in a stellar interior, and why?

> **Solution.** (a) $F = 2\pi\int_{-1}^1(B+\mu B')\mu\,d\mu = 2\pi B'\cdot\frac23 = \frac{4\pi}{3}B'$.
> (b) $1/\kappa_R = 0.5/1+0.3/10+0.2/1000 = 0.5302\Rightarrow\kappa_R = 1.89$. $\kappa_P = 0.5+3+200 = 203.5$.
> (c) The Rosseland mean, because the flux is $\propto\sum(1/\kappa_\nu)$: radiation leaks through the most transparent band, so $\kappa_R\approx2\times$ the window opacity, while the Planck mean is dominated by the most opaque band.

---

## Part C — Essay question (choose one, 10 marks)

**C1.** "Local thermodynamic equilibrium is a statement about matter, not about radiation." Discuss, with reference to Kirchhoff's law, the two-level atom and the thermalisation depth.

> **Model answer outline.** (1) Define TE and LTE; Maxwell, Boltzmann and Saha at the local $T$. (2) Kirchhoff: $j = \alpha B$ depends only on the matter state, hence $S = B$ in LTE while $I\neq B$ (escape at the surface; $I(0,\mu<0) = 0$; $J(0)\approx B/2$). (3) Validity: collisions must dominate radiative rates; two-level atom $S = (1-\varepsilon)\bar J+\varepsilon B$, so LTE when $\varepsilon\to1$. (4) Even with $\varepsilon$ close to but below 1, $S$ deviates from $B$ within $\tau\sim1/\sqrt\varepsilon$ of the surface, with $S(0) = \sqrt\varepsilon B$. (5) Consequences: LTE is good for continua and weak lines in dwarf photospheres; it fails for strong lines, chromospheres, hot or low-density stars and nebulae. (6) Practical: LTE turns the RTE into an explicit formal solution once $T(\tau)$ is known; NLTE requires solving rate equations coupled to the radiation field (ALI).

**C2.** Describe how a model stellar atmosphere is computed, starting from the gray LTE solution, and how its predictions are compared with observations.

> **Model answer outline.** Inputs $T_{\rm eff}$, $\log g$, composition → gray starting $T(\tau) = [\frac34T_{\rm eff}^4(\tau+q)]^{1/4}$ → hydrostatic $P(\tau)$ from $dP/d\tau = g/\kappa$ → Saha–Boltzmann populations → $\kappa_\nu,\ j_\nu$ → solve the RTE at many frequencies (formal solution, or Feautrier/ALI with scattering) → check radiative equilibrium $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$ and constant flux → temperature correction (Unsöld–Lucy) → iterate to convergence → emergent spectrum, limb darkening, line profiles (Milne–Eddington intuition, curve of growth) → compare with observed spectra, colours, Balmer jump and line equivalent widths → derive $T_{\rm eff}$, $g$ and abundances.
