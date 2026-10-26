"""
Numerical tools for the radiative-transfer course.

Everything here works in a semi-infinite, plane-parallel atmosphere with the
optical depth tau measured inward from the surface (tau = 0).

Contents
--------
planck_nu, planck_lambda      Planck functions (SI units)
lambda_matrix                 Discrete Lambda operator J = Lambda[S]
solve_scattering_atmosphere   S = eps*B + (1-eps)*J   (exact, by matrix inversion)
solve_two_level_crd           two-level atom, complete redistribution (Mihalas Ch. 11)
lambda_iteration              Same problem solved by (slow) Lambda iteration
hopf_function                 Exact gray-atmosphere Hopf function q(tau)
chandrasekhar_H               H-function for conservative isotropic scattering
milne_eddington_residual      LTE line profile in the Milne-Eddington model
saha_hydrogen, balmer_fraction  Saha-Boltzmann populations for hydrogen

Run this file directly to print a short self-test of the main results that
are quoted in the lecture notes.
"""
import numpy as np
from scipy.special import expn, wofz

# ---------------------------------------------------------------- constants (SI)
h = 6.62607015e-34      # J s
c = 2.99792458e8        # m/s
k = 1.380649e-23        # J/K
sigma_SB = 5.670374e-8  # W m^-2 K^-4
m_e = 9.1093837e-31     # kg
eV = 1.602176634e-19    # J


# ---------------------------------------------------------------- Planck
def planck_nu(nu, T):
    """B_nu(T) in W m^-2 Hz^-1 sr^-1."""
    x = h * nu / (k * T)
    return 2 * h * nu**3 / c**2 / np.expm1(x)


def planck_lambda(lam, T):
    """B_lambda(T) in W m^-2 m^-1 sr^-1 (lam in metres)."""
    x = h * c / (lam * k * T)
    return 2 * h * c**2 / lam**5 / np.expm1(x)


# ---------------------------------------------------------------- Lambda operator
def tau_grid(tau_min=1e-4, tau_max=40.0, n=240):
    """Logarithmic grid plus tau = 0."""
    return np.concatenate(([0.0], np.logspace(np.log10(tau_min), np.log10(tau_max), n)))


def tau_grid_fine(eps, tau_max, h=0.25):
    """
    Grid for scattering problems with small eps: logarithmic to tau = 1, then
    uniform steps h (< 1 mean free path, so the diffusion term is resolved)
    through a few thermalisation lengths 1/sqrt(3 eps), then logarithmic.
    """
    t1 = 8.0 / np.sqrt(3.0 * eps)
    return np.unique(np.concatenate([[0.0], np.logspace(-5, 0, 50), np.arange(1.0, t1, h),
                                     np.geomspace(t1, max(tau_max, 2 * t1), 80)]))


def _E(n, x):
    return expn(n, np.maximum(x, 0.0)) if n > 1 else expn(1, np.maximum(x, 1e-300))


def lambda_matrix(tau):
    """
    Matrix L such that J_i = sum_k L_ik S_k + (tail term) for a source function
    that is piecewise linear between grid points:

        J(tau) = 1/2 int_0^inf S(t) E1(|t - tau|) dt     (Schwarzschild-Milne)

    Beyond tau[-1] the source function is held at S[-1]; that tail contribution
    1/2 S[-1] E2(tau_max - tau_i) is folded into the last column.
    """
    n = len(tau)
    L = np.zeros((n, n))
    for i, ti in enumerate(tau):
        for kk in range(n - 1):
            a_t, b_t = tau[kk], tau[kk + 1]
            hseg = b_t - a_t
            if a_t >= ti:                       # segment above the point
                a, b = a_t - ti, b_t - ti
                M0 = _E(2, a) - _E(2, b)
                M1 = (a * _E(2, a) + _E(3, a)) - (b * _E(2, b) + _E(3, b))
            else:                               # segment below the point
                a, b = ti - b_t, ti - a_t
                M0 = _E(2, a) - _E(2, b)
                M1 = -((a * _E(2, a) + _E(3, a)) - (b * _E(2, b) + _E(3, b)))
            L[i, kk] += 0.5 * ((b_t - ti) / hseg * M0 - M1 / hseg)
            L[i, kk + 1] += 0.5 * ((ti - a_t) / hseg * M0 + M1 / hseg)
        L[i, -1] += 0.5 * _E(2, tau[-1] - ti)   # constant tail
    return L


