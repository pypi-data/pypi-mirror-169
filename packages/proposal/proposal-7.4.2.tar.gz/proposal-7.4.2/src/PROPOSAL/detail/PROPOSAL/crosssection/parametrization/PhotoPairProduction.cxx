
#include <cmath>

#include "PROPOSAL/crosssection/parametrization/PhotoPairProduction.h"

#include "PROPOSAL/Constants.h"
#include "PROPOSAL/Logging.h"
#include "PROPOSAL/math/MathMethods.h"
#include "PROPOSAL/math/RandomGenerator.h"
#include "PROPOSAL/medium/Components.h"
#include "PROPOSAL/particle/Particle.h"
#include "PROPOSAL/crosssection/parametrization/ParamTables.h"
#include "PROPOSAL/math/Interpolant.h"
#include "PROPOSAL/math/Integral.h"

using namespace PROPOSAL;
using std::make_tuple;

double crosssection::PhotoPairProduction::GetLowerEnergyLim(
    const ParticleDef&) const noexcept
{
    return 2. * ME;
}

crosssection::KinematicLimits
crosssection::PhotoPairProduction::GetKinematicLimits(
    const ParticleDef&, const Component&, double energy) const noexcept
{
    // x is the integration variable here
    KinematicLimits lim;
    if (energy <= 2. * ME) {
        lim.v_min = 0.5;
        lim.v_max = 0.5;
    } else {
        lim.v_min = ME / energy;
        lim.v_max = 1. - ME / energy;
    }
    return lim;
}

std::unique_ptr<crosssection::Parametrization<Component>>
crosssection::PhotoPairTsai::clone() const
{
    using param_t = std::remove_cv_t<std::remove_pointer_t<decltype(this)>>;
    return std::make_unique<param_t>(*this);
}

std::unique_ptr<crosssection::Parametrization<Component>>
crosssection::PhotoPairKochMotz::clone() const
{
    using param_t = std::remove_cv_t<std::remove_pointer_t<decltype(this)>>;
    return std::make_unique<param_t>(*this);
}

crosssection::PhotoPairKochMotz::PhotoPairKochMotz()
    : interpolant_(new Interpolant(photopair_KM_Z, photopair_KM_energies,
                                   photopair_KM_cross, 2, false, false,
                                   2, false, false))
{
    hash_combine(hash, std::string("kochmotz"));
}

double crosssection::PhotoPairKochMotz::DifferentialCrossSection(
        const ParticleDef& p, const Component& comp, double energy, double v) const
{
    if (energy > 50)
        return DifferentialCrossSectionWithoutA(p, comp, energy, v);

    // Correction factor A for low energies given by the Storm and Israel data
    // (doi.org/10.1016/S0092-640X(70)80017-1)
    auto limits = PhotoPairProduction::GetKinematicLimits(p, comp, energy);
    Integral i;
    auto integrand = [this, &p, &comp, energy](double v) {
        return this->DifferentialCrossSectionWithoutA(p, comp, energy, v) / NA * comp.GetAtomicNum() / (1e-24);
    };
    auto dNdx_nocorrection = i.Integrate(limits.v_min, limits.v_max, integrand, 3);
    auto A = interpolant_->InterpolateArray(comp.GetNucCharge(), energy) / dNdx_nocorrection;
    return A * DifferentialCrossSectionWithoutA(p, comp, energy, v);
}

