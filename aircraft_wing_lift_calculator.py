print("\n✈️ Aircraft Wing Lift Calculator\n")

air_density = float(input("Air Density (kg/m³): "))
velocity = float(input("Velocity (m/s): "))
wing_area = float(input("Wing Area (m²): "))
lift_coefficient = float(input("Lift Coefficient (CL): "))

lift = 0.5 * air_density * (velocity ** 2) * wing_area * lift_coefficient

print("\n===== Results =====")
print(f"Calculated Lift Force: {lift:.2f} N")
