"""
Reproduces every numerical answer quoted in the worked examples and exam
solutions of the course.  Run:   python3 scripts/worked_examples.py
"""
import numpy as np
from lte_solvers import (h, c, k, sigma_SB, m_e, eV, planck_lambda, planck_nu,
                         saha_hydrogen, hopf_function, chandrasekhar_H,
                         solve_scattering_atmosphere)

a_rad = 4 * sigma_SB / c
L_sun, R_sun, AU, M_sun = 3.828e26, 6.957e8, 1.496e11, 1.989e30
m_H = 1.6735e-27
sigma_T = 6.6524587e-29
r_e = 2.8179403e-15


def hdr(s):
    print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)


def T_from_Blambda(B, lam):
    return h * c / (lam * k) / np.log(1 + 2 * h * c**2 / (lam**5 * B))


hdr("L2  Solar intensity, flux, constancy")
F_surf = L_sun / (4 * np.pi * R_sun**2)
Teff = (F_surf / sigma_SB) ** 0.25
I_sun = F_surf / np.pi
Omega = np.pi * (R_sun / AU) ** 2
print(f"F_surface = {F_surf:.4e} W/m^2  -> Teff = {Teff:.0f} K")
print(f"mean disk intensity I = F/pi = {I_sun:.4e} W m^-2 sr^-1")
print(f"solid angle of Sun at 1 AU = {Omega:.4e} sr ; F(1 AU) = I*Omega = {I_sun*Omega:.1f} W/m^2")
print(f"same via inverse square: {F_surf*(R_sun/AU)**2:.1f} W/m^2")
Tc = 1.57e7
u = a_rad * Tc**4
print(f"solar centre: u = aT^4 = {u:.3e} J/m^3 ; P_rad = u/3 = {u/3:.3e} Pa ; P_gas ~ 2.3e16 Pa -> ratio {u/3/2.3e16:.1e}")

hdr("L3  Planck function")
T_cmb = 2.725
print(f"CMB: nu_max(B_nu) = 5.879e10*T = {5.879e10*T_cmb:.4e} Hz ; lambda_max(B_lambda) = {2.8978e-3/T_cmb*1e3:.3f} mm")
n_gamma = 16 * np.pi * 1.2020569 * (k * T_cmb / (h * c)) ** 3
print(f"CMB photon number density = {n_gamma:.4e} m^-3 = {n_gamma*1e-6:.0f} cm^-3")
print(f"CMB energy density aT^4 = {a_rad*T_cmb**4:.3e} J/m^3")
lam = 500e-9
print(f"B_lambda(500 nm, 5772 K) = {planck_lambda(lam, 5772):.4e} W m^-3 sr^-1")
x = h * c / (lam * k * 5772); print(f"   x = hc/lambda kT = {x:.3f}")
# radio brightness temperature
print("RJ brightness temperature: T_b = c^2 I_nu / (2 k nu^2)")
nu = 1.4e9
Inu = 2.0e-19   # W m^-2 Hz^-1 sr^-1
print(f"   I_nu = {Inu:.1e} at 1.4 GHz -> T_b = {c**2*Inu/(2*k*nu**2):.0f} K")

hdr("L4  Opacity, mean free path, random walk in the Sun")
rho_bar = M_sun / (4 / 3 * np.pi * R_sun**3)
X = 0.7
mu_e = 2 / (1 + X)
n_e = rho_bar / (mu_e * m_H)
ell = 1 / (n_e * sigma_T)
tau = R_sun / ell
t_diff = R_sun**2 / (ell * c)
print(f"mean density = {rho_bar:.0f} kg/m^3 ; mu_e = {mu_e:.3f} ; n_e = {n_e:.3e} m^-3")
print(f"kappa_es = 0.02(1+X) m^2/kg = {0.02*(1+X):.3f} ; check sigma_T/(mu_e m_H) = {sigma_T/(mu_e*m_H):.4f}")
print(f"mean free path = {ell*100:.2f} cm ; tau = {tau:.2e} ; N = tau^2 = {tau**2:.2e}")
print(f"diffusion time R^2/(ell c) = {t_diff:.2e} s = {t_diff/3.156e7:.0f} yr  (light crossing {R_sun/c:.2f} s)")

hdr("L4/L6  Stimulated emission correction 1 - exp(-h nu / kT)")
for xx in (10, 1, 0.1, 0.01):
    print(f"   h nu/kT = {xx:5}: factor = {1-np.exp(-xx):.4f}")
nu21 = 1.420405751e9
print(f"21 cm, T = 100 K: h nu/kT = {h*nu21/(k*100):.3e}")

hdr("L5  HII region free-free slab")
Te = 8000.0
for tau_ in (0.01, 0.1, 1, 3, 10):
    print(f"   tau = {tau_:5}: T_b = Te(1-e^-tau) = {Te*(1-np.exp(-tau_)):.0f} K")
print("Absorption line from foreground cloud: I = I0 e^-tau + S(1-e^-tau)")
I0, S = 1.0, 0.3
for tau_ in (0.1, 1, 5):
    print(f"   I0=1, S=0.3, tau={tau_}: I = {I0*np.exp(-tau_)+S*(1-np.exp(-tau_)):.3f}")
