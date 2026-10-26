# Final Examination — Course B: Stellar Atmospheres (with complete solutions)

> **Format suggestion:** 3 hours. Part A (20 %): short answers. Part B (50 %): answer any 6 of the 8 problems. Part C (15 %): one essay. Part D (15 %): classification. Solutions follow each question; numbers were checked with `scripts/lte_solvers.py` and `scripts/sa_physics.py`.
> Constants: $h = 6.626\times10^{-34}$ J s, $k = 1.381\times10^{-23}$ J K$^{-1}$, $c = 2.998\times10^8$ m s$^{-1}$, $\sigma = 5.670\times10^{-8}$ W m$^{-2}$ K$^{-4}$, $m_e = 9.109\times10^{-31}$ kg, $m_H = 1.674\times10^{-27}$ kg, $r_e = 2.818\times10^{-15}$ m, $\sigma_T = 6.652\times10^{-29}$ m$^2$, $R_\odot = 6.957\times10^8$ m, 1 pc $= 3.086\times10^{16}$ m, 1 eV $= 1.602\times10^{-19}$ J.
> $\int_0^\infty E_n(t)\,dt = \dfrac1n$, $\int_0^\infty t\,E_n(t)\,dt = \dfrac{1}{n+1}$, $E_n(0) = \dfrac1{n-1}$.

---

## Part A — Short answers (2 marks each)

**A1.** True or false: "In LTE the specific intensity equals the Planck function."

> **False.** In LTE the **source function** equals $B_\nu(T)$. $I_\nu = B_\nu$ only in full TE, or deep inside an optically thick, isothermal region.

**A2.** What is the exact boundary temperature of a gray atmosphere in units of $T_{\rm eff}$?

> $(\sqrt3/4)^{1/4} = 0.811$.

**A3.** Why do Balmer lines peak in A stars?

> Boltzmann excitation into $n = 2$ increases with $T$, while Saha ionisation removes neutral H above about $10^4$ K. The product peaks near 9900 K.

**A4.** Name the integral equation of the gray LTE atmosphere.

> Milne's equation, $J(\tau) = \Lambda_\tau[J] = \frac12\int_0^\infty J(t)E_1|t-\tau|dt$.

**A5.** Why are NLTE effects strongest in strong resonance lines?

> They form in high, low-density layers where $C\ll A$ ($\varepsilon\ll1$), and the thermalisation depth $1/\sqrt\varepsilon$ is very large.

**A6.** What does a positive $\beta$ in $B = B_0(1+\beta\tau)$ imply for limb darkening and for line formation in LTE?

> Temperature increasing inward: limb darkening, and absorption lines.

**A7.** What is the threshold wavelength of H$^-$ bound–free absorption, and why?

> 1.64 µm: the extra electron is bound by only 0.754 eV, and $\lambda = hc/0.754\,{\rm eV}$.

**A8.** Write the Klein–Rosseland relation between collisional excitation and de-excitation.

> $q_{lu}/q_{ul} = (g_u/g_l)\,e^{-\Delta E/kT}$.

**A9.** In the coronal approximation, how does the upper-level population scale with electron density?

> $n_u/n_l = n_eq_{lu}/A_{ul}\propto n_e$ (far below the Boltzmann value).

**A10.** Which part of a Voigt profile measures pressure, and what is its asymptotic form?

> The far wings: $H(a,v)\approx a/(\sqrt\pi v^2)$, with $a\propto\gamma$, which grows with the perturber density.

---

## Part B — Problems

### B1. Kirchhoff's law and LTE (8 marks)

(a) Using the Einstein coefficients, write $j_\nu$ and $\alpha_\nu$ for a line. (b) Show that if the level populations obey Boltzmann's law at temperature $T$, then $S_\nu = B_\nu(T)$. (c) Explain why this result does not require $I_\nu = B_\nu$.

> **Solution.** (a) $j_\nu = \frac{h\nu}{4\pi}n_2A_{21}\phi$, $\alpha_\nu = \frac{h\nu}{4\pi}\phi(n_1B_{12}-n_2B_{21})$.
> (b) $S = \frac{n_2A_{21}}{n_1B_{12}-n_2B_{21}} = \frac{A_{21}/B_{21}}{\frac{n_1g_2}{n_2g_1}-1}$ (using $g_1B_{12} = g_2B_{21}$). Boltzmann gives $\frac{n_1g_2}{n_2g_1} = e^{h\nu/kT}$, and $A_{21}/B_{21} = 2h\nu^3/c^2$, so $S = B_\nu(T)$.
> (c) Only the **populations** (a property of the matter, set by collisions) were used. The radiation field does not appear, so $S = B$ holds whenever the matter is in LTE, whatever $I_\nu$ is.

