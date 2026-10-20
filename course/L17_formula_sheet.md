# Formula Sheet — Radiative Transfer (for revision and the exam)

## Radiation field (Lecture 2)

| | |
|---|---|
| Specific intensity | $dE = I_\nu\cos\theta\,dA\,d\Omega\,d\nu\,dt$; $I_\nu$ constant along rays in vacuum; $I_\nu/\nu^3$ invariant |
| Mean intensity | $J_\nu = \frac1{4\pi}\oint I_\nu d\Omega = \frac12\int_{-1}^1I_\nu d\mu$ |
| Flux | $F_\nu = \oint I_\nu\cos\theta\,d\Omega = 2\pi\int_{-1}^1I_\nu\mu\,d\mu$; $H_\nu = F_\nu/4\pi$ |
| K-integral, pressure | $K_\nu = \frac12\int_{-1}^1I_\nu\mu^2d\mu$; $P_\nu = 4\pi K_\nu/c$ |
| Energy density | $u_\nu = 4\pi J_\nu/c$ |
| Isotropic field | $F = 0$, $K = J/3$, $P = u/3$ |
| Uniform hemisphere | $F = \pi I$ |
| Sphere seen from $d$ | $F = \pi I(R/d)^2$ |
| $\nu\leftrightarrow\lambda$ | $I_\lambda = (c/\lambda^2)I_\nu$ |

## Black body (Lecture 3)

$$B_\nu = \frac{2h\nu^3}{c^2}\frac1{e^{h\nu/kT}-1},\quad B_\lambda = \frac{2hc^2}{\lambda^5}\frac1{e^{hc/\lambda kT}-1}$$

- RJ: $B_\nu\approx2\nu^2kT/c^2$ · Wien: $B_\nu\approx\frac{2h\nu^3}{c^2}e^{-h\nu/kT}$ · $h\nu_{\max} = 2.821kT$ · $\lambda_{\max}T = 2.898\times10^{-3}$ m K
- $\int B_\nu d\nu = \sigma T^4/\pi$ · $F = \sigma T^4$ · $u = aT^4$, $a = 4\sigma/c$ · $dB/dT = 4\sigma T^3/\pi$ · $n_\gamma = 2.03\times10^7T^3$ m$^{-3}$
- $T_b$: $I_\nu = B_\nu(T_b)$, RJ $T_b = c^2I_\nu/2k\nu^2$ · $L = 4\pi R^2\sigma T_{\rm eff}^4$

## Coefficients (Lecture 4)

- $\alpha_\nu = n\sigma_\nu = \rho\kappa_\nu$ · $\ell = 1/\alpha_\nu$ · $\tau_\nu = \int\alpha_\nu ds$ · $S_\nu = j_\nu/\alpha_\nu$ · $\kappa_{\rm es} = 0.02(1+X)$ m$^2$ kg$^{-1}$
- Einstein: $g_1B_{12} = g_2B_{21}$, $A_{21} = \frac{2h\nu^3}{c^2}B_{21}$
- $j_\nu = \frac{h\nu}{4\pi}n_2A_{21}\phi$, $\alpha_\nu = \frac{h\nu}{4\pi}\phi(n_1B_{12}-n_2B_{21})$, $S = \frac{2h\nu^3/c^2}{g_2n_1/g_1n_2-1}$
- Scattering + absorption: $S = \varepsilon B+(1-\varepsilon)J$ · Random walk: $R = \sqrt N\ell$, $N\approx\max(\tau,\tau^2)$

## Transfer equation (Lectures 5, 7)

- $\dfrac{dI_\nu}{d\tau_\nu} = S_\nu - I_\nu$ (τ along the ray) · $I = I_0e^{-\tau}+\int_0^\tau S(t)e^{-(\tau-t)}dt$ · slab: $I = I_0e^{-\tau}+S(1-e^{-\tau})$
- Plane-parallel ($\tau$ inward): $\mu\dfrac{dI}{d\tau} = I-S$ · $I(0,\mu) = \int_0^\infty S\,e^{-t/\mu}dt/\mu$
- $J = \frac12\int_0^\infty S\,E_1|t-\tau|dt$ · $F = 2\pi\left[\int_\tau^\infty SE_2(t-\tau)dt-\int_0^\tau SE_2(\tau-t)dt\right]$ · $K = \frac12\int SE_3|t-\tau|dt$
- $E_n(x) = \int_1^\infty e^{-xt}t^{-n}dt$, $E_n' = -E_{n-1}$, $E_n(0) = 1/(n-1)$, $\int_0^\infty E_n = 1/n$, $\int_0^\infty tE_n = 1/(n+1)$
- **Eddington–Barbier:** $I(0,\mu)\approx S(\tau = \mu)$, $F(0)\approx\pi S(\tau = 2/3)$ (exact for linear $S$)

