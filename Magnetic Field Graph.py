import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5], [0, 0.046, 0.092, 0.137, 0.183, 0.229, 0.275, 0.321, 0.366, 0.412, 0.458, 0.504, 0.550, 0.595, 0.641, 0.687], 'o-', linewidth=2.5, markersize=8, markerfacecolor='skyblue', markeredgecolor='darkblue', markeredgewidth=1)

plt.title('Proton Beam Deflection against Magnetic Field Strength', fontsize=14, pad=15)
plt.xlabel('Magnetic Field Strength (Teslas)', fontsize=12)
plt.ylabel('Deflection Angle (Degrees)', fontsize=12)

plt.grid(True, alpha=0.3, linestyle='--')

plt.yticks(ticks=np.arange(0, 0.8, 0.1))
plt.xticks(ticks=np.arange(0, 1.6, 0.2))

plt.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)

plt.savefig("Magnetic Field Graph.png", format='png', dpi=150, bbox_inches='tight')
