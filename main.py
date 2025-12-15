"""
main.py
-------
N-cisim galaksi çarpışması simülasyonunun ana dosyası.
VS Code / Terminal ortamında çalışacak şekilde düzenlenmiştir.
"""

# --- MATPLOTLIB BACKEND (ÇOK KRİTİK) ---
import matplotlib
matplotlib.use("TkAgg")

import numpy as np
import time

from galaxy import create_spiral_galaxy
from integrators import velocity_verlet_step
from energy import compute_total_energy
from visualization import plot_energy, animate_simulation


def run_simulation():
    """
    Galaksi çarpışması simülasyonunu çalıştırır.
    """

    # Tekrarlanabilirlik
    np.random.seed(42)

    # === GALAKSİLERİ OLUŞTUR ===
    pos1, vel1, m1 = create_spiral_galaxy(
        N=150,
        center=[-3.5, 0],
        velocity=[0.7, 0]
    )

    pos2, vel2, m2 = create_spiral_galaxy(
        N=150,
        center=[3.5, 0],
        velocity=[-0.7, 0]
    )

    # === SİSTEMİ BİRLEŞTİR ===
    positions = np.vstack((pos1, pos2))
    velocities = np.vstack((vel1, vel2))
    masses = np.hstack((m1, m2))

    # === SİMÜLASYON PARAMETRELERİ ===
    dt = 0.02
    steps = 600

    trajectory = []
    energy_history = []

    print("Simülasyon başlatıldı...")

    # === ZAMAN DÖNGÜSÜ ===
    for step in range(steps):
        positions, velocities = velocity_verlet_step(
            positions, velocities, masses, dt
        )

        if step % 10 == 0:
            trajectory.append(positions.copy())
            energy_history.append(
                compute_total_energy(positions, velocities, masses)
            )

        if step % 200 == 0:
            print(f"Adım: {step}/{steps}")

    print("Simülasyon tamamlandı.")

    # === GÖRSELLEŞTİRME ===
    plot_energy(energy_history)

    # Grafik kapatılmadan animasyon açılmasın diye küçük bekleme
    time.sleep(1)

    animate_simulation(np.array(trajectory))


# === PROGRAM BAŞLANGICI ===
if __name__ == "__main__":
    run_simulation()
