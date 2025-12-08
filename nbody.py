import numpy as np

class NBodyEngine:
    def __init__(self, G=1.0, softening=0.1):
        self.G = G
        self.softening = softening # 0'a bölünme hatasını önler

    def compute_accelerations(self, mass, pos):
        """
        Tüm parçacıklar arasındaki kuvveti ve ivmeyi hesaplar.
        Kullanılan Yöntem: Vectorized Brute Force O(N^2)
        """
        N = pos.shape[0]
        
        # Fark matrisleri (x_j - x_i)
        # Broadcasting: (N, 1, 3) - (1, N, 3) -> (N, N, 3)
        pos_diff = pos[None, :, :] - pos[:, None, :]
        
        # Uzaklıkların küpü (r^3)
        dist_sq = np.sum(pos_diff**2, axis=2) + self.softening**2
        dist_inv_cube = dist_sq**(-1.5)
        
        # Kendisiyle etkileşimi (köşegen) 0 yap
        np.fill_diagonal(dist_inv_cube, 0.0)
        
        # İvme Hesabı: a = G * sum( m_j * r_ij / r^3 )
        # (N,N,1) * (N,N,3) -> (N,N,3) -> sum -> (N,3)
        acc = self.G * (pos_diff * dist_inv_cube[:, :, None])
        acc = np.sum(acc * mass[None, :, None], axis=1)
        
        return acc

    def compute_energy(self, mass, pos, vel):
        """
        Enerji Korunumu Analizi için Toplam Enerji hesabı.
        """
        # Kinetik Enerji (KE) = 0.5 * m * v^2
        ke = 0.5 * np.sum(mass[:, None] * vel**2)
        
        # Potansiyel Enerji (PE) = - G * m_i * m_j / r
        pos_diff = pos[None, :, :] - pos[:, None, :]
        dist = np.sqrt(np.sum(pos_diff**2, axis=2) + self.softening**2)
        
        pe_matrix = -self.G * (mass[None, :] * mass[:, None]) / dist
        np.fill_diagonal(pe_matrix, 0.0)
        
        # Matriste her çift iki kere sayıldığı için (i-j ve j-i) 2'ye bölüyoruz
        pe = 0.5 * np.sum(pe_matrix)
        
        return ke, pe, ke + pe

    def velocity_verlet_step(self, mass, pos, vel, acc, dt):
        """
        Enerji kararlılığı için Euler yerine Velocity Verlet integrasyonu.
        """
        # 1. Hızın yarım adım güncellenmesi
        vel_half = vel + 0.5 * acc * dt
        
        # 2. Konumun tam adım güncellenmesi
        pos_new = pos + vel_half * dt
        
        # 3. Yeni konumdaki ivmelerin hesaplanması
        acc_new = self.compute_accelerations(mass, pos_new)
        
        # 4. Hızın kalan yarım adımının güncellenmesi
        vel_new = vel_half + 0.5 * acc_new * dt
        
        return pos_new, vel_new, acc_new