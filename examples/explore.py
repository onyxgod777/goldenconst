#!/usr/bin/env python3
"""goldenconst — explore the unified constant system."""

import math
from goldenconst import GoldenUniverse

phi = (1 + math.sqrt(5)) / 2

# ── Default universe ──────────────────────────────────────────────────
g = GoldenUniverse()

# Full report
print(g.report())

print()
print()

# ── Interactive exploration ──────────────────────────────────────────
print("=== SPOT CHECKS ===")
print()

# Check 21/25*(1+√5) ≈ e from earlier (1+√5 = 2φ, so 21/25*2φ = 42φ/25)
euler_approx = 42 * phi / 25
print(f"21/25*(1+√5) = 42φ/25 = {euler_approx:.10f}")
print(f"e (Euler)              = {g.euler_number:.10f}")
print()

# Golden pi squared
print(f"πᵴ² = {g.golden_pi_squared:.10f}")
print(f"16/φ = {16/g.golden_ratio:.10f}")
print(f"πᵴ² = 16/φ? {abs(g.golden_pi_squared - 16/g.golden_ratio) < 1e-12}")
print()

# 4/φ² approximation quality
print(f"4/φ² = {g.four_over_phi_sq:.10f}")
print(f"  k  = {g.plejaren_coefficient:.10f}")
print(f"k / (4/φ²) = {g.correction_factor:.10f}")
print()

# Verify everything
g.verify(verbose=True)