double crosssection::PhotoPairKochMotz::DifferentialCrossSectionWithoutA(
        const ParticleDef&, const Component& comp, double energy, double v) const
{
    double Z3 = std::pow(comp.GetNucCharge(), -1. / 3);
    double logZ = std::log(comp.GetNucCharge());

    double delta = ME * ME / (2 * energy * v * (1 - v));
    double x = 136 * Z3 * 2 * delta / ME;

    // structure functions
    double phi1, phi2, aux;
    if (x <= 1.0) {
        aux = x * x;
        phi1 = 20.867 - 3.242 * x + 0.625 * aux;
        phi2 = 20.029 - 1.930 * x - 0.086 * aux;
    } else {
        phi1 = 21.12 - 4.184 * std::log(x + 0.952);
        phi2 = phi1;
    }

    aux = ALPHA * comp.GetNucCharge();
    aux *= aux;
    auto f_c = aux
               * (1 / (1 + aux) + 0.20206
                  + aux * (-0.0369 + aux * (0.0083 - 0.002 * aux)));

    double Lr, Lp, xi;

    switch ((int)(comp.GetNucCharge() + 0.5)) {
        case 1: {
            Lr = 5.31;
            Lp = 6.144;
            break;
        }
        case 2: {
            Lr = 4.79;
            Lp = 5.621;
            break;
        }

        case 3: {
            Lr = 4.74;
            Lp = 5.805;
            break;
        }

        case 4: {
            Lr = 4.71;
            Lp = 5.924;
            break;
        }

        default: {
            Lr = std::log(184.15 * Z3);
            Lp = std::log(1194 * Z3 * Z3);
            break;
        }
    }

    xi = Lp / (Lr - f_c);

    if (energy < 50)
        f_c = 0;

    auto result = comp.GetNucCharge() * (comp.GetNucCharge() + xi);

    result *= RE * RE * ALPHA * ( (2 * v * v - 2 * v + 1) * (phi1 - 4./3. * logZ - 4. * f_c)
            + 2./3 * v * (1. - v) * (phi2 - 4./3. * logZ - 4 * f_c));

    return result * NA / comp.GetAtomicNum();

}