### B2. Saha equation (8 marks)

Pure hydrogen has $n_e = 10^{20}$ m$^{-3}$. Find the ionised fraction at (a) $T = 6000$ K and (b) $T = 8000$ K. ($U_{\rm I} = 2$, $U_{\rm II} = 1$, $\chi = 13.6$ eV.)

> **Solution.** $\frac{N_{\rm II}}{N_{\rm I}} = \frac{1}{n_e}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$ (the factor $2U_{\rm II}/U_{\rm I} = 1$).
> (a) $T = 6000$ K: $(\dots)^{3/2} = 2.415\times10^{21}\times6000^{1.5} = 1.12\times10^{27}$ m$^{-3}$; $\chi/kT = 26.3$, so $e^{-26.3} = 3.8\times10^{-12}$. Ratio $= 1.12\times10^{27}\times3.8\times10^{-12}/10^{20} = 4.2\times10^{-5}$: essentially neutral.
> (b) $T = 8000$ K: $(\dots)^{3/2} = 1.73\times10^{27}$; $\chi/kT = 19.7$, so $e^{-19.7} = 2.7\times10^{-9}$. Ratio $= 0.047$; ionised fraction $= 0.045$.
> A 33 % rise in $T$ increases ionisation by a factor of about 1000: Saha ionisation is extremely sensitive to temperature.

### B3. The gray LTE atmosphere — full derivation (12 marks)

(a) Starting from the plane-parallel RTE with $S = B$ and gray opacity, show that radiative equilibrium implies $J = B$ and $H$ = constant. (b) Using the Eddington approximation, derive $T(\tau)$. (c) For $T_{\rm eff} = 10\,000$ K, tabulate $T$ at $\tau = 0, 2/3, 1, 4$. (d) Derive the emergent intensity $I(0,\mu)$ and the limb-darkening law. (e) The exact surface temperature is $0.811\,T_{\rm eff}$. What is the percentage error of the Eddington value?

> **Solution.** (a) RE: $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$, which with $\kappa_\nu = \kappa$ gives $J = B$. The zeroth moment $dH/d\tau = J - S = J - B = 0$ gives $H$ = const $= \sigma T_{\rm eff}^4/4\pi$.
> (b) $dK/d\tau = H\Rightarrow K = H\tau+$const; $K = J/3\Rightarrow J = 3H(\tau+C)$; $J(0) = 2H\Rightarrow C = 2/3$. $J = B = \sigma T^4/\pi$ gives $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$.
> (c) $T(0) = 8409$ K, $T(2/3) = 10\,000$ K, $T(1) = 10\,574$ K, $T(4) = 13\,678$ K.
> (d) $S = 3H(\tau+2/3)$ is linear, so $I(0,\mu) = 3H(\mu+2/3) = \frac{3\sigma T_{\rm eff}^4}{4\pi}(\mu+\frac23)$, and $I(\mu)/I(1) = (2+3\mu)/5$.
> (e) $(0.841-0.811)/0.811 = 3.7\,\%$.

### B4. Milne–Eddington line in LTE (10 marks)

In an LTE atmosphere $B_\nu = B_0(1+\beta\tau_c)$, and a line has a constant ratio $\eta_\nu = \eta_0e^{-v^2}$ of line to continuum opacity. (a) Derive $F_\nu/F_c$. (b) For $\beta = 3$, find the central depth for $\eta_0 = 0.1$, $1$, $\infty$. (c) Show that for weak lines the equivalent width is proportional to $\eta_0$, and find the constant (in units of $\Delta\nu_D$).

> **Solution.** (a) $\tau_\nu = (1+\eta_\nu)\tau_c$, so $B$ is linear in $\tau_\nu$ and E–B is exact: $r = \frac{1+2\beta/[3(1+\eta)]}{1+2\beta/3}$.
> (b) $\beta = 3$: $1+2\beta/3 = 3$. $\eta_0 = 0.1$: $r = (1+2/1.1)/3 = 0.939$, depth 0.061. $\eta_0 = 1$: $r = 2/3$, depth 0.333. $\eta_0\to\infty$: $r = 1/3$, depth 0.667.
> (c) For $\eta\ll1$: $1-r\approx\frac{2\beta/3}{1+2\beta/3}\eta_\nu$, so $W/\Delta\nu_D = \int(1-r)dv = \frac{2\beta/3}{1+2\beta/3}\eta_0\sqrt\pi$. For $\beta = 3$: $W/\Delta\nu_D = \frac23\sqrt\pi\,\eta_0 = 1.18\,\eta_0$.

