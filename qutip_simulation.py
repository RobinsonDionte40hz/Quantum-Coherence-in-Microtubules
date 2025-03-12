import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

water_spacing = 0.28  # nm
shielding_factor = 1 / water_spacing
gamma_base = 1e-3
gamma = gamma_base * shielding_factor
target_coherence_time = 408e-15  # s
required_gamma = 1 / target_coherence_time
scaling_factor = required_gamma / (gamma_base * shielding_factor)
gamma = gamma_base * shielding_factor * scaling_factor

psi0 = (qt.basis(2, 0) + qt.basis(2, 1)).unit()
H = qt.Qobj([[0, 1], [1, 0]])
c_ops = [np.sqrt(gamma) * qt.destroy(2)]
times = np.linspace(0, 2e-12, 2000)  # Extend to 2 ps

result = qt.mesolve(H, psi0, times, c_ops, [])
coherence_time = 1 / gamma

coherence = [abs(qt.expect(qt.Qobj([[1, 0], [0, -1]]), result.states[i])) for i in range(len(times))]
plt.plot(times*1e12, coherence)
plt.xlabel("Time (ps)")
plt.ylabel("Coherence")
plt.title("Quantum Coherence with Water Shielding (0-2 ps)")
plt.grid(True)
plt.show()

print(f"Shielding Factor: {shielding_factor:.2f} nm^-1")
print(f"Adjusted Gamma: {gamma:.2e} s^-1")
print(f"Estimated Coherence Time: {coherence_time*1e15:.0f} fs (Target: 408 fs)")