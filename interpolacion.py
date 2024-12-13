import pandas as pd
from scipy.interpolate import interp1d
import math

# Carga los datos de la Hoja1
FILE_PATH = "excel/ejercicio_practico.xlsx"
data_file = pd.read_excel(FILE_PATH, sheet_name='Hoja1', header=None, names=['UM', 'TANQUE', 'FLUX'], skiprows=2, usecols='A:C')

# Carga los datos de la Hoja2
data_sheet2 = pd.read_excel(FILE_PATH, sheet_name='Hoja2', header=None, names=['Unidades Mueble', 'Tanque', 'Fluxómetro'], skiprows=3, usecols='B:D')

# Verifica si hay valores NaN en las columnas esperadas
data_file[['UM', 'TANQUE', 'FLUX']] = data_file[['UM', 'TANQUE', 'FLUX']].fillna(0)
data_sheet2 = data_sheet2.fillna(0)

# Verifica que no haya duplicados en la columna UM y ordena los datos
data_file = data_file.drop_duplicates(subset='UM').sort_values(by='UM')

# Pide al usuario que ingrese el valor de "Unidades Mueble"
try:
    unidades_mueble = float(input("Ingrese el valor de 'Unidades Mueble': "))
except ValueError:
    print("Error: Debe ingresar un número válido.")
    exit()

# Redondea el valor de 'Unidades Mueble'
if unidades_mueble % 1 >= 0.5:
    unidades_mueble = math.ceil(unidades_mueble)
else:
    unidades_mueble = math.floor(unidades_mueble)

# Comprueba si el valor redondeado está dentro del rango de la columna UM de Hoja1
if not (data_file['UM'].min() <= unidades_mueble <= data_file['UM'].max()):
    print(
        f"Error: El valor redondeado ({unidades_mueble}) está fuera del rango permitido ({data_file['UM'].min()} - {data_file['UM'].max()}).")
    exit()

# Crea un objeto de interpolación para TANQUE
f_tanque = interp1d(data_file['UM'], data_file['TANQUE'], fill_value="extrapolate")

# Crea un objeto de interpolación para FLUX
f_flux = interp1d(data_file['UM'], data_file['FLUX'], fill_value="extrapolate")

# Realiza la interpolación para TANQUE y FLUX basado en 'Unidades Mueble'
tanque_interpolado = f_tanque(unidades_mueble)
flux_interpolado = f_flux(unidades_mueble)

# Busca los valores correspondientes en la Hoja2
row_sheet2 = data_sheet2.loc[data_sheet2['Unidades Mueble'] == unidades_mueble]
if not row_sheet2.empty:
    tanque_hoja2 = row_sheet2['Tanque'].values[0]
    flux_hoja2 = row_sheet2['Fluxómetro'].values[0]
    print(f"\nValores obtenidos de la Hoja2:\n\tTanque = {tanque_hoja2}\n\tFluxómetro = {flux_hoja2}")
else:
    print("\nNo se encontraron valores coincidentes en la Hoja2.")

# Imprime los resultados
print(f"\nValores interpolados:\n\tQ TANQ = {tanque_interpolado}\n\tQ FLUX = {flux_interpolado}\n")
