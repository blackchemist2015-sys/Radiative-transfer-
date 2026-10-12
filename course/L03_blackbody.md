# Lecture 3 — Black-Body Radiation: the Planck Function

> **Sources:** MIT 8.901 Lec. 7 (Stefan–Boltzmann, Wien); Hu Set 1; Collins Ch. 9.1 (STE and photon statistics); Rybicki & Lightman Ch. 1 (standard reference).

## Learning goals

1. Derive the Planck function from photon statistics.
2. Obtain its Rayleigh–Jeans and Wien limits, Wien's displacement law and the Stefan–Boltzmann law.
3. Define and use brightness, colour and effective temperatures.

---

## 3.1 Black-body radiation

A **black body** is matter that absorbs all radiation falling on it. Radiation in an opaque cavity in thermodynamic equilibrium at temperature $T$ (**Hohlraum** radiation) is isotropic, unpolarised and depends **only on $T$**. Its intensity is the **Planck function**
$$\boxed{\;B_\nu(T) = \frac{2h\nu^3}{c^2}\,\frac{1}{e^{h\nu/kT}-1}\;}
\qquad
\boxed{\;B_\lambda(T) = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/\lambda kT}-1}\;}$$

### Derivation (photon gas)

1. **Number of modes.** In a box of volume $V$ the number of photon states with momentum in $d^3p$ is $2\,V\,d^3p/h^3$ (the factor 2 counts polarisations). With $p = h\nu/c$ and $d^3p = 4\pi p^2dp$, the number of modes per unit volume in $d\nu$ is $\dfrac{8\pi\nu^2}{c^3}d\nu$.
2. **Mean occupation number.** Photons are bosons with zero chemical potential: $\bar n = 1/(e^{h\nu/kT}-1)$.
3. **Energy density.** $u_\nu = \dfrac{8\pi\nu^2}{c^3}\,h\nu\,\bar n = \dfrac{8\pi h\nu^3}{c^3}\dfrac{1}{e^{h\nu/kT}-1}$.
4. **Intensity.** For isotropic radiation, $u_\nu = 4\pi I_\nu/c$ (Lecture 2), so $I_\nu = cu_\nu/4\pi = B_\nu$. ∎

![Planck curves and their limits](../figures/L03_planck.png)

*Figure 3.1 — Left: $B_\lambda$ for four temperatures, with the Wien peak (dots and dashed line). Hotter bodies are brighter at **every** wavelength, so Planck curves never cross. Right: the Rayleigh–Jeans ($h\nu\ll kT$) and Wien ($h\nu\gg kT$) limits.*

## 3.2 Limits

**Rayleigh–Jeans** ($x \equiv h\nu/kT \ll 1$, radio): $e^x - 1\approx x$, so
$$B_\nu \approx \frac{2\nu^2kT}{c^2} = \frac{2kT}{\lambda^2}.$$
This is linear in $T$ and contains no $h$ (classical). Integrated over all $\nu$ it diverges: the "ultraviolet catastrophe".

**Wien** ($x\gg1$, UV and X-ray tail): $B_\nu\approx\dfrac{2h\nu^3}{c^2}e^{-h\nu/kT}$. The steep exponential makes the UV very sensitive to $T$.

## 3.3 Wien's displacement law

Set $\partial B_\nu/\partial\nu = 0$: with $x = h\nu/kT$ we need $3(1-e^{-x}) = x$, whose root is $x = 2.821$:
$$\nu_{\max} = 2.821\frac{kT}{h} = 5.879\times10^{10}\ {\rm Hz\,K^{-1}}\times T .$$
Set $\partial B_\lambda/\partial\lambda = 0$: $5(1-e^{-y}) = y$ with $y = hc/\lambda kT$, so $y = 4.965$:
$$\lambda_{\max}T = 2.898\times10^{-3}\ {\rm m\,K}.$$
Note that $\lambda_{\max}\neq c/\nu_{\max}$: the peak depends on the variable used (Lecture 2, Q5).

## 3.4 Stefan–Boltzmann law

$$\int_0^\infty B_\nu\,d\nu = \frac{2h}{c^2}\left(\frac{kT}{h}\right)^4\int_0^\infty\frac{x^3dx}{e^x-1} = \frac{2k^4T^4}{c^2h^3}\cdot\frac{\pi^4}{15} \equiv \frac{\sigma}{\pi}T^4,$$
with
$$\sigma = \frac{2\pi^5k^4}{15c^2h^3} = 5.670\times10^{-8}\ {\rm W\,m^{-2}\,K^{-4}}.$$

