#include "complex.h"
#include "core.h"
#include "cspecial.h"
#include "special.h"

// Gaussian {{{

WITHIN_KERNEL
ftype gaussian(const ftype x, const ftype mu, const ftype sigma) {
  const ftype s2 = sigma * sigma;
  ftype d2 = (x - mu);
  d2 *= d2;

  return exp(-0.5 * d2 / s2); // / (SQRT_2PI_INV*sigma);
}

// TODO make sure we use the same factor in gaussian and gaussian integral
WITHIN_KERNEL ftype gaussian_integral(const ftype xL, const ftype xU,
                                      const ftype mu, const ftype sigma) {

  const ftype tL = (xL - mu) / sigma;
  const ftype tU = (xU - mu) / sigma;
  /* code from NIKHEF
  if (tL >= tU) return 0; // needed in case umin > a2

  // N.B. Erf is integral from 0
  if (tL*tU<0) // they are at different side of zero
  {
    return M_SQRTPI_2 * (erf(fabs(tU)/M_SQRT2) + erf(fabs(tL)/M_SQRT2) );
  }
  else //They are at the same side of zero
  {
    return M_SQRTPI_2 * fabs( erf(fabs(tU)/M_SQRT2) - erf(fabs(tL)/M_SQRT2) );
  }
  */
  const ftype ans = erf(tU / 1.414213562373095) - erf(tL / 1.414213562373095);
  return ans * sigma * M_SQRTPI_2;
}

// }}}

// Double gaussian {{{

WITHIN_KERNEL
ftype double_gaussian(const ftype x, const ftype mu, const ftype sigma,
                      const ftype dmu, const ftype dsigma, const ftype yae,
                      const ftype res) {
  const ftype mup = mu + dmu;
  const ftype sigmap = sigma + dsigma;
  // if (get_global_id(0) == 0) {
  //   printf("mu=%.2f, sigma=%.2f, dmu=%.2f, dsigma=%.2f, yae=%.2f,
  //   res=%.2f\n", mu, sigma, dmu, dsigma, yae, res);
  // }

  const ftype gauss11 = gaussian(x, mu, sigma);
  const ftype gauss12 = gaussian(x, mu, sigmap);
  const ftype gauss21 = gaussian(x, mup, sigma);
  const ftype gauss22 = gaussian(x, mup, sigmap);

  const ftype gauss = res * gauss11 + (1 - res) * gauss12;
  const ftype gaussp = res * gauss22 + (1 - res) * gauss22;

  return yae * gauss + (1 - yae) * gaussp;
}

WITHIN_KERNEL
ftype double_gaussian_integral(const ftype xL, const ftype xU, const ftype mu,
                               const ftype sigma, const ftype dmu,
                               const ftype dsigma, const ftype yae,
                               const ftype res) {
  const ftype mup = mu + dmu;
  const ftype sigmap = sigma + dsigma;

  const ftype gauss11 = gaussian_integral(xL, xU, mu, sigma);
  const ftype gauss12 = gaussian_integral(xL, xU, mu, sigmap);
  const ftype gauss21 = gaussian_integral(xL, xU, mup, sigma);
  const ftype gauss22 = gaussian_integral(xL, xU, mup, sigmap);

  const ftype gauss = res * gauss11 + (1 - res) * gauss12;
  const ftype gaussp = res * gauss22 + (1 - res) * gauss22;

  return yae * gauss + (1 - yae) * gaussp;
}

// }}}

// Power law {{{

WITHIN_KERNEL ftype power_law_integral(const ftype xL, const ftype xU,
                                       const ftype alpha, const ftype n) {
  int useLog = 0;
  if (fabs(n - 1.0) < 1.0e-14)
    useLog = 1;

  const ftype A = rpow(n / fabs(alpha), n) * exp(-alpha * alpha / 2);
  const ftype B = n / fabs(alpha) - fabs(alpha);

  ftype result = 0.;
  if (useLog) {
    result = A * (log(B + xU) - log(B + xL));
  } else {
    result = A / (1. - n) * (rpow(B + xU, 1. - n) - rpow(B + xL, 1. - n));
  }
  return result;
}

