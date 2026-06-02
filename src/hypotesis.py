import numpy as np
import scipy.stats as stats

def z_test_one_sample(x_bar, mu0, sigma, n, alternative='two-sided', alpha=0.05):
    """
    Melakukan Z-Test untuk membandingkan rata-rata satu sampel dengan nilai tertentu.
    Referensi: Tsun (2020), hal. 306.
    
    Parameters:
    x_bar (float): Rata-rata sampel
    mu0 (float): Rata-rata populasi (hipotesis nol)
    sigma (float): Standar deviasi
    n (int): Jumlah sampel
    alternative (str): 'two-sided', 'greater', atau 'less'
    alpha (float): Tingkat signifikansi
    """
    # Menghitung Z-Statistic
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))
    
    # Menghitung P-Value berdasarkan arah pengujian
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("Alternative harus 'two-sided', 'greater', atau 'less'")
        
    # Menentukan keputusan
    decision = "reject H0" if p_value < alpha else "fail to reject H0"
    
    interpretation = (
        f"Karena p-value ({p_value:.4f}) {'<' if p_value < alpha else '>='} alpha ({alpha}), "
        f"maka keputusan statistik yang diambil adalah {decision}."
    )
    
    return {
        'z_stat': z_stat,
        'p_value': p_value,
        'decision': decision,
        'interpretation': interpretation
    }

def z_test_two_sample(x_bar1, x_bar2, sigma1, sigma2, n1, n2, alternative='two-sided', alpha=0.05):
    """
    Melakukan Z-Test untuk membandingkan rata-rata dari dua sampel independen.
    Cocok untuk membandingkan rata-rata waktu penyelesaian (time-to-close) Core vs Contributor.
    Referensi: Tsun (2020), hal. 309.
    
    Parameters:
    x_bar1, x_bar2 (float): Rata-rata dari sampel 1 dan sampel 2
    sigma1, sigma2 (float): Standar deviasi dari sampel 1 dan sampel 2
    n1, n2 (int): Jumlah data pada sampel 1 dan sampel 2
    alternative (str): 'two-sided', 'greater', atau 'less'
    alpha (float): Tingkat signifikansi
    """
    # Standard error untuk selisih dua rata-rata
    se = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    z_stat = (x_bar1 - x_bar2) / se
    
    # Menghitung P-Value
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("Alternative harus 'two-sided', 'greater', atau 'less'")
        
    # Menentukan keputusan (Anti-jebakan 'accept H0')
    decision = "reject H0" if p_value < alpha else "fail to reject H0"
    
    interpretation = (
        f"Karena p-value ({p_value:.4f}) {'<' if p_value < alpha else '>='} alpha ({alpha}), "
        f"maka keputusan uji hipotesis ini adalah {decision}."
    )
    
    return {
        'z_stat': z_stat,
        'p_value': p_value,
        'decision': decision,
        'interpretation': interpretation
    }