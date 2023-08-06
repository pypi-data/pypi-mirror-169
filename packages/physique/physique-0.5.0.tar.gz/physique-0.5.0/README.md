# Librairie Python pour la physique au lycée

## Installation

Lancer dans un terminal :

    pip install physique

Pour une mise à jour :

```python
pip install --upgrade physique
```

## Module `physique.signal`

Module Module pour le traitement des signaux.

### Fonctions disponibles

`periode(t, y)`

`integre(x, y, xmin, xmax)`

---

`spectre_amplitude(t, y, T)`

`spectre_RMS(t, y, T)`

`spectre_RMS_dBV(t, y, T)`

### Exemple

```python
from physique.signal import load_oscillo_csv, periode

t, u = load_oscillo_csv('scope.csv')
T = periode(t, u)
```

## Module `physique.modelisation`

Fonctions pour réaliser une modélisation d'une courbe du type `y=f(x)`.

### Fonctions disponibles

`ajustement_lineaire(x, y)`

`ajustement_affine(x, y)`

`ajustement_parabolique(x, y)`

`ajustement_exponentielle_croissante(x, y)`

`ajustement_exponentielle_croissante_x0(x, y)`

`ajustement_exponentielle_decroissante(x, y)`

`ajustement_exponentielle_decroissante_x0(x, y)`

### Exemple

```python
import numpy as np
import matplotlib.pyplot as plt
from physique.modelisation import ajustement_parabolique

x = np.array([0.003,0.141,0.275,0.410,0.554,0.686,0.820,0.958,1.089,1.227,1.359,1.490,1.599,1.705,1.801])
y = np.array([0.746,0.990,1.175,1.336,1.432,1.505,1.528,1.505,1.454,1.355,1.207,1.018,0.797,0.544,0.266])

[a, b, c] = ajustement_parabolique(x, y)
print(a, b, c)

x_mod = np.linspace(0,max(x),50)
y_mod = a*x_mod**2 + b*x_mod + c

plt.plot(x_mod, y_mod, '-')
plt.plot(x, y, 'x')
plt.show()
```

## Module `physique.csv`

Module d'importation de tableau de données au format CSV à partir des logiciels Aviméca3, Regavi, ...

#### Fonctions disponibles

`import_avimeca3_txt(fichier)`  

`import_regavi_txt(fichier)`  

---

`load_oscillo_csv(filename)`

`load_ltspice_csv(filename)`

#### Exemple

```python
import matplotlib.pyplot as plt
from physique.csv import import_avimeca3_txt

t, x, y = import_avimeca3_txt('data1_avimeca3.txt')

plt.plot(x,y,'.')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.title("Trajectoire d'un ballon")
plt.show()
```