// }}}

// Crystal Ball (right-tail only) {{{

WITHIN_KERNEL
ftype crystal_ball(const ftype x, const ftype c, const ftype s, const ftype a,
                   const ftype n) {
  const ftype t = (a < 0 ? -1 : +1) * (x - c) / s;
  const ftype aa = fabs(a);

  if (t >= -aa)
    return exp(-0.5 * t * t);
  else {
    const ftype A = pow(n / aa, n) * exp(-0.5 * aa * aa);
    const ftype B = n / aa - aa;

    return A / pow(B - t, n);
  }
}

WITHIN_KERNEL
ftype crystal_ball_integral(const ftype xL, const ftype xU, const ftype m0,
                            const ftype sigma, const ftype alpha,
                            const ftype n) {
  const double sqrtPiOver2 = 1.2533141373;
  const double sqrt2 = 1.4142135624;

  double result = 0.0;
  bool useLog = false;

  if (fabs(n - 1.0) < 1.0e-05)
    useLog = true;

  double sig = fabs((double)sigma);

  double tmin = (xL - m0) / sig;
  double tmax = (xU - m0) / sig;

  if (alpha < 0) {
    double tmp = tmin;
    tmin = -tmax;
    tmax = -tmp;
  }

  double absAlpha = fabs((double)alpha);

  if (tmin >= -absAlpha) {
    result += sig * sqrtPiOver2 * (erf(tmax / sqrt2) - erf(tmin / sqrt2));
  } else if (tmax <= -absAlpha) {
    double a = rpow(n / absAlpha, n) * exp(-0.5 * absAlpha * absAlpha);
    double b = n / absAlpha - absAlpha;

    if (useLog) {
      result += a * sig * (log(b - tmin) - log(b - tmax));
    } else {
      result +=
          a * sig / (1.0 - n) *
          (1.0 / (rpow(b - tmin, n - 1.0)) - 1.0 / (rpow(b - tmax, n - 1.0)));
    }
  } else {
    double a = rpow(n / absAlpha, n) * exp(-0.5 * absAlpha * absAlpha);
    double b = n / absAlpha - absAlpha;

    double term1 = 0.0;
    if (useLog) {
      term1 = a * sig * (log(b - tmin) - log(n / absAlpha));
    } else {
      term1 = a * sig / (1.0 - n) *
              (1.0 / (rpow(b - tmin, n - 1.0)) -
               1.0 / (rpow(n / absAlpha, n - 1.0)));
    }

    double term2 =
        sig * sqrtPiOver2 * (erf(tmax / sqrt2) - erf(-absAlpha / sqrt2));

    result += term1 + term2;
  }

  return result != 0. ? result : 1.E-300;
}

// }}}

// Double Crystal Ball {{{

WITHIN_KERNEL ftype double_crystal_ball(const ftype x, const ftype mu,
                                        const ftype sigma, const ftype aL,
                                        const ftype nL, const ftype aR,
                                        const ftype nR) {
  const ftype t = (x - mu) / sigma;

  if (t > fabs(aR)) {
    const ftype A = rpow(nR / fabs(aR), nR) * exp(-0.5 * aR * aR);
    const ftype B = nR / aR - aR;
    return A / rpow(B + t, nR);
  } else if (t < -fabs(aL)) {
    const ftype A = rpow(nL / fabs(aL), nL) * exp(-0.5 * aL * aL);
    const ftype B = nL / aL - aL;
    return A / rpow(B - t, nL);
  } else {
    return exp(-0.5 * t * t);
  }
}