| Quantity | Black-body value |
|---|---|
| Intensity $B = \int B_\nu d\nu$ | $\sigma T^4/\pi$ |
| Flux from a surface $F = \pi B$ | $\sigma T^4$ |
| Energy density $u = 4\pi B/c$ | $aT^4$, $a = 4\sigma/c = 7.566\times10^{-16}$ J m$^{-3}$ K$^{-4}$ |
| Pressure $P = u/3$ | $aT^4/3$ |
| Photon number density | $n_\gamma = 16\pi\zeta(3)(kT/hc)^3 = 2.03\times10^7\,T^3$ m$^{-3}$ |
| Mean photon energy | $\langle h\nu\rangle = 2.70\,kT$ |

A useful derivative, needed for the diffusion approximation (Lecture 8):
$$\frac{dB}{dT} = \frac{4\sigma T^3}{\pi}.$$

## 3.5 Characteristic temperatures

| Name | Definition | Use |
|---|---|---|
| **Brightness temperature** $T_b(\nu)$ | $I_\nu = B_\nu(T_b)$; in RJ: $T_b = c^2I_\nu/(2k\nu^2)$ | radio astronomy; $T_b$ = actual $T$ only for an optically thick thermal source |
| **Colour temperature** $T_c$ | shape (slope) of the spectrum fitted by $B_\nu(T_c)$ | photometric colours |
| **Effective temperature** $T_{\rm eff}$ | $F = \sigma T_{\rm eff}^4$, i.e. $L = 4\pi R^2\sigma T_{\rm eff}^4$ | stars; defines the surface flux |
| **Excitation temperature** $T_{\rm ex}$ | $n_2/n_1 = (g_2/g_1)e^{-h\nu/kT_{\rm ex}}$ | lines; $T_{\rm ex} = T$ only in LTE |

For a real star these all differ. They coincide only for a true black body.

---

## Worked example 3.1 — The cosmic microwave background

*$T = 2.725$ K. Find (a) $\nu_{\max}$ of $B_\nu$, (b) $\lambda_{\max}$ of $B_\lambda$, (c) the photon number and energy densities.*

**(a)** $\nu_{\max} = 5.879\times10^{10}\times2.725 = 1.60\times10^{11}$ Hz = 160 GHz.
**(b)** $\lambda_{\max} = 2.898\times10^{-3}/2.725 = 1.06$ mm. Note that $c/\nu_{\max} = 1.87$ mm $\neq\lambda_{\max}$.
**(c)** $n_\gamma = 2.03\times10^7\times2.725^3 = 4.1\times10^8$ m$^{-3}$ = **411 photons cm$^{-3}$**; $u = aT^4 = 4.17\times10^{-14}$ J m$^{-3}$.

## Worked example 3.2 — The Sun at 500 nm

*Compute $B_\lambda(500\ {\rm nm}, 5772\ {\rm K})$ and decide whether the Wien approximation is adequate.*

$x = hc/(\lambda kT) = 1.4388\times10^{-2}/(5\times10^{-7}\times5772) = 4.985$, and $2hc^2/\lambda^5 = 3.811\times10^{15}$ W m$^{-3}$ sr$^{-1}$, so
$$B_\lambda = \frac{3.811\times10^{15}}{e^{4.985}-1} = 2.62\times10^{13}\ {\rm W\,m^{-3}\,sr^{-1}}.$$
Wien drops the "$-1$": the relative error is $e^{-x} = 0.7\,\%$, so Wien is adequate in the visible for solar-type stars.

## Worked example 3.3 — Brightness temperature of a radio source

*At 1.4 GHz a source has $I_\nu = 2.0\times10^{-19}$ W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$. Find $T_b$.*

$h\nu/k = 0.067$ K, so the RJ limit is excellent for any $T\gg0.07$ K:
$$T_b = \frac{c^2I_\nu}{2k\nu^2} = \frac{(3\times10^8)^2\times2\times10^{-19}}{2\times1.381\times10^{-23}\times(1.4\times10^9)^2} = 332\ {\rm K}.$$
If the source is an optically thin H II region with $T_e = 8000$ K, then $T_b = T_e\tau$ (Lecture 5), so $\tau\approx0.04$.

