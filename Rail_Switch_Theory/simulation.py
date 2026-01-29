import numpy as np
import matplotlib.pyplot as plt

# ANALYTIC SOLUTION (no solver needed!)
t = np.logspace(-43, -35, 100)  # Planck epoch
a_planck = 1e-35

# Torsion bounce: a(t) ≈ a_planck * cosh(H_planck * t)
H_planck = 1e40
a = a_planck * np.cosh(H_planck * t)

plt.figure(figsize=(10,6))
plt.semilogx(t, a, 'b-', linewidth=3, label='Torsion Bounce')
plt.axhline(y=a_planck, color='r', linestyle='--', label='Planck Scale')
plt.axvline(x=1e-43, color='g', linestyle=':', label='Bounce (t=10⁻⁴³s)')
plt.xlabel('Time from Bounce (s)')
plt.ylabel('Scale Factor a')
plt.title('ECSK Rail-Switch: Analytic Torsion Bounce')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(a_planck/2, a_planck*10)
plt.tight_layout()
plt.savefig('bounce_planck_analytic.png', dpi=300)
plt.show()

print("✅ INSTANT: Perfect Planck bounce plot ready!")
print("File saved: bounce_planck_analytic.png")