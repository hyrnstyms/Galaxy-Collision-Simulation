import numpy as np

def generate_galaxy(n_stars, center, velocity, radius, mass_total):
    """
    Belirli bir merkezde, yarıçapta ve kütlede dönen bir galaksi oluşturur.
    """
    # Kütleler eşit dağıtıldı
    mass = np.ones(n_stars) * (mass_total / n_stars)
    
    # Konumlar: Merkez etrafında rastgele dağılım (Disk şeklinde olması için z ekseni dar)
    # Gaussian (Normal) dağılım gerçekçilik katar
    r_scale = radius / 2.0
    x = np.random.normal(0, r_scale, n_stars)
    y = np.random.normal(0, r_scale, n_stars)
    z = np.random.normal(0, r_scale * 0.1, n_stars) # İnce disk yapısı
    
    local_pos = np.stack((x, y, z), axis=1)
    
    # Hızlar: Dönme hareketi (Merkezcil kuvvet dengesi için yaklaşık hız)
    local_vel = np.zeros_like(local_pos)
    local_vel[:, 0] = -y 
    local_vel[:, 1] = x
    
    # Dönme hızını normalize et ve ayarla
    r = np.linalg.norm(local_pos[:, :2], axis=1, keepdims=True) + 1e-5
    v_orbital = np.sqrt(mass_total / r) # Basitleştirilmiş orbital hız
    local_vel = (local_vel / r) * v_orbital * 0.8 # 0.8 faktörü dağılmayı yavaşlatır
    
    # Global koordinatlara taşıma
    final_pos = local_pos + np.array(center)
    final_vel = local_vel + np.array(velocity)
    
    return mass, final_pos, final_vel

# --- utils.py DOSYASINDAKİ DEĞİŞİKLİK ---

def get_initial_conditions():
    """
    İki galaksiyi çarpışma rotasına sokar.
    """
    
    # 1. Galaksi (Daha büyük) -> n_stars=150
    m1, p1, v1 = generate_galaxy(n_stars=150, center=[0, 0, 0], velocity=[0.2, 0.2, 0], radius=20, mass_total=2000)
    
    # 2. Galaksi (Daha küçük) -> n_stars=75
    m2, p2, v2 = generate_galaxy(n_stars=75, center=[40, 20, 0], velocity=[-0.8, -0.4, 0], radius=10, mass_total=800)
    
    # Dizileri birleştir
    mass = np.concatenate((m1, m2))
    pos = np.concatenate((p1, p2))
    vel = np.concatenate((v1, v2))
    
    return mass, pos, vel