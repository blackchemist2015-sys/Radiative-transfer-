# Formula Sheet — Course B: Stellar Atmospheres

## LTE (Lecture SA1)

- Kirchhoff: $j_\nu = \alpha_\nu B_\nu(T)$ ⇒ $S_\nu = B_\nu(T)$ (but $I_\nu\ne B_\nu$)
- Boltzmann: $\dfrac{N_j}{N_i} = \dfrac{g_j}{g_i}e^{-\Delta E/kT}$ · Saha: $\dfrac{N_{r+1}n_e}{N_r} = \dfrac{2U_{r+1}}{U_r}\left(\dfrac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$, $(2\pi m_ek/h^2)^{3/2} = 2.415\times10^{21}$ m$^{-3}$K$^{-3/2}$
- LTE opacity factor $1-e^{-h\nu/kT}$ · two-level atom: $S = (1-\varepsilon)\bar J+\varepsilon B$, $\varepsilon'= \frac{C_{21}}{A_{21}}(1-e^{-h\nu/kT})$, $\varepsilon = \frac{\varepsilon'}{1+\varepsilon'}$ · $n_{\rm crit} = A_{21}/q_{21}$

## Continuous opacity (Lecture SA2)

- Kramers: $\sigma_{\rm bf}(n,\nu) = 2.815\times10^{29}Z^4g_{\rm bf}/(n^5\nu^3)$ cm$^2$ for $\nu\ge\nu_n = 3.288\times10^{15}Z^2/n^2$ Hz; edges $\lambda_n = 91.13\,n^2/Z^2$ nm
- LTE: $\alpha^{\rm bf}_\nu = \sum_nN_n\sigma_{\rm bf}(n,\nu)(1-e^{-h\nu/kT})$, $N_n = N_{\rm H\,I}2n^2e^{-E_n/kT}/U$
- Free–free: $\alpha^{\rm ff}_\nu = 3.69\times10^8Z^2n_en_iT^{-1/2}\nu^{-3}g_{\rm ff}(1-e^{-h\nu/kT})$ cm$^{-1}$ (cgs)
- H$^-$: $\chi = 0.754$ eV, threshold 1.64 µm, $\sigma_{\max}\approx4\times10^{-17}$ cm$^2$ near 850 nm; $\frac{n({\rm H^-})}{n({\rm H\,I})n_e} = \frac14\left(\frac{h^2}{2\pi m_ekT}\right)^{3/2}e^{0.754\,{\rm eV}/kT}$
- Thomson: $\sigma_T = 6.652\times10^{-29}$ m$^2$, $\kappa_{\rm es} = 0.020(1+X)$ m$^2$/kg · Rayleigh $\propto\lambda^{-4}$ · Kramers' law $\bar\kappa\propto\rho T^{-3.5}$

## Transition rates (Lecture SA3)

- Statistical equilibrium: $n_i\sum_j(R_{ij}+C_{ij}) = \sum_jn_j(R_{ji}+C_{ji})$
- Photo-ionisation: $R_{i\kappa} = 4\pi\int\frac{\sigma_i}{h\nu}J_\nu d\nu$ · recombination (Milne): $R_{\kappa i} = \left(\frac{n_i}{n_\kappa}\right)^*4\pi\int\frac{\sigma_i}{h\nu}\left(\frac{2h\nu^3}{c^2}+J_\nu\right)e^{-h\nu/kT}d\nu$
- Collisions: $q_{ul} = 8.629\times10^{-6}\Omega/(g_u\sqrt T)$ cm$^3$ s$^{-1}$ · Klein–Rosseland: $q_{lu} = (g_u/g_l)q_{ul}e^{-\Delta E/kT}$
- Critical density $n_{\rm crit} = A_{ul}/q_{ul}$ · two-level, no radiation: $\frac{(n_u/n_l)}{(n_u/n_l)^*} = \frac{n_e/n_{\rm crit}}{1+n_e/n_{\rm crit}}$
- Coronal: $n_u/n_l = n_eq_{lu}/A_{ul}$; $n_{i+1}/n_i = q_{\rm ion}(T)/\alpha_{\rm rec}(T)$ · Nebular: $J_\nu\approx WB_\nu(T_*)$, $W\approx\frac14(R_*/r)^2$

## Line absorption and broadening (Lecture SA4)

- $\alpha^{\rm line}_\nu = \frac{\pi e^2}{m_ec}f_{lu}n_l\phi(\nu)(1-e^{-h\nu/kT})$, $\frac{\pi e^2}{m_ec} = 0.02654$ cm$^2$ Hz · $A_{ul} = 0.6670\frac{g_l}{g_u}\frac{f_{lu}}{\lambda^2[{\rm cm}]}$ s$^{-1}$
- Natural: $\gamma_{\rm rad} = \Gamma_u+\Gamma_l$, $\Delta\lambda_{\rm FWHM} = \lambda^2\gamma/(2\pi c)$; classical $\gamma_{\rm cl} = 2.47\times10^{-22}\nu^2$ s$^{-1}$
- Doppler: $\Delta\nu_D = \frac{\nu_0}{c}\sqrt{2kT/m+\xi^2}$ · pressure: $\Delta\nu = C_n/r^n$, $n = 2$ (linear Stark), 3 (resonance), 4 (quadratic Stark), 6 (van der Waals); impact width $\gamma_n\propto N C_n^{2/(n-1)}\bar v^{(n-3)/(n-1)}$
- Voigt: $\phi = H(a,v)/(\sqrt\pi\Delta\nu_D)$, $a = \gamma/(4\pi\Delta\nu_D)$, wings $H\approx a/(\sqrt\pi v^2)$ · rotation: $\Delta\lambda_L = \lambda v\sin i/c$

## Gray LTE atmosphere (Lecture SA5)

- $J = B = S$, $H = \sigma T_{\rm eff}^4/4\pi$
- Eddington: $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$, $T(0) = 0.841T_{\rm eff}$, $T(2/3) = T_{\rm eff}$
- Exact: $T^4 = \frac34T_{\rm eff}^4[\tau+q(\tau)]$, $q(0) = 1/\sqrt3$, $q(\infty) = 0.7104$, $T(0) = 0.811T_{\rm eff}$
- Limb darkening: Eddington $I(\mu)/I(1) = (2+3\mu)/5$; exact $H(\mu)/H(1)$, $I(0)/I(1) = 0.344$
- Two-stream ($\mu = \pm1/\sqrt3$): $T^4 = \frac34T_{\rm eff}^4(\tau+1/\sqrt3)$
- Hydrostatic: $dP/d\tau = g/\kappa$ ⇒ $P = g\tau/\kappa$

## Lines (Lecture SA6)

- $\int\sigma_\nu d\nu = \pi r_ecf$ · $\Delta\nu_D = \frac{\nu_0}c\sqrt{2kT/m+\xi^2}$ · Voigt $a = \gamma/4\pi\Delta\nu_D$
- Milne–Eddington (LTE): $\dfrac{F_\nu}{F_c} = \dfrac{1+2\beta/[3(1+\eta_\nu)]}{1+2\beta/3}$, maximum depth $1-\frac1{1+2\beta/3}$
- Weak line: $W_\lambda = \pi r_e\lambda^2Nf$ · Curve of growth: $W\propto N$ → $\sqrt{\ln N}$ → $\sqrt N$
- NLTE: $S^{\rm line} = \frac{2h\nu^3}{c^2}\left[\frac{b_l}{b_u}e^{h\nu/kT}-1\right]^{-1}$

## TE, LTE, NLTE (Lecture SA7)

- TE: $I_\nu = B_\nu(T)$ · LTE: $S_\nu = B_\nu(T(\mathbf r))$ · NLTE: rate equations, $S_\nu\ne B_\nu$
- Statistical equilibrium: $n_i\sum_j(R_{ij}+C_{ij}) = \sum_jn_j(R_{ji}+C_{ji})$ · $b_i = n_i/n_i^{\rm LTE}$
- $S^{\rm line} = \frac{2h\nu^3}{c^2}\left[\frac{b_l}{b_u}e^{h\nu/kT}-1\right]^{-1}\approx\frac{b_u}{b_l}B_\nu$ · criterion: $n_e$ vs $n_{\rm crit} = A\beta_{\rm esc}/q$

## Stellar atmospheres (Lecture SA8)

- $dP/d\tau = g/\kappa$ · $F_{\rm rad}+F_{\rm conv} = \sigma T_{\rm eff}^4$ · scale height $H = kT/(\mu m_Hg)$
- Convection if $\nabla_{\rm rad}>\nabla_{\rm ad}$ (0.4 ideal monatomic); gray atmosphere: $\nabla_{\rm rad} = \tau/[4(\tau+2/3)]<0.25$