### B5. Hydrogen bound–free opacity and the Balmer jump (8 marks)

(a) Compute Kramers' cross-section ($g_{\rm bf} = 1$) at the Balmer edge. (b) Give the wavelengths of the Paschen and Brackett edges. (c) Explain why the Balmer jump is large in A stars and small in the Sun.

> **Solution.** (a) $\nu_2 = 3.288\times10^{15}/4 = 8.22\times10^{14}$ Hz; $\sigma = 2.815\times10^{29}/(2^5\nu_2^3)$ cm$^2 = 1.6\times10^{-17}$ cm$^2 = 1.6\times10^{-21}$ m$^2$. (b) $\lambda_n = 91.13\,n^2$ nm: Paschen 820 nm, Brackett 1458 nm. (c) Near 9000–10 000 K, hydrogen bound–free from $n = 2$ dominates the continuum; blueward of 364.7 nm the opacity jumps by a factor of about 26, we see higher and cooler layers, and the flux drops. In the Sun H$^-$ dominates by a factor of about 100 and has no edge at 364.7 nm, so the hydrogen jump is diluted.

### B6. The negative hydrogen ion (8 marks)

Using Saha's equation with $\chi = 0.754$ eV, $U({\rm H^-}) = 1$, $U({\rm H\,I}) = 2$, compute $n({\rm H^-})/n({\rm H\,I})$ for $n_e = 10^{19}$ m$^{-3}$ at (a) 6000 K and (b) 5000 K. Explain the trend and why metal-poor stars have less H$^-$ opacity.

> **Solution.** $n({\rm H^-})/n({\rm H\,I}) = n_e\big/\left[4(2\pi m_ekT/h^2)^{3/2}e^{-0.754\,{\rm eV}/kT}\right]$. (a) 6000 K: $(\dots)^{3/2} = 1.12\times10^{27}$ m$^{-3}$, $e^{-1.458} = 0.233$, ratio $= 9.6\times10^{-9}$. (b) 5000 K: $8.5\times10^{26}$, $e^{-1.750} = 0.174$, ratio $= 1.7\times10^{-8}$. At fixed $n_e$, cooler gas holds more H$^-$ (the weak binding is less easily broken). In a real atmosphere, however, $n_e$ itself falls steeply with $T$. Since the electrons come from metals, metal-poor stars have lower $n_e$, hence less H$^-$ and lower opacity.

### B7. Transition rates and critical density (10 marks)

A forbidden line has $A_{ul} = 0.01$ s$^{-1}$, $\Omega = 1$, $g_u = 3$, at $T = 8000$ K. (a) Compute $q_{ul}$ and $n_{\rm crit}$. (b) Find $(n_u/n_l)/(n_u/n_l)_{\rm LTE}$ at $n_e = 10^{10}$ m$^{-3}$. (c) Show that in the coronal limit the ionisation balance is independent of density.

> **Solution.** (a) $q_{ul} = 8.629\times10^{-12}\Omega/(g_u\sqrt T) = 8.629\times10^{-12}/(3\times89.4) = 3.2\times10^{-14}$ m$^3$ s$^{-1}$; $n_{\rm crit} = A/q_{ul} = 3.1\times10^{11}$ m$^{-3}$. (b) With $x = n_e/n_{\rm crit} = 0.032$, the ratio is $x/(1+x) = 0.031$: the upper level holds 3 % of its LTE population. (c) Coronal limit: $n_in_eq_{\rm ion}(T) = n_{i+1}n_e\alpha_{\rm rec}(T)$; $n_e$ cancels, so $n_{i+1}/n_i = q_{\rm ion}/\alpha_{\rm rec}$ depends only on $T$.

### B8. Broadening of the Na D line (8 marks)

For Na I D at 589 nm in the solar photosphere, take $T = 5772$ K, $m = 23$ u, $\xi = 1$ km s$^{-1}$ and total damping $\gamma = 1.5\times10^9$ s$^{-1}$. Compute (a) the Doppler width in mÅ, (b) the damping parameter $a$, (c) the distance from line centre (in mÅ) where the Lorentzian wing equals the Gaussian core.