def solve_scattering_atmosphere(eps, B=1.0, tau=None):
    """
    Isothermal atmosphere with coherent isotropic scattering:
        S = eps*B + (1-eps)*J,   J = Lambda[S].
    Solved exactly (to discretisation accuracy) by inverting (1 - (1-eps)Lambda).
    """
    if tau is None:
        tau = tau_grid_fine(eps, tau_max=max(40.0, 30.0 / np.sqrt(eps)))
    L = _lambda_matrix_vec(tau)
    A = np.eye(len(tau)) - (1 - eps) * L
    S = np.linalg.solve(A, eps * B * np.ones(len(tau)))
    return tau, S


def _lambda_matrix_vec(tau):
    """Vectorised lambda_matrix, with rows renormalised for photon conservation."""
    tau = np.asarray(tau, float)
    ti = tau[:, None]
    a_t, b_t = tau[None, :-1], tau[None, 1:]
    hseg = b_t - a_t
    above = a_t >= ti
    a = np.where(above, a_t - ti, ti - b_t)
    b = np.where(above, b_t - ti, ti - a_t)
    E2a, E2b, E3a, E3b = _E(2, a), _E(2, b), _E(3, a), _E(3, b)
    M0 = E2a - E2b
    M1 = (a * E2a + E3a) - (b * E2b + E3b)
    M1 = np.where(above, M1, -M1)
    L = np.zeros((len(tau), len(tau)))
    L[:, :-1] += 0.5 * ((b_t - ti) / hseg * M0 - M1 / hseg)
    L[:, 1:] += 0.5 * ((ti - a_t) / hseg * M0 + M1 / hseg)
    L[:, -1] += 0.5 * _E(2, tau[-1] - tau)
    # renormalise rows so that a constant S gives the exact J = S (1 - E2(tau)/2):
    # for eps << 1 small row-sum errors would act like spurious photon destruction
    L *= ((1.0 - 0.5 * _E(2, tau)) / L.sum(axis=1))[:, None]
    return L


def solve_two_level_crd(eps, B=1.0, profile="doppler", a_damp=1e-3, tau=None, nx=60, xmax=None):
    """
    Two-level atom in an isothermal atmosphere with complete redistribution:
        S = eps*B + (1-eps)*Jbar,  Jbar = int phi(x) J_x dx,
    where tau is the line-centre optical depth and tau_x = tau*phi(x)/phi(0).
    profile: "doppler" (Gaussian) or "voigt" (damping a_damp).
    Returns tau, S.  The exact surface value is S(0) = sqrt(eps) B for any profile.
    """
    if tau is None:
        deep = 1.0 / eps if profile == "doppler" else max(1.0 / eps, a_damp / eps**2)
        tau = tau_grid_fine(eps, tau_max=max(40.0, 30.0 * deep), h=0.5)
    if xmax is None:
        xmax = 5.0 if profile == "doppler" else min(2e3, 10.0 / np.sqrt(eps))
    # quadrature in x >= 0 (profile symmetric): log-spaced beyond the core
    x = np.concatenate([np.linspace(0, 3, 31)[:-1], np.geomspace(3, xmax, nx)])
    phi = (np.exp(-x**2) / np.sqrt(np.pi) if profile == "doppler"
           else np.real(wofz(x + 1j * a_damp)) / np.sqrt(np.pi))
    w = np.gradient(x) * 2.0                      # both wings
    w /= np.sum(w * phi)                          # enforce int phi dx = 1
    Lbar = np.zeros((len(tau), len(tau)))
    for xi, pi, wi in zip(x, phi, w):
        r = pi / phi[0]
        Lbar += wi * pi * _lambda_matrix_vec(r * tau)
    A = np.eye(len(tau)) - (1 - eps) * Lbar
    S = np.linalg.solve(A, eps * B * np.ones(len(tau)))
    return tau, S