double crosssection::PhotoPairTsai::DifferentialCrossSection(
    const ParticleDef&, const Component& comp, double energy, double x) const
{
    // Pair production and bremsstrahlung of chraged leptons, Yung-Su Tsai,
    // Review of Modern Physics, Vol. 46, No. 4, October 1974
    // see formula (3.9)

    double Phi1, Phi2, Psi1, Psi2;
    double Z = comp.GetNucCharge();
    double logZ = std::log(comp.GetNucCharge());
    double eta;
    double k = energy;
    double delta = std::pow(ME, 2.) / (2. * k * x * (1. - x)); // (3.20);

    if (Z <= 2.5) {
        // Hydrogen or Helium
        if (Z <= 1.5) {
            eta = 1;
        } else {
            eta = 1.6875;
        }

        double C = delta / (2. * ALPHA * ME * eta);

        Phi1 = 4. / 3. * logZ + 4. * std::log(1. / (2. * eta * ALPHA))
            + 13. / 3. - 2. * std::log(1. + std::pow(C, 2.))
            - (13. / 2.) * C * std::atan(1. / C)
            + (1. / 6.) / (1 + std::pow(C, -2.)); // (3.25), with erratum
        Phi2 = 4. / 3. * logZ + 4. * std::log(1. / (2. * eta * ALPHA))
            + 11. / 3. - 2. * std::log(1 + std::pow(C, 2.))
            + 25. * std::pow(C, 2.) * (1. - C * std::atan(1. / C))
            - 14. * std::pow(C, 2.) * std::log(1 + std::pow(C, -2.)); // (3.26)
        Psi1 = 8. / 3. * logZ + 4. * std::log(1. / (2. * eta * ALPHA))
            + 23. / 3. - 2. * std::log(1 + std::pow(C, 2.))
            - 17.5 * C * std::atan(1. / C)
            + 8. * std::pow(C, 2.) * std::log(1 + std::pow(C, -2.))
            - 1. / 6. / (1 + std::pow(C, -2.)); // (3.27)
        Psi2 = 8. / 3. * logZ + 4. * std::log(1. / (2. * eta * ALPHA))
            + 21. / 3. - 2. * std::log(1 + std::pow(C, 2.))
            - 105. * std::pow(C, 2.) * (1. - C * std::atan(1. / C))
            + 50. * std::pow(C, 2.) * std::log(1. + std::pow(C, -2.))
            - 24. * std::pow(C, 2.)
                * (-std::log(std::pow(C, 2.)) * std::log(1 + std::pow(C, -2.))
                    + dilog(1. + std::pow(C, -2.)) - dilog(1)); // (3.28)
    } else if (Z <= 4.5) {
        // Lithium or Berylium
        double a, b, ap, bp;
        if (Z <= 3.5) {
            a = 100. * std::pow(Z, -1. / 3.) / ME;
            ap = 418.6 * std::pow(Z, -2. / 3.) / ME;
        } else {
            a = 106. * std::pow(Z, -1. / 3.) / ME;
            ap = 571.4 * std::pow(Z, -2. / 3.) / ME;
        }
        b = delta * a;
        bp = delta * ap;

        Phi1 = 2.
                * (1.
                    + std::log(std::pow(a, 2.) * std::pow(Z, 2. / 3.)
                        * std::pow(ME, 2.)))
            - 2. * std::log(1. + std::pow(b, 2.))
            - 4. * b * std::atan(1. / b); // (3.46)
        Phi2 = 2.
                * (2. / 3.
                    + std::log(std::pow(a, 2.) * std::pow(Z, 2. / 3.)
                        * std::pow(ME, 2.)))
            - 2. * std::log(1. + std::pow(b, 2.))
            + 8. * std::pow(b, 2.)
                * (1 - b * std::atan(1. / b)
                    - 0.75 * std::log(1 + std::pow(b, -2.))); // (3.47)
        Psi1 = 2.
                * (1.
                    + std::log(std::pow(ap, 2.) * std::pow(Z, 4. / 3.)
                        * std::pow(ME, 2.)))
            - 2. * std::log(1 + std::pow(bp, 2.))
            - 4. * bp * std::atan(1. / b); // (3.48)
        Psi2 = 2.
                * (2. / 3.
                    + std::log(std::pow(ap, 2.) * std::pow(Z, 4. / 3.)
                        * std::pow(ME, 2.)))
            - 2. * std::log(1. + std::pow(bp, 2.))
            + 8. * std::pow(bp, 2.)
                * (1. - b * std::atan(1. / bp)
                    - 0.75 * std::log(1 + std::pow(bp, -2.))); // (3.49)
    } else {
        // Heavier elements
        double gamma = 200. * delta / (ME * std::pow(Z, 1. / 3.));   // (3.30)
        double epsilon = 200. * delta / (ME * std::pow(Z, 2. / 3.)); // (3.31)

        Phi1 = 20.863 - 2. * std::log(1. + std::pow(0.55846 * gamma, 2.))
            - 4.
                * (1. - 0.6 * std::exp(-0.9 * gamma)
                    - 0.4 * std::exp(-1.5 * gamma)); // (3.38)
        Phi2 = Phi1
            - 2. / 3. * 1.
                / (1. + 6.5 * gamma + 6. * std::pow(gamma, 2.)); // (3.39)
        Psi1 = 28.340 - 2. * std::log(1. + std::pow(3.621 * epsilon, 2.))
            - 4.
                * (1. - 0.7 * std::exp(-8. * epsilon)
                    - 0.3 * std::exp(-29.2 * epsilon)); // (3.40)
        Psi2 = Psi1
            - 2. / 3. * 1.
                / (1. + 40. * epsilon + 400. * std::pow(epsilon, 2.)); // (3.41)
    }

    double z = std::pow(Z / 137., 2.);
    double f = 1.202 * z - 1.0369 * std::pow(z, 2.)
        + 1.008 * std::pow(z, 3.) / (1. + z); // (3.3)

    double aux = (4. / 3. * std::pow(x, 2.) - 4. / 3. * x + 1.)
            * (std::pow(Z, 2.) * (Phi1 - 4. / 3. * logZ - 4. * f)
                + Z * (Psi1 - 8. / 3. * logZ))
        - 2. / 3. * x * (1. - x)
            * (std::pow(Z, 2.) * (Phi1 - Phi2) + Z * (Psi1 - Psi2)); // (3.9)

    aux *= ALPHA * std::pow(RE, 2.) / k; // (3.9)

    double p = std::sqrt(
        std::pow(x * k, 2.) - std::pow(ME, 2.)); // electron momentum
    aux *= x * std::pow(k, 2.) / p; // conversion from differential cross
                                    // section in electron momentum to x

    return std::max(NA / comp.GetAtomicNum() * aux,
        0.); // TODO what are the real factors here, those are just guesses
}

