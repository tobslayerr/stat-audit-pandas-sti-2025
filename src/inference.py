import numpy as np
import scipy.stats as stats

def confidence_interval(theta_hat, sigma, n, confidence=0.95):
    """
    Menghitung Confidence Interval (Frequentist) menggunakan pendekatan Distribusi Normal (Z-distribution).
    
    Formula: theta_hat \pm z * sigma / sqrt(n)
    Referensi: Tsun (2020), hal. 300.
    
    Parameters:
    theta_hat (float): Nilai estimasi parameter (sample mean / proportion).
    sigma (float): Standar deviasi dari sampel.
    n (int): Jumlah observasi/sampel.
    confidence (float): Tingkat kepercayaan (default 0.95).
    
    Returns:
    tuple: (lower_bound, upper_bound)
    """
    if n == 0:
        return (0.0, 0.0)
        
    alpha_level = 1.0 - confidence
    # Mencari nilai Z-score (critical value) dari tabel distribusi normal baku
    z_stat = stats.norm.ppf(1.0 - (alpha_level / 2.0))
    
    margin_of_error = z_stat * (sigma / np.sqrt(n))
    
    lower_bound = theta_hat - margin_of_error
    upper_bound = theta_hat + margin_of_error
    
    return (lower_bound, upper_bound)

def ci_bernoulli(k, n, confidence=0.95):
    """
    Menghitung Confidence Interval untuk distribusi Bernoulli (proporsi).
    
    Formula: theta_hat \pm z * sigma / sqrt(n)
    Keterangan: sigma untuk proporsi diestimasi dengan sqrt(p_hat * (1 - p_hat)).
    Referensi: Tsun (2020), hal. 300.
    
    Parameters:
    k (int): Jumlah kejadian sukses.
    n (int): Total sampel observasi.
    confidence (float): Tingkat kepercayaan (default 0.95).
    
    Returns:
    tuple: (lower_bound, upper_bound)
    """
    if n == 0:
        return (0.0, 0.0)
        
    p_hat = k / n
    # Estimasi standard deviasi sampel untuk proporsi (Bernoulli)
    sigma_hat = np.sqrt(p_hat * (1.0 - p_hat))
    
    return confidence_interval(p_hat, sigma_hat, n, confidence)

def ci_poisson(data, confidence=0.95):
    """
    Menghitung Confidence Interval untuk distribusi Poisson (rata-rata tingkat kejadian).
    
    Formula: theta_hat \pm z * sigma / sqrt(n)
    Keterangan: Pada distribusi Poisson, varians setara dengan rata-rata (lambda_hat).
    Sehingga sigma diestimasi dengan sqrt(lambda_hat).
    Referensi: Tsun (2020), hal. 300.
    
    Parameters:
    data (array-like): Array dari data observasi harian.
    confidence (float): Tingkat kepercayaan (default 0.95).
    
    Returns:
    tuple: (lower_bound, upper_bound)
    """
    n = len(data)
    if n == 0:
        return (0.0, 0.0)
        
    lambda_hat = np.mean(data)
    # Estimasi standard deviasi untuk Poisson
    sigma_hat = np.sqrt(lambda_hat)
    
    return confidence_interval(lambda_hat, sigma_hat, n, confidence)

def credible_interval(alpha, beta, confidence=0.95):
    """
    Menghitung Credible Interval (Bayesian) dari Distribusi Posterior Beta.
    
    Formula: Batas persentil dari fungsi probabilitas kumulatif (PPF) Distribusi Beta.
    Referensi: Tsun (2020), hal. 269.
    """
    
    alpha_level = 1.0 - confidence
    
    # Titik bawah batas luasan probabilitas
    lower_bound = stats.beta.ppf(alpha_level / 2.0, alpha, beta)
    # Titik atas batas luasan probabilitas
    upper_bound = stats.beta.ppf(1.0 - (alpha_level / 2.0), alpha, beta)
    
    return (lower_bound, upper_bound)