## Worked example 3.4 — Inverting the Planck function

*An observed intensity equals $B_\lambda$; solve for $T$.*
$$T = \frac{hc}{\lambda k}\;\frac{1}{\ln\!\left(1+\dfrac{2hc^2}{\lambda^5B_\lambda}\right)}.$$
For $\lambda = 500$ nm and $B_\lambda = 4.0\times10^{13}$ W m$^{-3}$ sr$^{-1}$: $T = 28\,776/\ln(1+95.3) = 6300$ K. We use this formula in Lecture 7 to map out the solar temperature from limb darkening.

---

## Exam questions and answers — Lecture 3

**Q1.** Derive the Planck function from the density of photon states and Bose–Einstein statistics.

> **A1.** See §3.1. Modes per unit volume per $d\nu$: $8\pi\nu^2/c^3$. Mean energy per mode: $h\nu/(e^{h\nu/kT}-1)$. Therefore $u_\nu = (8\pi h\nu^3/c^3)/(e^{h\nu/kT}-1)$, and $B_\nu = cu_\nu/4\pi$.

**Q2.** Show that $B_\nu$ has its maximum at $h\nu = 2.821\,kT$. Is the peak of $B_\lambda$ at $\lambda = c/\nu_{\max}$?

> **A2.** $B_\nu\propto x^3/(e^x-1)$; $d/dx = 0\Rightarrow 3x^2(e^x-1) - x^3e^x = 0\Rightarrow 3(1-e^{-x}) = x$, whose root is $x = 2.821$ (solve by iteration: $x_{n+1} = 3(1-e^{-x_n})$). For $B_\lambda\propto y^5/(e^y-1)$ the condition is $5(1-e^{-y}) = y$, $y = 4.965$. Since $4.965\neq2.821$, $\lambda_{\max}\neq c/\nu_{\max}$; the two differ by a factor $1.76$.

**Q3.** Derive the Stefan–Boltzmann law, giving $\sigma$ in terms of fundamental constants. (Use $\int_0^\infty x^3/(e^x-1)\,dx = \pi^4/15$.)

> **A3.** $F = \pi\int B_\nu d\nu = \pi\frac{2h}{c^2}\left(\frac{kT}{h}\right)^4\frac{\pi^4}{15} = \frac{2\pi^5k^4}{15c^2h^3}T^4 = \sigma T^4$.

**Q4.** Write the RJ and Wien limits. In which limit is a black body's intensity linear in $T$? Why is the RJ limit used in radio astronomy?

> **A4.** RJ: $B_\nu\approx2\nu^2kT/c^2$ (linear in $T$). Wien: $B_\nu\approx(2h\nu^3/c^2)e^{-h\nu/kT}$. At radio frequencies $h\nu/k\sim0.05$–$1$ K $\ll T$ for almost all sources, so $I_\nu\propto T_b$ and the RTE becomes linear in temperature (Lecture 5).

**Q5.** Two stars have the same $T_{\rm eff}$ but radii differing by a factor 10. Compare their surface fluxes, surface brightnesses and luminosities.

> **A5.** Surface flux $\sigma T_{\rm eff}^4$ and surface brightness ($I\approx F/\pi$) are the **same**. Luminosity $\propto R^2$ differs by a factor 100.

**Q6.** Show that $dB/dT = 4\sigma T^3/\pi$ and that $\partial B_\nu/\partial T > 0$ at every frequency.

> **A6.** $B = \sigma T^4/\pi$, so $dB/dT = 4\sigma T^3/\pi$. $\partial B_\nu/\partial T = \frac{2h\nu^3}{c^2}\frac{(h\nu/kT^2)e^{h\nu/kT}}{(e^{h\nu/kT}-1)^2} > 0$. So Planck curves never cross: hotter means brighter at every frequency. This is why absorption lines form where $T$ decreases outward (Lecture 10).

**Q7.** Why is $T_b$ of an optically thin source **less** than its kinetic temperature? Under what condition are they equal?

> **A7.** For an isothermal slab with no background, $I_\nu = B_\nu(T)(1-e^{-\tau_\nu})$ (Lecture 5), so in RJ $T_b = T(1-e^{-\tau})<T$, and $T_b\approx T\tau$ when $\tau\ll1$. They are equal only when $\tau_\nu\gg1$ (and the source is thermal, $S_\nu = B_\nu$).