WITHIN_KERNEL ftype double_crystal_ball_integral(
    const ftype xL, const ftype xU, const ftype mu, const ftype sigma,
    const ftype aL, const ftype nL, const ftype aR, const ftype nR) {

  const ftype tL = (xL - mu) / sigma;
  const ftype tU = (xU - mu) / sigma;

  ftype ans = 0.;

  ans += power_law_integral(rmax(-tU, fabs(aL)), rmax(-tL, fabs(aL)), aL, nL);
  ans += power_law_integral(rmax(tL, fabs(aR)), rmax(tU, fabs(aR)), aR, nR);
  // ans += gaussian_integral(max( tL,-fabs(a1)), min( tU, fabs(a2)), 0., 1.);
  ans += gaussian_integral(rmax(tL, -fabs(aL)), rmin(tU, fabs(aR)), 0., 1.);
  // printf("%.16f\\n", gaussian_integral(xL, xU, mu, sigma));

  return sigma * ans;
}

// }}}

// Amoroso {{{

WITHIN_KERNEL ftype amoroso(const ftype x, const ftype a, const ftype theta,
                            const ftype alpha, const ftype beta) {
  const ftype d = (x - a) / theta;
  return rpow(d, alpha * beta - 1) * exp(-rpow(d, beta));
}

WITHIN_KERNEL ftype amoroso_integral(const ftype x, const ftype a,
                                     const ftype theta, const ftype alpha,
                                     const ftype beta) {
  const ftype d = (x - a) / theta;
  return rpow(d, alpha * beta - 1) * exp(-rpow(d, beta));
}

// }}}

// Shoulder {{{

WITHIN_KERNEL
ftype shoulder(const ftype x, const ftype mu, const ftype sigma,
               const ftype trans) {
  const ftype shift = mu - trans;
  const ftype beta = (mu - shift) / (sigma * sigma);
  const ftype c = exp(-0.5 * rpow((shift) / sigma, 2)) * exp(-beta * shift);
  if (x <= shift) {
    return c * exp(beta * x);
  };
  return exp(-0.5 * rpow((x - mu) / sigma, 2));
}

// }}}

// Argus {{{

WITHIN_KERNEL
ftype argus(const ftype x, const ftype m0, const ftype c, const ftype p) {
  if (x >= m0) {
    return 0.0;
  }
  const ftype a = x * rpow(1 - (x / m0) * (x / m0), p);
  const ftype b = exp(c * (1 - (x / m0) * (x / m0)));

  return a * b;
}

WITHIN_KERNEL
ftype argus_integral(const ftype xLL, const ftype xUL, const ftype m0,
                     const ftype c, const ftype p) {
  // if (x>=m0)
  // {
  //   return 0.0;
  // }
  const ftype pi = M_PI;
  const ftype min = (xLL < m0) ? xLL : m0;
  const ftype max = (xUL < m0) ? xUL : m0;
  const ftype f1 = (1. - rpow(min / m0, 2));
  const ftype f2 = (1. - rpow(max / m0, 2));
  ftype aLow, aHigh;

  if (c < 0.) {
    aLow = -0.5 * m0 * m0 *
           (exp(c * f1) * sqrt(f1) / c +
            0.5 / rpow(-c, 1.5) * sqrt(pi) * erf(sqrt(-c * f1)));
    aHigh = -0.5 * m0 * m0 *
            (exp(c * f2) * sqrt(f2) / c +
             0.5 / rpow(-c, 1.5) * sqrt(pi) * erf(sqrt(-c * f2)));
  } else if (c == 0.) {
    aLow = -m0 * m0 / 3. * f1 * sqrt(f1);
    aHigh = -m0 * m0 / 3. * f1 * sqrt(f2);
  } else {
    aLow = 0.5 * m0 * m0 * exp(c * f1) / (c * sqrt(c)) *
           (0.5 * sqrt(pi) * cim(cwofz(C(sqrt(c * f1), 0))) - sqrt(c * f1));
    aHigh = 0.5 * m0 * m0 * exp(c * f2) / (c * sqrt(c)) *
            (0.5 * sqrt(pi) * cim(cwofz(C(sqrt(c * f2), 0))) - sqrt(c * f2));
  }
  const ftype area = aHigh - aLow;
  // cout << "c = " << c << "aHigh = " << aHigh << " aLow = " << aLow << " area
  // = " << area << endl ;
  return area;
}

