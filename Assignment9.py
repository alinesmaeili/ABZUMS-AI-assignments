import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

size = 256
xx, yy = np.meshgrid(np.arange(size) - size / 2, np.arange(size) - size / 2)

image = np.zeros((size, size))
image += np.exp( - (xx**2 + yy**2) / (2 * 30**2) )
image += np.exp( - ((xx - 40)**2 + (yy + 40)**2) / (2 * 20**2) )
image += np.exp( - ((xx + 50)**2 + (yy - 30)**2) / (2 * 25**2) )
image /= image.max()

support_radius = 100
support = (xx**2 + yy**2 < support_radius**2) * 1.0

Ftrue = np.fft.fft2(image)
Mtrue = np.abs(Ftrue)

fx = np.fft.fftfreq(size)
fy = np.fft.fftfreq(size)[:, np.newaxis]
dist = np.sqrt(fx**2 + fy**2)
fraction_keep = 0.3
cutoff = np.sqrt(fraction_keep / np.pi)
K = dist < cutoff

M = np.zeros_like(Mtrue)
M[K] = Mtrue[K]
noise_level = 0.05 * np.mean(M[K])
noise = np.random.normal(0, noise_level, size=(size, size))
M[K] += noise[K]
M = np.maximum(0, M)

def phase_retrieval(M, K, support, beta=0.8, num_iters=1000, num_hio=800):
    errors = []
    current = np.random.uniform(0, 1, size=support.shape) * support
    for i in range(num_iters):
        F_curr = np.fft.fft2(current)
        abs_curr = np.abs(F_curr)
        sum_m_sq = np.sum(M[K]**2)
        err = np.sqrt(np.sum((abs_curr[K] - M[K])**2) / sum_m_sq) if sum_m_sq > 0 else 0
        errors.append(err)
        abs_new = abs_curr.copy()
        abs_new[K] = M[K]
        phase = np.angle(F_curr)
        F_new = abs_new * np.exp(1j * phase)
        image_prime = np.real(np.fft.ifft2(F_new))
        if i < num_hio:
            viol = (image_prime < 0) | (support == 0)
            next_image = np.zeros_like(image_prime)
            next_image[~viol] = image_prime[~viol]
            next_image[viol] = current[viol] - beta * image_prime[viol]
        else:
            next_image = np.maximum(0, image_prime) * support
        current = next_image
    return current, errors

num_trials = 5
best_nmse = np.inf
best_recons = None
best_errors = None
for trial in range(num_trials):
    recons, errors = phase_retrieval(M, K, support)
    nmse = np.sum((recons - image)**2) / np.sum(image**2)
    if nmse < best_nmse:
        best_nmse = nmse
        best_recons = recons
        best_errors = errors

corr = np.corrcoef(best_recons.ravel(), image.ravel())[0, 1]
final_fourier_err = best_errors[-1]
print(f"Normalized MSE: {best_nmse}")
print(f"Correlation: {corr}")
print(f"Fourier Consistency Error: {final_fourier_err}")

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].imshow(image, cmap='gray', vmin=0, vmax=1)
axs[0, 0].set_title('Ground Truth')
axs[0, 1].imshow(np.fft.fftshift(K), cmap='gray')
axs[0, 1].set_title('Frequency Sampling Mask K')
axs[0, 2].imshow(best_recons, cmap='gray', vmin=0, vmax=1)
axs[0, 2].set_title('Final Reconstruction')
log_mag_gt = np.fft.fftshift(np.log(1 + Mtrue))
axs[1, 0].imshow(log_mag_gt, cmap='viridis')
axs[1, 0].set_title('Log-Magnitude Spectrum (GT)')
F_rec = np.fft.fft2(best_recons)
log_mag_rec = np.fft.fftshift(np.log(1 + np.abs(F_rec)))
axs[1, 1].imshow(log_mag_rec, cmap='viridis')
axs[1, 1].set_title('Log-Magnitude Spectrum (Recons)')
residual = best_recons - image
axs[1, 2].imshow(residual, cmap='bwr', vmin=-0.5, vmax=0.5)
axs[1, 2].set_title('Residual (Recons - GT)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(best_errors)
plt.xlabel('Iteration')
plt.ylabel('Relative Fourier Error')
plt.title('Error over Iterations')
plt.show()