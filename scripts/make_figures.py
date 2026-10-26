"""
Generate every figure used in the course notes.

    python3 scripts/make_figures.py

Figures are written to ../figures/ as PNG (200 dpi).
"""
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle, Ellipse

sys.path.insert(0, os.path.dirname(__file__))
import lte_solvers as rt  # noqa: E402

c_light = rt.c
eV = rt.eV

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11,
    "legend.fontsize": 9.5, "figure.dpi": 100, "axes.grid": True,
    "grid.alpha": 0.25, "mathtext.fontset": "cm",
})
C = ["#1f5fa8", "#d1495b", "#2a9d8f", "#e9a03b", "#6a4c93", "#444444"]


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


def arrow(ax, p, q, color="k", lw=1.6, ms=14, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, **kw))


# =====================================================================
# Lecture 1 — the big picture: where RT sits between source and observer
# =====================================================================
def fig_overview():
    fig, ax = plt.subplots(figsize=(10, 3.4))
    ax.set_xlim(0, 10); ax.set_ylim(-0.7, 3.4); ax.axis("off")
    ax.add_patch(Circle((1.0, 1.7), 0.9, color="#f4a259"))
    ax.text(1.0, 1.7, "source\n(star, disk,\nCMB...)", ha="center", va="center", fontsize=10)
    ax.add_patch(Rectangle((3.6, 0.4), 2.6, 2.6, color="#9ec5e8", alpha=0.6))
    for _ in range(60):
        x, y = np.random.uniform(3.7, 6.1), np.random.uniform(0.5, 2.9)
        ax.plot(x, y, "o", ms=2.5, color="#1f5fa8")
    ax.text(4.9, 3.15, "medium: gas, dust, electrons", ha="center", fontsize=10)
    arrow(ax, (2.0, 1.7), (3.55, 1.7), color=C[1])
    ax.text(2.75, 1.85, r"$I_\nu(0)$", ha="center", color=C[1])
    arrow(ax, (6.25, 1.7), (8.3, 1.7), color=C[1])
    ax.text(7.25, 1.85, r"$I_\nu(s)$", ha="center", color=C[1])
    ax.text(4.9, 0.12, r"absorption $\alpha_\nu$,  emission $j_\nu$,  scattering",
            ha="center", fontsize=10)
    ax.add_patch(Polygon([[8.4, 1.2], [8.4, 2.2], [9.4, 2.5], [9.4, 0.9]], color="#555"))
    ax.text(8.9, 0.55, "telescope /\nspectrograph", ha="center", fontsize=9.5)
    ax.text(4.9, -0.5, r"$\dfrac{dI_\nu}{ds}=-\alpha_\nu I_\nu + j_\nu$", ha="center",
            fontsize=14, color=C[0])
    save(fig, "L01_overview.png")


# =====================================================================
# Lecture 2 — intensity, flux, constancy of I along rays
# =====================================================================
def fig_intensity_geometry():
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.set_xlim(-3, 4); ax.set_ylim(-1.6, 3.6); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Ellipse((0, 0), 2.4, 0.7, fc="#9ec5e8", ec="#1f5fa8", lw=1.5))
    ax.text(-1.55, -0.55, r"$dA$", fontsize=14, color="#1f5fa8")
    arrow(ax, (0, 0), (0, 2.8), color="k")
    ax.text(0.1, 2.9, r"$\hat{\mathbf{n}}$ (normal)", fontsize=12)
    d = np.array([np.sin(np.radians(40)), np.cos(np.radians(40))])
    arrow(ax, (0, 0), tuple(3.2 * d), color=C[1], lw=2.2)
    ax.text(*(3.25 * d + [0.05, 0.05]), r"direction $\hat{\mathbf{k}}$", color=C[1], fontsize=12)
    th = np.linspace(np.pi / 2, np.pi / 2 - np.radians(40), 40)
    ax.plot(0.9 * np.cos(th), 0.9 * np.sin(th), "k", lw=1)
    ax.text(0.22, 1.05, r"$\theta$", fontsize=14)
    # cone
    for ang in (34, 46):
        dd = np.array([np.sin(np.radians(ang)), np.cos(np.radians(ang))])
        ax.plot([0, 2.8 * dd[0]], [0, 2.8 * dd[1]], color=C[1], lw=0.8, ls="--")
    ax.add_patch(Ellipse(tuple(2.8 * d), 0.6, 0.22, angle=-40, fc="none", ec=C[1], lw=1.2))
    ax.text(1.05, 2.45, r"$d\Omega$", color=C[1], fontsize=14)
    ax.text(-2.9, -1.45,
            r"$dE = I_\nu\,\cos\theta\,dA\,d\Omega\,d\nu\,dt$", fontsize=13, color=C[0])
    save(fig, "L02_intensity_geometry.png")


def fig_constancy():
    fig, ax = plt.subplots(figsize=(9, 3.4))
    ax.set_xlim(-0.5, 10); ax.set_ylim(-2, 2); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0.6, 0), 0.8, color="#f6bd60"))
    ax.text(0.6, 0, "Sun", ha="center", va="center")
    for x, lab in ((4.0, r"$r_1$"), (8.6, r"$r_2=2r_1$")):
        ax.plot([0.6, x], [0.8, 0.02], color=C[1], lw=0.8)
        ax.plot([0.6, x], [-0.8, -0.02], color=C[1], lw=0.8)
        ax.plot(x, 0, "ko", ms=4)
        ax.text(x, -0.45, lab, ha="center", fontsize=12)
    ax.text(4.0, 1.25, r"$F_1$,  $\Delta\Omega_1$", ha="center", fontsize=12)
    ax.text(8.6, 1.25, r"$F_2=F_1/4$,  $\Delta\Omega_2=\Delta\Omega_1/4$", ha="center", fontsize=12)
    ax.text(5.0, -1.6, r"$I=F/\Delta\Omega$ is the same at both points: specific intensity is conserved along a ray in vacuum",
            ha="center", fontsize=11, color=C[0])
    save(fig, "L02_constancy.png")


# =====================================================================
# Lecture 3 — Planck function
# =====================================================================
def fig_planck():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    lam = np.logspace(np.log10(80e-9), np.log10(5e-6), 800)
    for T, col in zip((3000, 5772, 10000, 20000), C):
        B = rt.planck_lambda(lam, T)
        axs[0].loglog(lam * 1e9, B, color=col, label=f"T = {T} K")
        lpk = 2.897771955e-3 / T
        axs[0].plot(lpk * 1e9, rt.planck_lambda(lpk, T), "o", color=col, ms=5)
    lp = np.logspace(np.log10(140), np.log10(1000), 50) * 1e-9
    axs[0].loglog(lp * 1e9, rt.planck_lambda(lp, 2.897771955e-3 / lp), "k--", lw=1,
                  label=r"Wien peak $\lambda_{\max}T=2.898\times10^{-3}$ m K")
    axs[0].set_ylim(1e8, 3e16)
    axs[0].set_xlabel(r"wavelength $\lambda$ [nm]")
    axs[0].set_ylabel(r"$B_\lambda(T)$  [W m$^{-2}$ m$^{-1}$ sr$^{-1}$]")
    axs[0].axvspan(380, 750, color="gold", alpha=0.15)
    axs[0].text(420, 2e8, "visible", fontsize=9)
    axs[0].legend(loc="lower right")
    axs[0].set_title("Planck curves never cross: hotter is brighter at every $\\lambda$")

    T = 5772
    nu = np.logspace(11, 16, 600)
    x = rt.h * nu / (rt.k * T)
    B = rt.planck_nu(nu, T)
    RJ = 2 * nu**2 * rt.k * T / rt.c**2
    W = 2 * rt.h * nu**3 / rt.c**2 * np.exp(-x)
    axs[1].loglog(x, B, "k", lw=2.2, label="Planck")
    axs[1].loglog(x, RJ, color=C[0], ls="--", label=r"Rayleigh–Jeans  $2\nu^2kT/c^2$")
    axs[1].loglog(x, W, color=C[1], ls="--", label=r"Wien  $\frac{2h\nu^3}{c^2}e^{-h\nu/kT}$")
    axs[1].axvline(2.821, color=C[2], lw=1)
    axs[1].text(3.0, 1e-15, r"peak of $B_\nu$: $x=2.821$", color=C[2], fontsize=9.5)
    axs[1].set_ylim(1e-16, 1e-7)
    axs[1].set_xlabel(r"$x = h\nu/kT$")
    axs[1].set_ylabel(r"$B_\nu$  [W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$]")
    axs[1].set_title("Limits of the Planck function (T = 5772 K)")
    axs[1].legend(loc="lower center")
    save(fig, "L03_planck.png")


# =====================================================================
# Lecture 4 — emission/absorption processes; random walk
# =====================================================================
def fig_processes():
    fig, axs = plt.subplots(1, 4, figsize=(12, 3.1))
    titles = ["absorption", "spontaneous\nemission", "stimulated\nemission", "scattering"]
    for ax, t in zip(axs, titles):
        ax.set_xlim(0, 4); ax.set_ylim(-0.4, 3.2); ax.axis("off")
        ax.plot([1.2, 2.8], [0.4, 0.4], "k", lw=2); ax.plot([1.2, 2.8], [2.4, 2.4], "k", lw=2)
        ax.text(3.0, 0.35, "1", fontsize=11); ax.text(3.0, 2.35, "2", fontsize=11)
        ax.set_title(t, fontsize=11)

    def wave(ax, x0, y0, x1, y1, col):
        tt = np.linspace(0, 1, 200)
        xs = x0 + (x1 - x0) * tt; ys = y0 + (y1 - y0) * tt + 0.12 * np.sin(2 * np.pi * 6 * tt)
        ax.plot(xs, ys, color=col, lw=1.4)
        arrow(ax, (xs[-6], ys[-6]), (xs[-1], ys[-1]), color=col, ms=10)

    a = axs[0]; arrow(a, (2, 0.45), (2, 2.35), color=C[0]); wave(a, 0.0, 1.4, 1.75, 1.4, C[1])
    a.text(2, -0.3, r"$B_{12}\,\bar J$", ha="center")
    a = axs[1]; arrow(a, (2, 2.35), (2, 0.45), color=C[0]); wave(a, 2.2, 1.4, 4.0, 2.4, C[1])
    a.text(2, -0.3, r"$A_{21}$", ha="center")
    a = axs[2]; arrow(a, (2, 2.35), (2, 0.45), color=C[0]); wave(a, 0.0, 1.4, 1.75, 1.4, C[1])
    wave(a, 2.25, 1.6, 4.0, 1.6, C[1]); wave(a, 2.25, 1.1, 4.0, 1.1, C[1])
    a.text(2, -0.3, r"$B_{21}\,\bar J$  (same direction, phase)", ha="center", fontsize=9)
    a = axs[3]; a.plot(2, 1.4, "o", color=C[0], ms=10)
    wave(a, 0.0, 1.4, 1.8, 1.4, C[1]); wave(a, 2.2, 1.55, 3.4, 2.2, C[1])
    a.text(2, -0.3, r"$\alpha^{sc}_\nu$: direction changes", ha="center", fontsize=9)
    save(fig, "L04_processes.png")


