"""
energy.py
---------
Toplam mekanik enerji hesapları.
"""

import numpy as np
from physics import G, EPSILON


def compute_total_energy(positions, velocities, masses):
    """
    Sistem toplam enerjisini hesaplar.

    Returns
    -------
    total_energy : float
    """
    # Kinetik enerji
    kinetic = 0.5 * np.sum(
        masses * np.sum(velocities**2, axis=1)
    )

    # Potansiyel enerji
    potential = 0.0
    N = len(masses)

    for i in range(N):
        for j in range(i + 1, N):
            r = np.linalg.norm(positions[i] - positions[j]) + EPSILON
            potential -= G * masses[i] * masses[j] / r

    return kinetic + potential