print(f"Extinction A_V = 1.086 tau_V ; tau_V=1 -> A_V = {2.5*np.log10(np.e):.3f} mag")

hdr("L6  Boltzmann and Saha for hydrogen")
for T in (5772, 9900, 20000):
    kT = k * T / eV
    r21 = 4 * np.exp(-10.199 / kT)
    print(f"   T = {T}: kT = {kT:.4f} eV ; N2/N1 = {r21:.3e}")
T, Pe = 9900.0, 20.0
ne = Pe / (k * T)
xr = saha_hydrogen(T, Pe)
print(f"T=9900 K, Pe=20 Pa: n_e = {ne:.3e} m^-3 ; (2pi m_e kT/h^2)^1.5 = {(2*np.pi*m_e*k*T/h**2)**1.5:.3e}")
print(f"   N_II/N_I = {xr:.3f} ; ionized fraction = {xr/(1+xr):.3f}")
T = 5772.0; Pe = 1.5   # roughly photospheric electron pressure ~ 15 dyn/cm^2
xr = saha_hydrogen(T, Pe)
print(f"Solar photosphere T=5772, Pe=1.5 Pa: N_II/N_I = {xr:.2e}")
print(f"Saha constant (2 pi m_e k / h^2)^1.5 = {(2*np.pi*m_e*k/h**2)**1.5:.4e} m^-3 K^-1.5")

hdr("L7  Eddington-Barbier inversion of solar limb darkening at 500 nm")
lam = 500e-9
I1 = 4.0e13
for tau_, frac in ((0.0, 0.36), (1.0, 1.0), (0.5, 0.68)):
    B = frac * I1
    print(f"   S(tau={tau_}) = {frac}*I1 -> T = {T_from_Blambda(B, lam):.0f} K")
print(f"   hc/(lambda k) = {h*c/(lam*k):.0f} K ; 2hc^2/lambda^5 = {2*h*c**2/lam**5:.4e}")

hdr("L8  Scattering atmospheres / Rosseland")
for eps in (0.1, 0.01, 1e-3):
    t, S = solve_scattering_atmosphere(eps)
    edd = 1 - (1 - eps) / (1 + 2 * np.sqrt(eps / 3))
    print(f"   eps={eps:g}: numerical S(0)/B = {S[0]:.4f}, sqrt(eps)={np.sqrt(eps):.4f}, Eddington = {edd:.4f}, "
          f"thermalization depth 1/sqrt(eps) = {1/np.sqrt(eps):.1f}")
print("   Electron scattering atmosphere of an O star: eps = kappa_abs/(kappa_abs+kappa_es)")

hdr("L9  Gray atmosphere")
for Te in (5772.0,):
    print(f"   Teff = {Te}: Eddington T(0) = {Te*0.5**0.25:.0f} K ; exact T(0) = {Te*(np.sqrt(3)/4)**0.25:.0f} K")
    for tau_ in (0.0, 2/3, 1.0, 2.0, 10.0):
        print(f"      tau={tau_:.3f}: T_Edd = {Te*(0.75*(tau_+2/3))**0.25:.0f} K")
t, q = hopf_function()
print(f"   q(0) = {q[0]:.4f}, q(0.1)={np.interp(0.1,t,q):.4f}, q(1) = {np.interp(1,t,q):.4f}, q(inf)~{q[-1]:.4f}")
mu = np.array([0.0, 0.2, 0.5, 1.0]); H = chandrasekhar_H(mu)
print("   exact limb darkening I(mu)/I(1):", np.round(H / H[-1], 4))
print("   Eddington          I(mu)/I(1):", np.round((2 + 3 * mu) / 5, 4))
g = 274.0; kap = 0.03
print(f"   hydrostatic P = g tau / kappa at tau=2/3 (g=274, kappa=0.03 m^2/kg): {g*(2/3)/kap:.3e} Pa")
print(f"   T^4 ratio check: emergent flux 2pi int I mu dmu with I = (3F/4pi)(mu+2/3) -> {2*np.pi*(3/(4*np.pi))*(1/3+1/3):.4f} F")

hdr("L10 Line formation")
for (name, m, lam0, T) in (("H-alpha", m_H, 656.28e-9, 5772.0), ("Fe I", 55.845 * 1.6605e-27, 500e-9, 5772.0),
                           ("H-alpha in A star", m_H, 656.28e-9, 9500.0)):
    v = np.sqrt(2 * k * T / m)
    print(f"   {name}: v_th = {v:.0f} m/s ; Doppler width = {lam0*v/c*1e12:.2f} pm = {lam0*v/c*1e10*1000:.1f} mA")
Nf = 1e15
lam0 = 500e-9
W = np.pi * r_e * lam0**2 * Nf
print(f"   weak line W_lambda = pi r_e lambda^2 N f = {W:.3e} m = {W*1e13:.2f} mA  (N f = 1e15 m^-2)")
beta = 1.5
print(f"   Milne-Eddington max depth (beta=1.5): 1 - 1/(1+2beta/3) = {1-1/(1+2*beta/3):.3f}")
for eta in (1, 10):
    r = (1 + 2 * beta / (3 * (1 + eta))) / (1 + 2 * beta / 3)
    print(f"   eta={eta}: central residual flux = {r:.3f}")