def fig_random_walk():
    rng = np.random.default_rng(3)
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3))
    ax = axs[0]
    for col, seed in zip(C[:4], range(4)):
        r = np.random.default_rng(seed + 10)
        steps = r.normal(size=(400, 2)); steps /= np.linalg.norm(steps, axis=1)[:, None]
        p = np.vstack(([0, 0], np.cumsum(steps, axis=0)))
        ax.plot(p[:, 0], p[:, 1], color=col, lw=0.7)
        ax.plot(*p[-1], "o", color=col, ms=5)
    ax.add_patch(Circle((0, 0), 20, fill=False, ls="--", color="k"))
    ax.text(0, 21.5, r"$R_{\rm rms}=\sqrt{N}\,\ell=20\,\ell$ for $N=400$", ha="center")
    ax.set_aspect("equal"); ax.set_xlim(-38, 38); ax.set_ylim(-38, 38)
    ax.set_title("Photon random walk (step = mean free path $\\ell$)")
    ax = axs[1]
    Ns = np.arange(1, 2001)
    R2 = np.zeros_like(Ns, dtype=float)
    trials = 400
    for _ in range(trials):
        s = rng.normal(size=(2000, 3)); s /= np.linalg.norm(s, axis=1)[:, None]
        R2 += np.sum(np.cumsum(s, axis=0) ** 2, axis=1)
    R2 /= trials
    ax.loglog(Ns, np.sqrt(R2), color=C[0], label="simulation (3D, 400 photons)")
    ax.loglog(Ns, np.sqrt(Ns), "k--", label=r"$\sqrt{N}$")
    ax.set_xlabel("number of scatterings $N$"); ax.set_ylabel(r"$R_{\rm rms}/\ell$")
    ax.legend(); ax.set_title(r"$\langle R^2\rangle = N\ell^2 \;\Rightarrow\; N\simeq\tau^2$ to escape")
    save(fig, "L04_random_walk.png")


# =====================================================================
# Lecture 5 — formal solution: slab
# =====================================================================
def fig_slab():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    tau = np.linspace(0, 5, 300)
    S = 1.0
    for I0, col in zip((2.5, 1.6, 1.0, 0.5, 0.0), C):
        axs[0].plot(tau, I0 * np.exp(-tau) + S * (1 - np.exp(-tau)), color=col,
                    label=fr"$I_\nu(0)={I0}\,S_\nu$")
    axs[0].axhline(S, color="k", ls=":", lw=1)
    axs[0].set_xlabel(r"optical depth through slab $\tau_\nu$")
    axs[0].set_ylabel(r"$I_\nu(\tau_\nu)/S_\nu$")
    axs[0].set_title(r"$I_\nu=I_\nu(0)e^{-\tau_\nu}+S_\nu(1-e^{-\tau_\nu})$")
    axs[0].legend()
    # line formation through a slab: tau_nu = tau_c + tau_0 phi(nu)
    x = np.linspace(-5, 5, 600)
    phi = np.exp(-x**2)
    ax = axs[1]
    for (I0, S, lab, col) in ((1.0, 0.4, r"$I_{bg}>S$: absorption line", C[0]),
                              (0.0, 1.0, r"no background: emission line", C[1]),
                              (0.4, 1.0, r"$I_{bg}<S$: emission line", C[2])):
        tnu = 0.05 + 3.0 * phi
        ax.plot(x, I0 * np.exp(-tnu) + S * (1 - np.exp(-tnu)), color=col, label=lab)
    ax.set_xlabel(r"$(\nu-\nu_0)/\Delta\nu_D$")
    ax.set_ylabel(r"emergent $I_\nu$ (arb.)")
    ax.set_title(r"Isothermal slab, $\tau_\nu = 0.05+3\,e^{-x^2}$")
    ax.set_ylim(0, 1.45)
    ax.legend(loc="upper center", fontsize=8.8, ncol=1)
    save(fig, "L05_slab.png")


# =====================================================================
# Lecture 6 — LTE: Saha-Boltzmann; STE->LTE->NLTE regimes
# =====================================================================
def fig_saha():
    T = np.linspace(4000, 25000, 800)
    Pe = 20.0
    x = rt.saha_hydrogen(T, Pe)
    fion = x / (1 + x)
    bf = rt.balmer_fraction(T, Pe)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(T, fion, color=C[0], lw=2, label=r"ionized fraction $N_{\rm II}/N_{\rm tot}$ (Saha)")
    ax2 = ax.twinx()
    ax2.plot(T, bf * 1e5, color=C[1], lw=2, label=r"$N_2/N_{\rm tot}\times10^{5}$ (Saha+Boltzmann)")
    ax2.set_ylabel(r"$N_{2}/N_{\rm tot}$  [$10^{-5}$]", color=C[1])
    ax2.grid(False)
    Tp = T[np.argmax(bf)]
    ax2.axvline(Tp, color=C[1], ls=":")
    ax2.text(Tp + 1800, bf.max() * 1e5 * 0.82, f"Balmer lines strongest\nT ≈ {Tp:.0f} K", color=C[1])
    ax.set_xlabel("temperature T [K]"); ax.set_ylabel("ionized fraction", color=C[0])
    ax.set_title(r"Hydrogen in LTE, $P_e=20$ N m$^{-2}$ (A-star spectral sequence)")
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="center right")
    save(fig, "L06_saha_boltzmann.png")


def fig_regimes():
    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    cols = ["#e76f51", "#f4a261", "#e9c46a", "#a8dadc"]
    labs = ["STE\nstellar interior\n" r"$I_\nu=B_\nu$, $T_{rad}=T_{gas}$",
            "LTE\ndeep atmosphere\n" r"$S_\nu=B_\nu(T)$, $I_\nu\neq B_\nu$",
            "LTE breaking\n" r"$\tau\lesssim1$" "\nphotons escape",
            "NLTE\nupper layers / nebulae\nstatistical equilibrium"]
    for i, (cc, l) in enumerate(zip(cols, labs)):
        ax.add_patch(Rectangle((i * 2.5, 0.8), 2.5, 2.2, color=cc))
        ax.text(i * 2.5 + 1.25, 1.9, l, ha="center", va="center", fontsize=10)
    arrow(ax, (9.8, 0.45), (0.2, 0.45), color="k")
    ax.text(5, 0.12, r"increasing depth / density / collision rate  $\longleftarrow$", ha="center")
    ax.text(5, 3.25, r"photon mean free path $\ell_\gamma$ grows outward; particle mean free path stays $\ll \ell_\gamma$",
            ha="center", fontsize=10.5)
    save(fig, "L06_regimes.png")


# =====================================================================
# Lecture 7 — plane-parallel geometry, E_n, Eddington–Barbier
# =====================================================================
def fig_plane_parallel():
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.set_xlim(-0.5, 9); ax.set_ylim(-4.4, 1.6); ax.axis("off")
    for i, y in enumerate(np.linspace(0, -3.2, 9)):
        ax.add_patch(Rectangle((0, y - 0.4), 6, 0.4, color=plt.cm.YlOrRd(0.15 + 0.08 * i)))
    ax.plot([0, 6], [0, 0], "k", lw=2)
    ax.text(6.2, -0.05, r"surface $\tau_\nu=0$", fontsize=11)
    arrow(ax, (6.6, -0.6), (6.6, -3.2), color="k")
    ax.text(6.8, -2.0, r"$\tau_\nu$ increases inward" "\n" r"$d\tau_\nu=-\alpha_\nu dz$" "\n" r"$T$ increases inward",
            fontsize=10.5)
    ax.text(0.1, 1.2, "observer / space (no incident radiation)", fontsize=10)
    p = (3.0, -1.6)
    arrow(ax, p, (3.0, 0.9), color="k", lw=1)
    ax.text(3.05, 1.0, r"$z$ (outward normal)")
    th = np.radians(35)
    arrow(ax, p, (p[0] + 2.2 * np.sin(th), p[1] + 2.2 * np.cos(th)), color=C[0], lw=2.2)
    ax.text(p[0] + 2.3 * np.sin(th), p[1] + 2.3 * np.cos(th), r"$I^{+}(\tau,\mu)$, $\mu>0$",
            color=C[0], fontsize=11)
    arrow(ax, p, (p[0] - 1.3 * np.sin(th), p[1] - 1.3 * np.cos(th)), color=C[1], lw=2.2)
    ax.text(p[0] - 1.3 * np.sin(th) - 2.2, p[1] - 1.3 * np.cos(th) - 0.1, r"$I^{-}(\tau,\mu)$, $\mu<0$",
            color=C[1], fontsize=11, bbox=dict(fc="white", ec=C[1], alpha=0.9))
    a = np.linspace(np.pi / 2, np.pi / 2 - th, 30)
    ax.plot(p[0] + 0.7 * np.cos(a), p[1] + 0.7 * np.sin(a), "k", lw=1)
    ax.text(p[0] + 0.12, p[1] + 0.82, r"$\theta$", fontsize=12)
    ax.text(0.3, -4.25, r"$\mu\,\dfrac{dI_\nu}{d\tau_\nu}=I_\nu-S_\nu$,   $\mu=\cos\theta$",
            fontsize=13, color=C[0])
    save(fig, "L07_plane_parallel.png")


def fig_En():
    from scipy.special import expn
    x = np.linspace(0.001, 3, 400)
    fig, ax = plt.subplots(figsize=(6.4, 4))
    for n, col in zip((1, 2, 3), C):
        ax.plot(x, expn(n, x), color=col, label=fr"$E_{n}(x)$")
    ax.plot(x, np.exp(-x), "k:", label=r"$e^{-x}$")
    ax.set_ylim(0, 2.5); ax.set_xlabel("x")
    ax.set_title(r"Exponential integrals $E_n(x)=\int_1^\infty e^{-xt}t^{-n}dt$")
    ax.legend()
    save(fig, "L07_En.png")


def fig_eddington_barbier():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    tau = np.linspace(0, 4, 400)
    for mu, col in zip((1.0, 0.5, 0.2), C):
        axs[0].plot(tau, np.exp(-tau / mu) / mu, color=col, label=fr"$\mu={mu}$")
        axs[0].axvline(mu, color=col, ls=":")
    axs[0].set_xlabel(r"$\tau_\nu$"); axs[0].set_ylabel(r"weight  $e^{-\tau/\mu}/\mu$")
    axs[0].set_title(r"$I_\nu(0,\mu)=\int_0^\infty S_\nu(\tau)\,e^{-\tau/\mu}\,d\tau/\mu$")
    axs[0].legend(); axs[0].set_ylim(0, 2.5)
    axs[0].text(1.5, 1.6, r"mean depth seen: $\langle\tau\rangle=\mu$", fontsize=11)
    # limb-darkened Sun image
    ax = axs[1]
    n = 400
    yy, xx = np.mgrid[-1:1:n * 1j, -1:1:n * 1j]
    r2 = xx**2 + yy**2
    mu = np.sqrt(np.clip(1 - r2, 0, 1))
    img = 0.4 * (1 + 1.5 * mu)
    img[r2 > 1] = np.nan
    ax.imshow(img, cmap="afmhot", vmin=0, vmax=1.15, extent=(-1, 1, -1, 1))
    ax.set_title("Limb darkening: $I(\\mu)/I(1)=\\frac{2}{5}(1+\\frac{3}{2}\\mu)$")
    ax.axis("off")
    ax.annotate(r"centre: $\mu=1$, see $\tau\approx1$ (hot)", (0, 0), (-0.95, 1.12), fontsize=9.5,
                arrowprops=dict(arrowstyle="->"))
    ax.annotate(r"limb: $\mu\to0$, see $\tau\approx0$ (cool)", (0.99, 0), (0.15, -1.2), fontsize=9.5,
                arrowprops=dict(arrowstyle="->"))
    save(fig, "L07_eddington_barbier.png")


