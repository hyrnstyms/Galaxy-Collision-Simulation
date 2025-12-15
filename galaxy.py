"""
galaxy.py
---------
Galaksi veri setinin sentetik olarak oluşturulması.
Disk yapılı ve merkez yoğunluklu galaksiler üretilir.
"""

import numpy as np
from physics import G


def create_spiral_galaxy(
    N,
    center,
    velocity,
    total_mass=1.0,
    radius=2.0
):
    """
    Spiral/disk yapılı galaksi oluşturur.

    Parameters
    ----------
    N : int
        Parçacık sayısı
    center : list [x, y]
        Galaksi merkezi
    velocity : list [vx, vy]
        Galaksinin kütle merkezi hızı
    total_mass : float
        Galaksinin toplam kütlesi
    radius : float
        Galaksi yarıçapı

    Returns
    -------
    positions, velocities, masses
    """
    # Açısal dağılım
    angles = np.random.uniform(0, 4*np.pi, N)

    # Merkez yoğunluk için sqrt dağılım
    r = radius * np.sqrt(np.random.rand(N))

    # Konumlar
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    positions = np.column_stack((x, y)) + center

    # Dairesel hız profili
    v_mag = np.sqrt(G * total_mass / (r + 0.1))
    vx = -v_mag * np.sin(angles)
    vy =  v_mag * np.cos(angles)

    velocities = np.column_stack((vx, vy)) + velocity

    # Eşit kütle dağılımı
    masses = np.full(N, total_mass / N)

    return positions, velocities, masses