## LTE (Lecture 6)

- Kirchhoff: $j_\nu = \alpha_\nu B_\nu(T)$ ⇒ $S_\nu = B_\nu(T)$ (but $I_\nu\ne B_\nu$)
- Boltzmann: $\dfrac{N_j}{N_i} = \dfrac{g_j}{g_i}e^{-\Delta E/kT}$ · Saha: $\dfrac{N_{r+1}n_e}{N_r} = \dfrac{2U_{r+1}}{U_r}\left(\dfrac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$, $(2\pi m_ek/h^2)^{3/2} = 2.415\times10^{21}$ m$^{-3}$K$^{-3/2}$
- LTE opacity factor $1-e^{-h\nu/kT}$ · two-level atom: $S = (1-\varepsilon)\bar J+\varepsilon B$, $\varepsilon'= \frac{C_{21}}{A_{21}}(1-e^{-h\nu/kT})$, $\varepsilon = \frac{\varepsilon'}{1+\varepsilon'}$ · $n_{\rm crit} = A_{21}/q_{21}$

## Moments, diffusion, scattering (Lecture 8)

- $\dfrac{dH}{d\tau} = J-S$ · $\dfrac{dK}{d\tau} = H$ · RE: $\int\kappa_\nu(J_\nu-B_\nu)d\nu = 0$, $F = \sigma T_{\rm eff}^4$ = const
- Eddington: $K = J/3$, $J(0) = 2H(0)$ ⇒ $\frac13J'' = J-S$
- Diffusion: $F_\nu = \frac{4\pi}3\frac{dB_\nu}{d\tau_\nu}$ · $\dfrac1{\kappa_R} = \dfrac{\int\kappa_\nu^{-1}\partial_TB_\nu d\nu}{\int\partial_TB_\nu d\nu}$ · $F = -\dfrac{16\sigma T^3}{3\kappa_R\rho}\dfrac{dT}{dz}$
- Isothermal scattering: $S(0) = \sqrt\varepsilon\,B$ (exact) · Eddington $J = B\left[1-\frac{e^{-\sqrt{3\varepsilon}\tau}}{1+2\sqrt{\varepsilon/3}}\right]$ · $\tau_{\rm th}\sim1/\sqrt\varepsilon$

## Gray LTE atmosphere (Lecture 9)

- $J = B = S$, $H = \sigma T_{\rm eff}^4/4\pi$
- Eddington: $T^4 = \frac34T_{\rm eff}^4(\tau+\frac23)$, $T(0) = 0.841T_{\rm eff}$, $T(2/3) = T_{\rm eff}$
- Exact: $T^4 = \frac34T_{\rm eff}^4[\tau+q(\tau)]$, $q(0) = 1/\sqrt3$, $q(\infty) = 0.7104$, $T(0) = 0.811T_{\rm eff}$
- Limb darkening: Eddington $I(\mu)/I(1) = (2+3\mu)/5$; exact $H(\mu)/H(1)$, $I(0)/I(1) = 0.344$
- Two-stream ($\mu = \pm1/\sqrt3$): $T^4 = \frac34T_{\rm eff}^4(\tau+1/\sqrt3)$
- Hydrostatic: $dP/d\tau = g/\kappa$ ⇒ $P = g\tau/\kappa$

## Lines (Lecture 10)

- $\int\sigma_\nu d\nu = \pi r_ecf$ · $\Delta\nu_D = \frac{\nu_0}c\sqrt{2kT/m+\xi^2}$ · Voigt $a = \gamma/4\pi\Delta\nu_D$
- Milne–Eddington (LTE): $\dfrac{F_\nu}{F_c} = \dfrac{1+2\beta/[3(1+\eta_\nu)]}{1+2\beta/3}$, maximum depth $1-\frac1{1+2\beta/3}$
- Weak line: $W_\lambda = \pi r_e\lambda^2Nf$ · Curve of growth: $W\propto N$ → $\sqrt{\ln N}$ → $\sqrt N$
- NLTE: $S^{\rm line} = \frac{2h\nu^3}{c^2}\left[\frac{b_l}{b_u}e^{h\nu/kT}-1\right]^{-1}$

## Forming the RTE (Lecture 11)

- $I_\nu = (h^4\nu^3/c^2)f$ · Boltzmann: $\partial_tf+c\hat{\mathbf n}\cdot\nabla f = (\partial_tf)_{\rm coll}$
- General: $\frac1c\partial_tI_\nu+\hat{\mathbf n}\cdot\nabla I_\nu = -(\kappa_\nu+\sigma_\nu)\rho I_\nu+j_\nu+\frac{\sigma_\nu\rho}{4\pi}\iint RI_{\nu'}d\Omega'd\nu'$
- Spherical: $\mu\partial_rI+\frac{1-\mu^2}{r}\partial_\mu I = \chi(S-I)$ · invariants $I_\nu/\nu^3$, $\nu\chi_\nu$, $j_\nu/\nu^2$
- Energy: $\partial_tu+\nabla\cdot\mathbf F = 4\pi\int(j_\nu-\kappa_\nu\rho J_\nu)d\nu$ · force: $\mathbf f_{\rm rad} = \frac1c\int\chi_\nu\mathbf F_\nu d\nu$

## Historical approximations (Lecture 12)

- Schwarzschild ($\mu = \pm\frac12$): $T^4 = \frac12T_{\rm eff}^4(1+2\tau)$, $I(\mu)/I(1) = (1+2\mu)/3$
- Two-stream ($\mu = \pm1/\sqrt3$): $T^4 = \frac34T_{\rm eff}^4(\tau+1/\sqrt3)$ · Eddington: $\frac34T_{\rm eff}^4(\tau+\frac23)$ · exact: $\frac34T_{\rm eff}^4(\tau+q)$

## Polarization (Lecture 13)

- $I = I_1+I_2$, $Q = I_1-I_2$, $U = I_{1'}-I_{2'}$, $V = I_+-I_-$ · $p = \sqrt{Q^2+U^2+V^2}/I$ · $\chi = \frac12\arctan(U/Q)$
- $d\mathbf I/ds = -\mathsf K\mathbf I+\boldsymbol\epsilon$ (Unno–Rachkovsky with Zeeman profiles)
- Thomson/Rayleigh: $p = \sin^2\Theta/(1+\cos^2\Theta)$ · electron-scattering atmosphere: $p(\mu = 0) = 11.7\,\%$
- Zeeman: $\Delta\lambda_B = 4.67\times10^{-13}g\lambda^2B$ (λ, Δλ in Å; B in G) · weak field: $V\approx-\Delta\lambda_B\cos\gamma\,\partial I/\partial\lambda$

## TE, LTE, NLTE (Lecture 14)

- TE: $I_\nu = B_\nu(T)$ · LTE: $S_\nu = B_\nu(T(\mathbf r))$ · NLTE: rate equations, $S_\nu\ne B_\nu$
- Statistical equilibrium: $n_i\sum_j(R_{ij}+C_{ij}) = \sum_jn_j(R_{ji}+C_{ji})$ · $b_i = n_i/n_i^{\rm LTE}$
- $S^{\rm line} = \frac{2h\nu^3}{c^2}\left[\frac{b_l}{b_u}e^{h\nu/kT}-1\right]^{-1}\approx\frac{b_u}{b_l}B_\nu$ · criterion: $n_e$ vs $n_{\rm crit} = A\beta_{\rm esc}/q$

## Stellar atmospheres (Lecture 15)

- $dP/d\tau = g/\kappa$ · $F_{\rm rad}+F_{\rm conv} = \sigma T_{\rm eff}^4$ · scale height $H = kT/(\mu m_Hg)$
- Convection if $\nabla_{\rm rad}>\nabla_{\rm ad}$ (0.4 ideal monatomic); gray atmosphere: $\nabla_{\rm rad} = \tau/[4(\tau+2/3)]<0.25$