// }}}

// Physics Background {{{

WITHIN_KERNEL
ftype physbkg(const ftype m, const ftype m0, const ftype c, const ftype s) {
  // if (get_global_id(0) == 0){
  //   printf("pars = %f, %f %f\n", m0, c, s);
  // }

  /*
  const ftype ssq = s*s;
  const ftype sfth = ssq*ssq;
  const ftype csq = c*c;
  const ftype m0sq = m0*m0;
  const ftype xsq = m0sq;
  const ftype msq = m*m;

  const ftype up = 0.5*s * ( 2*exp(m0* (c + m/ssq) - (xsq + msq)/(2.*ssq) ) *s*
  (-m0sq + csq*sfth + xsq + m0*m + msq + ssq*(2 + c*m0 + 2*c*m) ) +
  exp((csq*sfth + xsq + 2*c*ssq*m + msq)/(2.*ssq) - (xsq +
  msq)/(2.*ssq))*sqrt(2*M_PI)* (c*ssq + m)*(-m0sq + csq*sfth + msq + ssq*(3 +
  2*c*m))* erf((c*ssq - m0 + m)/(sqrt(2.)*s)));

  const ftype down = 0.5*s*(exp(-(msq)/(2.*ssq)) *s * 2 *s* (-m0sq + csq*sfth +
                 msq + ssq*(2 + 2*c*m)) + exp((csq*sfth + 2*c*ssq*m +
  msq)/(2.*ssq) -(msq)/(2.*ssq)  )*sqrt(2*M_PI)* (c*ssq + m)*(-m0sq + csq*sfth +
  msq + ssq*(3 + 2*c*m))* erf((c*ssq + m)/(sqrt(2.)*s)));

  return (up-down)<=0 ? 0 : (m-m0)>6*s ? 0 : (up-down);
  */
  const ftype ssq = s * s;
  const ftype sfth = ssq * ssq;
  const ftype csq = c * c;
  const ftype m0sq = m0 * m0;
  const ftype xsq = m0sq;
  const ftype msq = m * m;

  const ftype up =
      0.5 * s *
      (2.0 * exp(m0 * (c + m / ssq) - (xsq + msq) / (2. * ssq)) * s *
           (-m0sq + csq * sfth + xsq + m0 * m + msq +
            ssq * (2 + c * m0 + 2 * c * m)) +
       exp((csq * sfth + xsq + 2 * c * ssq * m + msq) / (2. * ssq) -
           (xsq + msq) / (2. * ssq)) *
           sqrt(2. * M_PI) * (c * ssq + m) *
           (-m0sq + csq * sfth + msq + ssq * (3 + 2 * c * m)) *
           erf((c * ssq - m0 + m) / (sqrt(2.) * s)));

  const ftype down = 0.5 * s *
                     (exp(-(msq) / (2. * ssq)) * s * 2 * s *
                          (-m0sq + csq * sfth + msq + ssq * (2 + 2 * c * m)) +
                      exp((csq * sfth + 2 * c * ssq * m + msq) / (2. * ssq) -
                          (msq) / (2. * ssq)) *
                          sqrt(2. * M_PI) * (c * ssq + m) *
                          (-m0sq + csq * sfth + msq + ssq * (3 + 2 * c * m)) *
                          erf((c * ssq + m) / (sqrt(2.) * s)));

  // if (get_global_id(0) == 0){
  //   printf("up_erf = %f\n", erf((c*ssq - m0 + m)/(sqrt(2.)*s)) );
  //   printf("up, down = %f, %f\n", up, down);
  // }
  return (up - down) <= 0 ? 0 : (m - m0) > 6 * s ? 0 : (up - down);
}

