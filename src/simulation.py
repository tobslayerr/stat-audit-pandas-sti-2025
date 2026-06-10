import numpy as np
import hashlib

def estimate_probability(event_fn, n_trials=50000):
    """
    Melakukan Simulasi Monte Carlo untuk mengestimasi probabilitas suatu event.
    Referensi: Tsun (2020), hal. 320.
    
    Parameters:
    event_fn (callable): Fungsi yang mengembalikan True jika event terjadi, False jika tidak.
    n_trials (int): Jumlah iterasi simulasi.
    
    Returns:
    float: Estimasi probabilitas dari event tersebut.
    """
    successes = sum(1 for _ in range(n_trials) if event_fn())
    return successes / n_trials

class BloomFilter:
    """
    Implementasi struktur data probabilistik Bloom Filter.
    Referensi: Tsun (2020), hal. 329.
    """
    def __init__(self, k, m):
        self.k = k
        self.m = m
        self.bit_array = np.zeros(self.m, dtype=bool)
        
    def _hashes(self, item):
        """Fungsi internal untuk menghasilkan k buah nilai hash unik."""
        result = []
        for i in range(self.k):
            # Menggunakan hashlib md5 sebagai basis variasi hash
            h = int(hashlib.md5(f"{item}_{i}".encode('utf8')).hexdigest(), 16)
            result.append(h % self.m)
        return result

    def add(self, item):
        """Menambahkan item ke dalam struktur Bloom Filter."""
        for h in self._hashes(item):
            self.bit_array[h] = True

    def contains(self, item):
        """Mengecek apakah item secara probabilistik ada di dalam filter."""
        return all(self.bit_array[h] for h in self._hashes(item))

    def theoretical_fpr(self, n):
        """
        Menghitung False Positive Rate (FPR) teoretis.
        Sesuai syarat mutlak formula: (1 - (1 - 1/m)**n)**k
        Referensi: Tsun (2020), hal. 329.
        """
        return (1 - (1 - 1/self.m)**n)**self.k

def mcmc_knapsack(items, capacity, n_iter=100000):
    """
    Menyelesaikan Knapsack Problem menggunakan Markov Chain Monte Carlo (MCMC).
    Digunakan untuk optimasi Sprint Planning.
    Referensi: Tsun (2020), hal. 345.
    
    Parameters:
    items (list of tuples): Daftar item dengan format [(weight, value), ...]
    capacity (float): Kapasitas maksimal beban (jam kerja).
    n_iter (int): Jumlah iterasi random walk Metropolis-Hastings.
    
    Returns:
    tuple: (best_state_array, best_value)
    """
    n_items = len(items)
    current_state = np.zeros(n_items, dtype=bool)
    current_value = 0
    
    best_state = current_state.copy()
    best_value = 0
    
    for _ in range(n_iter):
        # Pilih satu item acak untuk di-flip (masuk/keluar dari knapsack)
        idx = np.random.randint(n_items)
        proposed_state = current_state.copy()
        proposed_state[idx] = not proposed_state[idx]
        
        prop_weight = sum(items[i][0] for i in range(n_items) if proposed_state[i])
        prop_value = sum(items[i][1] for i in range(n_items) if proposed_state[i])
        
        # Validasi batas kapasitas
        if prop_weight <= capacity:
            # Algoritma Metropolis: Terima state baru jika nilainya lebih baik
            if prop_value > current_value:
                accept = True
            else:
                # Jika lebih buruk, terima dengan probabilitas tertentu
                ratio = prop_value / current_value if current_value > 0 else 1.0
                accept = np.random.rand() < ratio
                
            if accept:
                current_state = proposed_state
                current_value = prop_value
                
                # Update rekor terbaik
                if current_value > best_value:
                    best_value = current_value
                    best_state = current_state.copy()
                    
    return best_state, best_value