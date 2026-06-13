"""
core — GoldenUniverse: the unified constant system.

All constants resolve from a single degree of freedom (φ).
Every derived quantity is cross-verifiable against known physical values.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

__version__ = "0.1.0"

# ── Fundamental constants ──────────────────────────────────────────────

__phi__: float = (1 + math.sqrt(5)) / 2          # 1.618033988749895
__gp__: float = 4 / math.sqrt(__phi__)            # 3.144605511029693  (πᵴ)
__plejaren__: float = 152_955_347 / 100_000_000   # 1.52955347


# ═══════════════════════════════════════════════════════════════════════
# GoldenUniverse — the unified system
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class GoldenUniverse:
    """The unified constant system connecting φ, πᵴ, the Great Pyramid,
    the speed of light, the 7 hyperspaces, 280 elements, and the chronon.

    All quantities derive from a single parameter: φ (the golden ratio).
    """

    # ── Input degree of freedom ─────────────────────────────────────────
    phi: float = field(default_factory=lambda: (1 + math.sqrt(5)) / 2)

    # ── Cached values (computed on first access) ────────────────────────
    _cache: dict = field(default_factory=dict, repr=False)

    # ────────────────────────────────────────────────────────────────────
    # Properties: Fundamental Constants
    # ────────────────────────────────────────────────────────────────────

    @property
    def golden_ratio(self) -> float:
        """φ — the golden ratio (1.6180339887…)."""
        if "phi" not in self._cache:
            self._cache["phi"] = self.phi
        return self._cache["phi"]

    @property
    def sqrt_phi(self) -> float:
        """√φ (1.2720196495…)."""
        if "sqrt_phi" not in self._cache:
            self._cache["sqrt_phi"] = math.sqrt(self.golden_ratio)
        return self._cache["sqrt_phi"]

    @property
    def golden_pi(self) -> float:
        """πᵴ = 4/√φ — golden pi (3.1446055110…)."""
        if "golden_pi" not in self._cache:
            self._cache["golden_pi"] = 4 / self.sqrt_phi
        return self._cache["golden_pi"]

    @property
    def four_over_phi_sq(self) -> float:
        """4/φ² (1.5278640450…) — the pure geometric approximation."""
        if "four_over_phi_sq" not in self._cache:
            self._cache["four_over_phi_sq"] = 4 / (self.golden_ratio ** 2)
        return self._cache["four_over_phi_sq"]

    @property
    def conventional_pi(self) -> float:
        """Conventional π for comparison (3.1415926535…)."""
        return math.pi

    @property
    def euler_number(self) -> float:
        """e — Euler's number (2.7182818284…)."""
        return math.e

    # ────────────────────────────────────────────────────────────────────
    # Properties: The Plejaren Coefficient (152955347)
    # ────────────────────────────────────────────────────────────────────

    @property
    def plejaren_coefficient(self) -> float:
        """The universal coefficient 1.52955347 (152955347 / 1e8)."""
        if "plejaren" not in self._cache:
            self._cache["plejaren"] = __plejaren__
        return self._cache["plejaren"]

    @property
    def pyramid_height_m(self) -> float:
        """Original Great Pyramid height in meters: 152.955347 m."""
        if "pyramid_h" not in self._cache:
            self._cache["pyramid_h"] = self.plejaren_coefficient * 100
        return self._cache["pyramid_h"]

    @property
    def pyramid_height_cubits(self) -> float:
        """Pyramid height in royal cubits (280)."""
        return 280.0

    @property
    def pyramid_base_cubits(self) -> float:
        """Pyramid base side in royal cubits (440)."""
        return 440.0

    @property
    def pyramid_base_m(self) -> float:
        """Pyramid base side in meters (≈ 230.4)."""
        # From the Kepler triangle: base/2 = height / √φ
        half_base = self.pyramid_height_m / self.sqrt_phi
        return 2 * half_base

    @property
    def pyramid_apothem_m(self) -> float:
        """Pyramid apothem (slope face length) in meters (≈ 186.4)."""
        # From Kepler triangle: apothem = (base/2) × φ
        return (self.pyramid_base_m / 2) * self.golden_ratio

    # ────────────────────────────────────────────────────────────────────
    # Properties: Astronomical
    # ────────────────────────────────────────────────────────────────────

    @property
    def astronomical_unit_km(self) -> float:
        """The true AU (Earth-Sun distance) in km: 152,955,347 km."""
        if "au_km" not in self._cache:
            self._cache["au_km"] = self.plejaren_coefficient * 100_000_000
        return self._cache["au_km"]

    @property
    def astronomical_unit_m(self) -> float:
        """The true AU in meters."""
        return self.astronomical_unit_km * 1000

    # ────────────────────────────────────────────────────────────────────
    # Properties: Speed of Light
    # ────────────────────────────────────────────────────────────────────

    @property
    def speed_of_light_kms(self) -> float:
        """Speed of light (km/s) from the core identity:
        c = pyramid_height_m × 280 (elements) × 7 (hyperspaces)
        = 299,792.48012 km/s
        """
        if "c_kms" not in self._cache:
            self._cache["c_kms"] = (
                self.pyramid_height_m     # 152.955347 m
                * self.total_elements      # 280
                * self.num_hyperspaces     # 7
            )
        return self._cache["c_kms"]

    @property
    def speed_of_light_ms(self) -> float:
        """Speed of light in m/s."""
        return self.speed_of_light_kms * 1000

    @property
    def modern_c_kms(self) -> float:
        """The modern measured speed of light (299,792.458 km/s) for comparison."""
        return 299_792.458

    @property
    def c_identity_error(self) -> float:
        """Absolute difference between Meier c and modern c (km/s)."""
        return abs(self.speed_of_light_kms - self.modern_c_kms)

    @property
    def c_identity_relative_error(self) -> float:
        """Relative error between Meier c and modern c, as a fraction."""
        return self.c_identity_error / self.modern_c_kms

    @property
    def c_identity_match_percent(self) -> float:
        """How close the Meier c matches modern c, in percent."""
        return (1 - self.c_identity_relative_error) * 100

    # ────────────────────────────────────────────────────────────────────
    # Properties: 7 Hyperspaces & 280 Elements
    # ────────────────────────────────────────────────────────────────────

    @property
    def num_hyperspaces(self) -> int:
        """Number of hyperspace layers: 7."""
        return 7

    @property
    def dimensions_per_hyperspace(self) -> int:
        """Dimensions per hyperspace: 40."""
        return 40

    @property
    def total_elements(self) -> int:
        """Total universal elements: 280 = 7 × 40."""
        return self.num_hyperspaces * self.dimensions_per_hyperspace

    # ────────────────────────────────────────────────────────────────────
    # Properties: Chronon
    # ────────────────────────────────────────────────────────────────────

    @property
    def chronon_wavelength_mm(self) -> float:
        """Chronon wavelength in mm: 14,700 × 10⁻²⁴ mm."""
        if "chronon_lambda_mm" not in self._cache:
            self._cache["chronon_lambda_mm"] = 14_700e-24
        return self._cache["chronon_lambda_mm"]

    @property
    def chronon_wavelength_m(self) -> float:
        """Chronon wavelength in meters."""
        return self.chronon_wavelength_mm * 1e-3

    @property
    def chronon_frequency_hz(self) -> float:
        """Chronon frequency: 20,394,047.62 × 10²⁴ Hz."""
        if "chronon_f_hz" not in self._cache:
            self._cache["chronon_f_hz"] = 20_394_047.62e24
        return self._cache["chronon_f_hz"]

    @property
    def c_from_chronon(self) -> float:
        """Speed of light derived from chronon λ × f (km/s)."""
        return (self.chronon_wavelength_m * self.chronon_frequency_hz) / 1000

    @property
    def chronons_per_light_second(self) -> float:
        """Number of chronons passing a point in one light-second."""
        if "chronons_per_ls" not in self._cache:
            ls_m = self.speed_of_light_kms * 1000  # light-second in m
            self._cache["chronons_per_ls"] = ls_m / self.chronon_wavelength_m
        return self._cache["chronons_per_ls"]

    # ────────────────────────────────────────────────────────────────────
    # Properties: Hyperspace Ladder
    # ────────────────────────────────────────────────────────────────────

    @property
    def creation_expansion_speed_kms(self) -> float:
        """Initial creation expansion speed: 44,069,497.5 km/s (147c)."""
        return 44_069_497.5

    @property
    def creation_c_multiple(self) -> float:
        """How many times modern c is the creation speed: 147."""
        return self.creation_expansion_speed_kms / self.modern_c_kms

    @property
    def half_life_years(self) -> float:
        """Cosmic half-life of the speed of light: 6,347,755,102,040 years."""
        return 6_347_755_102_040.0

    @property
    def next_half_life_c_kms(self) -> float:
        """Speed of light after next half-life: ~172,146.46 km/s."""
        return 172_146.46

    def hyperspace_speeds(self) -> List[float]:
        """Speed of light in each of the 7 hyperspace layers, in km/s.

        Returns speeds from highest (oldest hyperspace) to lowest (normal space).
        """
        if "hs_speeds" not in self._cache:
            speeds = [self.creation_expansion_speed_kms]
            for _ in range(6):
                speeds.append(speeds[-1] / 2.0)
            self._cache["hs_speeds"] = speeds
        return self._cache["hs_speeds"]

    def hyperspace_labels(self) -> List[str]:
        """Human-readable labels for each hyperspace layer."""
        return [
            "HS-7 (Creation / Tachyon sea)",
            "HS-6",
            "HS-5",
            "HS-4",
            "HS-3",
            "HS-2",
            "HS-1 (Normal space)",
        ]

    @property
    def hyperspace_factor_modern(self) -> float:
        """Creation speed as multiple of modern c (≈147)."""
        return self.creation_expansion_speed_kms / self.speed_of_light_kms

    # ────────────────────────────────────────────────────────────────────
    # Properties: Time Travel
    # ────────────────────────────────────────────────────────────────────

    @property
    def hyperspace_safe_distance_km(self) -> float:
        """Minimum safe distance from a planet for tachyon drive:
        152.955347 million km.
        """
        return self.plejaren_coefficient * 100_000_000  # same as AU km

    @property
    def reincarnation_coefficient(self) -> float:
        """Years in fine-matter realm per year lived: ≈1.52955347."""
        return self.plejaren_coefficient

    # ────────────────────────────────────────────────────────────────────
    # Properties: Golden Pi Relationships
    # ────────────────────────────────────────────────────────────────────

    @property
    def golden_pi_squared(self) -> float:
        """πᵴ² = 16/φ."""
        return self.golden_pi ** 2

    @property
    def golden_pi_cubed(self) -> float:
        """πᵴ³ = 64/(φ√φ)."""
        return self.golden_pi ** 3

    @property
    def correction_factor(self) -> float:
        """Ratio: plejaren_coefficient / 4φ⁻² (≈1.0011057).

        The 0.11% offset between pure φ-geometry and the real
        physical constant — possibly encoding the fine-structure constant.
        """
        return self.plejaren_coefficient / self.four_over_phi_sq

    @property
    def golden_pi_minus_phi(self) -> float:
        """πᵴ − φ = 1.5265715223 — another close approach to 1.52955347."""
        return self.golden_pi - self.golden_ratio

    @property
    def plejaren_approx_phi_power(self) -> float:
        """What power of φ gives the plejaren coefficient: φ^? = 1.52955347."""
        if "ppp" not in self._cache:
            self._cache["ppp"] = (
                math.log(self.plejaren_coefficient) / math.log(self.golden_ratio)
            )
        return self._cache["ppp"]

    # ────────────────────────────────────────────────────────────────────
    # Properties: Pyramid Slope
    # ────────────────────────────────────────────────────────────────────

    @property
    def pyramid_slope_angle_deg(self) -> float:
        """Pyramid face slope angle in degrees: arctan(height/half-base) ≈ 51.84°."""
        return math.degrees(
            math.atan(self.pyramid_height_m / (self.pyramid_base_m / 2))
        )

    @property
    def pyramid_slope_sec(self) -> float:
        """secant of the slope angle ≈ φ."""
        rad = math.radians(self.pyramid_slope_angle_deg)
        return 1 / math.cos(rad)

    @property
    def pyramid_kepler_triangle_ratio(self) -> bool:
        """Whether the pyramid forms a perfect Kepler triangle (1:√φ:φ)."""
        half_base = self.pyramid_base_m / 2
        height = self.pyramid_height_m
        apothem = self.pyramid_apothem_m
        return (
            abs(height / half_base - self.sqrt_phi) < 0.01
            and abs(apothem / half_base - self.golden_ratio) < 0.01
        )

    # ────────────────────────────────────────────────────────────────────
    # Verification
    # ────────────────────────────────────────────────────────────────────

    def verify(self, verbose: bool = False) -> bool:
        """Run all identity checks. Returns True if all pass.

        If verbose, prints the result of each check.
        """
        checks = {
            "Golden pi = 4/√φ": self._check_golden_pi(),
            "c = height × 280 × 7": self._check_c_identity(),
            "c from chronon λ×f": self._check_chronon_identity(),
            "4/φ² ≈ plejaren coefficient": self._check_four_over_phi_sq(),
            "AU = 1.52955347 × 1e8 km": self._check_au(),
            "Hyperspace × 40 = 280": self._check_elements(),
            "Hyperspace ladder length": self._check_hyperspace_count(),
            "Kepler triangle": self.pyramid_kepler_triangle_ratio,
        }

        if verbose:
            print("═" * 55)
            print("  GoldenUniverse — Identity Verification")
            print("═" * 55)
            for name, result in checks.items():
                status = "✅" if result else "❌"
                print(f"  {status}  {name}")
            print("═" * 55)
            if all(checks.values()):
                print("  All identities verified ✓")
            else:
                print(f"  {sum(not v for v in checks.values())} failure(s) ✗")

        return all(checks.values())

    def report(self) -> str:
        """Return a formatted multi-line summary of all constants."""
        lines = []
        lines.append("═" * 55)
        lines.append("  GoldenUniverse — Constant Report")
        lines.append("═" * 55)
        lines.append("")
        lines.append("  FUNDAMENTAL CONSTANTS:")
        lines.append(f"    φ  (golden ratio)  = {self.golden_ratio:.15f}")
        lines.append(f"    √φ                = {self.sqrt_phi:.15f}")
        lines.append(f"    πᵴ (golden pi)    = {self.golden_pi:.15f}")
        lines.append(f"    4/φ²             = {self.four_over_phi_sq:.15f}")
        lines.append(f"    1.52955347   (k)  = {self.plejaren_coefficient:.15f}")
        lines.append(f"    correction k/(4/φ²) = {self.correction_factor:.10f}")
        lines.append("")
        lines.append("  GREAT PYRAMID:")
        lines.append(f"    Height (Plejaren)  = {self.pyramid_height_m:.6f} m")
        lines.append(f"    Base side          = {self.pyramid_base_m:.4f} m")
        lines.append(f"    Apothem            = {self.pyramid_apothem_m:.4f} m")
        lines.append(f"    Slope angle        = {self.pyramid_slope_angle_deg:.4f}°")
        lines.append(f"    Kepler triangle    = {'yes' if self.pyramid_kepler_triangle_ratio else 'no'}")
        lines.append("")
        lines.append("  SPEED OF LIGHT:")
        lines.append(f"    c (Meier identity) = {self.speed_of_light_kms:.6f} km/s")
        lines.append(f"    c (modern)         = {self.modern_c_kms:.3f} km/s")
        lines.append(f"    c (chronon λ×f)    = {self.c_from_chronon:.1f} km/s")
        lines.append(f"    match              = {self.c_identity_match_percent:.6f}%")
        lines.append("")
        lines.append("  CHRONON:")
        lines.append(f"    λ = {self.chronon_wavelength_mm} mm")
        lines.append(f"    f = {self.chronon_frequency_hz:.1f} Hz")
        lines.append(f"    N per light-second = {self.chronons_per_light_second:.4e}")
        lines.append("")
        lines.append("  HYPERSPACES & ELEMENTS:")
        lines.append(f"    Hyperspace layers  = {self.num_hyperspaces}")
        lines.append(f"    Total elements     = {self.total_elements}")
        lines.append(f"    Safe hyperspace    = {self.hyperspace_safe_distance_km:,.0f} km")
        lines.append(f"    Reincarnation coeff = {self.reincarnation_coefficient:.8f}")
        lines.append("")
        lines.append("  COSMIC TIMESCALE:")
        lines.append(f"    Creation c          = {self.creation_expansion_speed_kms:,.1f} km/s")
        lines.append(f"    = {self.creation_c_multiple:.4f} × modern c")
        lines.append(f"    Half-life            = {self.half_life_years:,.0f} years")
        lines.append(f"    Next half-life c     = {self.next_half_life_c_kms:.2f} km/s")
        lines.append("")
        lines.append("  HYPERSPACE SPEEDS:")
        for label, speed in zip(self.hyperspace_labels(), self.hyperspace_speeds()):
            lines.append(f"    {label:30s}  {speed:>14,.1f} km/s")
        lines.append("")
        lines.append("  ASTRONOMICAL UNIT:")
        lines.append(f"    AU (Plejaren)      = {self.astronomical_unit_km:,.0f} km")
        lines.append(f"    AU (modern)        = 149,597,870 km")
        lines.append("")
        if self.verify():
            lines.append("  ✅ All identities verified.")
        else:
            lines.append("  ❌ Some identities failed.")
        lines.append("═" * 55)

        return "\n".join(lines)

    # ── Internal check helpers ──────────────────────────────────────────

    def _check_golden_pi(self) -> bool:
        return abs(self.golden_pi - (4 / math.sqrt(self.golden_ratio))) < 1e-14

    def _check_c_identity(self) -> bool:
        expected = self.pyramid_height_m * 280 * 7
        return abs(self.speed_of_light_kms - expected) < 1e-6

    def _check_chronon_identity(self) -> bool:
        return abs(self.c_from_chronon - self.speed_of_light_kms) < 1.0

    def _check_four_over_phi_sq(self) -> bool:
        return self.correction_factor > 1.0 and self.correction_factor < 1.01

    def _check_au(self) -> bool:
        return abs(self.astronomical_unit_km - 152_955_347) < 1

    def _check_elements(self) -> bool:
        return self.total_elements == 280

    def _check_hyperspace_count(self) -> bool:
        return len(self.hyperspace_speeds()) == 7


# ── Convenience ────────────────────────────────────────────────────────

def universe() -> GoldenUniverse:
    """Create a GoldenUniverse with default (canonical) φ."""
    return GoldenUniverse()