> **Solution.** (a) $v_D = \sqrt{2kT/m+\xi^2} = \sqrt{4.17\times10^6+10^6} = 2.27$ km s$^{-1}$; $\Delta\lambda_D = \lambda v_D/c = 44.7$ mÅ. (b) $\Delta\nu_D = v_D/\lambda = 3.86\times10^9$ Hz, so $a = \gamma/(4\pi\Delta\nu_D) = 0.031$. (c) Solve $e^{-v^2} = a/(\sqrt\pi v^2)$: $v\approx2.41$, i.e. $2.41\times44.7\approx108$ mÅ from centre. Beyond about 0.1 Å the wings are controlled by collisions, which is why the broad Na D wings measure pressure.

---

## Part C — Essay (choose one, 10 marks)

**C1.** "Local thermodynamic equilibrium is a statement about matter, not about radiation." Discuss, with reference to Kirchhoff's law, the two-level atom and the thermalisation depth.

> **Model answer outline.** (1) Define TE and LTE; Maxwell, Boltzmann and Saha at the local $T$. (2) Kirchhoff: $j = \alpha B$ depends only on the matter state, hence $S = B$ in LTE while $I\neq B$ (escape at the surface; $I(0,\mu<0) = 0$; $J(0)\approx B/2$). (3) Validity: collisions must dominate radiative rates; two-level atom $S = (1-\varepsilon)\bar J+\varepsilon B$, so LTE when $\varepsilon\to1$. (4) Even with $\varepsilon$ close to but below 1, $S$ deviates from $B$ within $\tau\sim1/\sqrt\varepsilon$ of the surface, with $S(0) = \sqrt\varepsilon B$. (5) Consequences: LTE is good for continua and weak lines in dwarf photospheres; it fails for strong lines, chromospheres, hot or low-density stars and nebulae. (6) Practical: LTE turns the RTE into an explicit formal solution once $T(\tau)$ is known; NLTE requires solving rate equations coupled to the radiation field (ALI).

**C2.** Describe how a model stellar atmosphere is computed, starting from the gray LTE solution, and how its predictions are compared with observations.

> **Model answer outline.** Inputs $T_{\rm eff}$, $\log g$, composition → gray starting $T(\tau) = [\frac34T_{\rm eff}^4(\tau+q)]^{1/4}$ → hydrostatic $P(\tau)$ from $dP/d\tau = g/\kappa$ → Saha–Boltzmann populations → $\kappa_\nu,\ j_\nu$ → solve the RTE at many frequencies (formal solution, or Feautrier/ALI with scattering) → check radiative equilibrium $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$ and constant flux → temperature correction (Unsöld–Lucy) → iterate to convergence → emergent spectrum, limb darkening, line profiles (Milne–Eddington intuition, curve of growth) → compare with observed spectra, colours, Balmer jump and line equivalent widths → derive $T_{\rm eff}$, $g$ and abundances.

---

## Part D — Regimes and opacity (4 marks each)

**D1.** (Lectures SA1, SA3) Classify as TE, LTE or NLTE, with one sentence of justification each: (a) radiation 0.5 $R_\odot$ from the centre of the Sun; (b) the continuum at 500 nm in the solar photosphere; (c) the core of the Ca II K line; (d) [O III] 500.7 nm in a planetary nebula with $n_e = 10^{10}$ m$^{-3}$.

> **Solution.** (a) **TE**: the photon mean free path (cm) is $10^{-10}$ of the temperature scale height, so the radiation is isotropic and Planckian at the local $T$. (b) **LTE**: H$^-$ populations are set by collisions at $n_e\sim10^{19}$–$10^{20}$ m$^{-3}$, so $S = B$, although $I\neq B$ at the surface. (c) **NLTE**: a strong resonance line forming high in the low-density chromosphere, with photon losses ($S<B$) and non-radiative heating. (d) **NLTE**: $n_e\approx0.016\,n_{\rm crit}$, so every collisional excitation is followed by radiative decay.

**D2.** (Lecture SA5) Explain line blanketing and backwarming, and name the dominant continuum opacity source in (a) an O star, (b) an A0 star, (c) the Sun, (d) an M dwarf.

> **Solution.** Many lines block flux (mainly in the UV). The energy must still escape, so it is redistributed to other frequencies and partly returned to deeper layers, which become hotter (backwarming), while the outer layers cool. Opacity sources: (a) electron scattering and He bound-free; (b) H I bound-free (Balmer continuum); (c) H$^-$ bound-free and free-free; (d) H$^-$ plus molecules (TiO, H$_2$O).