# =====================================================================
# Lecture 8 — scattering + thermal: thermalization, Lambda iteration
# =====================================================================
def fig_scattering():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4))
    ax = axs[0]
    for eps, col in zip((1.0, 1e-1, 1e-2, 1e-3), C):
        if eps == 1.0:
            t = np.logspace(-3, 3, 50); S = np.ones_like(t)
        else:
            t, S = rt.solve_scattering_atmosphere(eps)
        ax.semilogx(np.maximum(t, 1e-4), S, color=col, lw=2, label=fr"$\varepsilon={eps:g}$")
        if eps < 1:
            ax.axvline(1 / np.sqrt(eps), color=col, ls=":", lw=1)
            # Eddington approximation
            tt = np.logspace(-4, 3.5, 300)
            Cc = -1.0 / (1 + 2 * np.sqrt(eps / 3))
            J = 1 + Cc * np.exp(-np.sqrt(3 * eps) * tt)
            ax.semilogx(tt, eps + (1 - eps) * J, color=col, ls="--", lw=1)
            ax.plot(1e-4, np.sqrt(eps), "o", color=col)
    ax.set_xlim(1e-4, 3e3); ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$S/B$")
    ax.set_title(r"$S=\varepsilon B+(1-\varepsilon)J$, isothermal ($B$ = const)")
    ax.text(1.3e-4, 0.92, "solid: exact (numerical)\ndashed: Eddington approx.\n"
            r"dots: $S(0)=\sqrt{\varepsilon}\,B$;  vertical: $\tau_{th}=1/\sqrt{\varepsilon}$",
            fontsize=8.8, va="top")
    ax.legend(loc="lower right")

    ax = axs[1]
    eps = 1e-2
    t, Sex = rt.solve_scattering_atmosphere(eps)
    _, its = rt.lambda_iteration(eps, 200, tau=t)
    ax.semilogx(np.maximum(t, 1e-4), Sex, "k", lw=2.5, label="exact")
    for n, col in zip((0, 1, 3, 10, 50, 200), C + ["#999"]):
        ax.semilogx(np.maximum(t, 1e-4), its[n], color=col, lw=1.2, label=f"iteration {n}")
    ax.set_xlim(1e-4, 3e3); ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$S/B$")
    ax.set_title(r"$\Lambda$-iteration, $\varepsilon=0.01$: each step reaches only $\Delta\tau\sim1$")
    ax.legend(fontsize=8.5, loc="lower right")
    save(fig, "L08_scattering.png")


# =====================================================================
# Lecture 9 — gray LTE atmosphere
# =====================================================================
def fig_gray():
    t, q = rt.hopf_function()
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.2))
    ax = axs[0]
    tt = np.maximum(t, 1e-4)
    ax.semilogx(tt, (0.75 * (t + 2 / 3)) ** 0.25, color=C[0], lw=2, label=r"Eddington: $q=2/3$")
    ax.semilogx(tt, (0.75 * (t + q)) ** 0.25, color=C[1], lw=2, ls="--", label=r"exact: $q(\tau)$ (Hopf)")
    ax.axhline(1, color="k", ls=":"); ax.axvline(2 / 3, color="k", ls=":")
    ax.text(0.75, 0.86, r"$T=T_{\rm eff}$ at $\tau=2/3$", fontsize=9.5)
    ax.set_xlabel(r"$\tau$ (Rosseland/gray)"); ax.set_ylabel(r"$T/T_{\rm eff}$")
    ax.set_xlim(1e-4, 30); ax.set_title(r"$T^4=\frac{3}{4}T_{\rm eff}^4[\tau+q(\tau)]$")
    ax.legend(loc="upper left")
    ax = axs[1]
    ax.semilogx(tt, q, color=C[1], lw=2, label="exact $q(\\tau)$ (this course's solver)")
    ax.axhline(2 / 3, color=C[0], label="Eddington 2/3")
    ax.axhline(1 / np.sqrt(3), color="k", ls=":", lw=1); ax.text(1.2e-4, 0.582, r"$1/\sqrt{3}$")
    ax.axhline(rt.Q_INF, color="k", ls=":", lw=1); ax.text(1.2e-4, 0.715, "0.7104")
    ax.set_xlim(1e-4, 30); ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$q(\tau)$")
    ax.set_title("Hopf function"); ax.legend(loc="center right")
    ax = axs[2]
    mu = np.linspace(0, 1, 101)
    H = rt.chandrasekhar_H(mu)
    ax.plot(mu, H / H[-1], color=C[1], lw=2, ls="--", label="exact gray (Chandrasekhar $H$)")
    ax.plot(mu, 0.4 * (1 + 1.5 * mu), color=C[0], lw=2, label=r"Eddington $\frac{2}{5}(1+\frac{3}{2}\mu)$")
    # Chandrasekhar (1950) Table, I(0,mu)/I(0,1) isotropic
    muC = np.array([0, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95, 1])
    IC = np.array([.34390, .39094, .42897, .46455, .49878, .53213, .56486, .59715, .62909, .66075,
                   .69220, .72346, .75456, .78554, .81641, .84719, .87788, .90850, .93905, .96955, 1.0])
    ax.plot(muC, IC, "ko", ms=3.5, label="Chandrasekhar (1950) table")
    ax.set_xlabel(r"$\mu=\cos\theta$"); ax.set_ylabel(r"$I(0,\mu)/I(0,1)$")
    ax.set_title("Emergent intensity (limb darkening)"); ax.legend(loc="lower right")
    save(fig, "L09_gray_atmosphere.png")


# =====================================================================
# Lecture 10 — LTE line formation: Milne-Eddington, curve of growth
# =====================================================================
def fig_lines():
    fig, axs = plt.subplots(1, 3, figsize=(14.5, 4.2))
    ax = axs[0]
    tau = np.linspace(0, 3, 300)
    beta = 1.5
    ax.plot(tau, 1 + beta * tau, "k", lw=2, label=r"$S=B=B_0(1+\beta\tau_c)$")
    for eta, col in zip((0, 3, 20), C):
        tc_eff = (2 / 3) / (1 + eta)
        ax.plot(tc_eff, 1 + beta * tc_eff, "o", color=col, ms=8,
                label=fr"$\eta={eta}$: $\tau_\nu=2/3$ at $\tau_c={tc_eff:.2f}$")
    ax.set_xlabel(r"continuum optical depth $\tau_c$"); ax.set_ylabel(r"$S/B_0$")
    ax.set_title("Line photons escape from higher, cooler layers")
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axs[1]
    v = np.linspace(-6, 6, 800)
    for eta0, col in zip((0.3, 1, 3, 10, 100), C):
        ax.plot(v, rt.milne_eddington_residual(v, eta0, beta), color=col, label=fr"$\eta_0={eta0}$")
    ax.axhline(1 / (1 + 2 * beta / 3), color="k", ls=":")
    ax.text(2.2, 0.515, "saturation limit", fontsize=9)
    ax.set_xlabel(r"$v=(\nu-\nu_0)/\Delta\nu_D$"); ax.set_ylabel(r"$F_\nu/F_c$")
    ax.set_title(r"Milne–Eddington LTE profiles ($\beta=1.5$)"); ax.legend(fontsize=8.5, loc="lower left", bbox_to_anchor=(0.0, 0.08))
    ax = axs[2]
    etas = np.logspace(-2, 6, 50)
    for a_d, col, lab in ((0.0, C[0], "Gaussian (no damping)"), (1e-2, C[1], r"Voigt, $a=0.01$")):
        W = np.array([rt.equivalent_width(e, beta, a_d) for e in etas])
        ax.loglog(etas, W, color=col, lw=2, label=lab)
    ax.loglog(etas[:20], np.sqrt(np.pi) * etas[:20] * (2 * beta / 3) / (1 + 2 * beta / 3), "k:",
              label=r"linear: $W\propto\eta_0\propto N$")
    ax.set_xlabel(r"line strength $\eta_0\propto N f$"); ax.set_ylabel(r"$W/\Delta\nu_D$")
    ax.set_title("Curve of growth"); ax.legend(fontsize=8.5, loc="upper left")
    ax.text(30, 0.6, "flat\n" r"$W\propto\sqrt{\ln\eta_0}$", fontsize=9)
    ax.text(1e4, 8, r"damping: $W\propto\sqrt{\eta_0}$", fontsize=9)
    save(fig, "L10_lines.png")


def fig_two_stream():
    """Two-stream / Eddington solution for an LTE slab (lecture 8 example)."""
    fig, ax = plt.subplots(figsize=(6.6, 4))
    tau = np.linspace(0, 6, 400)
    for eps, col in zip((1.0, 0.3, 0.05), C):
        k_ = np.sqrt(3 * eps)
        Cc = -1.0 / (1 + 2 * np.sqrt(eps / 3))
        J = 1 + Cc * np.exp(-k_ * tau)
        ax.plot(tau, J, color=col, label=fr"$J/B$, $\varepsilon={eps}$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$J/B$")
    ax.set_title(r"Eddington solution: $J=B\,[1-\frac{e^{-\sqrt{3\varepsilon}\tau}}{1+2\sqrt{\varepsilon/3}}]$")
    ax.legend()
    save(fig, "L08_eddington_J.png")


def gray_emergent(lam, Teff=5772.0, mu=None):
    """LTE emergent intensity / flux of the exact gray atmosphere at wavelength lam."""
    from scipy.special import expn
    global _HOPF
    if "_HOPF" not in globals():
        _HOPF = rt.hopf_function()
    t, q = _HOPF
    tau = np.concatenate((np.linspace(0, 1, 400), np.linspace(1.0025, 30, 2000)))
    qq = np.interp(tau, t, q)
    T = Teff * (0.75 * (tau + qq)) ** 0.25
    B = rt.planck_lambda(lam, T)
    if mu is None:   # flux F = 2 pi int B E2 dtau
        return 2 * np.pi * np.trapezoid(B * expn(2, tau), tau)
    return np.array([np.trapezoid(B * np.exp(-tau / m) / m, tau) for m in mu])


def fig_gray_spectrum():
    Teff = 5772.0
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.3))
    lam = np.linspace(150e-9, 2500e-9, 240)
    F = np.array([gray_emergent(l, Teff) for l in lam])
    ax = axs[0]
    ax.plot(lam * 1e9, F / 1e13, color=C[1], lw=2, label="gray LTE atmosphere (exact $T(\\tau)$)")
    ax.plot(lam * 1e9, np.pi * rt.planck_lambda(lam, Teff) / 1e13, "k--", label=r"$\pi B_\lambda(T_{\rm eff})$")
    ax.set_xlabel(r"$\lambda$ [nm]"); ax.set_ylabel(r"$F_\lambda$ [$10^{13}$ W m$^{-2}$ m$^{-1}$]")
    ax.set_title(r"Emergent flux, $T_{\rm eff}=5772$ K: same $\int F_\lambda d\lambda$, different shape")
    ax.legend()
    ax = axs[1]
    mu = np.linspace(0.02, 1, 40)
    for l, col in zip((400e-9, 550e-9, 800e-9, 1600e-9), C):
        I = gray_emergent(l, Teff, mu)
        ax.plot(mu, I / I[-1], color=col, lw=2, label=f"{l*1e9:.0f} nm")
    Hm = rt.chandrasekhar_H(mu)
    ax.plot(mu, Hm / Hm[-1], "k:", lw=1.5, label="bolometric (exact gray)")
    ax.set_xlabel(r"$\mu$"); ax.set_ylabel(r"$I_\lambda(0,\mu)/I_\lambda(0,1)$")
    ax.set_title("Monochromatic limb darkening is stronger in the blue")
    ax.legend(loc="lower right")
    save(fig, "L09_gray_spectrum.png")


# =====================================================================
# MIT 8.901 Lecture 7 material: RTE build-up, thin cloud, two-layer star
# =====================================================================
def fig_mit_rte_panels():
    """MIT 8.901 Fig. 9: vacuum -> absorbing -> absorbing + emitting."""
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.0))
    titles = [r"vacuum: $dI_\nu/ds=0$", r"absorber: $dI_\nu/ds=-\alpha_\nu I_\nu$",
              r"absorber + emitter: $dI_\nu/ds=j_\nu-\alpha_\nu I_\nu$"]
    rng = np.random.default_rng(4)
    for i, (ax, t) in enumerate(zip(axs, titles)):
        ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off"); ax.set_title(t, fontsize=11)
        if i > 0:
            ax.add_patch(Rectangle((3, 0.6), 4, 2.8, color="#9ec5e8", alpha=0.6))
            pts = rng.uniform([3.2, 0.8], [6.8, 3.2], size=(25, 2))
            ax.plot(pts[:, 0], pts[:, 1], "o", ms=2.5, color="#1f5fa8")
        widths = {0: (2.6, 2.6), 1: (2.6, 1.0), 2: (2.6, 1.8)}[i]
        arrow(ax, (0.3, 2.0), (2.9, 2.0), color=C[1], lw=widths[0])
        arrow(ax, (7.1, 2.0), (9.7, 2.0), color=C[1], lw=widths[1])
        ax.text(1.6, 2.35, r"$I_0$", ha="center", color=C[1])
        lab = {0: r"$I=I_0$", 1: r"$I=I_0e^{-\tau}$", 2: r"$I=I_0e^{-\tau}+S(1-e^{-\tau})$"}[i]
        ax.text(8.4, 2.35 if i < 2 else 0.2, lab, ha="center", color=C[1], fontsize=10)
        if i == 2:
            for y in (1.2, 2.6):
                arrow(ax, (5.0, y), (6.4, y + 0.5), color=C[3], lw=1.2, ms=9)
            ax.text(5.0, 3.55, r"$j_\nu$", color=C[3], ha="center")
    save(fig, "L05_mit_rte_panels.png")