/* PhotoAngleTsaiIntegral::PhotoAngleTsaiIntegral() */
/*     : PhotoAngleDistribution() */
/*     , integral_(IROMB, IMAXS, IPREC) */
/* { */
/* } */

/* PhotoAngleDistribution::DeflectionAngles
 * PhotoAngleTsaiIntegral::SampleAngles( */
/*     const Component& comp, double energy, double rho) */
/* { */
/*     PhotoAngleDistribution::DeflectionAngles angles; */

/*     double rnd1 = RandomGenerator::Get().RandomDouble(); */
/*     double rnd2 = RandomGenerator::Get().RandomDouble(); */
/*     double rnd3 = RandomGenerator::Get().RandomDouble(); */

/*     double subst = std::max(1., std::log10(energy)); */

/*     auto integrand_substitution = [&](double energy, double rho, double t) {
 */
/*         return subst * std::pow(t, subst - 1.) */
/*             * this->FunctionToIntegral(comp, energy, rho, std::pow(t,
 * subst)); */
/*     }; */

/*     double t_min = 0; */
/*     double t_max = std::pow(PI, 1. / subst); */

/*     static_cast<void>(integral_.IntegrateWithRandomRatio(t_min, t_max, */
/*         std::bind(integrand_substitution, energy, rho,
 * std::placeholders::_1), */
/*         3, rnd1)); */

/*     angles.cosphi0 = std::cos(std::pow(integral_.GetUpperLimit(), subst)); */

/*     static_cast<void>(integral_.IntegrateWithRandomRatio(t_min, t_max, */
/*         std::bind(integrand_substitution, energy, rho,
 * std::placeholders::_1), */
/*         3, rnd2)); */

/*     angles.cosphi1 = std::cos(std::pow(integral_.GetUpperLimit(), subst)); */

/*     angles.theta0 = rnd3 * 2. * PI; */
/*     angles.theta1 = std::fmod(angles.theta0 + PI, 2. * PI); */

/*     // Sometimes the intergration fails and -1 instead of 1 is returned... */
/*     if (angles.cosphi0 == -1.) { */
/*         angles.cosphi0 *= (-1); */
/*     } */

/*     if (angles.cosphi1 == -1.) { */
/*         angles.cosphi1 *= (-1); */
/*     } */

/*     return angles; */
/* } */

/* double PhotoAngleTsaiIntegral::FunctionToIntegral( */
/*     const Component& comp, double energy, double x, double theta) */
/* { */

/*     // Pair production and bremsstrahlung of chraged leptons, Yung-Su Tsai,
 */
/*     // Review of Modern Physics, Vol. 46, No. 4, October 1974 */
/*     // see formula (3.5) */

/*     double aux; */
/*     double E = energy * x; // electron energy */
/*     double l = E * E * theta * theta / (ME * ME); */
/*     double Z = comp.GetNucCharge(); */
/*     double Z3 = std::pow(comp.GetNucCharge(), -1. / 3); */
/*     double G2 = Z * Z + Z; */
/*     double tminprimesqrt = (ME * ME * (1. + l)) / (2. * energy * x * (1. -
 * x)); */

/*     double z = std::pow(Z / 137., 2.); */
/*     double f = 1.202 * z - 1.0369 * std::pow(z, 2.) */
/*         + 1.008 * std::pow(z, 3.) / (1. + z); // (3.3) */

/*     double delta; */
/*     double B; */
/*     double X; */
/*     double Xel, Xinel; */

/*     if (Z < 2.5) { */
/*         double eta; */

/*         if (Z < 1.5) { */
/*             eta = 1.; // for hydrogen */
/*         } else { */
/*             eta = 1.6875; // for helium */
/*         } */

