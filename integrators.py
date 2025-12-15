"""
integrators.py
--------------
Zaman integrasyonu için kullanılan nümerik yöntemler.
Bu projede Velocity–Verlet yöntemi uygulanmaktadır.
"""

from physics import compute_accelerations


def velocity_verlet_step(positions, velocities, masses, dt):
    """
    Velocity–Verlet algoritmasının tek zaman adımı.

    Parameters
    ----------
    positions : ndarray (N, 2)
    velocities : ndarray (N, 2)
    masses : ndarray (N,)
    dt : float
        Zaman adımı

    Returns
    -------
    new_positions, new_velocities
    """
    # Mevcut ivmeler
    acc = compute_accelerations(positions, masses)

    # Konum güncelleme
    new_positions = (
        positions
        + velocities * dt
        + 0.5 * acc * dt**2
    )

    # Yeni ivmeler
    new_acc = compute_accelerations(new_positions, masses)

    # Hız güncelleme
    new_velocities = (
        velocities
        + 0.5 * (acc + new_acc) * dt
    )

    return new_positions, new_velocities