def _hydrogen_lines(lam_nm, tau0=3.0, width_nm=1.2, n1_list=(2, 3)):
    """Optical depth profile of Balmer + Paschen lines (Rydberg formula).
    Lines are artificially broadened (width_nm) so they are visible on the plot."""
    R_H = 1.09678e7
    tau = np.zeros_like(lam_nm)
    for n1 in n1_list:
        for n2 in range(n1 + 1, n1 + 12):
            lam0 = 1e9 / (R_H * (1 / n1**2 - 1 / n2**2))
            strength = tau0 * ((n1 + 1) / n2) ** 3 * (1.0 if n1 == 2 else 0.6)
            tau += strength * np.exp(-((lam_nm - lam0) / width_nm) ** 2)
    return tau


def fig_mit_two_layer():
    """MIT 8.901 Figs. 10-11: thin hot cloud, two-layer star, thermal inversion."""
    lam = np.linspace(360, 1000, 4000)
    L = lam * 1e-9
    tau_l = _hydrogen_lines(lam)
    tau_c = 0.02
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.2))
    # (a) thin hot cloud on dark sky
    T = 8000.0
    tau = tau_c + 0.15 * tau_l
    I = rt.planck_lambda(L, T) * (1 - np.exp(-tau))
    axs[0].plot(lam, I / 1e12, color=C[1])
    axs[0].set_title(r"(a) thin H cloud, $T=8000$ K, dark background:" "\n" r"$I_\nu\approx\tau_\nu B_\nu(T)$ → emission lines")
    # (b) two-layer star T_H > T_C
    TH, TC = 6500.0, 4500.0
    for ax, (Tbase, Ttop, ttl) in zip(axs[1:], ((TH, TC, "(b) two-layer star, $T_C<T_H$:\nabsorption lines"),
                                               (TC, TH, "(c) thermal inversion, $T_{top}>T_{base}$:\nemission lines"))):
        tau = tau_c + tau_l
        I = rt.planck_lambda(L, Tbase) * np.exp(-tau) + rt.planck_lambda(L, Ttop) * (1 - np.exp(-tau))
        ax.plot(lam, I / 1e12, color=C[0], lw=1.3, label=r"$I_\nu=B_\nu(T_{base})e^{-\tau_\nu}+B_\nu(T_{top})(1-e^{-\tau_\nu})$")
        ax.plot(lam, rt.planck_lambda(L, Tbase) / 1e12, "k--", lw=1, label=fr"$B_\lambda$({Tbase:.0f} K) base")
        ax.plot(lam, rt.planck_lambda(L, Ttop) / 1e12, ":", color=C[1], lw=1.4, label=fr"$B_\lambda$({Ttop:.0f} K) top layer")
        ax.set_title(ttl)
        ax.legend(fontsize=8, loc="upper right")
    for ax in axs:
        ax.set_xlabel(r"$\lambda$ [nm]  (Balmer + Paschen series; lines widened for display)")
        ax.set_ylabel(r"$I_\lambda$ [$10^{12}$ W m$^{-3}$ sr$^{-1}$]")
        ax.xaxis.label.set_size(9)
    axs[1].set_ylim(0, 1.45 * rt.planck_lambda(L, TH).max() / 1e12)
    axs[2].set_ylim(0, 1.45 * rt.planck_lambda(L, TH).max() / 1e12)
    save(fig, "L05_mit_two_layer.png")


if __name__ == "__main__" and not any(f in sys.argv for f in ("--part2", "--sa", "--concepts")):
    np.random.seed(1)
    fig_overview(); fig_intensity_geometry(); fig_constancy(); fig_planck()
    fig_processes(); fig_random_walk(); fig_slab(); fig_saha(); fig_regimes()
    fig_plane_parallel(); fig_En(); fig_eddington_barbier(); fig_scattering()
    fig_two_stream(); fig_gray(); fig_gray_spectrum(); fig_lines()
    fig_mit_rte_panels(); fig_mit_two_layer()
    fig_rte_element(); fig_rte_hierarchy(); fig_history(); fig_polarization(); fig_nlte(); fig_solar_atmosphere()
    fig_sa_opacity(); fig_sa_rates(); fig_sa_broadening()


# =====================================================================
# Part II figures (Lectures 11-15)
# =====================================================================
def fig_rte_element():
    """Lecture 11: bookkeeping of a pencil of radiation through a cylinder."""
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.set_xlim(0, 10); ax.set_ylim(-0.4, 5.4); ax.axis("off")
    ax.add_patch(Ellipse((2.5, 2.2), 0.6, 1.8, fc="#9ec5e8", ec=C[0], lw=1.5))
    ax.add_patch(Ellipse((7.5, 2.2), 0.6, 1.8, fc="#9ec5e8", ec=C[0], lw=1.5, alpha=.6))
    ax.plot([2.5, 7.5], [3.1, 3.1], color=C[0], lw=1.2); ax.plot([2.5, 7.5], [1.3, 1.3], color=C[0], lw=1.2)
    ax.text(2.5, 0.95, r"$dA$", ha="center", color=C[0], fontsize=12)
    ax.annotate("", (7.5, 0.75), (2.5, 0.75), arrowprops=dict(arrowstyle="<->", color="k"))
    ax.text(5, 0.45, r"$ds$", ha="center", fontsize=12)
    arrow(ax, (0.3, 2.2), (2.2, 2.2), color=C[1], lw=2.6)
    ax.text(1.2, 2.45, r"$I_\nu(s)$", color=C[1], ha="center", fontsize=12)
    arrow(ax, (7.8, 2.2), (9.7, 2.2), color=C[1], lw=2.6)
    ax.text(8.8, 2.45, r"$I_\nu(s+ds)$", color=C[1], ha="center", fontsize=12)
    # losses
    arrow(ax, (4.0, 2.6), (4.0, 4.1), color=C[5], lw=1.5); ax.text(4.05, 4.15, "absorbed\n" r"$-\kappa_\nu\rho I_\nu ds$", fontsize=9.5, va="bottom")
    arrow(ax, (5.0, 2.4), (5.9, 3.9), color=C[4], lw=1.5); ax.text(5.9, 3.95, "scattered out\n" r"$-\sigma_\nu\rho I_\nu ds$", fontsize=9.5, va="bottom")
    # gains
    arrow(ax, (3.6, 0.0 + 0.2), (4.2, 1.9), color=C[2], lw=1.5); ax.text(2.2, -0.15, r"emitted $+j_\nu ds$", fontsize=9.5, color=C[2])
    arrow(ax, (6.6, 0.2), (6.0, 1.9), color=C[3], lw=1.5); ax.text(6.75, -0.15, "scattered in\n" r"$+\sigma_\nu\rho J_\nu ds$", fontsize=9.5, color=C[3])
    ax.text(5.0, 5.15, r"$I_\nu(s+ds)-I_\nu(s)=$ gains $-$ losses", ha="center", fontsize=12, color=C[0])
    save(fig, "L11_rte_element.png")


def fig_rte_hierarchy():
    fig, ax = plt.subplots(figsize=(10, 6.6))
    ax.set_xlim(0, 10); ax.set_ylim(-1.05, 10.4); ax.axis("off")
    boxes = [
        (9.6, "Boltzmann equation for photons",
         r"$\partial_t f+c\,\hat{n}\cdot\nabla f+\dot{p}\,\partial_p f=(\partial_t f)_{\rm coll}$"),
        (7.6, r"multiply by $h^4\nu^3/c^3$, use $I_\nu=(h^4\nu^3/c^2)f$",
         r"$\frac{1}{c}\partial_t I_\nu+\hat{n}\cdot\nabla I_\nu=j_\nu-\alpha_\nu I_\nu+$ scattering in"),
        (5.6, r"static medium ($t_{\rm light}\ll t_{\rm evol}$), no refraction or gravity",
         r"$\frac{dI_\nu}{ds}=j_\nu-\alpha_\nu I_\nu$  (along a straight ray)"),
        (3.6, r"plane-parallel layers, $\mu=\cos\theta$, $d\tau=-\alpha dz$",
         r"$\mu\frac{dI_\nu}{d\tau_\nu}=I_\nu-S_\nu$"),
        (1.6, "integrating factor, boundary conditions",
         r"$I_\nu(0,\mu)=\int_0^\infty S_\nu e^{-\tau/\mu}d\tau/\mu$"),
        (-0.2, r"moments: $\frac{dH}{d\tau}=J-S$, $\frac{dK}{d\tau}=H$; closure $K=J/3$", ""),
    ]
    for i, (y, cap, eq) in enumerate(boxes):
        ax.add_patch(Rectangle((0.6, y - 0.7), 8.8, 1.4, fc=plt.cm.Blues(0.12 + 0.07 * i), ec=C[0], lw=1))
        ax.text(5, y + (0.35 if eq else 0), cap, ha="center", va="center", fontsize=10.5)
        if eq:
            ax.text(5, y - 0.25, eq, ha="center", va="center", fontsize=11.5, color=C[0])
        if i < len(boxes) - 1:
            arrow(ax, (5, y - 0.72), (5, boxes[i + 1][0] + 0.72), color="k", lw=1.2, ms=10)
    save(fig, "L11_rte_hierarchy.png")


def fig_history():
    fig, ax = plt.subplots(figsize=(12, 5.2))
    ax.set_xlim(1895, 2025); ax.set_ylim(-4.4, 3.6); ax.axis("off")
    ax.plot([1897, 2023], [0, 0], color="k", lw=1.5)
    for yr in range(1900, 2021, 20):
        ax.plot([yr, yr], [-0.12, 0.12], color="k"); ax.text(yr, -0.42, str(yr), ha="center", fontsize=9.5)
    ax.axvspan(1895, 1960, ymin=0.5, ymax=1, color=C[0], alpha=0.06)
    ax.axvspan(1960, 2025, ymin=0, ymax=0.5, color=C[1], alpha=0.06)
    ax.text(1897, 3.35, "analytic era: approximations & exact solutions", fontsize=10.5, color=C[0], weight="bold")
    ax.text(2023, -4.25, "numerical era: computers, NLTE, 3D", fontsize=10.5, color=C[1], weight="bold", ha="right")
    up = [(1905, "Schuster: two-stream\nscattering atmosphere", 1.0), (1906, "Schwarzschild:\nradiative equilibrium", 2.3),
          (1921, "Milne: integral\nequations", 1.0), (1926, "Eddington\napproximation", 2.3), (1934, "Hopf: exact\ngray solution", 1.0),
          (1943, "Ambartsumian:\ninvariance", 2.3), (1950, "Chandrasekhar:\ndiscrete ordinates,\nH-functions, polarization", 1.0)]
    down = [(1957, "Sobolev:\nmoving envelopes", -0.8), (1964, "Feautrier\nmethod", -1.9), (1969, "Auer & Mihalas:\ncomplete\nlinearization", -2.95),
            (1973, "Cannon:\noperator\nperturbation", -0.8), (1986, "Olson, Auer &\nBuchler: ALI", -1.9), (1987, "short\ncharacteristics", -0.8),
            (1995, "Hubeny & Lanz: CL/ALI;\nTrujillo Bueno: GS/SOR", -2.95), (2005, "3D radiation-\nhydrodynamics", -0.8)]
    for yr, lab, y in up + down:
        ax.plot([yr, yr], [0, y * (0.75 if y > 0 else 0.92)], color=C[0] if y > 0 else C[1], lw=1)
        ax.plot(yr, 0, "o", color=C[0] if y > 0 else C[1], ms=6)
        ax.text(yr, y, lab, ha="center", va="bottom" if y > 0 else "top", fontsize=8.8)
    save(fig, "L12_history.png")


