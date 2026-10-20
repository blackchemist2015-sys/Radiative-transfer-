# Lecture RT2 — Describing the Radiation Field: Intensity, Flux and Moments

> **Sources:** Hu, *Astro 305 Set 1* (observables, auxiliary quantities); Collins Ch. 9.2–9.3 (specific intensity, moments); Chandrasekhar Ch. I §1–6; MIT 8.901 Lec. 7.

## Learning goals

1. Define the specific intensity $I_\nu$ and explain why it is the fundamental quantity.
2. Derive the mean intensity $J_\nu$, flux $F_\nu$, energy density $u_\nu$ and radiation pressure $P_\nu$ as angular moments of $I_\nu$.
3. Prove that $I_\nu$ is constant along a ray in empty space.
4. Use these definitions to compute fluxes from stars.


## Key concepts in plain words

**Intensity versus flux: brightness versus net flow.** Think of standing in a room lit by many lamps. *Intensity* answers "how bright does the room look when I point a narrow tube in one particular direction?" *Flux* answers "how much energy crosses this window per second, counting light going one way as positive and the other way as negative?" A single bright star seen through a narrow telescope gives an intensity; a light meter lying flat on a table measures a flux.

**Solid angle — the two-dimensional angle.** Just as an ordinary angle measures how much of a circle an object covers, a *solid angle* measures how much of the whole sky an object covers. The whole sky is $4\pi$ steradians (sr). The Sun, seen from Earth, covers only $6.8\times10^{-5}$ sr. Intensity is "energy per steradian", so it tells you how bright each little patch of the sky is.

**Why intensity does not fall with distance.** When you walk away from a lamp, the energy reaching you falls as $1/r^2$, but the lamp also looks smaller, and its solid angle also falls as $1/r^2$. The ratio, the brightness per steradian, stays the same. This is why a photograph of the Sun's surface from Mars would be exactly as bright, pixel by pixel, as one taken from Earth; the Sun would only look smaller. This conservation law ($I_\nu$ = constant along a ray in vacuum) is why intensity, not flux, is the natural quantity for transfer.

**Moments: replacing directions by averages.** Following the intensity in every direction is complicated, so we often use averages over directions, called *moments*:

- the **mean intensity** $J_\nu$ is the simple average: how strongly a point is bathed in light from all sides (it decides how fast atoms there absorb);
- the **flux** $F_\nu$ is the average weighted by $\cos\theta$: the *net* flow of energy in one direction (it decides how much light leaves a star);
- the **K-integral** $K_\nu$ is weighted by $\cos^2\theta$: it measures the momentum carried, i.e. the radiation *pressure*.

**Isotropic light carries no flux.** In a uniform fog, light arrives equally from all directions. Each point is strongly illuminated ($J$ large) but as much energy flows left as right, so the net flux is zero. A star shines only because its radiation is slightly **anisotropic**: a little more light goes outward than inward.

**Where the factor $\pi$ comes from.** If a surface glows with the same intensity $I$ in every outward direction, the flux it emits is $\pi I$, not $2\pi I$, because light leaving at a slant crosses the surface less efficiently (factor $\cos\theta$). This is why a black body emits $F = \pi B = \sigma T^4$.

---

## 2.1 The four observables

A detector can measure four things about radiation (Hu): **energy flux**, **direction**, **frequency** and **polarisation**. Measuring the first three together defines the specific intensity. Polarisation adds the Stokes parameters $Q, U, V$; we use only $I$ in this course.

## 2.2 Specific intensity

![Geometry defining the specific intensity](../../figures/L02_intensity_geometry.png)

*Figure 2.1 — Energy $dE$ crosses an area $dA$ whose normal $\hat{\mathbf n}$ makes angle $\theta$ with the direction of propagation $\hat{\mathbf k}$, into solid angle $d\Omega$, in frequency interval $d\nu$ and time $dt$.*

$$
\boxed{\;dE = I_\nu(\mathbf r,\hat{\mathbf k},t)\;\cos\theta\;dA\;d\Omega\;d\nu\;dt\;}
$$

**Units:** W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$ (cgs: erg s$^{-1}$ cm$^{-2}$ Hz$^{-1}$ sr$^{-1}$). The factor $\cos\theta$ is the *projected* area seen by the beam.