def lambda_iteration(eps, n_iter, B=1.0, tau=None):
    """Return the list of source functions S^(0..n_iter) from Lambda iteration."""
    if tau is None:
        tau = tau_grid(tau_max=max(40.0, 30.0 / np.sqrt(eps)))
    L = lambda_matrix(tau)
    S = B * np.ones(len(tau))           # start from LTE guess S = B
    out = [S.copy()]
    for _ in range(n_iter):
        S = eps * B + (1 - eps) * L @ S
        out.append(S.copy())
    return tau, out


# ---------------------------------------------------------------- gray atmosphere
Q_INF = 0.710446090    # Hopf constant q(infinity)


def hopf_function(tau=None):
    """
    Exact gray LTE atmosphere (radiative equilibrium, S = J = B):
        S(tau) = (3/4) (F/pi) [tau + q(tau)]   with F/pi normalised to 1.
    We solve S = Lambda[S] on a finite grid, attaching the known asymptotic
    form S = 3/4 (t + q_inf) below tau_max.
    """
    if tau is None:
        tau = np.concatenate(([0.0], np.logspace(-4, np.log10(30.0), 260)))
    tmax = tau[-1]
    L = lambda_matrix(tau)
    L[:, -1] -= 0.5 * _E(2, tmax - tau)          # remove constant tail
    d = tmax - tau
    tail = 0.5 * 0.75 * ((tau + Q_INF) * _E(2, d) + d * _E(2, d) + _E(3, d))
    n = len(tau)
    # last point fixed by asymptotic value
    A = np.eye(n) - L
    rhs = tail.copy()
    A[-1, :] = 0.0
    A[-1, -1] = 1.0
    rhs[-1] = 0.75 * (tmax + Q_INF)
    S = np.linalg.solve(A, rhs)
    q = S / 0.75 - tau
    return tau, q


def chandrasekhar_H(mu, n_quad=96, n_iter=4000):
    """H-function for conservative isotropic scattering (characteristic Psi = 1/2).
    Exact gray emergent intensity: I(0,mu) / I(0,1) = H(mu) / H(1)."""
    x, w = np.polynomial.legendre.leggauss(n_quad)
    x = 0.5 * (x + 1.0)
    w = 0.5 * w
    H = np.ones_like(x)
    for _ in range(n_iter):
        integ = (w[None, :] * 0.5 * H[None, :] / (x[:, None] + x[None, :])).sum(axis=1)
        H_new = 1.0 / (1.0 - x * integ)
        # conservative case: use the equivalent, better-converging form
        integ2 = (w[None, :] * 0.5 * x[None, :] * H[None, :] / (x[:, None] + x[None, :])).sum(axis=1)
        H_new = 1.0 / integ2
        if np.max(np.abs(H_new - H)) < 1e-12:
            H = H_new
            break
        H = 0.5 * (H + H_new)
    mu = np.atleast_1d(mu)
    integ = (w[None, :] * 0.5 * x[None, :] * H[None, :] / (mu[:, None] + x[None, :])).sum(axis=1)
    return 1.0 / integ


# ---------------------------------------------------------------- LTE line formation
def voigt(v, a):
    """Voigt function H(a, v) normalised so that H(0, v) = exp(-v^2)."""
    return np.real(wofz(v + 1j * a))