def fig_polarization():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4))
    ax = axs[0]
    th = np.linspace(0, 2 * np.pi, 300)
    a, b, chi = 1.0, 0.45, np.radians(30)
    x = a * np.cos(th) * np.cos(chi) - b * np.sin(th) * np.sin(chi)
    y = a * np.cos(th) * np.sin(chi) + b * np.sin(th) * np.cos(chi)
    ax.plot(x, y, color=C[0], lw=2.2)
    ax.annotate("", (x[40], y[40]), (x[30], y[30]), arrowprops=dict(arrowstyle="-|>", color=C[0], lw=1.5))
    ax.axhline(0, color="k", lw=.8); ax.axvline(0, color="k", lw=.8)
    ax.plot([0, 1.2 * np.cos(chi)], [0, 1.2 * np.sin(chi)], "--", color=C[1])
    ax.text(0.45, 0.08, r"$\chi$", fontsize=13, color=C[1])
    ax.text(1.18, -0.12, r"$E_x$"); ax.text(0.04, 1.12, r"$E_y$")
    ax.set_aspect("equal"); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.grid(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Polarization ellipse traced by the electric vector")
    ax.text(-1.25, -1.25, r"$Q=I_p\cos2\beta\cos2\chi$" "\n" r"$U=I_p\cos2\beta\sin2\chi$" "\n" r"$V=I_p\sin2\beta$,  $\tan\beta=b/a$",
            fontsize=10, va="bottom")
    ax = axs[1]
    mu = np.arange(0, 1.0001, 0.05)
    deg = np.array([.11713, .08979, .07448, .06311, .05410, .04667, .04041, .03502, .03033, .02619, .02252, .01923, .01627, .01358,
                    .011123, .008880, .006818, .004919, .003155, .001522, 0])
    Il = np.array([.28823, .34053, .38203, .42070, .45782, .49394, .52939, .56432, .59888, .63313, .66714, .70095, .73459, .76809,
                   .80147, .83475, .86794, .90105, .93409, .96707, 1.0])
    Ir = np.array([.36470, .40771, .44352, .47739, .51019, .54231, .57397, .60529, .63634, .66719, .69788, .72844, .75888, .78924,
                   .81950, .84971, .87986, .90996, .94001, .97002, 1.0])
    ax.plot(mu, 100 * deg, "o-", color=C[1], ms=4, label="degree of polarization [%]")
    ax.set_xlabel(r"$\mu=\cos\theta$  (1 = disk centre, 0 = limb)"); ax.set_ylabel("polarization [%]")
    ax.set_title("Electron-scattering atmosphere (Chandrasekhar 1950, Table XXIV)")
    ax2 = ax.inset_axes([0.45, 0.45, 0.5, 0.48])
    ax2.plot(mu, Il, color=C[0], label=r"$I_l$ (E in meridian plane)"); ax2.plot(mu, Ir, color=C[2], ls="--", label=r"$I_r$ (E parallel to limb)")
    ax2.set_title("law of darkening, two polarizations", fontsize=8.5); ax2.tick_params(labelsize=8); ax2.legend(fontsize=7.5, loc="lower right")
    ax.text(0.02, 11.9, "11.7 % at the limb", fontsize=9.5)
    save(fig, "L13_polarization.png")


def fig_nlte():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4))
    ax = axs[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    ax.plot([2, 8], [1, 1], "k", lw=2); ax.plot([2, 8], [4.6, 4.6], "k", lw=2)
    ax.text(8.2, 0.95, "lower level 1", va="center"); ax.text(8.2, 4.55, "upper level 2", va="center")
    arrow(ax, (3, 1.05), (3, 4.55), color=C[0], lw=1.8); ax.text(2.9, 2.8, r"$n_1B_{12}\bar J$", ha="right", color=C[0])
    arrow(ax, (4.2, 4.55), (4.2, 1.05), color=C[0], lw=1.8); ax.text(4.3, 2.8, r"$n_2(A_{21}+B_{21}\bar J)$", ha="left", color=C[0])
    arrow(ax, (6.6, 1.05), (6.6, 4.55), color=C[1], lw=1.8, style="-|>"); ax.text(6.5, 3.6, r"$n_1C_{12}$", ha="right", color=C[1])
    arrow(ax, (7.4, 4.55), (7.4, 1.05), color=C[1], lw=1.8); ax.text(7.5, 2.0, r"$n_2C_{21}$", ha="left", color=C[1])
    ax.text(5, 5.5, "radiative (blue) vs collisional (red) rates", ha="center", fontsize=10.5)
    ax.text(5, 0.25, r"statistical equilibrium: rates in = rates out", ha="center", fontsize=10.5)
    ax = axs[1]
    beta = 0.2
    tt = rt.tau_grid(tau_max=5000.0, n=240)
    L = rt.lambda_matrix(tt)
    keep = tt <= 300
    for eps, col in zip((1.0, 0.1, 1e-2, 1e-3), C):
        A = np.eye(len(tt)) - (1 - eps) * L
        S = np.linalg.solve(A, eps * (1 + beta * tt))
        ax.semilogx(np.maximum(tt[keep], 1e-4), (S / (1 + beta * tt))[keep], color=col, lw=2,
                    label=fr"$\varepsilon={eps:g}$" + (" (LTE)" if eps == 1 else f", $S(0)/B(0)={S[0]/1:.3f}$"))
    ax.set_xlim(1e-4, 300); ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"line optical depth $\tau$"); ax.set_ylabel(r"$S^{\rm line}/B$")
    ax.set_title(r"Two-level atom, $B=B_0(1+0.2\tau)$: NLTE source function")
    ax.legend(loc="lower right")
    save(fig, "L14_nlte.png")


def fig_solar_atmosphere():
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
    ax = axs[0]
    h = np.array([-100, 0, 100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1500, 1800, 2000, 2100, 2150, 2200, 2250, 2300, 2400, 3000, 6000])
    T = np.array([7800, 6420, 5650, 5150, 4750, 4400, 4170, 4250, 5300, 6000, 6300, 6600, 7000, 7500, 8500, 1.5e4, 5e4, 2e5, 5e5, 9e5, 1.3e6, 1.6e6])
    ax.semilogy(h, T, color=C[1], lw=2.5)
    for x0, x1, lab, col in ((-100, 500, "photosphere", C[3]), (500, 2100, "chromosphere", C[1]), (2100, 2300, "TR", C[4]), (2300, 6000, "corona", C[0])):
        ax.axvspan(x0, x1, color=col, alpha=.1)
        ax.text((x0 + x1) / 2 if lab != "TR" else 2200, 2.5e6, lab, ha="center", fontsize=9.5)
    ax.annotate("temperature minimum\n~4200 K", (500, 4170), (900, 2200), arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    ax.annotate(r"$\tau_{500}=1$", (0, 6420), (-80, 1.5e4), arrowprops=dict(arrowstyle="->"), fontsize=9.5)
    ax.set_xlim(-100, 6000); ax.set_ylim(2e3, 4e6)
    ax.set_xlabel("height above $\\tau_{500}=1$ [km]"); ax.set_ylabel("temperature [K]")
    ax.set_title("Solar atmosphere (schematic, after the VAL-C model)")
    ax = axs[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    steps = ["inputs: $T_{\\rm eff}$, $\\log g$, composition, $\\xi$", "starting model: gray $T(\\tau)$",
             "hydrostatic equilibrium → $P(\\tau)$", "EOS: Saha–Boltzmann (LTE) or rate equations (NLTE)",
             "opacities $\\kappa_\\nu$, $j_\\nu$ at ~$10^{5}$ frequencies", "solve RTE → $J_\\nu$, $F_\\nu$",
             "check flux constancy + radiative/convective equilibrium", "correct $T(\\tau)$ (Unsöld–Lucy) → iterate"]
    for i, s_ in enumerate(steps):
        y = 9.3 - i * 1.18
        ax.add_patch(Rectangle((0.4, y - 0.42), 8.6, 0.84, fc=plt.cm.Oranges(0.1 + 0.05 * i), ec=C[1], lw=1))
        ax.text(4.7, y, s_, ha="center", va="center", fontsize=9.8)
        if i < len(steps) - 1:
            arrow(ax, (4.7, y - 0.44), (4.7, y - 0.74), color="k", lw=1, ms=8)
    ax.annotate("", (9.2, 6.95), (9.2, 1.05), arrowprops=dict(arrowstyle="-|>", color=C[1], lw=1.5, connectionstyle="arc3,rad=-0.3"))
    ax.set_title("Computing a model atmosphere")
    save(fig, "L15_atmospheres.png")


if __name__ == "__main__" and "--part2" in sys.argv:
    fig_rte_element(); fig_rte_hierarchy(); fig_history(); fig_polarization(); fig_nlte(); fig_solar_atmosphere()


# =====================================================================
# Stellar Atmospheres course figures (SA2-SA4)
# =====================================================================
def fig_sa_opacity():
    import sa_physics as sp
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.4))
    ax = axs[0]
    lam = np.logspace(np.log10(50e-9), np.log10(3e-6), 3000)
    for (T, col) in ((6000.0, C[1]), (9000.0, C[0]), (12000.0, C[2])):
        bf, ff, es = sp.hydrogen_opacity_per_H(lam, T, 20.0)
        ax.loglog(lam * 1e9, bf + ff + es, color=col, lw=2, label=f"H bf + ff + e⁻ scattering, T = {T:.0f} K")
    ax.axvline(364.7, color="k", ls=":", lw=1); ax.text(370, 1e-30, "Balmer\nedge", fontsize=9)
    ax.axvline(820.6, color="k", ls=":", lw=1); ax.text(830, 1e-30, "Paschen\nedge", fontsize=9)
    ax.set_xlim(50, 3000); ax.set_ylim(1e-33, 1e-20)
    ax.set_xlabel("wavelength [nm]"); ax.set_ylabel(r"cross-section per neutral H atom [m$^2$]")
    ax.set_title(r"Continuous opacity of hydrogen in LTE ($P_e=20$ Pa)")
    ax.legend(fontsize=8.5, loc="upper right")
    ax = axs[1]
    for n, col in zip((1, 2, 3, 4), C):
        ax.loglog(lam * 1e9, np.maximum(sp.sigma_bf_H(n, c_light / lam), 1e-40), color=col, lw=2, label=f"n = {n}")
    ax.set_xlim(50, 3000); ax.set_ylim(1e-24, 2e-20)
    ax.set_xlabel("wavelength [nm]"); ax.set_ylabel(r"$\sigma_{bf}$ [m$^2$]")
    ax.set_title(r"Kramers cross-sections $\sigma_n\propto n^{-5}\nu^{-3}$ (edges at $91.2\,n^2$ nm)")
    ax.legend()
    save(fig, "SA2_continuous_opacity.png")


