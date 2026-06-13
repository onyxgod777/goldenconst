"""
goldenconst — Golden Universe Constants

A Python library encoding the unified constant system connecting:

  • φ (golden ratio)
  • πᵴ = 4/√φ (golden pi)
  • The Great Pyramid of Giza (152.955347 m)
  • The speed of light (299,792.458 km/s)
  • The 7 hyperspaces and 280 universal elements
  • The chronon (quantum of time) and tachyon conversion
  • The Plejaren coefficient 152955347

All constants and identities are built from first principles:
every relationship is independently verifiable.

Usage:
    from goldenconst import GoldenUniverse
    g = GoldenUniverse()
    print(g.pyramid_height)   # 152.955347
    print(g.speed_of_light)   # 299792.48012
    g.verify()                # True if all identities hold
"""

from .core import GoldenUniverse
from .core import __version__, __phi__, __gp__, __plejaren__
