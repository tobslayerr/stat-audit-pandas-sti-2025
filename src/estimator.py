import numpy as np

def mle_bernoulli(data):
    """
    Menghitung Maximum Likelihood Estimation (MLE) parameter p (peluang sukses).
    Referensi: Tsun (2020), hal. 254.
    """
    n = len(data)
    if n == 0:
        return 0
    success = np.sum(data)
    return success / n

def mle_poisson(data):
    """
    Menghitung Maximum Likelihood Estimation (MLE) parameter lambda (rata-rata kejadian).
    Referensi: Tsun (2020), hal. 269.
    """
    if len(data) == 0:
        return 0
    return np.mean(data)

def beta_posterior(alpha_prior, beta_prior, data):
    """
    Menghitung parameter distribusi Beta posterior (Konjugasi Beta-Bernoulli).
    """
    success = np.sum(data)
    n = len(data)
    alpha_post = alpha_prior + success
    beta_post = beta_prior + (n - success)
    return alpha_post, beta_post