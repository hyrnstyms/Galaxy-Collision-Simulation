"""
physics.py
----------
Bu dosya N-cisim probleminde kullanılan
fiziksel modeli ve kuvvet/ivme hesaplarını içerir.
"""

import numpy as np

# Normalize edilmiş kütleçekim sabiti
G = 1.0

# Sayısal kararlılık için yumuşatma parametresi
EPSILON = 0.05


def compute_accelerations(positions, masses):
    """
    Her parçacık için kütleçekim ivmesini hesaplar.

    Parameters
    ----------
    positions : ndarray (N, 2)
        Parçacık konumları
    masses : ndarray (N,)
        Parçacık kütleleri

    Returns
    -------
    acc : ndarray (N, 2)
        Her parçacığın ivmesi
    """
    N = len(masses)
    acc = np.zeros_like(positions)

    for i in range(N):
        # i. parçacığa göre fark vektörleri
        diff = positions - positions[i]

        # Mesafe (softening dahil)
        dist = np.sqrt(np.sum(diff**2, axis=1) + EPSILON**2)

        # Kendisi hariç
        mask = np.arange(N) != i

        # Newton kuvveti
        acc[i] = G * np.sum(
            masses[mask][:, None] * diff[mask] / dist[mask][:, None]**3,
            axis=0
        )

    return acc
