def celsius_a_fahrenheit(gradi):
    return gradi * 9 / 5 + 32

for c in [0, 25, 100]:
    print(f"{c}°C corrispondono a {celsius_a_fahrenheit(c)}°F")