// }}}

// Generalized hyperbolic distribution {{{

WITHIN_KERNEL
ftype hyperbolic_distribution(const ftype x, const ftype lambda,
                              const ftype alpha, const ftype beta,
                              const ftype delta) {
  // WARNING: This function is defined by the logaritm of its parts, and
  //          afterwards the exponetial is taken. This is mainly to avoid
  //          posible numerical problems.

  ftype out = 0.0;
  ftype const var = x * x + delta * delta;

  // NOTE: This is just a note for the future reader. If you get in trouble
  //       because of some differences you found in the ipatia distribution
  //       they could have be arisen by the following lines.

  // The generalized hyperbolic distribuition definition is defined such that
  // gamma = sqrt(alpha*alpha - beta*beta). But this only affect the p.d.f.
  // normalization. hyperbolic_distribution is called in ipatia distribution
  // where it was defined to be gamma = alpha.
  // ftype const gamma = sqrt(alpha*alpha - beta*beta);
  ftype const gamma = alpha;

  // numerator: eq 8 of arXiv:1312.5000v2
  out += 0.5 * (lambda - 0.5) * log(var); // (var)^(lambda/2-1/4)
  out += beta * x;                        // exp(beta(m-mu))
  // printf("a %f\n", out);
  out += log(rkv(lambda - 0.5, alpha * sqrt(var))); // besselK term
  // printf("lambda, x %f %f\n", lambda-0.5, alpha*sqrt(var));
  // printf("b %f\n", out);
  //  denominator: normalize pdf
  out -= (lambda - 0.5) * log(alpha); // 1/(alpha^(0.5-lambda))
  // printf("out -> %f\n", out);
  out -= lambda * log(delta / gamma);     // (gamma/delta)^lambda
  out -= log(sqrt(2.0 * M_PI));           // 1/sqrt(2*pi)
  out -= log(rkv(lambda, gamma * delta)); // besselK(lmabda,gamma*delta)
  // printf("out --> %f\n", out);
  return exp(out);
}

// }}}

// Ipatia {{{

