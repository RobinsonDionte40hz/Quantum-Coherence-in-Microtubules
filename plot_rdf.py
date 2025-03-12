import matplotlib.pyplot as plt
import numpy as np

# Load the RDF data from water_rdf.xvg
data = np.loadtxt("water_rdf.xvg", comments=["#", "@"])

# Extract distance (x-axis) and RDF value (y-axis)
distances = data[:, 0]  # First column is distance in nm
rdf_values = data[:, 1]  # Second column is g(r)

# Find the index of the first peak
peak_index = np.argmax(rdf_values)  # Index of the maximum g(r)
water_spacing = distances[peak_index]  # Distance at the first peak

# Plot the RDF
plt.plot(distances, rdf_values, label="RDF")
plt.axvline(x=water_spacing, color='r', linestyle='--', label=f'Water Spacing: {water_spacing:.2f} nm')
plt.xlabel("Distance (nm)")
plt.ylabel("g(r)")
plt.title("Radial Distribution Function of Water around Protein")
plt.legend()
plt.grid(True)
plt.show()

# Print the water spacing
print(f"The water spacing (first peak) is approximately {water_spacing:.2f} nm at g(r) = {rdf_values[peak_index]:.2f}")