# Final Examination — Course A: Radiative Transfer (with complete solutions)

> **Format suggestion:** 3 hours. Part A (20 %): short answers. Part B (50 %): answer any 6 of the 8 problems. Part C (20 %): RT6, RT9 and RT10 topics. Part E (10 %): essay. Solutions follow each question; numbers were checked with `scripts/worked_examples.py` and `scripts/lte_solvers.py`.
> Constants: $h = 6.626\times10^{-34}$ J s, $k = 1.381\times10^{-23}$ J K$^{-1}$, $c = 2.998\times10^8$ m s$^{-1}$, $\sigma = 5.670\times10^{-8}$ W m$^{-2}$ K$^{-4}$, $m_e = 9.109\times10^{-31}$ kg, $m_H = 1.674\times10^{-27}$ kg, $r_e = 2.818\times10^{-15}$ m, $\sigma_T = 6.652\times10^{-29}$ m$^2$, $R_\odot = 6.957\times10^8$ m, 1 pc $= 3.086\times10^{16}$ m, 1 eV $= 1.602\times10^{-19}$ J.
> $\int_0^\infty E_n(t)\,dt = \dfrac1n$, $\int_0^\infty t\,E_n(t)\,dt = \dfrac{1}{n+1}$, $E_n(0) = \dfrac1{n-1}$.

---

## Part A — Short answers (2 marks each)

**A1.** What is conserved along a ray in vacuum: $F_\nu$, $I_\nu$ or $J_\nu$?

> $I_\nu$ (more generally $I_\nu/\nu^3$).

**A2.** Give the source function for coherent isotropic scattering plus thermal absorption.

> $S_\nu = \varepsilon B_\nu + (1-\varepsilon)J_\nu$, with $\varepsilon = \kappa^a/(\kappa^a+\sigma^{\rm sc})$.

**A3.** At what optical depth does the emergent flux "originate" according to Eddington–Barbier?

> $\tau_\nu = 2/3$: $F_\nu(0)\approx\pi S_\nu(2/3)$.

**A4.** Why is the Rosseland mean a harmonic mean?

> The flux in each frequency band is $\propto1/\kappa_\nu$ (like conductances in parallel), so the total is dominated by low-opacity windows.

**A5.** Write the Eddington closure and the Eddington surface condition.

> $K = J/3$; $J(0) = 2H(0)$.

**A6.** What does the factor $1-e^{-h\nu/kT}$ represent?

> The LTE correction for stimulated emission (negative absorption).

**A7.** For an isothermal scattering atmosphere, what is $S(0)/B$ exactly?

> $\sqrt\varepsilon$.

**A8.** What is an optically thin source's brightness temperature in terms of $T$ and $\tau$?

> $T_b = T(1-e^{-\tau})\approx T\tau$ (RJ, no background).

**A9.** Two stars with equal $T_{\rm eff}$ but different radii: which quantity is the same, the flux at Earth or the surface brightness?

> The surface brightness.

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

### B3. Formal solution in a plane-parallel atmosphere (8 marks)

$S(\tau) = a + b\tau + c\tau^2$ in a semi-infinite atmosphere. (a) Find $I(0,\mu)$. (b) Find $F(0)$. (c) Compare with the Eddington–Barbier values and state when they are exact.

> **Solution.** (a) $I(0,\mu) = \int_0^\infty(a+bt+ct^2)e^{-t/\mu}dt/\mu = a+b\mu+2c\mu^2$.
> (b) $F = 2\pi\int_0^1(a+b\mu+2c\mu^2)\mu\,d\mu = 2\pi(a/2+b/3+c/2) = \pi(a+\frac23b+c)$.
> (c) E–B: $I\approx S(\mu) = a+b\mu+c\mu^2$ (error $c\mu^2$); $F\approx\pi S(2/3) = \pi(a+\frac23b+\frac49c)$ (error $\frac59\pi c$). Both are exact when $c = 0$ (linear $S$).

### B4. Testing the Eddington solution with the $\Lambda$ operator (8 marks)

For the Eddington gray solution $S(\tau) = 3H(\tau+\frac23)$, compute $J(0) = \Lambda_0[S] = \frac12\int_0^\infty S(t)E_1(t)dt$. Compare with $S(0)$ and with the exact (Hopf–Bronstein) value $J(0) = \sqrt3H$. What does this tell you?

> **Solution.** $J(0) = \frac{3H}{2}\left[\int_0^\infty tE_1dt+\frac23\int_0^\infty E_1dt\right] = \frac{3H}{2}\left[\frac12+\frac23\right] = \frac74H = 1.750\,H$. But $S(0) = 2H$, so $\Lambda[S]\neq S$: the Eddington solution does **not** satisfy Milne's equation exactly ($J\neq S$ at the surface). The exact value $\sqrt3H = 1.732H$ is close to the result of one $\Lambda$-iteration (1.750H), which shows that $\Lambda$-iteration improves the solution near the surface, where it couples to the boundary.