WITHIN_KERNEL
ftype ipatia(const ftype x, const ftype mu, const ftype sigma,
             const ftype lambda, const ftype zeta, const ftype beta,
             const ftype a, const ftype n, const ftype a2, const ftype n2) {
  const ftype d = x - mu; // define the running centroid
  const ftype d2 = d * d;
  const ftype aLsigma = a * sigma;  // left tail starting point
  const ftype aRsigma = a2 * sigma; // right tail starting point

  if (zeta != 0.0) {
    // WARNING: careful if zeta -> 0. You can implement a function for the
    //          ratio, but carefull again that |nu + 1 | != |nu| + 1 so you
    //          jave to deal wiht the signs
    const ftype phi = rkv(lambda + 1., zeta) / rkv(lambda, zeta);
    const ftype alpha = sqrt(zeta * phi) / sigma;
    const ftype delta = sqrt(zeta / phi) * sigma;
    // const ftype cons1 = sigma/sqrt(phi);
    // alpha = sqrt(zeta) / const1
    // delta = sqrt(zeta) * const1

    // constrain alpha and beta
    // if (alpha*alpha > beta*beta)
    // {
    //   printf("tails will raise\n");
    //   return 0.0; // WARNING HERE
    // }

    if (d < -aLsigma) {
      const ftype b = -aLsigma;
      // const ftype gamma = sqrt(alpha*alpha - beta*beta);
      const ftype gamma = alpha; /* original ipatia implementation */
      const ftype dg = delta * gamma;
      const ftype var = delta * delta + b * b;
      const ftype sqvar = sqrt(var);
      const ftype alphasq = alpha * sqvar;
      const ftype no =
          rpow(gamma / delta, lambda) / rkv(lambda, dg) * SQRT_2PI_INV;
      const ftype ns1 = 0.5 - lambda;
      const ftype k1 = hyperbolic_distribution(b, lambda, alpha, beta, delta);
      ftype k2;
      k2 = -b * alphasq *
           (rkv(lambda - 1.5, alphasq) + rkv(lambda + 0.5, alphasq));
      k2 += (2.0 * (beta * var + b * lambda) - b) * rkv(ns1, alphasq);
      k2 *= no * rpow(alpha, ns1);
      k2 *= rpow(var, 0.5 * lambda - 1.25);
      k2 *= 0.5 * exp(beta * b);
      const ftype B = -aLsigma + n * k1 / k2;
      const ftype A = k1 * rpow(B + aLsigma, n);
      return A * rpow(B - d, -n);
    } else if (d > aRsigma) {
      const ftype b = aRsigma;
      // const ftype gamma = sqrt(alpha*alpha - beta*beta);
      const ftype gamma = alpha; /* original ipatia implementation */
      const ftype dg = delta * gamma;
      const ftype var = delta * delta + b * b;
      const ftype sqvar = sqrt(var);
      const ftype alphasq = alpha * sqvar;
      const ftype no =
          rpow(gamma / delta, lambda) / rkv(lambda, dg) * SQRT_2PI_INV;
      const ftype ns1 = 0.5 - lambda;
      const ftype k1 = hyperbolic_distribution(b, lambda, alpha, beta, delta);
      ftype k2;
      k2 = -b * alphasq *
           (rkv(lambda - 1.5, alphasq) + rkv(lambda + 0.5, alphasq));
      k2 += (2.0 * (beta * var + b * lambda) - b) * rkv(ns1, alphasq);
      k2 *= no * rpow(alpha, ns1);
      k2 *= rpow(var, 0.5 * lambda - 1.25);
      k2 *= 0.5 * exp(beta * b);
      const ftype B = -aRsigma - n2 * k1 / k2;
      const ftype A = k1 * rpow(B + aRsigma, n2);
      return A * rpow(B + d, -n2);
    } else {
      return hyperbolic_distribution(d, lambda, alpha, beta, delta);
    }
  } else if (lambda < 0.0) {
    // For z == 0 the phi ratio is much simpler (if lambda is negative).
    // Actually this function can be analytically integrated too. This integral
    // is not yet implemented in ipanema. Some 2F1 functions need to be
    // writen before.
    ftype delta2 = (lambda >= -1.0) ? sigma : sigma * sqrt(-2.0 - 2.0 * lambda);
    delta2 *= delta2;
    if (delta2 == 0) {
      // printf("DIVISION BY ZERO\n");
      return MAXNUM;
    }

    if (d < -aLsigma) {
      const ftype fb = exp(-beta * aLsigma); // function at boundary
      const ftype phi = 1. + aLsigma * aLsigma / delta2;
      const ftype k1 = fb * rpow(phi, lambda - 0.5);
      ftype k2 = beta * k1;
      k2 -= 2.0 * fb * (lambda - 0.5) * rpow(phi, lambda - 1.5) * aLsigma /
            delta2;
      const ftype B = -aLsigma + n * k1 / k2;
      const ftype A = k1 * rpow(B + aLsigma, n);
      return A * rpow(B - d, -n);
    } else if (d > aRsigma) {
      const ftype fb = exp(beta * aRsigma); // function at boundary
      const ftype phi = 1. + aRsigma * aRsigma / delta2;
      const ftype k1 = fb * rpow(phi, lambda - 0.5);
      ftype k2 = beta * k1;
      k2 += 2.0 * fb * (lambda - 0.5) * rpow(phi, lambda - 1.5) * aRsigma /
            delta2;
      const ftype B = -aRsigma - n2 * k1 / k2;
      const ftype A = k1 * rpow(B + aRsigma, n2);
      return A * rpow(B + d, -n2);
    } else {
      return exp(beta * d) * rpow(1.0 + d2 / delta2, lambda - 0.5);
    }
  } else {
    // printf("zeta = 0 only suported if lambda < 0, and lambda = %f\n",
    // lambda);
    return MAXNUM;
  }
}