/*         delta = ME * ME / (2. * energy * x * (1. - x)); // (3.20) */
/*         B = 2. * ALPHA * ME * eta / tminprimesqrt;      // (3.21) */
/*         Xel = 2. * std::log(ME / delta) - std::log(1. + B * B) + 1. / 6. */
/*             - (4. / 3.) / (1. + B * B) */
/*             + (1. / 6.) / std::pow(1. + B * B, 2.); // (3.18) with erratum */
/*         Xel *= Z * Z; */
/*         Xinel = 2. * std::log(ME / delta) - std::log(1. + B * B) + 11. / 6.
 */
/*             - 4. / (B * B) * std::log(1. + B * B) + (4. / 3.) / (1. + B * B)
 */
/*             - (1. / 6.) / std::pow(1. + B * B, 2.); // (3.19) with erratum */
/*         Xinel *= Z; */
/*     } else { */
/*         // a and aprime according to Table (B.4.) */
/*         double a, aprime; */
/*         if (Z <= 1.5) { */
/*             a = 122.8; */
/*             aprime = 282.4; */
/*         } else if (Z <= 2.5) { */
/*             a = 90.8; */
/*             aprime = 265.8; */
/*         } else if (Z <= 3.5) { */
/*             a = 100.; */
/*             aprime = 418.6; */
/*         } else if (Z <= 4.5) { */
/*             a = 106; */
/*             aprime = 571.4; */
/*         } else { */
/*             a = 111.7; */
/*             aprime = 724.2; */
/*         } */

/*         a *= Z3 / ME; */
/*         aprime *= Z3 * Z3 / ME; */

/*         Xel = std::log(a * a * ME * ME * std::pow(1. + l, 2.) */
/*                   / (a * a * tminprimesqrt * tminprimesqrt + 1.)) */
/*             - 1.; */
/*         Xel *= Z * Z; // (3.44) */
/*         Xinel = std::log(aprime * aprime * ME * ME * std::pow(1. + l, 2.) */
/*                     / (aprime * aprime * tminprimesqrt * tminprimesqrt + 1.))
 */
/*             - 1.; */
/*         Xinel *= Z; // (3.45) */
/*     } */

/*     X = Xel + Xinel; */

/*     // (3.5) with erratum */
/*     aux = G2 */
/*         * (2. * x * (1. - x) / std::pow(1. + l, 2.) */
/*               - 12. * l * x * (1. - x) / std::pow(1. + l, 4.)); */
/*     aux += (X - 2. * Z * Z * f) */
/*         * ((2. * x * x - 2. * x + 1.) / std::pow(1. + l, 2.) */
/*               + (4. * l * x * (1. - x)) / std::pow(1. + l, 4)); */

/*     // aux *= 2. * std::pow(ALPHA, 3.) / (PI * energy) * (E * E / */
/*     // std::pow(ME, 4.)); only overall factor relevant */

/*     aux *= sin(theta); // conversion from differential in cos(theta) to */
/*                        // differential in theta */

/*     return aux; */
/* } */

/* PhotoAngleDistribution::DeflectionAngles
 * PhotoAngleNoDeflection::SampleAngles( */
/*     const Component&, double energy, double rho) */
/* { */
/*     (void)energy; */
/*     (void)rho; */

/*     PhotoAngleDistribution::DeflectionAngles angles; */

/*     angles.cosphi0 = 1.; */
/*     angles.theta0 = 0.; */
/*     angles.cosphi1 = 1.; */
/*     angles.theta1 = 0.; */

/*     return angles; */
/* } */

/* PhotoAngleEGS::PhotoAngleEGS() */
/*     : PhotoAngleDistribution() */
/* { */
/* } */

/* PhotoAngleDistribution::DeflectionAngles PhotoAngleEGS::SampleAngles( */
/*     const Component&, double energy, double rho) */
/* { */
/*     (void)rho; */

/*     double rnd = RandomGenerator::Get().RandomDouble(); */

/*     PhotoAngleDistribution::DeflectionAngles angles; */

/*     double k = energy / ME; */

/*     angles.cosphi0 = std::cos(1. / k); */
/*     angles.cosphi1 = std::cos(1. / k); */
/*     angles.theta0 = rnd * 2. * PI; */
/*     angles.theta1 = std::fmod(angles.theta0 + PI, 2. * PI); */

/*     return angles; */
/* } */
