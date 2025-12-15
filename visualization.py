"""
visualization.py
----------------
VS Code uyumlu görselleştirme ve animasyon fonksiyonları.
"""

import matplotlib.pyplot as plt
from matplotlib import animation


def plot_energy(energy):
    plt.figure()
    plt.plot(energy)
    plt.xlabel("Zaman Adımı")
    plt.ylabel("Toplam Enerji")
    plt.title("Enerji Korunumu (Velocity–Verlet)")
    plt.grid(True)
    plt.show()


def animate_simulation(trajectory, limits=6):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-limits, limits)
    ax.set_ylim(-limits, limits)
    ax.set_aspect("equal")
    ax.set_title("Galaksi Çarpışması – N-Cisim Simülasyonu")

    scat = ax.scatter([], [], s=4, alpha=0.7)

    def update(frame):
        scat.set_offsets(trajectory[frame])
        return scat,

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(trajectory),
        interval=40,
        blit=True
    )

    plt.show()
