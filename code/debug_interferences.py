import numpy as np

print("=== DÉBUGAGE DU CALCUL D'INTERFÉRENCES ===")
print()

# Test simple avec moins de simulations pour comprendre
n_simulations = 10000
phases = np.random.uniform(0, 2*np.pi, (n_simulations, 2))

# Calcul correct des différences de phase
delta_phi = np.abs(phases[:, 0] - phases[:, 1])
delta_phi = np.minimum(delta_phi, 2*np.pi - delta_phi)

print("Distribution des différences de phase :")
print(f"  Min : {np.min(delta_phi):.3f}")
print(f"  Max : {np.max(delta_phi):.3f}")
print(f"  Moyenne : {np.mean(delta_phi):.3f}")
print(f"  Écart-type : {np.std(delta_phi):.3f}")
print()

# Vérifions les bornes des intervalles
print("Vérification des intervalles de classification :")
print(f"0 à π/4 = 0 à {np.pi/4:.3f} = 0 à 0.785 rad")
print(f"π/4 à 3π/4 = {np.pi/4:.3f} à {3*np.pi/4:.3f} = 0.785 à 2.356 rad")
print(f"3π/4 à π = {3*np.pi/4:.3f} à {np.pi:.3f} = 2.356 à 3.142 rad")
print()

# Classification avec affichage du décompte
constructive = delta_phi < np.pi/4
partial = (delta_phi >= np.pi/4) & (delta_phi < 3*np.pi/4)
destructive = delta_phi >= 3*np.pi/4

print("Décompte des interférences :")
print(f"Constructives (0 à π/4) : {np.sum(constructive)} = {np.sum(constructive)/n_simulations*100:.2f}%")
print(f"Partielles (π/4 à 3π/4) : {np.sum(partial)} = {np.sum(partial)/n_simulations*100:.2f}%")
print(f"Destructives (3π/4 à π) : {np.sum(destructive)} = {np.sum(destructive)/n_simulations*100:.2f}%")
print()

print("Vérification de la couverture complète :")
total = np.sum(constructive) + np.sum(partial) + np.sum(destructive)
print(f"Total classifié : {total}/{n_simulations} = {total/n_simulations*100:.2f}%")

if total == n_simulations:
    print("✅ Tous les cas sont classifiés")
else:
    print("❌ Il manque des cas dans la classification !")

print()
print("=== ANALYSE MATHÉMATIQUE ===")
print("Pour une distribution uniforme de phases, les probabilités devraient être :")
print("  Constructives : (π/4 - 0) / (2π) = 0.785 / 6.283 = 0.125 (12.5%)")
print("  Partielles : (3π/4 - π/4) / (2π) = (2.356 - 0.785) / 6.283 = 1.571 / 6.283 = 0.250 (25.0%)")
print("  Destructives : (π - 3π/4) / (2π) = (3.142 - 2.356) / 6.283 = 0.786 / 6.283 = 0.125 (12.5%)")
print()
print("ATTENTION : Ces valeurs ne correspondent pas non plus à 5-27-68% !")
print("Il y a une ERREUR FONDAMENTALE dans la formulation théorique !")