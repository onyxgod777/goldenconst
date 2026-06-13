"""Tests for goldenconst."""

import math
from goldenconst import GoldenUniverse


def test_default_phi():
    g = GoldenUniverse()
    assert abs(g.golden_ratio - 1.618033988749895) < 1e-14


def test_golden_pi():
    g = GoldenUniverse()
    assert abs(g.golden_pi - 3.144605511029693) < 1e-14


def test_pyramid_height():
    g = GoldenUniverse()
    assert abs(g.pyramid_height_m - 152.955347) < 1e-6


def test_speed_of_light_identity():
    g = GoldenUniverse()
    expected = 152.955347 * 280 * 7
    assert abs(g.speed_of_light_kms - expected) < 1e-6


def test_modern_c_match():
    g = GoldenUniverse()
    # Within 0.03 km/s of modern c
    assert abs(g.speed_of_light_kms - g.modern_c_kms) < 0.03


def test_au():
    g = GoldenUniverse()
    assert abs(g.astronomical_unit_km - 152_955_347) < 1


def test_hyperspaces():
    g = GoldenUniverse()
    assert g.num_hyperspaces == 7
    assert g.total_elements == 280
    assert len(g.hyperspace_speeds()) == 7


def test_chronon():
    g = GoldenUniverse()
    # Chronon identity should produce c
    assert abs(g.c_from_chronon - g.speed_of_light_kms) < 1.0


def test_four_over_phi_sq():
    g = GoldenUniverse()
    expected = 4 / (g.golden_ratio ** 2)
    assert abs(g.four_over_phi_sq - expected) < 1e-15


def test_plejaren_coefficient():
    g = GoldenUniverse()
    assert abs(g.plejaren_coefficient - 1.52955347) < 1e-8


def test_pyramid_slope():
    g = GoldenUniverse()
    # Should be close to 51.84°
    assert abs(g.pyramid_slope_angle_deg - 51.84) < 0.02


def test_kepler_triangle():
    g = GoldenUniverse()
    assert g.pyramid_kepler_triangle_ratio


def test_verify():
    g = GoldenUniverse()
    assert g.verify()


def test_correction_factor():
    g = GoldenUniverse()
    assert 1.0 < g.correction_factor < 1.01


def test_safe_distance():
    g = GoldenUniverse()
    assert abs(g.hyperspace_safe_distance_km - 152_955_347) < 1


def test_reincarnation():
    g = GoldenUniverse()
    assert abs(g.reincarnation_coefficient - 1.52955347) < 1e-8


def test_hyperspace_ladder_monotonic():
    g = GoldenUniverse()
    speeds = g.hyperspace_speeds()
    for i in range(len(speeds) - 1):
        assert speeds[i] > speeds[i + 1]


def test_half_life():
    g = GoldenUniverse()
    assert g.half_life_years == 6_347_755_102_040.0
    assert abs(g.next_half_life_c_kms - 172_146.46) < 0.01


def test_golden_pi_squared():
    g = GoldenUniverse()
    assert abs(g.golden_pi_squared - 16 / g.golden_ratio) < 1e-12


def test_pyramid_dimensions_consistency():
    g = GoldenUniverse()
    # In a Kepler triangle: height = (base/2) × √φ
    half_base = g.pyramid_base_m / 2
    height_from_sqrt = half_base * g.sqrt_phi
    assert abs(height_from_sqrt - g.pyramid_height_m) < 0.01


def test_create_expansion():
    g = GoldenUniverse()
    # 147 × 299,792.458 ≈ 44,069,491.3
    # Actual figure is 44,069,497.5
    assert abs(g.creation_expansion_speed_kms - 147 * g.modern_c_kms) < 10


def test_report_string():
    g = GoldenUniverse()
    report = g.report()
    assert "GoldenUniverse" in report
    assert "299792" in report
    assert "152.955" in report
