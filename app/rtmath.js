// Radiative Transfer Lab: physics core (shared with the course scripts' methods).
// SI units throughout. Works in the browser (global RT) and in Node (module.exports).
(function (root) {
  const h = 6.62607015e-34, c = 2.99792458e8, k = 1.380649e-23, sigma = 5.670374e-8;
  const me = 9.1093837e-31, eV = 1.602176634e-19, mH = 1.6735e-27, re = 2.8179403e-15;
  const a_rad = 4 * sigma / c;

  const planckLam = (lam, T) => 2 * h * c * c / Math.pow(lam, 5) / Math.expm1(h * c / (lam * k * T));
  const planckNu = (nu, T) => 2 * h * nu * nu * nu / (c * c) / Math.expm1(h * nu / (k * T));

  // Exponential integrals (Numerical Recipes style)
  function E1(x) {
    if (x <= 0) return Infinity;
    if (x < 1) {
      let sum = 0, term = 1;
      for (let n = 1; n < 60; n++) {
        term *= -x / n;
        const add = -term / n;
        sum += add;
        if (Math.abs(add) < 1e-16 * Math.abs(sum)) break;
      }
      return -0.5772156649015329 - Math.log(x) + sum;
    }
    // continued fraction (Lentz)
    let b = x + 1, cc = 1e300, d = 1 / b, hh = d;
    for (let i = 1; i < 200; i++) {
      const an = -i * i;
      b += 2;
      d = 1 / (an * d + b);
      cc = b + an / cc;
      const del = cc * d;
      hh *= del;
      if (Math.abs(del - 1) < 1e-15) break;
    }
    return hh * Math.exp(-x);
  }
  function En(n, x) {
    if (x <= 0) return n > 1 ? 1 / (n - 1) : Infinity;
    let e = E1(x);
    for (let m = 2; m <= n; m++) e = (Math.exp(-x) - x * e) / (m - 1);
    return e;
  }

  // Voigt function H(a,v) = Re w(v + i a), Humlicek (1982) W4 algorithm
  function voigt(a, v) {
    const x = v, y = a;
    const tr = y, ti = -x;                       // t = y - i x
    const s = Math.abs(x) + y;
    const cmul = (ar, ai, br, bi) => [ar * br - ai * bi, ar * bi + ai * br];
    const cdiv = (ar, ai, br, bi) => { const d = br * br + bi * bi; return [(ar * br + ai * bi) / d, (ai * br - ar * bi) / d]; };
    let w;
    if (s >= 15) {
      const [ur, ui] = cmul(tr, ti, tr, ti);
      const num = [tr * 0.5641896, ti * 0.5641896];
      w = cdiv(num[0], num[1], 0.5 + ur, ui);
    } else if (s >= 5.5) {
      const [ur, ui] = cmul(tr, ti, tr, ti);
      const n1 = cmul(tr, ti, 1.410474 + ur * 0.5641896, ui * 0.5641896);
      const d1 = cmul(ur, ui, 3 + ur, ui);
      w = cdiv(n1[0], n1[1], 0.75 + d1[0], d1[1]);
    } else if (y >= 0.195 * Math.abs(x) - 0.176) {
      const poly = (coefs) => { let r = [coefs[coefs.length - 1], 0]; for (let i = coefs.length - 2; i >= 0; i--) { r = cmul(r[0], r[1], tr, ti); r[0] += coefs[i]; } return r; };
      const num = poly([16.4955, 20.20933, 11.96482, 3.778987, 0.5642236]);
      const den = poly([16.4955, 38.82363, 39.27121, 21.69274, 6.699398, 1]);
      w = cdiv(num[0], num[1], den[0], den[1]);
    } else {
      const [ur, ui] = cmul(tr, ti, tr, ti);
      const polyU = (coefs) => { let r = [coefs[coefs.length - 1], 0]; for (let i = coefs.length - 2; i >= 0; i--) { r = cmul(r[0], r[1], ur, ui); r[0] += coefs[i]; } return r; };
      const num = polyU([36183.31, -3321.9905, 1540.787, -219.0313, 35.76683, -1.320522, 0.56419]);
      const den = polyU([32066.6, -24322.84, 9022.228, -2186.181, 364.2191, -61.57037, 1.841439, -1]);
      const ratio = cdiv(num[0], num[1], den[0], den[1]);
      const tq = cmul(tr, ti, ratio[0], ratio[1]);
      const ex = Math.exp(ur);
      w = [ex * Math.cos(ui) - tq[0], ex * Math.sin(ui) - tq[1]];
    }
    return w[0];
  }

  // Lambda operator matrix for piecewise-linear S on grid tau (constant tail beyond last point)
  function lambdaMatrix(tau) {
    const n = tau.length;
    const L = Array.from({ length: n }, () => new Float64Array(n));
    const E2 = (x) => En(2, Math.max(x, 0)), E3 = (x) => En(3, Math.max(x, 0));
    for (let i = 0; i < n; i++) {
      const ti = tau[i];
      for (let kk = 0; kk < n - 1; kk++) {
        const at = tau[kk], bt = tau[kk + 1], hs = bt - at;
        let M0, M1;
        if (at >= ti) {
          const a = at - ti, b = bt - ti;
          M0 = E2(a) - E2(b);
          M1 = (a * E2(a) + E3(a)) - (b * E2(b) + E3(b));
        } else {
          const a = ti - bt, b = ti - at;
          M0 = E2(a) - E2(b);
          M1 = -((a * E2(a) + E3(a)) - (b * E2(b) + E3(b)));
        }
        L[i][kk] += 0.5 * ((bt - ti) / hs * M0 - M1 / hs);
        L[i][kk + 1] += 0.5 * ((ti - at) / hs * M0 + M1 / hs);
      }
      L[i][n - 1] += 0.5 * E2(tau[n - 1] - ti);
    }
    return L;
  }

  function solveLinear(A, b) {
    const n = b.length, M = A.map((r, i) => { const row = Array.from(r); row.push(b[i]); return row; });
    for (let col = 0; col < n; col++) {
      let piv = col;
      for (let r = col + 1; r < n; r++) if (Math.abs(M[r][col]) > Math.abs(M[piv][col])) piv = r;
      [M[col], M[piv]] = [M[piv], M[col]];
      for (let r = col + 1; r < n; r++) {
        const f = M[r][col] / M[col][col];
        if (f === 0) continue;
        for (let cc = col; cc <= n; cc++) M[r][cc] -= f * M[col][cc];
      }
    }
    const x = new Array(n).fill(0);
    for (let r = n - 1; r >= 0; r--) {
      let s = M[r][n];
      for (let cc = r + 1; cc < n; cc++) s -= M[r][cc] * x[cc];
      x[r] = s / M[r][r];
    }
    return x;
  }

  function tauGrid(tmax, n) {
    const g = [0];
    const lo = Math.log10(1e-4), hi = Math.log10(tmax);
    for (let i = 0; i < n; i++) g.push(Math.pow(10, lo + (hi - lo) * i / (n - 1)));
    return g;
  }

  // Isothermal scattering atmosphere S = eps B + (1-eps) J, B = 1
  function scatteringAtmosphere(eps, nIter, n) {
    n = n || 230;
    const tau = tauGrid(Math.max(40, 30 / Math.sqrt(eps)), n);
    const L = lambdaMatrix(tau);
    const N = tau.length;
    const A = L.map((row, i) => Array.from(row, (v, j) => (i === j ? 1 : 0) - (1 - eps) * v));
    const exact = solveLinear(A, new Array(N).fill(eps));
    let S = new Array(N).fill(1);
    for (let it = 0; it < nIter; it++) {
      const Sn = new Array(N);
      for (let i = 0; i < N; i++) { let s = 0; const row = L[i]; for (let j = 0; j < N; j++) s += row[j] * S[j]; Sn[i] = eps + (1 - eps) * s; }
      S = Sn;
    }
    const k3 = Math.sqrt(3 * eps), C = -1 / (1 + 2 * Math.sqrt(eps / 3));
    const edd = tau.map(t => eps + (1 - eps) * (1 + C * Math.exp(-k3 * t)));
    return { tau, exact, iter: S, edd };
  }

  // Saha for hydrogen: N_II/N_I with U_I = 2, U_II = 1, Pe in Pa
  function sahaH(T, Pe) {
    const ne = Pe / (k * T);
    return Math.pow(2 * Math.PI * me * k * T / (h * h), 1.5) * Math.exp(-13.598 * eV / (k * T)) / ne;
  }
  function balmerFraction(T, Pe) {
    const r21 = 4 * Math.exp(-10.199 * eV / (k * T));
    const x = sahaH(T, Pe);
    return (r21 / (1 + r21)) / (1 + x);
  }

  // Milne-Eddington residual flux
  function meResidual(v, eta0, beta, a) {
    const phi = a > 0 ? voigt(a, v) : Math.exp(-v * v);
    const eta = eta0 * phi;
    return (1 + 2 * beta / (3 * (1 + eta))) / (1 + 2 * beta / 3);
  }
  function equivalentWidth(eta0, beta, a) {
    // integrate 1 - r over v on a sinh-stretched grid (handles damping wings)
    const vmax = a > 0 ? Math.max(12, 20 * Math.sqrt(eta0 * a) + 12) : 12;
    const n = 1200, sMax = Math.asinh(vmax / 2);
    let W = 0, prevV = 0, prevF = 1 - meResidual(0, eta0, beta, a);
    for (let i = 1; i <= n; i++) {
      const v = 2 * Math.sinh(sMax * i / n), f = 1 - meResidual(v, eta0, beta, a);
      W += 0.5 * (f + prevF) * (v - prevV);
      prevV = v; prevF = f;
    }
    // analytic far-wing tail: H(a,v) ~ a / (sqrt(pi) v^2), 1 - r ~ C eta
    if (a > 0) W += (2 * beta / 3) / (1 + 2 * beta / 3) * eta0 * a / (Math.sqrt(Math.PI) * vmax);
    return 2 * W;
  }

  function interp(x, xs, ys) {
    if (x <= xs[0]) return ys[0];
    if (x >= xs[xs.length - 1]) return ys[ys.length - 1];
    let lo = 0, hi = xs.length - 1;
    while (hi - lo > 1) { const m = (lo + hi) >> 1; if (xs[m] > x) hi = m; else lo = m; }
    const t = (x - xs[lo]) / (xs[hi] - xs[lo]);
    return ys[lo] + t * (ys[hi] - ys[lo]);
  }

  const RT = { h, c, k, sigma, me, eV, mH, re, a_rad, planckLam, planckNu, E1, En, voigt,
    lambdaMatrix, solveLinear, tauGrid, scatteringAtmosphere, sahaH, balmerFraction,
    meResidual, equivalentWidth, interp };
  if (typeof module !== 'undefined' && module.exports) module.exports = RT; else root.RT = RT;
})(typeof window !== 'undefined' ? window : globalThis);
