import svgwrite


planets = [
    {"Planet Name": "Mercuria", "Distance (AU)": 0.4, "Size (km)": 4879},
    {"Planet Name": "Earthia", "Distance (AU)": 1, "Size (km)": 12742},
    {"Planet Name": "Marsia", "Distance (AU)": 1.5, "Size (km)": 6779},
    {"Planet Name": "Venusia", "Distance (AU)": 0.7, "Size (km)": 12104}
]

def calculate_light_intensity(planet, planets):
    """
    Calculates the light intensity on a given planet based on the presence of shadow planets.

    Parameters:
    planet (dict): A dictionary representing the planet for which light intensity needs to be calculated.
    planets (list): A list of dictionaries representing all the planets in the system.

    Returns:
    str: The light intensity on the planet. Possible values are "None (Multiple Shadows)", "None", "Partial", or "Full".
    """
    shadow_planets = [p for p in planets if p["Distance (AU)"] < planet["Distance (AU)"] and p["Size (km)"] > planet["Size (km)"]]
    if len(shadow_planets) > 1:
        return "None (Multiple Shadows)"
    elif len(shadow_planets) == 1:
        return "None"
    elif any(p["Size (km)"] < planet["Size (km)"] for p in planets if p["Distance (AU)"] < planet["Distance (AU)"]):
        return "Partial"
    else:
        return "Full"

planets.sort(key=lambda planet: planet["Distance (AU)"])

light_intensities = [calculate_light_intensity(planet, planets) for planet in planets]

for planet, light_intensity in zip(planets, light_intensities):
    print(f"The planet {planet['Planet Name']} receives a light intensity of {light_intensity}")


dwg = svgwrite.Drawing('planets.svg', size=(1000, 1000))

colors = {"Full": "yellow", "Partial": "orange", "None": "gray", "None (Multiple Shadows)": "black"}

for i, (planet, light_intensity) in enumerate(zip(planets, light_intensities)):
    dwg.add(dwg.circle(center=(100 + i * 100, 200), r=planet["Size (km)"] / 800, fill=colors[light_intensity]))

dwg.save()