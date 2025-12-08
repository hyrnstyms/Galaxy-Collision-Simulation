import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm  # İlerleme çubuğu için: pip install tqdm

# Kendi modüllerimiz
from nbody import NBodyEngine
from utils import get_initial_conditions

# --- AYARLAR ---
DT = 0.05           # Zaman adımı
STEPS = 500         # Toplam adım
G_CONSTANT = 1.0    # Kütle çekim sabiti
OUTPUT_DIR = "results"

# Klasör yoksa oluştur
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def main():
    print(">>> Simülasyon Başlatılıyor...")
    
    # 1. Başlangıç Durumunu Al
    mass, pos, vel = get_initial_conditions()
    
    # 2. Fizik Motorunu Başlat
    engine = NBodyEngine(G=G_CONSTANT, softening=0.8)
    
    # İlk ivme hesabı
    acc = engine.compute_accelerations(mass, pos)
    
    # Veri Saklama
    time_vals = []
    energy_vals = []
    
    # --- GÖRSELLEŞTİRME AYARLARI ---
    plt.ion() # İnteraktif mod açık
    fig = plt.figure(figsize=(12, 6))
    
    # Sol taraf: 3D Galaksi
    ax_sim = fig.add_subplot(1, 2, 1, projection='3d')
    # Sağ taraf: Enerji Grafiği
    ax_energy = fig.add_subplot(1, 2, 2)
    
    print(f">>> {len(mass)} cisim için {STEPS} adım hesaplanacak.")
    
    # --- ANA DÖNGÜ ---
    for step in tqdm(range(STEPS)):
        t = step * DT
        
        # A. FİZİK HESAPLAMA (nbody.py)
        pos, vel, acc = engine.velocity_verlet_step(mass, pos, vel, acc, DT)
        
        # B. ENERJİ ANALİZİ
        ke, pe, total_e = engine.compute_energy(mass, pos, vel)
        time_vals.append(t)
        energy_vals.append(total_e)
        
        # C. EKRANA ÇİZİM (Güzelleştirilmiş Versiyon)
        if step % 5 == 0:
            # --- 1. Simülasyon Ekranı ---
            ax_sim.cla()
            
            # Hıza göre renk belirleme (Velocity-based Coloring)
            # Hız vektörünün büyüklüğünü alıyoruz (Speed)
            speed = np.linalg.norm(vel, axis=1)
            # Hızı normalize et (0 ile 1 arasına sıkıştır) ki renk haritasına otursun
            max_speed = np.max(speed) if np.max(speed) > 0 else 1
            colors = speed / max_speed 
            
            # SCATTER AYARLARI:
            # c=colors: Hıza göre renk ata
            # cmap='inferno': Siyah-Mor-Turuncu-Sarı renk paleti (Ateş gibi)
            # s=3.5: Nokta boyutu (biraz büyüttük)
            # alpha=0.5: Saydamlık (Üst üste binince parlar)
            ax_sim.scatter(pos[:,0], pos[:,1], pos[:,2], c=colors, cmap='inferno', s=3.5, alpha=0.5)
            
            # Arka plan ve Görüş Açısı
            ax_sim.set_xlim(-60, 80)
            ax_sim.set_ylim(-60, 80)
            ax_sim.set_zlim(-40, 40)
            
            # Simsiyah uzay teması
            ax_sim.set_facecolor('black') 
            fig.patch.set_facecolor('black') # Pencerenin kenarlarını da siyah yap
            
            # Eksenleri ve yazıları tamamen kaldır
            ax_sim.axis('off') 
            ax_sim.set_title(f"Time: {t:.2f}", color='white') # Başlık beyaz olsun
            
            # --- 2. Enerji Ekranı ---
            ax_energy.cla()
            ax_energy.plot(time_vals, energy_vals, color='#00ff00', linewidth=1.5, label='Total Energy')
            
            # Enerji grafiği stilini de "Dark Mode" yapalım
            ax_energy.set_facecolor('#121212') # Koyu gri zemin
            ax_energy.tick_params(axis='x', colors='white')
            ax_energy.tick_params(axis='y', colors='white')
            ax_energy.spines['bottom'].set_color('white')
            ax_energy.spines['left'].set_color('white')
            ax_energy.spines['top'].set_color('#121212')
            ax_energy.spines['right'].set_color('#121212')
            
            ax_energy.set_title("Energy Conservation", color='white')
            ax_energy.grid(True, color='gray', linestyle='--', alpha=0.2)
            
            plt.pause(0.001)
    plt.ioff()
    print(">>> Simülasyon Tamamlandı.")
    
    # --- SONUÇLARI KAYDETME ---
    
    # Enerji grafiğini temiz bir şekilde kaydet
    plt.figure(figsize=(10, 6))
    plt.plot(time_vals, energy_vals, label='Total Energy')
    plt.title(f'Nümerik Analiz Enerji Korunumu\nYöntem: Velocity Verlet | N={len(mass)}')
    plt.xlabel('Time')
    plt.ylabel('Energy')
    plt.grid(True)
    plt.legend()
    
    save_path = os.path.join(OUTPUT_DIR, "enerji_analizi.png")
    plt.savefig(save_path)
    print(f">>> Grafik kaydedildi: {save_path}")
    
    # Son görüntüyü ekranda tut
    plt.show()

if __name__ == "__main__":
    main()