Per unit wavelength: $I_\nu\,|d\nu| = I_\lambda\,|d\lambda|$. Since $\nu = c/\lambda$, $|d\nu/d\lambda| = c/\lambda^2$, so
$$I_\lambda = \frac{c}{\lambda^2}I_\nu, \qquad \nu I_\nu = \lambda I_\lambda .$$

**Relation to the photon distribution function** (Collins eq. 9.2.8). If $f(\mathbf r,\mathbf p)$ is the photon phase-space density, then
$$I_\nu = \frac{h^4\nu^3}{c^2}\,f .$$
Since $f$ is conserved along a photon trajectory (Liouville's theorem), $I_\nu/\nu^3$ is invariant. This is why surface brightness dims as $(1+z)^{-4}$ in cosmology (Hu).

## 2.3 Constancy of $I_\nu$ along a ray in vacuum

![Intensity is conserved along a ray](../../figures/L02_constancy.png)

*Figure 2.2 — The flux from the Sun falls as $r^{-2}$, but so does the solid angle it subtends. Their ratio, the intensity, is independent of distance.*

**Proof.** Consider two small areas $dA_1$ and $dA_2$ separated by distance $r$ along a ray, both perpendicular to it. Photons that pass through both areas cross $dA_1$ into solid angle $d\Omega_1 = dA_2/r^2$, and cross $dA_2$ from solid angle $d\Omega_2 = dA_1/r^2$. With no matter in between, energy is conserved:
$$I_{\nu,1}\,dA_1\,d\Omega_1\,d\nu\,dt = I_{\nu,2}\,dA_2\,d\Omega_2\,d\nu\,dt
\;\Rightarrow\;
I_{\nu,1}\frac{dA_1dA_2}{r^2} = I_{\nu,2}\frac{dA_2dA_1}{r^2}
\;\Rightarrow\; I_{\nu,1} = I_{\nu,2}.$$
So $dI_\nu/ds = 0$ in vacuum. **Consequence:** the surface brightness of a resolved object does not depend on its distance (in a static, non-expanding space).

## 2.4 Angular moments of the intensity

Use spherical coordinates around a chosen axis: $d\Omega = \sin\theta\,d\theta\,d\phi = -d\mu\,d\phi$ with $\mu = \cos\theta$.

| Moment | Definition | Plane-parallel form ($I$ independent of $\phi$) | Physical meaning |
|---|---|---|---|
| **zeroth** $J_\nu$ | $\dfrac{1}{4\pi}\oint I_\nu\,d\Omega$ | $\tfrac12\int_{-1}^{1}I_\nu\,d\mu$ | mean intensity |
| **first** $F_\nu$ | $\oint I_\nu\cos\theta\,d\Omega$ | $2\pi\int_{-1}^{1}I_\nu\,\mu\,d\mu$ | net (physical) flux |
| **first** $H_\nu$ | $\dfrac{1}{4\pi}\oint I_\nu\cos\theta\,d\Omega$ | $\tfrac12\int_{-1}^{1}I_\nu\,\mu\,d\mu$ | Eddington flux, $H_\nu = F_\nu/4\pi$ |
| **second** $K_\nu$ | $\dfrac{1}{4\pi}\oint I_\nu\cos^2\theta\,d\Omega$ | $\tfrac12\int_{-1}^{1}I_\nu\,\mu^2\,d\mu$ | radiation pressure, $P_\nu = 4\pi K_\nu/c$ |

> **Warning about flux definitions** (Collins §9.3b). Books use three different "fluxes": the physical flux $F_\nu$ (W m$^{-2}$ Hz$^{-1}$), the Eddington flux $H_\nu = F_\nu/4\pi$, and the "astrophysical flux" $\mathcal F_\nu = F_\nu/\pi$. Always check which one a formula uses. **In this course, $F$ is the physical flux** and $F = \sigma T_{\rm eff}^4$.

### Energy density

Radiation crossing $dA$ in time $dt$ fills a cylinder of volume $dV = c\,dt\,dA$ (Hu). The energy in that volume travelling into $d\Omega$ is $dE = I_\nu\,dA\,d\Omega\,d\nu\,dt$, so the specific energy density per solid angle is $I_\nu/c$. Integrating over angles:
$$u_\nu = \frac1c\oint I_\nu\,d\Omega = \frac{4\pi}{c}J_\nu, \qquad u = \int_0^\infty u_\nu\,d\nu .$$

### Radiation pressure

A photon carries momentum $E/c$ along $\hat{\mathbf k}$. The component normal to a surface is $(E/c)\cos\theta$, and the rate at which it crosses the surface carries another factor $\cos\theta$. For a surface that absorbs everything that hits it:
$$P_\nu = \frac1c\oint I_\nu\cos^2\theta\,d\Omega = \frac{4\pi}{c}K_\nu .$$
(A perfectly reflecting wall feels twice this from one side; Hu.)

### The isotropic case

If $I_\nu = I$ is independent of direction:
$$J_\nu = I,\qquad F_\nu = 2\pi I\int_{-1}^{1}\mu\,d\mu = 0,\qquad K_\nu = \tfrac12 I\int_{-1}^1\mu^2d\mu = \frac I3 = \frac{J_\nu}{3}.$$
Therefore
$$\boxed{\;P = \tfrac13 u\;}\qquad\text{(equation of state of isotropic radiation)},$$
and $K_\nu = J_\nu/3$ is the basis of the **Eddington approximation** (Lecture RT8).

### One-sided flux

The flux leaving a surface that radiates with the same intensity $I$ in every outward direction ($0\le\mu\le1$), with nothing coming in:
$$F^+ = 2\pi\int_0^1 I\,\mu\,d\mu = \pi I .$$
This is the origin of the ubiquitous factor $\pi$: a black body has $F = \pi B = \sigma T^4$.

## 2.5 Flux from a uniform sphere

A star of radius $R$ with uniform surface intensity $I$ (no limb darkening), seen from distance $r$: it subtends a cone of half-angle $\theta_c$ with $\sin\theta_c = R/r$.
$$F(r) = \int_0^{2\pi}\!\!\int_0^{\theta_c} I\cos\theta\sin\theta\,d\theta\,d\phi = \pi I\sin^2\theta_c = \pi I\left(\frac Rr\right)^2 .$$
At the surface ($r = R$), $F = \pi I$; far away, $F \propto r^{-2}$, while $I$ itself is unchanged.

---

## Worked example 2.1 — The Sun: from luminosity to intensity

*Given $L_\odot = 3.828\times10^{26}$ W, $R_\odot = 6.957\times10^8$ m and 1 AU $= 1.496\times10^{11}$ m, find (a) the surface flux and $T_{\rm eff}$, (b) the mean intensity of the solar disk, (c) the solar constant, computed two ways.*

**(a)** $F_\odot = L_\odot/(4\pi R_\odot^2) = 6.294\times10^7$ W m$^{-2}$. With $F = \sigma T_{\rm eff}^4$: $T_{\rm eff} = (F/\sigma)^{1/4} = 5772$ K.

**(b)** $\bar I = F/\pi = 2.003\times10^7$ W m$^{-2}$ sr$^{-1}$.

**(c)** Solid angle of the Sun at 1 AU: $\Omega_\odot = \pi(R_\odot/{\rm AU})^2 = 6.794\times10^{-5}$ sr. Since $I$ is conserved and the disk is small (so $\cos\theta\approx1$), $F_{\oplus} = \bar I\,\Omega_\odot = 1361$ W m$^{-2}$. By the inverse-square law, $F_\odot(R_\odot/{\rm AU})^2 = 1361$ W m$^{-2}$, the same.

## Worked example 2.2 — Radiation versus gas pressure at the centre of the Sun

*At the solar centre, $T_c = 1.57\times10^7$ K and $P_{\rm gas}\approx2.3\times10^{16}$ Pa. Find $P_{\rm rad}$.*

**Solution.** In the interior the radiation is in TE, so it is isotropic and $P_{\rm rad} = u/3 = aT^4/3$, with $a = 4\sigma/c = 7.566\times10^{-16}$ J m$^{-3}$ K$^{-4}$. Then $u = 4.6\times10^{13}$ J m$^{-3}$ and $P_{\rm rad} = 1.5\times10^{13}$ Pa, so $P_{\rm rad}/P_{\rm gas}\approx7\times10^{-4}$. Radiation pressure is negligible in the Sun but dominates in very massive stars ($M \gtrsim 50\,M_\odot$).

## Worked example 2.3 — Moments of a linear (Eddington) intensity field

*Suppose $I(\mu) = I_0 + I_1\mu$ for all $-1\le\mu\le1$. Compute $J$, $H$, $K$ and show that $K = J/3$ exactly.*

$$J = \tfrac12\int_{-1}^1(I_0+I_1\mu)\,d\mu = I_0,\quad
H = \tfrac12\int_{-1}^1(I_0+I_1\mu)\mu\,d\mu = \frac{I_1}{3},\quad
K = \tfrac12\int_{-1}^1(I_0+I_1\mu)\mu^2d\mu = \frac{I_0}{3}.$$
So $K = J/3$ even though the field is **anisotropic** and carries a flux $F = 4\pi H = 4\pi I_1/3$. This is why the Eddington approximation works well deep in a star, where $I$ is very nearly linear in $\mu$.

---

## Common misconceptions

1. **"Intensity falls as $1/r^2$."** Flux does; intensity (surface brightness) does not, in empty static space.
2. **"Zero flux means no light."** A perfectly isotropic radiation field can be extremely intense and still carry zero net flux, as deep inside a star.
3. **"Every book's flux is the same flux."** Watch for $F$ (physical), $H = F/4\pi$ (Eddington) and $\mathcal F = F/\pi$ (astrophysical). Mixing them up gives errors of $\pi$ or $4\pi$.
4. **"The peak of a spectrum is a fixed property."** Its position depends on whether you plot per unit frequency or per unit wavelength.

## Lecture summary

- $I_\nu$ is energy per time, area, frequency and solid angle: the brightness of one beam.
- $I_\nu$ is conserved along rays in vacuum; flux falls as $1/r^2$ only because objects look smaller.
- $J_\nu$, $F_\nu$ and $K_\nu$ are the 0th, 1st and 2nd angular moments: illumination, net flow and pressure.
- Isotropic radiation has $F = 0$ and $P = u/3$; a surface of uniform intensity emits $F = \pi I$.

---

## Exam questions and answers — Lecture RT2

**Q1.** Define $I_\nu$, $J_\nu$, $F_\nu$ and $K_\nu$, give their units, and say which can be measured by a single pixel of a telescope pointed at a resolved source.

> **A1.** $I_\nu = dE/(\cos\theta\,dA\,d\Omega\,d\nu\,dt)$ [W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$]; $J_\nu = \frac{1}{4\pi}\oint I_\nu d\Omega$ [same units]; $F_\nu = \oint I_\nu\cos\theta\,d\Omega$ [W m$^{-2}$ Hz$^{-1}$]; $K_\nu = \frac{1}{4\pi}\oint I_\nu\cos^2\theta\,d\Omega$ [same as $I_\nu$]. A pixel collects photons from a small solid angle, so it measures $I_\nu$ (the surface brightness). For an **unresolved** source the whole object falls in one pixel, and we measure $F_\nu$.

**Q2.** Prove that $I_\nu$ is constant along a ray in vacuum. Hence explain why the Sun's disk looks equally bright from Earth and from Mars.

> **A2.** See §2.3: energy conservation between two areas $dA_1$, $dA_2$ at distance $r$ gives $I_1dA_1(dA_2/r^2) = I_2dA_2(dA_1/r^2)$, so $I_1 = I_2$. From Mars the flux is lower by $(1/1.52)^2 = 0.43$, but the Sun's solid angle is smaller by the same factor. The surface brightness, i.e. $I_\nu$, is the same.

**Q3.** A surface emits $I(\mu) = I_0$ for $\mu > 0$ and nothing for $\mu < 0$. Find $J$, $F$ and $K$ at the surface. What is $J/F$?

> **A3.** $J = \tfrac12\int_0^1 I_0d\mu = I_0/2$; $F = 2\pi\int_0^1I_0\mu\,d\mu = \pi I_0$; $K = \tfrac12\int_0^1I_0\mu^2d\mu = I_0/6$. So $J/F = 1/(2\pi)$, i.e. $J = 2H$ where $H = F/4\pi$. This is **Eddington's surface boundary condition** $J(0) = 2H(0)$, used in Lecture SA5.

**Q4.** A star of radius $R$ and uniform surface intensity $I$ is observed from distance $d \gg R$. Derive $F = \pi I(R/d)^2$, and hence $L = 4\pi R^2\pi I$.

> **A4.** $F = \int I\cos\theta\,d\Omega$ over the cone $\theta\le\theta_c$, $\sin\theta_c = R/d$: $F = 2\pi I\int_0^{\theta_c}\cos\theta\sin\theta\,d\theta = \pi I\sin^2\theta_c = \pi I R^2/d^2$. Then $L = 4\pi d^2F = 4\pi R^2(\pi I)$, consistent with a surface flux $\pi I$.