// }}}

// Johnson's SU {{{

WITHIN_KERNEL ftype johnson_su(const ftype x, const ftype mu, const ftype sigma,
                               const ftype gamma, const ftype delta) {
  const ftype d = (x - mu) / sigma;

  ftype ans = (delta) / (sigma * sqrt(2 * M_PI));
  ans /= sqrt(1 + d * d);
  ans *= exp(-0.5 * rpow(gamma + delta * asinh(d), 2));
  return ans;
}

// }}}

WITHIN_KERNEL ftype poly1(const double t, const double a, const double b) {
  return a * t + b;
}

WITHIN_KERNEL ftype poly2(const double t, const double a, const double b,
                          const double c) {
  return poly1(t, poly1(t, a, b), c);
}

WITHIN_KERNEL ftype poly3(const double t, const double a, const double b,
                          const double c, const double d) {
  return poly2(t, poly1(t, a, b), c, d);
}

/* Evaluates the Chebyshev polinomial in the [xL, xH] interval with the
   set of coefficients t[deg].
*/
WITHIN_KERNEL ftype chebyshev(const ftype _x, const GLOBAL_MEM ftype *t,
                              const int deg, const ftype xmin,
                              const ftype xmax) {
  const ftype x = -1. + 2. * (_x - xmin) / (xmax - xmin);
  const ftype x2 = x * x;
  ftype sum = 0;
  switch (deg) {
  case 7:
    sum += t[7] * x * poly3(x2, 64, -112, 56, -7);
  case 6:
    sum += t[6] * poly3(x2, 32, -48, 18, -1);
  case 5:
    sum += t[5] * x * poly2(x2, 16, -20, 5);
  case 4:
    sum += t[4] * poly2(x2, 8, -8, 1);
  case 3:
    sum += t[3] * x * poly1(x2, 4, -3);
  case 2:
    sum += t[2] * poly1(x2, 2, -1);
  case 1:
    sum += t[1] * x;
  case 0:
    sum += t[0] * 1;
    break;
  default:
    return Inf; // printf("Higher than 7 poly not implemented\n");
  }
  return sum;
}

WITHIN_KERNEL ftype chebyshevIntegral(const ftype _x, const GLOBAL_MEM ftype *t,
                                      const int deg, const ftype xmin,
                                      const ftype xmax) {
  const ftype x = -1. + 2. * (_x - xmin) / (xmax - xmin);
  const ftype x2 = x * x;
  ftype sum = 0;
  switch (deg) {
  case 7:
    sum += t[7] * x2 * poly3(x2, 8., -112. / 6., 14., -7. / 2.);
  case 6:
    sum += t[6] * x * poly3(x2, 32. / 7., -48. / 5., 6., -1.);
  case 5:
    sum += t[5] * x2 * poly2(x2, 16. / 6., -5., 2.5);
  case 4:
    sum += t[4] * x * poly2(x2, 8. / 5., -8. / 3., 1.);
  case 3:
    sum += t[3] * x2 * poly1(x2, 1., -3. / 2.);
  case 2:
    sum += t[2] * x * poly1(x2, 2. / 3., -1.);
  case 1:
    sum += t[1] * x2 * 0.5;
  case 0:
    sum += t[0] * x;
    break;
  default:
    return Inf; // printf("Higher than 7 poly not implemented\n");
  }

  // return half of the range since the normalised range runs from -1 to 1
  // which has a range of two
  return 0.5 * (xmax - xmin) * sum;
}

// vim:foldmethod=marker