def fig_sa_rates():
    import sa_physics as sp
    fig, axs = plt.subplots(1, 2, figsize=(12, 5.2))
    ax = axs[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    levels = [(1.0, "1"), (5.0, "2"), (6.8, "3")]
    for y, lab in levels:
        ax.plot([1.5, 7.5], [y, y], "k", lw=2); ax.text(7.7, y, f"level {lab}", va="center")
    ax.add_patch(Rectangle((1.5, 8.4), 6, 1.2, color=C[4], alpha=.15)); ax.text(7.7, 9.0, "continuum (ion + e⁻)", va="center")
    arrow(ax, (2.2, 1.05), (2.2, 4.95), color=C[0], lw=1.6); ax.text(2.1, 3, r"$B_{12}\bar J$", ha="right", color=C[0], fontsize=10)
    arrow(ax, (2.8, 4.95), (2.8, 1.05), color=C[0], lw=1.6); ax.text(2.9, 2.2, r"$A_{21}+B_{21}\bar J$", color=C[0], fontsize=10)
    arrow(ax, (4.6, 1.05), (4.6, 4.95), color=C[1], lw=1.6); ax.text(4.5, 3.6, r"$n_eq_{12}$", ha="right", color=C[1], fontsize=10)
    arrow(ax, (5.1, 4.95), (5.1, 1.05), color=C[1], lw=1.6); ax.text(5.2, 2.2, r"$n_eq_{21}$", color=C[1], fontsize=10)
    arrow(ax, (6.3, 5.05), (6.3, 8.35), color=C[2], lw=1.6); ax.text(6.2, 7.6, "photo-\nionisation", ha="right", color=C[2], fontsize=9)
    arrow(ax, (6.9, 8.35), (6.9, 6.85), color=C[3], lw=1.6); ax.text(7.0, 7.9, "recombination", color=C[3], fontsize=9)
    ax.text(5, 0.2, "radiative (blue, green, gold) and collisional (red) rates", ha="center", fontsize=10)
    ax = axs[1]
    T = 1e4
    ne = np.logspace(6, 26, 300)
    boltz = np.exp(-2.48 * eV / (rt.k * T))
    for (A, Om, lab, col) in ((0.027, 2.29, "forbidden line, A = 0.027 s⁻¹ ([O III]-like)", C[1]), (1e8, 10.0, "allowed line, A = 10⁸ s⁻¹", C[0])):
        r = sp.two_level_ratio(ne, A, Om, 5, 5, 2.48, T) / boltz
        ax.loglog(ne, r, color=col, lw=2.2, label=lab)
        ax.axvline(A / sp.q_ul(Om, 5, T), color=col, ls=":", lw=1)
    ax.axhline(1, color="k", ls="--", lw=1); ax.text(1.5e6, 1.3, "LTE (Boltzmann)", fontsize=9)
    ax.text(3e13, 3e-10, "coronal limit:\n" r"$n_u/n_l=n_eq_{lu}/A_{ul}\propto n_e$", fontsize=9)
    ax.set_ylim(1e-10, 3); ax.set_xlim(1e6, 1e26)
    ax.set_xlabel(r"electron density $n_e$ [m$^{-3}$]"); ax.set_ylabel(r"$(n_u/n_l)\,/\,(n_u/n_l)_{\rm LTE}$")
    ax.set_title(r"Two-level atom, $T=10^4$ K, no radiation: dotted = $n_{\rm crit}$")
    ax.legend(fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1)
    save(fig, "SA3_rates.png")


def fig_sa_broadening():
    import sa_physics as sp
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.4))
    ax = axs[0]
    v = np.linspace(0, 30, 1500)
    for a, col in zip((0.0, 1e-3, 1e-2, 0.1, 1.0), C):
        y = np.exp(-v**2) if a == 0 else sp.voigt(a, v)
        ax.semilogy(v, y, color=col, lw=2, label=("Gaussian (a = 0)" if a == 0 else f"Voigt, a = {a:g}"))
    ax.set_ylim(1e-8, 1.5); ax.set_xlim(0, 30)
    ax.set_xlabel(r"$v=\Delta\nu/\Delta\nu_D$"); ax.set_ylabel(r"$H(a,v)$")
    ax.set_title("Voigt profiles: Doppler core + Lorentzian damping wings")
    ax.text(12, 3e-3, r"wings: $H\approx a/(\sqrt{\pi}v^2)$", fontsize=10)
    ax.legend(fontsize=8.5)
    ax = axs[1]
    x = np.linspace(-1.5, 1.5, 600)
    vsini = 20.0
    for eps, col, ls in ((0.0, C[0], "-"), (0.6, C[1], "--")):
        ax.plot(x * vsini, sp.rotation_kernel(x, eps) / vsini, color=col, ls=ls, lw=2, label=fr"rotation, $v\sin i=20$ km/s, $\varepsilon={eps}$")
    vth = 2.0
    ax.plot(x * vsini, np.exp(-(x * vsini / vth) ** 2) / (np.sqrt(np.pi) * vth), color=C[2], lw=1.8, label="thermal + micro, 2 km/s")
    ax.set_xlabel("velocity [km/s]"); ax.set_ylabel("broadening kernel [per km/s]")
    ax.set_title("Rotational vs thermal broadening kernels")
    ax.legend(fontsize=8.5)
    save(fig, "SA4_broadening.png")


if __name__ == "__main__" and "--sa" in sys.argv:
    fig_sa_opacity(); fig_sa_rates(); fig_sa_broadening()


# =====================================================================
# Concept maps and concept illustrations (condensed courses)
# =====================================================================
from matplotlib.patches import FancyBboxPatch

KIND = {"core": ("#dbe7f7", "#1f5fa8"), "law": ("#fbe3d6", "#c0532b"), "result": ("#dff3ea", "#1f8a5f"),
        "app": ("#efe7fb", "#6250d6"), "warn": ("#fdf1d6", "#a8740a")}


def concept_map(fname, title, nodes, edges, size=(12, 6.2)):
    fig, ax = plt.subplots(figsize=size)
    ax.set_xlim(0, 12); ax.set_ylim(0, 6.2); ax.axis("off")
    ax.set_title(title, fontsize=13.5, weight="bold", color="#1f2a3a", loc="left")
    boxes = {}
    for key, (x, y, label, kind) in nodes.items():
        fc, ec = KIND[kind]
        t = ax.text(x, y, label, ha="center", va="center", fontsize=10.2, zorder=4, color="#16202c")
        bb = t.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transData.inverted())
        w, hgt = bb.width + 0.35, bb.height + 0.25
        ax.add_patch(FancyBboxPatch((x - w / 2, y - hgt / 2), w, hgt, boxstyle="round,pad=0.04,rounding_size=0.15",
                                    fc=fc, ec=ec, lw=1.6, zorder=3))
        for k2, (x2, y2, w2, h2) in boxes.items():
            if abs(x - x2) < (w + w2) / 2 + 0.1 and abs(y - y2) < (hgt + h2) / 2 + 0.1:
                print(f"  overlap in {fname}: {key} / {k2}")
        if x - w / 2 < 0 or x + w / 2 > 12:
            print(f"  outside in {fname}: {key}")
        boxes[key] = (x, y, w, hgt)
    for a, b, lab in edges:
        xa, ya, wa, ha = boxes[a]; xb, yb, wb, hb = boxes[b]
        dx, dy = xb - xa, yb - ya
        def edge_pt(x, y, w, h, ux, uy):
            tx = (w / 2 + 0.05) / abs(ux) if ux else np.inf
            ty = (h / 2 + 0.05) / abs(uy) if uy else np.inf
            t = min(tx, ty); return x + ux * t, y + uy * t
        L = np.hypot(dx, dy); ux, uy = dx / L, dy / L
        p0 = edge_pt(xa, ya, wa, ha, ux, uy); p1 = edge_pt(xb, yb, wb, hb, -ux, -uy)
        ax.add_patch(FancyArrowPatch(p0, (p1[0], p1[1]), arrowstyle="-|>", mutation_scale=13, color="#555", lw=1.3, zorder=2))
        if lab:
            ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.12, lab, fontsize=8.6, ha="center", color="#444",
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=1), zorder=5)
    handles = [Rectangle((0, 0), 1, 1, fc=KIND[k][0], ec=KIND[k][1]) for k in ("core", "law", "result", "app")]
    ax.legend(handles, ["concept", "law / equation", "result", "application"], loc="lower right", fontsize=8.5, frameon=False, ncol=4)
    save(fig, fname)