def milne_eddington_residual(v, eta0, beta=1.5, a_damp=0.0):
    """
    LTE (pure absorption) line in the Milne-Eddington model.
        S = B = B0 (1 + beta * tau_c),  tau_nu = (1 + eta_nu) tau_c,
        eta_nu = eta0 * H(a, v).
    Residual flux r = F_nu / F_c (Eddington-Barbier for flux is exact here):
        r = [1 + 2 beta / (3 (1 + eta))] / [1 + 2 beta / 3]
    """
    eta = eta0 * (voigt(v, a_damp) if a_damp > 0 else np.exp(-v**2))
    return (1.0 + 2.0 * beta / (3.0 * (1.0 + eta))) / (1.0 + 2.0 * beta / 3.0)


def equivalent_width(eta0, beta=1.5, a_damp=0.0):
    v = np.linspace(-400, 400, 160001) if a_damp > 0 else np.linspace(-12, 12, 24001)
    r = milne_eddington_residual(v, eta0, beta, a_damp)
    return np.trapezoid(1.0 - r, v)


# ---------------------------------------------------------------- Saha-Boltzmann
def saha_hydrogen(T, Pe):
    """N_II / N_I for hydrogen with electron pressure Pe (Pa). U_I = 2, U_II = 1."""
    ne = Pe / (k * T)
    return (2.0 * 1.0 / 2.0) / ne * (2 * np.pi * m_e * k * T / h**2) ** 1.5 * np.exp(-13.598 * eV / (k * T))


def balmer_fraction(T, Pe):
    """N(n=2) / N_total(H), the population that produces Balmer absorption."""
    r21 = 4.0 * np.exp(-10.199 * eV / (k * T))       # g2/g1 = 8/2
    x = saha_hydrogen(T, Pe)
    return (r21 / (1 + r21)) * (1.0 / (1.0 + x))


# ---------------------------------------------------------------- self test
if __name__ == "__main__":
    print("Wien: lambda_max T =", 2.897771955e-3, "m K ; check numerically:")
    lam = np.linspace(100e-9, 3000e-9, 200001)
    print("   T = 5772 K ->", lam[np.argmax(planck_lambda(lam, 5772))] * 1e9, "nm")
    nu = np.linspace(1e12, 3e15, 300001)
    tot = np.trapezoid(planck_nu(nu, 5772), nu)
    print("int B_nu dnu / (sigma T^4/pi) =", tot / (sigma_SB * 5772**4 / np.pi))

    for eps in (1e-1, 1e-2, 1e-4):
        t, S = solve_scattering_atmosphere(eps)
        print(f"eps = {eps:g}:  S(0)/B = {S[0]:.4f},  sqrt(eps) = {np.sqrt(eps):.4f}")

    for eps in (1e-2, 1e-3):
        t, S = solve_two_level_crd(eps)
        print(f"two-level atom, CRD Doppler, eps = {eps:g}: S(0)/B = {S[0]:.4f} (sqrt(eps) = {np.sqrt(eps):.4f}),"
              f" S = 0.9 B at tau = {np.interp(0.9, S, t):.0f}")

    t, q = hopf_function()
    print(f"Hopf: q(0) = {q[0]:.4f} (exact 1/sqrt3 = {1/np.sqrt(3):.4f}),"
          f" q(1) = {np.interp(1.0, t, q):.4f}, q(5) = {np.interp(5.0, t, q):.4f}")
    print("T(0)/Teff exact gray =", (0.75 * q[0]) ** 0.25, "; Eddington =", 0.5 ** 0.25)

    mu = np.array([0.0, 0.1, 0.2, 0.5, 1.0])
    H = chandrasekhar_H(mu)
    print("H(mu):", np.round(H, 4), " (H(1) tabulated 2.9078)")
    print("exact I(mu)/I(1):", np.round(H / H[-1], 4))
    print("Eddington I(mu)/I(1):", np.round(0.4 * (1 + 1.5 * mu), 4))

    T = np.linspace(4000, 25000, 2000)
    bf = balmer_fraction(T, 20.0)   # Pe = 20 N m^-2 (Carroll & Ostlie example)
    print("Balmer population peaks at T =", T[np.argmax(bf)], "K")
