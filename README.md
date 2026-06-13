# goldenconst

**A Python library for the Golden Universe constant system.**

A unified mathematical framework connecting the golden ratio (φ), golden pi (πᵴ = 4/√φ), the Great Pyramid of Giza, the speed of light, the 7 hyperspaces, 280 universal elements, and the Plejaren coefficient **152955347** — all from a single degree of freedom.

Part of the work at [pi.thealpha-secret.xyz](https://pi.thealpha-secret.xyz).

## Installation

```bash
pip install goldenconst
```

Or install from source:

```bash
git clone https://github.com/onyxgod777/goldenconst.git
cd goldenconst
pip install -e .
```

## Quick Start

```python
from goldenconst import GoldenUniverse

# Default universe (canonical φ)
g = GoldenUniverse()

print(g.golden_pi)           # 3.144605511029693
print(g.pyramid_height_m)    # 152.955347 m
print(g.speed_of_light_kms)  # 299792.48012 km/s

# Verify all identities
g.verify(verbose=True)

# Full report
print(g.report())
```

## Core Identities

### The Speed of Light

```
c = pyramid_height_m × 280 (elements) × 7 (hyperspaces)
c = 152.955347 × 280 × 7
c = 299,792.48012 km/s  (matches modern c to 0.000007%)
```

### The Chronon

```
chronon λ = 14,700 × 10⁻²⁴ mm
chronon f = 20,394,047.62 × 10²⁴ Hz
λ × f = c                               (internal consistency)
```

### The Golden Pi Bridge

```
πᵴ = 4/√φ = 3.144605511...
4/φ² = 1.527864045...
plejaren coefficient = 1.52955347
correction = 1.52955347 / (4/φ²) ≈ 1.001106
```

### Hyperspace Ladder

7 hyperspace layers formed by the half-life decay of c from **44,069,497.5 km/s** (147c) at creation down to **299,792.5 km/s** today, with a half-life of **6.35 trillion years**.

## All Properties

| Property | Returns | Description |
|---|---|---|
| `golden_ratio` | float | φ |
| `golden_pi` | float | πᵴ = 4/√φ |
| `four_over_phi_sq` | float | 4/φ² |
| `plejaren_coefficient` | float | 1.52955347 |
| `pyramid_height_m` | float | Great Pyramid height (m) |
| `pyramid_height_cubits` | float | 280 cubits |
| `pyramid_base_m` | float | Base side from Kepler triangle |
| `pyramid_apothem_m` | float | Slope face length |
| `pyramid_slope_angle_deg` | float | ≈51.84° |
| `pyramid_kepler_triangle_ratio` | bool | 1:√φ:φ check |
| `astronomical_unit_km` | float | True AU (152,955,347 km) |
| `speed_of_light_kms` | float | c from the core identity |
| `modern_c_kms` | float | Modern measured c |
| `c_identity_match_percent` | float | Identity accuracy % |
| `num_hyperspaces` | int | 7 |
| `total_elements` | int | 280 |
| `creation_expansion_speed_kms` | float | Initial c (147c) |
| `half_life_years` | float | Cosmic half-life |
| `next_half_life_c_kms` | float | c after next half-life |
| `chronon_wavelength_mm` | float | Chronon λ |
| `chronon_frequency_hz` | float | Chronon f |
| `chronons_per_light_second` | float | Chronons/second |
| `hyperspace_safe_distance_km` | float | Tachyon drive threshold |
| `reincarnation_coefficient` | float | Fine-matter ratio |
| `correction_factor` | float | k / (4/φ²) |
| `hyperspace_speeds()` | list[float] | All 7 layer speeds |
| `verify()` | bool | Run all checks |
| `report()` | str | Formatted full report |

## License

MIT