### B5. Two-stream (Schuster–Schwarzschild) gray atmosphere (10 marks)

Represent the radiation field by two streams, $I^+$ at $\mu = +1/\sqrt3$ and $I^-$ at $\mu = -1/\sqrt3$, so that $J = \frac12(I^++I^-)$, $H = \frac{1}{2\sqrt3}(I^+-I^-)$, $K = \frac16(I^++I^-)$. (a) Show that $K = J/3$ exactly. (b) With $I^-(0) = 0$, show $J(0) = \sqrt3H$. (c) Hence derive $T^4 = \frac34T_{\rm eff}^4(\tau+1/\sqrt3)$ and compare $T(0)$ with the exact result.

> **Solution.** (a) $K = \frac12\sum\mu_i^2I_i = \frac12\cdot\frac13(I^++I^-) = J/3$.
> (b) $J(0) = I^+/2$ and $H(0) = I^+/(2\sqrt3)$, so $J(0) = \sqrt3H(0)$.
> (c) As in B6: $J = 3H(\tau+C)$ with $3HC = \sqrt3H\Rightarrow C = 1/\sqrt3$. So $T^4 = \frac34T_{\rm eff}^4(\tau+0.577)$ and $T(0) = (\sqrt3/4)^{1/4}T_{\rm eff} = 0.811\,T_{\rm eff}$, which is **exactly the true surface value**. This is Chandrasekhar's "first approximation" of the discrete-ordinate method; it gives $J(0)$ exactly in every order (Chandrasekhar eq. 64), while $q(\infty)$ improves with the order.

### B6. Limb darkening and LTE temperature structure (8 marks)

At $\lambda = 500$ nm, the observed solar limb darkening is $I(\mu) = I(1)(0.36+0.64\mu)$ with $I(1) = 4.0\times10^{13}$ W m$^{-3}$ sr$^{-1}$. Assuming LTE and the Eddington–Barbier relation, find $T(\tau_{500} = 0)$ and $T(\tau_{500} = 1)$. Comment.

> **Solution.** $S(\tau) = I(1)(0.36+0.64\tau)$, and LTE gives $S = B_\lambda(T)$, so $T = (hc/\lambda k)/\ln(1+2hc^2/(\lambda^5B))$, with $hc/\lambda k = 28\,776$ K and $2hc^2/\lambda^5 = 3.811\times10^{15}$. $\tau = 0$: $B = 1.44\times10^{13}$, so $T = 28776/\ln(265.7) = 5155$ K. $\tau = 1$: $B = 4.0\times10^{13}$, so $T = 28776/\ln(96.3) = 6300$ K. The temperature rises inward by about 1100 K per unit optical depth, which is why the Sun shows limb darkening and absorption lines. The values bracket $T_{\rm eff} = 5772$ K, consistent with the gray model (Lecture SA5).

### B7. Scattering and thermalisation (10 marks)

An isothermal atmosphere has $S = \varepsilon B+(1-\varepsilon)J$. (a) In the Eddington approximation, derive the differential equation for $J$ and solve it with the appropriate boundary conditions. (b) For $\varepsilon = 10^{-2}$, find $S(0)/B$ (Eddington) and compare with the exact value. (c) Estimate the thermalisation depth and the number of scatterings a photon undergoes before destruction. (d) Why does $\Lambda$-iteration starting from $S = B$ converge so slowly?

> **Solution.** (a) $dH/d\tau = J - S = \varepsilon(J-B)$ and $H = \frac13dJ/d\tau$, so $\frac13J'' = \varepsilon(J-B)$. Then $J = B+Ce^{-\sqrt{3\varepsilon}\tau}$; with $J(0) = \frac23J'(0)$, $C = -B/(1+2\sqrt{\varepsilon/3})$.
> (b) $\sqrt{\varepsilon/3} = 0.0577$, so $J(0)/B = 1-1/1.1155 = 0.1035$ and $S(0)/B = 0.01+0.99\times0.1035 = 0.1125$. The exact value is $\sqrt\varepsilon = 0.100$; Eddington overestimates by 12 %.
> (c) $\tau_{\rm th}\sim1/\sqrt\varepsilon = 10$ (Eddington: $1/\sqrt{3\varepsilon} = 5.8$); $N\sim1/\varepsilon = 100$ scatterings.
> (d) Each iteration transmits information only about $\Delta\tau\sim1$, and the error decreases by a factor $(1-\varepsilon) = 0.99$ per step, so hundreds of iterations are needed (see Figure 8.1). Our solver gives $S(0)$ errors of 95 % after 10 iterations, 17 % after 50, 5 % after 100 and 0.9 % after 200; yet beyond 100 iterations each step changes $S(0)$ by less than 0.1 %, so a naive convergence test would stop far too early.