def all_concept_maps():
    concept_map("RT1_map.png", "RT1 concept map — describing radiation", {
        "src": (1.4, 4.9, "photons from\na source", "core"), "I": (4.3, 4.9, "specific intensity $I_\\nu$\n(brightness of one beam)", "core"),
        "cons": (8.0, 5.3, "conserved along rays\nin vacuum", "result"), "J": (2.2, 2.6, "mean intensity $J_\\nu$\n(illumination)", "law"),
        "F": (5.0, 2.6, "flux $F_\\nu$\n(net flow)", "law"), "K": (7.8, 2.6, "$K_\\nu$ → pressure\n$P=u/3$ if isotropic", "law"),
        "tau": (10.3, 3.9, "optical depth $\\tau$\n(mean free paths)", "core"), "rte": (10.0, 1.4, "RTE\n$dI/d\\tau=S-I$", "result"),
        "obs": (4.2, 0.8, "what telescopes measure:\npixels ($I$), unresolved stars ($F$)", "app")},
        [("src", "I", ""), ("I", "cons", ""), ("I", "J", "average"), ("I", "F", "weight cosθ"), ("I", "K", "weight cos²θ"),
         ("I", "tau", "through matter"), ("tau", "rte", ""), ("F", "obs", ""), ("I", "obs", "")])
    concept_map("RT2_map.png", "RT2 concept map — black bodies and light–matter interaction", {
        "te": (1.6, 5.0, "thermal\nequilibrium", "core"), "B": (4.6, 5.0, "Planck $B_\\nu(T)$", "law"),
        "wien": (8.0, 5.4, "Wien: colour ↔ T\nStefan–Boltzmann: $\\sigma T^4$", "result"), "mat": (1.6, 2.6, "matter:\natoms, ions, e⁻", "core"),
        "proc": (4.6, 2.6, "absorption, emission,\nstimulated emission, scattering", "core"), "ein": (8.2, 3.2, "Einstein relations\n$A$, $B$", "law"),
        "kir": (10.4, 1.6, "Kirchhoff\n$j_\\nu=\\alpha_\\nu B_\\nu$", "result"), "rw": (4.8, 0.7, "random walk\n$N\\approx\\tau^2$", "result"),
        "app": (10.4, 4.3, "star colours, CMB,\nradio $T_b$", "app")},
        [("te", "B", ""), ("B", "wien", ""), ("wien", "app", ""), ("mat", "proc", ""), ("proc", "ein", "atomic rates"),
         ("ein", "kir", "+ equilibrium"), ("B", "kir", ""), ("proc", "rw", "scattering")])
    concept_map("RT3_map.png", "RT3 concept map — forming and solving the transfer equation", {
        "f": (1.6, 5.0, "photons in\nphase space $f$", "core"), "boltz": (4.6, 5.0, "photon conservation\n(Boltzmann equation)", "law"),
        "gl": (8.4, 5.0, "gains − losses:\nemission, absorption, scattering", "core"), "rte": (8.4, 3.1, "$dI_\\nu/d\\tau_\\nu=S_\\nu-I_\\nu$", "law"),
        "S": (11.0, 3.9, "source function\n$S=j/\\alpha$", "core"), "fs": (4.8, 3.1, "formal solution\n$I=I_0e^{-\\tau}+\\int Se^{-(\\tau-t)}dt$", "result"),
        "thin": (1.9, 1.4, "thin: $I\\approx I_0+\\tau(S-I_0)$", "result"), "thick": (5.4, 1.2, "thick: $I\\to S$", "result"),
        "lines": (9.4, 1.0, "absorption vs emission lines;\nMIT two-layer star", "app")},
        [("f", "boltz", ""), ("boltz", "gl", ""), ("gl", "rte", "static, along a ray"), ("S", "rte", ""), ("rte", "fs", "integrating factor"),
         ("fs", "thin", ""), ("fs", "thick", ""), ("thick", "lines", ""), ("thin", "lines", "")])
    concept_map("RT4_map.png", "RT4 concept map — atmospheres, moments and scattering", {
        "pp": (2.2, 5.0, "plane-parallel layers\n$\\mu\\,dI/d\\tau=I-S$", "law"), "em": (6.0, 5.0, "emergent intensity\n$\\int S e^{-\\tau/\\mu}d\\tau/\\mu$", "result"),
        "eb": (10.0, 5.0, "Eddington–Barbier\n$I(0,\\mu)\\approx S(\\tau=\\mu)$", "result"), "ld": (10.0, 3.2, "limb darkening →\n$T(\\tau)$ of the Sun", "app"),
        "mom": (2.2, 2.8, "moments\n$dH/d\\tau=J-S$, $dK/d\\tau=H$", "law"), "edd": (5.8, 2.8, "Eddington closure\n$K=J/3$", "law"),
        "diff": (5.6, 0.9, "diffusion, Rosseland mean\n(stellar interiors)", "result"), "sc": (1.9, 0.9, "scattering\n$S=\\varepsilon B+(1-\\varepsilon)J$", "core"),
        "th": (9.7, 0.9, "thermalisation:\n$S(0)=\\sqrt{\\varepsilon}B$", "result")},
        [("pp", "em", ""), ("em", "eb", "linear S"), ("eb", "ld", ""), ("pp", "mom", "average over μ"), ("mom", "edd", "close"),
         ("edd", "diff", "deep inside"), ("sc", "th", ""), ("mom", "sc", "")])
    concept_map("RT5_map.png", "RT5 concept map — polarized light", {
        "E": (1.8, 5.0, "electric-field\nellipse", "core"), "st": (5.0, 5.0, "Stokes $I,Q,U,V$", "law"),
        "vrte": (9.0, 5.0, "vector RTE\n$d\\mathbf{I}/ds=-\\mathsf{K}\\mathbf{I}+\\epsilon$", "law"),
        "sc": (2.0, 2.6, "scattering\n(Thomson, Rayleigh)", "core"), "lin": (5.4, 2.6, "linear polarization\n$p=\\sin^2\\Theta/(1+\\cos^2\\Theta)$", "result"),
        "ch": (9.6, 2.8, "11.7 % at the limb\n(Chandrasekhar)", "result"), "B": (2.0, 0.8, "magnetic field", "core"),
        "z": (5.6, 0.8, "Zeeman: $V\\propto B_\\parallel$,\nHanle (weak fields)", "result"), "app": (9.6, 0.8, "magnetograms, CMB,\nISM dust, synchrotron", "app")},
        [("E", "st", ""), ("st", "vrte", ""), ("sc", "lin", ""), ("lin", "ch", "in atmospheres"), ("B", "z", ""), ("z", "app", ""),
         ("lin", "app", ""), ("st", "lin", "")])
    concept_map("RT6_map.png", "RT6 concept map — how the problem was solved", {
        "two": (1.8, 5.0, "two streams\nSchuster, Schwarzschild\n1905–1906", "law"), "edd": (5.4, 5.0, "Eddington closure\n1926", "law"),
        "milne": (9.2, 5.0, "integral equations\nMilne 1921", "law"), "exact": (5.4, 2.9, "exact solutions:\nHopf, Ambartsumian,\nChandrasekhar 1930–1950", "result"),
        "num": (2.0, 1.0, "numerical era:\nFeautrier, linearization", "core"), "ali": (6.2, 1.0, "accelerated Λ-iteration,\nshort characteristics", "core"),
        "now": (10.0, 1.0, "3D radiation-\nhydrodynamics, NLTE", "app")},
        [("two", "edd", ""), ("milne", "edd", ""), ("edd", "exact", "benchmarks"), ("milne", "exact", ""), ("exact", "num", "computers"),
         ("num", "ali", ""), ("ali", "now", "")])
    concept_map("SA1_map.png", "SA1 concept map — the state of the gas", {
        "te": (1.7, 5.0, "TE: one T for\nmatter and light", "core"), "lte": (5.4, 5.0, "LTE: matter at\nlocal T(r)", "core"),
        "nlte": (9.4, 5.0, "NLTE: populations set\nby the radiation field", "core"), "sb": (2.6, 2.7, "Boltzmann (excitation)\nSaha (ionisation)", "law"),
        "kir": (6.4, 2.7, "Kirchhoff\n$S_\\nu=B_\\nu(T)$", "law"), "crit": (10.0, 2.7, "criterion:\n$n_e$ vs $n_{crit}$", "law"),
        "bal": (2.6, 0.8, "spectral sequence:\nBalmer lines peak at A0", "app"), "par": (7.0, 0.8, "atmosphere fixed by\n$T_{\\rm eff}$, $\\log g$, composition", "result")},
        [("te", "lte", "photons escape"), ("lte", "nlte", "collisions rare"), ("lte", "sb", ""), ("lte", "kir", ""), ("nlte", "crit", ""),
         ("sb", "bal", ""), ("kir", "par", "")])
    concept_map("SA2_map.png", "SA2 concept map — where opacity comes from", {
        "pop": (1.8, 5.0, "populations\n(Saha–Boltzmann)", "core"), "xs": (5.4, 5.0, "cross-sections\n(atomic physics)", "core"),
        "cont": (2.3, 2.8, "continuous opacity:\nbound–free, free–free,\nH⁻, e⁻ scattering", "law"), "line": (7.0, 2.9, "line opacity:\n$f$-value × profile $\\phi(\\nu)$", "law"),
        "br": (10.3, 4.6, "broadening: natural,\nDoppler, pressure → Voigt", "law"), "tot": (5.0, 0.8, "total $\\kappa_\\nu$ →\nthe spectrum's shape", "result"),
        "app": (10.2, 1.2, "Balmer jump, H⁻ in the Sun,\ngravity from line wings", "app")},
        [("pop", "cont", ""), ("xs", "cont", ""), ("xs", "line", ""), ("pop", "line", ""), ("br", "line", ""), ("cont", "tot", ""),
         ("line", "tot", ""), ("tot", "app", "")])
    concept_map("SA3_map.png", "SA3 concept map — rates and non-LTE", {
        "rad": (1.8, 5.0, "radiative rates\n(depend on $J_\\nu$)", "core"), "col": (5.6, 5.0, "collisional rates\n(depend on $n_e$, $T$)", "core"),
        "db": (9.6, 5.0, "detailed balance:\nEinstein, Milne,\nKlein–Rosseland", "law"), "se": (5.6, 3.0, "statistical equilibrium\nrates in = rates out", "law"),
        "lte": (1.6, 1.0, "collisions win\n→ LTE", "result"), "cor": (5.0, 1.0, "coronal / nebular\nlimits", "result"),
        "nlte": (8.6, 1.0, "NLTE: $b_i\\neq1$,\n$S\\neq B$", "result"), "m": (11.0, 2.8, "methods:\nALI, CL, MC", "app")},
        [("rad", "se", ""), ("col", "se", ""), ("db", "se", ""), ("se", "lte", ""), ("se", "cor", ""), ("se", "nlte", ""), ("nlte", "m", "")])
    concept_map("SA4_map.png", "SA4 concept map — the gray atmosphere and LTE lines", {
        "as": (1.8, 5.0, "gray, LTE,\nradiative equilibrium", "core"), "jb": (5.2, 5.0, "$J=B$, flux constant", "law"),
        "T": (9.0, 5.0, "$T^4=\\frac{3}{4}T_{\\rm eff}^4(\\tau+q)$", "result"), "ld": (10.4, 3.0, "limb darkening,\nnon-Planck spectrum", "result"),
        "line": (2.0, 2.6, "line opacity\nraises $\\tau_\\nu$", "core"), "hi": (5.6, 2.6, "line forms higher,\nwhere T is lower", "law"),
        "me": (5.0, 0.8, "Milne–Eddington profiles", "result"), "cog": (9.2, 0.8, "curve of growth\n→ abundances", "app")},
        [("as", "jb", ""), ("jb", "T", ""), ("T", "ld", ""), ("line", "hi", "Eddington–Barbier"), ("T", "hi", ""), ("hi", "me", ""), ("me", "cog", "")])
    concept_map("SA5_map.png", "SA5 concept map — real model atmospheres", {
        "in": (1.8, 5.0, "inputs: $T_{\\rm eff}$,\n$\\log g$, composition", "core"), "eq": (5.6, 5.0, "structure equations:\nhydrostatic + energy + RTE", "law"),
        "it": (9.6, 5.0, "iterate: correct T(τ)\n(Unsöld–Lucy)", "law"), "nong": (2.4, 2.7, "non-gray opacity:\nblanketing, backwarming", "core"),
        "conv": (6.0, 2.7, "convection,\nsphericity, winds", "core"), "sun": (9.8, 2.7, "the Sun: photosphere →\nchromosphere → corona", "app"),
        "grid": (3.2, 0.8, "grids: ATLAS, MARCS,\nPHOENIX, TLUSTY", "result"), "diag": (8.0, 0.8, "diagnostics:\n$T_{\\rm eff}$, $\\log g$, abundances", "app")},
        [("in", "eq", ""), ("eq", "it", ""), ("nong", "eq", ""), ("conv", "eq", ""), ("it", "sun", ""), ("eq", "grid", ""), ("grid", "diag", "")])


def fig_flux_vs_intensity():
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.9))
    for ax in axs:
        ax.set_xlim(-3, 3); ax.set_ylim(-0.8, 3.6); ax.axis("off"); ax.set_aspect("equal")
        ax.add_patch(Rectangle((-0.8, -0.35), 1.6, 0.35, fc="#9ec5e8", ec=C[0]))
        ax.text(0, -0.65, "detector area dA", ha="center", fontsize=10, color=C[0])
    ax = axs[0]
    for ang in np.linspace(-70, 70, 9):
        t = np.radians(ang); s = (2.8 * np.sin(t), 2.8 * np.cos(t))
        arrow(ax, s, (0.25 * np.sin(t), 0.05), color=C[1], lw=1.4, ms=10)
    ax.set_title("FLUX: count light from all directions\n" r"$F_\nu=\oint I_\nu\cos\theta\,d\Omega$  (falls as $1/r^2$)", fontsize=10.5)
    ax = axs[1]
    ax.plot([-0.8, -0.25], [0.05, 1.6], "k", lw=2); ax.plot([0.8, 0.25], [0.05, 1.6], "k", lw=2)
    for xx in (-0.12, 0, 0.12):
        arrow(ax, (xx * 3, 3.2), (xx, 0.05), color=C[1], lw=1.4, ms=10)
    for ang in (-60, -35, 35, 60):
        t = np.radians(ang); ax.plot([2.8 * np.sin(t), 1.4 * np.sin(t)], [2.8 * np.cos(t), 1.4 * np.cos(t)], color="#bbb", lw=1.2)
        ax.plot(1.4 * np.sin(t), 1.4 * np.cos(t), "x", color="#999")
    ax.text(0.0, 3.35, r"$d\Omega$", ha="center", fontsize=12, color=C[1])
    ax.set_title("INTENSITY: a collimator picks one direction\n" r"$I_\nu=dE/(dt\,dA\,d\Omega\,d\nu)$  (constant along a ray)", fontsize=10.5)
    save(fig, "RT1_flux_vs_intensity.png")


def fig_interactions():
    fig, axs = plt.subplots(1, 4, figsize=(13, 3.6))
    titles = ["bound–bound\n(spectral line)", "bound–free\n(photo-ionisation)", "free–free\n(inverse bremsstrahlung)", "scattering\n(redirected, not destroyed)"]
    for ax, t in zip(axs, titles):
        ax.set_xlim(0, 4); ax.set_ylim(-0.6, 4.2); ax.axis("off"); ax.set_title(t, fontsize=10.5)
        ax.add_patch(Rectangle((0.6, 3.0), 2.8, 1.0, color=C[4], alpha=.15)); ax.text(3.45, 3.5, "continuum", fontsize=8, va="center")
        ax.plot([0.6, 3.4], [0.6, 0.6], "k", lw=2); ax.plot([0.6, 3.4], [2.0, 2.0], "k", lw=2)

    def wave(ax, x0, y0, x1, y1, col=C[1]):
        tt = np.linspace(0, 1, 200); xs = x0 + (x1 - x0) * tt; ys = y0 + (y1 - y0) * tt + 0.1 * np.sin(2 * np.pi * 5 * tt)
        ax.plot(xs, ys, color=col, lw=1.4); arrow(ax, (xs[-6], ys[-6]), (xs[-1], ys[-1]), color=col, ms=9)
    a = axs[0]; wave(a, 0.0, 1.3, 1.45, 1.3); arrow(a, (1.7, 0.65), (1.7, 1.95), color=C[0], lw=1.8)
    a.text(2.0, -0.4, r"narrow: $h\nu=E_2-E_1$", ha="center", fontsize=9)
    a = axs[1]; wave(a, 0.0, 1.3, 1.45, 1.3); arrow(a, (1.7, 0.65), (1.7, 3.3), color=C[0], lw=1.8)
    a.text(2.0, -0.4, r"any $h\nu\geq\chi$: an edge", ha="center", fontsize=9)
    a = axs[2]; wave(a, 0.0, 3.5, 1.4, 3.5); arrow(a, (1.6, 3.2), (2.6, 3.8), color=C[0], lw=1.8)
    a.plot(1.9, 3.35, "o", color=C[2], ms=8); a.text(2.0, -0.4, r"e⁻ near an ion; $\propto\nu^{-3}$", ha="center", fontsize=9)
    a = axs[3]; wave(a, 0.0, 1.3, 1.6, 1.3); a.plot(1.85, 1.3, "o", color=C[0], ms=10); wave(a, 2.05, 1.45, 3.4, 2.6)
    a.text(2.0, -0.4, "Thomson (e⁻), Rayleigh (atoms)", ha="center", fontsize=9)
    save(fig, "RT2_interactions.png")


