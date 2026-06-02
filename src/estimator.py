import numpy as np

def mle_bernoulli(data):
    """
    Menghitung Maximum Likelihood Estimation (MLE) parameter p (peluang sukses).
    Referensi: Tsun (2020), hal. 254.
    """
    n = len(data)
    if n == 0: return 0.0
    return np.sum(data) / n

def mle_poisson(data):
    """
    Menghitung Maximum Likelihood Estimation (MLE) parameter lambda (rata-rata kejadian).
    Referensi: Tsun (2020), hal. 254.
    """
    if len(data) == 0: return 0.0
    return np.mean(data)

def beta_posterior(k, m):
    """
    Menghitung parameter distribusi Beta posterior.
    Syarat mutlak rubrik: alpha = k + 1, beta = m + 1.
    Referensi: Tsun (2020), hal. 269.
    """
    alpha_post = k + 1
    beta_post = m + 1
    
    mean = alpha_post / (alpha_post + beta_post)
    if (alpha_post + beta_post) > 2:
        mode = (alpha_post - 1) / (alpha_post + beta_post - 2)
    else:
        mode = mean
        
    return {
        "alpha": alpha_post,
        "beta": beta_post,
        "mode": mode,
        "mean": mean
    }

def log_likelihood_bernoulli(theta, k, n):
    """
    Menghitung Log-Likelihood dari distribusi Bernoulli.
    """
    if theta <= 0 or theta >= 1: return -np.inf
    return k * np.log(theta) + (n - k) * np.log(1 - theta)

def log_likelihood_poisson(theta, data):
    """
    Menghitung Log-Likelihood dari distribusi Poisson.
    """
    if theta <= 0: return -np.inf
    n = len(data)
    sum_x = np.sum(data)
    return sum_x * np.log(theta) - n * theta