### B8. Diffusion and Rosseland mean (8 marks)

(a) From $I\approx B+\mu\,dB/d\tau$, derive $F = \frac{4\pi}{3}\frac{dB}{d\tau}$. (b) A gas has three frequency bands carrying 50 %, 30 % and 20 % of $\partial B/\partial T$, with $\kappa = 1$, $10$ and $1000$ (arbitrary units). Find the Rosseland and Planck means. (c) Which mean controls the energy flux in a stellar interior, and why?

> **Solution.** (a) $F = 2\pi\int_{-1}^1(B+\mu B')\mu\,d\mu = 2\pi B'\cdot\frac23 = \frac{4\pi}{3}B'$.
> (b) $1/\kappa_R = 0.5/1+0.3/10+0.2/1000 = 0.5302\Rightarrow\kappa_R = 1.89$. $\kappa_P = 0.5+3+200 = 203.5$.
> (c) The Rosseland mean, because the flux is $\propto\sum(1/\kappa_\nu)$: radiation leaks through the most transparent band, so $\kappa_R\approx2\times$ the window opacity, while the Planck mean is dominated by the most opaque band.

---

## Part C — Formation of the RTE, polarization, history (4 marks each)

**C1.** (Lecture RT6) Show how the term $\frac{1-\mu^2}{r}\frac{\partial I}{\partial\mu}$ arises in the spherical RTE, and state when it may be neglected.

> **Solution.** Along a straight ray with impact parameter $p$: $r^2 = p^2+z^2$, $\mu = z/r$, so $dr/dz = \mu$ and $d\mu/dz = (1-\mu^2)/r$. Then $dI/dz = \mu\,\partial_rI+\frac{1-\mu^2}{r}\partial_\mu I$. The term describes the change of a ray's angle to the local vertical. It is negligible when the atmosphere is thin compared with $r$ (about $10H\ll R$), e.g. the Sun.

**C2.** (Lecture RT10) Schwarzschild (1906) used two streams at $\mu = \pm\frac12$ and found $T^4 = \frac12T_{\rm eff}^4(1+2\tau)$. Derive the corresponding limb-darkening law and compare $I(0)/I(1)$ with the exact gray value 0.344.

> **Solution.** $S\propto1+2\tau$ is linear, so Eddington–Barbier is exact: $I(0,\mu)\propto1+2\mu$ and $I(\mu)/I(1) = (1+2\mu)/3$. At the limb, $I(0)/I(1) = 1/3 = 0.333$, only 3 % below the exact 0.344 (Eddington's approximation gives 0.400).

**C3.** (Lecture RT9) Light is measured through filters: $I_1 = 0.55$, $I_2 = 0.45$, $I_{1'} = 0.50$, $I_{2'} = 0.50$, $I_+ = 0.52$, $I_- = 0.48$ (units of the total). Find $p$, $p_L$ and $p_V$. Which physical process could produce circular polarization in a stellar line?

> **Solution.** $I = 1$, $Q = 0.10$, $U = 0$, $V = 0.04$. Then $p = \sqrt{0.01+0.0016} = 0.108$, $p_L = 0.10$, $p_V = 0.04$. Circular polarization in a spectral line comes from the Zeeman effect with a magnetic field component along the line of sight ($V\propto B\cos\gamma\,\partial I/\partial\lambda$ in the weak-field limit).

---

## Part E — Essay (10 marks)

**E1.** Starting from photon conservation, explain how the radiative transfer equation is derived, which assumptions lead to its plane-parallel static form, and how the main historical approximations (two-stream, Eddington, diffusion) and exact methods (Hopf, Chandrasekhar) solve it.

> **Model answer outline.** (1) Photon distribution $f$, $I_\nu = (h^4\nu^3/c^2)f$; Boltzmann equation; gains and losses (absorption with stimulated emission, emission, scattering out and in with redistribution function). (2) Assumptions: static, straight rays, plane-parallel, so $\mu\,dI/d\tau = I-S$. (3) Formal solution and Schwarzschild–Milne equations; scattering makes the problem an integral equation. (4) Approximations: two-stream (Schuster, Schwarzschild 1906: $T^4 = \frac12T_{\rm eff}^4(1+2\tau)$), Eddington $K = J/3$, $J(0) = 2H$, diffusion and Rosseland mean deep inside. (5) Exact: Hopf $q(\tau)$, Chandrasekhar's discrete ordinates and $H$-functions (limb darkening 0.344 at the limb). (6) Numerical era: Feautrier, Λ-iteration and its failure, ALI, short characteristics, Monte Carlo.