def fig_formal_contributions():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.1))
    edges = np.arange(0, 5.01, 0.25)
    a, b = 1.0, 1.5
    contrib = []
    for t0, t1 in zip(edges[:-1], edges[1:]):
        tt = np.linspace(t0, t1, 200); contrib.append(np.trapezoid((a + b * tt) * np.exp(-tt), tt))
    contrib = np.array(contrib); total = a + b
    ax = axs[0]
    ax.bar(edges[:-1] + 0.125, contrib / total, width=0.22, color=C[0])
    ax.set_xlabel(r"depth of the emitting layer, $\tau$ (from the observer)"); ax.set_ylabel("fraction of the emergent intensity")
    frac1 = contrib[edges[:-1] < 1].sum() / total
    ax.set_title(f"Who sends the light we see? (S = 1 + 1.5τ)\n{100*frac1:.0f} % comes from τ < 1, the rest from deeper layers")
    ax = axs[1]
    tau = np.linspace(0, 5, 300)
    ax.plot(tau, a + b * tau, color=C[1], lw=2, label=r"source function $S(\tau)$")
    ax.plot(tau, np.exp(-tau), color=C[0], lw=2, label=r"survival to the surface $e^{-\tau}$")
    ax.plot(tau, (a + b * tau) * np.exp(-tau) / total, color=C[2], lw=2.5, label=r"contribution $S e^{-\tau}$ (normalised)")
    ax.axvline(1 - a / b, color="#999", ls=":")
    ax.axhline(0, color="k", lw=.6)
    ax.set_xlabel(r"$\tau$"); ax.set_ylim(0, 3); ax.legend(fontsize=9)
    ax.set_title("Deep layers are bright but hidden;\nsurface layers are visible but faint")
    save(fig, "RT3_contributions.png")


def fig_te_lte_nlte():
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.3))
    rng = np.random.default_rng(7)
    def box(ax, title, sub, shade):
        ax.set_xlim(0, 4); ax.set_ylim(-0.9, 4.4); ax.axis("off"); ax.set_title(title, fontsize=12, weight="bold")
        img = np.linspace(shade[0], shade[1], 100)[:, None] * np.ones((1, 10))
        ax.imshow(img, extent=(0.3, 3.7, 0.3, 3.7), origin="lower", cmap="YlOrRd", vmin=0, vmax=1, aspect="auto")
        ax.text(2, -0.55, sub, ha="center", fontsize=9.5, va="center")
    def particles(ax, n):
        p = rng.uniform(0.45, 3.55, size=(n, 2)); ax.plot(p[:, 0], p[:, 1], "o", ms=3, color="#1f2a3a")
    def photon(ax, x, y, dx, dy, col):
        arrow(ax, (x, y), (x + dx, y + dy), color=col, lw=1.4, ms=9)
    a = axs[0]; box(a, "TE", "closed and isothermal:\nevery process balances its inverse; $I_\\nu=B_\\nu$", (0.6, 0.6))
    a.add_patch(Rectangle((0.3, 0.3), 3.4, 3.4, fill=False, ec="k", lw=3)); particles(a, 70)
    for _ in range(14):
        x, y = rng.uniform(0.6, 3.2, 2); t = rng.uniform(0, 2 * np.pi); photon(a, x, y, 0.4 * np.cos(t), 0.4 * np.sin(t), C[0])
    a = axs[1]; box(a, "LTE", "dense gas, open top: collisions keep the local T;\nphotons leak out, so $S_\\nu=B_\\nu(T)$ but $I_\\nu\\neq B_\\nu$", (0.85, 0.25))
    a.plot([0.3, 0.3, 3.7, 3.7], [3.7, 0.3, 0.3, 3.7], "k", lw=3); particles(a, 70)
    for x in (0.8, 1.6, 2.4, 3.2): photon(a, x, 3.3, 0.1, 0.9, C[0])
    a.text(2, 4.25, "escaping photons", ha="center", fontsize=9, color=C[0])
    a = axs[2]; box(a, "NLTE", "thin gas: few collisions; populations follow\nthe radiation field (here from a star outside), $S_\\nu\\neq B_\\nu$", (0.15, 0.15))
    a.plot([0.3, 0.3, 3.7, 3.7], [3.7, 0.3, 0.3, 3.7], "k", lw=1, ls="--"); particles(a, 12)
    a.add_patch(Circle((-0.25, 2.0), 0.35, color="#f6bd60", clip_on=False))
    for y in (1.0, 1.6, 2.2, 2.8): photon(a, 0.15, y, 1.4, 0.0, C[1])
    save(fig, "SA1_te_lte_nlte.png")


def fig_line_formation_depth():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))
    v = np.linspace(-4, 4, 400); eta0, beta = 30.0, 1.5
    eta = eta0 * np.exp(-v**2)
    r = rt.milne_eddington_residual(v, eta0, beta)
    ax = axs[0]; ax.plot(v, r, color=C[0], lw=2.2)
    ax.set_xlabel(r"distance from line centre $v=\Delta\nu/\Delta\nu_D$"); ax.set_ylabel(r"$F_\nu/F_c$")
    ax.set_title(r"The line we observe ($\eta_0=30$)")
    ax = axs[1]
    tc = (2 / 3) / (1 + eta)
    T = 5772 * (0.75 * (tc + 2 / 3)) ** 0.25
    ax.plot(v, T, color=C[1], lw=2.2)
    ax.set_xlabel(r"$v$"); ax.set_ylabel(r"temperature of the layer we see [K]")
    ax2 = ax.twinx(); ax2.plot(v, tc, color=C[2], lw=1.5, ls="--"); ax2.set_ylabel(r"continuum depth $\tau_c$ where $\tau_\nu=2/3$", color=C[2]); ax2.grid(False)
    ax.set_title("Where it forms: line centre is seen higher,\nin cooler gas (gray Sun, Eddington–Barbier)")
    save(fig, "SA4_line_depth.png")


def fig_novotny_model():
    import sa_physics as sp
    tt = np.array(sp.NOVOTNY_TAU); PP = np.array(sp.NOVOTNY_P)
    tg = np.linspace(0.02, 2.0, 200)
    fig, axs = plt.subplots(1, 3, figsize=(14, 4.2))
    ax = axs[0]
    ax.plot(tg, sp.novotny_T(tg), color="#c0392b")
    ax.axhline(5800, color="#999", ls=":"); ax.text(1.4, 5830, "$T_{\\rm eff}=5800$ K", fontsize=9, color="#666")
    ax.set_xlabel("optical depth $\\tau$"); ax.set_ylabel("T [K]"); ax.set_title("Step 1: temperature from\nEddington's approximation")
    ax = axs[1]
    ax.plot(tg, sp.novotny_P_powerlaw(tg) / 1e4, color="#1f5fa8", label="analytic, $\\kappa=10^{-4.4}P^{0.8}$")
    ax.plot(tt, PP / 1e4, "o", color="#16a085", label="Novotny's numerical model")
    ax.set_xlabel("optical depth $\\tau$"); ax.set_ylabel("gas pressure P [$10^4$ dyn cm$^{-2}$]")
    ax.set_title("Step 2: pressure from\nhydrostatic equilibrium $dP/d\\tau=g/\\kappa$"); ax.legend(fontsize=8.5)
    ax = axs[2]
    tf = np.linspace(0.2, 6, 300)
    ax.plot(tt, sp.schwarzschild_ratio(tt, PP), "o-", color="#16a085", label="Novotny model (real opacity)")
    ax.plot(tf, sp.schwarzschild_ratio(tf, sp.novotny_P_powerlaw(tf)), color="#1f5fa8", label="power-law opacity")
    ax.axhline(2.5, color="#c0392b", ls="--"); ax.text(3.2, 2.62, "convection below 2.5", color="#c0392b", fontsize=9)
    ax.set_ylim(1, 8); ax.set_xlabel("optical depth $\\tau$"); ax.set_ylabel("$d\\ln P/d\\ln T$")
    ax.set_title("Step 3: Schwarzschild test\nconvection starts near $\\tau\\approx1.2$"); ax.legend(fontsize=8.5)
    fig.tight_layout(); save(fig, "SA5_novotny_model.png")


def fig_crd_thermalization():
    """Mihalas Ch. 11: coherent scattering vs complete redistribution (Doppler profile)."""
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.4))
    ax = axs[0]
    for eps, col in zip((1e-2, 1e-3), (C[0], C[1])):
        t, S = rt.solve_scattering_atmosphere(eps)
        ax.semilogx(np.maximum(t, 1e-3), S, color=col, ls="--", lw=1.8, label=fr"coherent, $\varepsilon={eps:g}$")
        t, S = rt.solve_two_level_crd(eps)
        ax.semilogx(np.maximum(t, 1e-3), S, color=col, lw=2.4, label=fr"CRD Doppler, $\varepsilon={eps:g}$")
        ax.axhline(np.sqrt(eps), color=col, ls=":", lw=1)
    ax.set_xlim(1e-3, 3e4); ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"line-centre optical depth $\tau$"); ax.set_ylabel(r"$S/B$")
    ax.set_title("Same surface value $\\sqrt{\\varepsilon}\\,B$, very different depths")
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axs[1]
    eps_list = np.array([1e-1, 3e-2, 1e-2, 3e-3, 1e-3])
    th_coh, th_crd = [], []
    for eps in eps_list:
        t, S = rt.solve_scattering_atmosphere(eps); th_coh.append(np.interp(0.9, S, t))
        t, S = rt.solve_two_level_crd(eps); th_crd.append(np.interp(0.9, S, t))
    ax.loglog(1 / eps_list, th_coh, "o--", color=C[2], label="coherent: grows as $1/\\sqrt{\\varepsilon}$")
    ax.loglog(1 / eps_list, th_crd, "s-", color=C[3], label="CRD, Doppler: grows as $\\sim1/\\varepsilon$")
    x = 1 / eps_list
    ax.loglog(x, 1.3 * np.sqrt(x), color=C[2], lw=0.8, alpha=.6); ax.loglog(x, 0.62 * x, color=C[3], lw=0.8, alpha=.6)
    ax.set_xlabel(r"$1/\varepsilon$ (scatterings before destruction)"); ax.set_ylabel(r"depth where $S=0.9\,B$")
    ax.set_title("Thermalization depth"); ax.legend(fontsize=9)
    fig.tight_layout(); save(fig, "SA3_crd_thermalization.png")


def all_concept_figs():
    all_concept_maps(); fig_flux_vs_intensity(); fig_interactions(); fig_formal_contributions(); fig_te_lte_nlte(); fig_line_formation_depth()
    fig_novotny_model(); fig_crd_thermalization()


if __name__ == "__main__" and "--concepts" in sys.argv:
    all_concept_figs()
