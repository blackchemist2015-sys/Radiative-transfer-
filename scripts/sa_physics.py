"""
Physical processes for the Stellar Atmospheres course (lectures SA2-SA4):
hydrogenic bound-free / free-free opacity, H- abundance, collisional rates,
two-level populations from coronal to LTE, Voigt and rotational profiles.
SI units unless stated.
"""
import numpy as np
from scipy.special import wofz
import lte_solvers as rt

h, c, k, eV, me = rt.h, rt.c, rt.k, rt.eV, rt.m_e
sigma_T = 6.6524587e-29
KRAMERS = 2.815e25          # m^2 Hz^3   (= 2.815e29 cm^2 Hz^3)
NU_LYMAN = 3.28805e15        # Hz, hydrogen ionisation frequency
SAHA_CONST = (2 * np.pi * me * k / h**2) ** 1.5


def sigma_bf_H(n, nu, gbf=1.0):
    """Kramers hydrogenic bound-free cross-section of level n [m^2]."""
    nu = np.asarray(nu, float)
    return np.where(nu >= NU_LYMAN / n**2, KRAMERS * gbf / (n**5 * nu**3), 0.0)


def hydrogen_opacity_per_H(lam, T, Pe, nmax=12):
    """Bound-free, free-free and electron-scattering cross-section per neutral H atom [m^2]."""
    nu = c / lam
    stim = 1 - np.exp(-h * nu / (k * T))
    bf = np.zeros_like(nu)
    for n in range(1, nmax + 1):
        frac = 2 * n**2 * np.exp(-13.598 * (1 - 1 / n**2) * eV / (k * T)) / 2.0   # N_n / N_HI with U = 2
        bf += frac * sigma_bf_H(n, nu)
    bf *= stim
    ne = Pe / (k * T)
    x = rt.saha_hydrogen(T, Pe)                                 # N_II / N_I  (= n_e / n_HI for pure H)
    ff = 3.69e8 * (ne * 1e-6) * x * T**-0.5 * nu**-3 * 1e-4 * stim   # cgs formula converted to m^2
    es = np.full_like(nu, sigma_T * x)                          # sigma_T n_e / n_HI
    return bf, ff, es


def hminus_fraction(T, ne):
    """n(H-) / n(H I) from Saha with chi = 0.754 eV, U(H-) = 1, U(H I) = 2."""
    return ne / (4 * SAHA_CONST * T**1.5 * np.exp(-0.754 * eV / (k * T)))


def q_lu(Omega, gl, dE_eV, T):
    """Collisional excitation rate coefficient [m^3 s^-1] from collision strength Omega."""
    return 8.629e-12 * Omega / (gl * np.sqrt(T)) * np.exp(-dE_eV * eV / (k * T))


def q_ul(Omega, gu, T):
    return 8.629e-12 * Omega / (gu * np.sqrt(T))


def two_level_ratio(ne, A, Omega, gl, gu, dE_eV, T):
    """n_u/n_l for an optically thin two-level atom with no radiation field."""
    return ne * q_lu(Omega, gl, dE_eV, T) / (A + ne * q_ul(Omega, gu, T))


def voigt(a, v):
    return np.real(wofz(v + 1j * a))


def rotation_kernel(x, eps):
    """Gray's rotational broadening kernel G(x), x = dlambda / dlambda_L, limb-darkening eps."""
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = np.abs(x) < 1
    out[m] = (2 * (1 - eps) * np.sqrt(1 - x[m]**2) + 0.5 * np.pi * eps * (1 - x[m]**2)) / (np.pi * (1 - eps / 3))
    return out


if __name__ == "__main__":
    print("Kramers sigma at Lyman edge:", sigma_bf_H(1, NU_LYMAN), "m^2 ; edges (nm):",
          [round(c / (NU_LYMAN / n**2) * 1e9, 1) for n in (1, 2, 3, 4)])
    T, ne = 6000.0, 1e19
    fHm = hminus_fraction(T, ne)
    print(f"H-/HI at 6000 K, ne=1e19: {fHm:.3e} ; H- opacity per H atom (sigma_max 4e-21 m^2): {fHm*4e-21:.2e} m^2")
    nu = c / 500e-9
    n3 = 9 * np.exp(-13.598 * (1 - 1 / 9) * eV / (k * T))
    print(f"N3/NHI = {n3:.3e}; sigma_3(500nm) = {sigma_bf_H(3, nu):.3e}; per H atom = {n3*sigma_bf_H(3, nu):.3e} m^2")
    print("ratio H-/H(n=3) ~", fHm * 4e-21 / (n3 * sigma_bf_H(3, nu)))
    # [O III]-like forbidden line and an allowed line, T = 1e4
    T = 1e4
    qul_f = q_ul(2.29, 5, T); print(f"[OIII] q_ul = {qul_f:.3e} m^3/s ; n_crit = {0.027/qul_f:.3e} m^-3")
    qul_a = q_ul(10, 5, T); print(f"allowed (A=1e8, Omega=10) n_crit = {1e8/qul_a:.3e} m^-3")
    print("Boltzmann ratio (g equal, 2.48 eV, 1e4 K):", np.exp(-2.48 * eV / (k * T)))
    for ne in (1e8, 1e10, 1e12, 1e14):
        print(f"  ne={ne:.0e}: forbidden nu/nl / Boltzmann = {two_level_ratio(ne,0.027,2.29,5,5,2.48,T)/np.exp(-2.48*eV/(k*T)):.3e}")
    # natural width of H-alpha
    gam = (5.58e7 + 4.41e7) + 6.27e8
    lam = 656.28e-9
    print(f"H-alpha natural gamma = {gam:.3e} s^-1 ; FWHM = {lam**2*gam/(2*np.pi*c)*1e10:.4f} A")
    print(f"classical gamma at 500 nm = {2.47e-22*(c/500e-9)**2:.3e} s^-1")
    vD = np.sqrt(2 * k * 5772 / (55.845 * 1.66054e-27) + 1e6)
    dnuD = vD / 500e-9
    print(f"Fe 500 nm: v_D = {vD:.0f} m/s, dnu_D = {dnuD:.3e} Hz, a(gamma=1e9) = {1e9/(4*np.pi*dnuD):.4f}")
    print(f"rotation 50 km/s at 500 nm: {500*50/3e5:.4f} nm")
