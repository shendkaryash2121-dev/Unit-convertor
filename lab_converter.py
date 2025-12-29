import math
import streamlit as st

##### main program ########
def mass_converter():
    print("Mass Converter")
    print("Available units: kilogram (kg), gram (g), milligram (mg), ounce (oz)")

    # Input mass and units
    value = float(input("Enter the mass to convert: "))
    from_unit = input("Enter the unit you want to convert from: ").lower()
    to_unit = input("Enter the unit you want to convert to: ").lower()

    # Conversion factors (to grams)
    to_gram = {
        "kilogram": 1000,   # 1 kg = 1000 g
        "kg": 1000,
        "gram": 1,          # 1 g = 1 g
        "g": 1,
        "milligram": 0.001, # 1 mg = 0.001 g
        "mg": 0.001,
        "ounce": 28.35,     # 1 oz ≈ 28.35 g
        "oz": 28.35
    }

    # Check if units are valid
    if from_unit not in to_gram or to_unit not in to_gram:
        print("Invalid unit entered. Please use kg, g, mg, or oz.")
        return

    # Convert to grams first, then to target unit
    grams = value * to_gram[from_unit]
    converted_value = grams / to_gram[to_unit]

    print(f"{value} {from_unit} = {converted_value} {to_unit}")

def volume_converter():
    print("Volume Converter")
    print("Available units: liter (L), milliliter (mL), microliter (µL), cubic_meter (m³)")

    # Input volume and units
    value = float(input("Enter the volume to convert: "))
    from_unit = input("Enter the unit you want to convert from: ").lower()
    to_unit = input("Enter the unit you want to convert to: ").lower()

    # Conversion factors (to liters)
    to_liter = {
        "liter": 1,
        "l": 1,
        "milliliter": 0.001,
        "ml": 0.001,
        "microliter": 0.000001,
        "µl": 0.000001,
        "cubic_meter": 1000,
        "m³": 1000
    }

    # Check if units are valid
    if from_unit not in to_liter or to_unit not in to_liter:
        print("Invalid unit entered. Please use L, mL, µL, or m³.")
        return

    # Convert to liters first, then to target unit
    liters = value * to_liter[from_unit]
    converted_value = liters / to_liter[to_unit]

    print(f"{value} {from_unit} = {converted_value} {to_unit}")

def concentration_converter():
    print("Concentration Converter (Dilution Formula: C1 × V1 = C2 × V2)")
    print("Note: Enter any three values to calculate the fourth.")
    print("Units: You can use mg/mL, µg/µL, or M (molar), but they must be consistent.")

    # Initialize variables
    C1 = input("Enter initial concentration (C1) or leave blank if unknown: ")
    V1 = input("Enter initial volume (V1) or leave blank if unknown: ")
    C2 = input("Enter final concentration (C2) or leave blank if unknown: ")
    V2 = input("Enter final volume (V2) or leave blank if unknown: ")

    # Convert non-empty inputs to float
    C1 = float(C1) if C1 else None
    V1 = float(V1) if V1 else None
    C2 = float(C2) if C2 else None
    V2 = float(V2) if V2 else None

    # Check how many values are missing
    missing = [C1, V1, C2, V2].count(None)

    if missing > 1:
        print("❌ Error: Please leave only ONE value blank to calculate it.")
        return

    # Apply the dilution formula
    if C1 is None:
        C1 = (C2 * V2) / V1
        print(f"\nC1 (Initial Concentration) = {C1}")
    elif V1 is None:
        V1 = (C2 * V2) / C1
        print(f"\nV1 (Initial Volume) = {V1}")
    elif C2 is None:
        C2 = (C1 * V1) / V2
        print(f"\nC2 (Final Concentration) = {C2}")
    elif V2 is None:
        V2 = (C1 * V1) / C2
        print(f"\nV2 (Final Volume) = {V2}")
    else:
        print("✅ All values are provided; no calculation needed.")

    print("\nReminder: Keep units consistent for accurate results (e.g., all in mL and mg/mL).")

def calculate_Grams_of_substance_to_add():
    print("Molarity CALCULATION IN GRAMS")
    molarity=float(input("enter your molarity(M)="))
    molecular_Weight=float(input("enter yourmolecular weight (gm/mol)="))
    volume_of_solution=float(input("enter your volume of solution(L)="))
    Grams=molarity*molecular_Weight*volume_of_solution
    print(f"Grams={Grams:} gm")

def molarity_by_dilusion():
  print("Molarity by Dilution Converter (Dilution Formula: M1 × V1 = M2 × V2)") # Fixed typo M11 to M1
  print("Note: Enter any three values to calculate the fourth.")
  print("Units: You can use mg/mL, µg/µL, or M (molar), but they must be consistent.")
  M1_str = input("Enter initial molarity (M1) or leave blank if unknown: ") # Changed to handle string input first
  V1_str = input("Enter initial volume (V1) or leave blank if unknown: ")
  M2_str = input("Enter final molarity (M2) or leave blank if unknown: ")
  V2_str = input("Enter final volume (V2) or leave blank if unknown: ")

  # Convert non-empty inputs to float
  M1 = float(M1_str) if M1_str else None
  V1 = float(V1_str) if V1_str else None
  M2 = float(M2_str) if M2_str else None
  V2 = float(V2_str) if V2_str else None

  # Check how many values are missing
  missing = [M1, V1, M2, V2].count(None)

  if missing > 1:
      print("❌ Error: Please leave only ONE value blank to calculate it.")
      return

  # Apply the dilution formula
  if M1 is None:
      M1 = (M2 * V2) / V1
      print(f"\nM1 (Initial Molarity) = {M1} mol/L") # Changed C1 to M1
  elif V1 is None:
      V1 = (M2 * V2) / M1
      print(f"\nV1 (Initial Volume) = {V1} L")
  elif M2 is None:
      M2 = (M1 * V1) / V2
      print(f"\nM2 (Final Molarity) = {M2} mol/L") # Changed C2 to M2
  elif V2 is None:
      V2 = (M1 * V1) / M2
      print(f"\nV2 (Final Volume) = {V2} L")
  else:
      print("✅ All values are provided; no calculation needed.")

  print("\nReminder: Keep units consistent for accurate results (e.g., all in mL and mg/mL).")


def Normality_dilusion():
    N1_str = input("Enter initial normality (N1) or leave blank if unknown: ")
    V1_str = input("Enter initial volume (V1) or leave blank if unknown: ")
    N2_str = input("Enter final normality (N2) or leave blank if unknown: ")
    V2_str = input("Enter final volume (V2) or leave blank if unknown: ")

    # Convert non-empty inputs to float
    N1 = float(N1_str) if N1_str else None
    V1 = float(V1_str) if V1_str else None
    N2 = float(N2_str) if N2_str else None # Corrected: used N2_str
    V2 = float(V2_str) if V2_str else None

    # Check how many values are missing
    missing = [N1, V1, N2, V2].count(None)

    if missing > 1:
        print("❌ Error: Please leave only ONE value blank to calculate it.")
        return

    # Apply the dilution formula
    if N1 is None:
        N1 = (N2 * V2) / V1
        print(f"\nN1 (Initial Normality) = {N1} eq/L") # Corrected: changed M1 to N1
    elif V1 is None:
        V1 = (N2 * V2) / N1
        print(f"\nV1 (Initial Volume) = {V1} L")
    elif N2 is None:
        N2 = (N1 * V1) / V2
        print(f"\nN2 (Final Normality) = {N2}eq/L") # Corrected: changed M2 to N2
    elif V2 is None:
        V2 = (N1 * V1) / N2
        print(f"\nV2 (Final Volume) = {V2} L")
    else:
        print("✅ All values are provided; no calculation needed.")

def percentage_to_grams():
    print("\n1. %(w/v)\n2. %(v/v)\n3. %(m/v)")
    choice = int(input("Choose type: "))

    if choice == 1:
        grams = float(input("Enter grams of solute: "))
        volume = float(input("Enter volume of solution (ml): "))
        percent = (grams / volume) * 100
        print(f"%(w/v) = {percent:.2f} %")

    elif choice == 2:
        vol_solute = float(input("Enter volume of solute (ml): "))
        vol_solution = float(input("Enter volume of solution (ml): "))
        percent = (vol_solute / vol_solution) * 100
        print(f"%(v/v) = {percent:.2f} %")

    elif choice == 3:
        mass = float(input("Enter mass of solute (g): "))
        volume = float(input("Enter volume of solution (ml): "))
        percent = (mass / volume) * 100
        print(f"%(m/v) = {percent:.2f} %")


def molarity_to_normality():

     molarity=float(input("enter molarity="))
     n=float(input("enter n(number of equivalance)="))
     normality=molarity*n
     print(f"normality= {normality:} eq/L")

def calculate_molality():
     moles_of_solute =float(input("enter enter moles of solute ="))
     mass_of_solvent=float(input("enter mass of solvent="))
     molality=moles_of_solute/ mass_of_solvent
     print(f"molality= {molality:} mol/L")


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print("Temperature in Kelvin =", kelvin)
    elif choice == "2":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print("Temperature in Celsius =", celsius)
    elif choice == "3":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius =", celsius)
    elif choice == "4":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print("Temperature in Fahrenheit =", fahrenheit)
    elif choice == "5":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print("Temperature in Kelvin =", kelvin)
    elif choice == "6":
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print("Temperature in Fahrenheit =", fahrenheit)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

def protein_concentration():
    print("Protein Concentration Calculator") # Added for consistency
    A280 = float(input("Enter absorbance at 280 nm (A280): "))
    protein = A280 * 1.5
    print(f"Protein concentration = {protein:.3f} mg/ml")


def molarity():
    moles = float(input("Enter moles of solute: "))
    volume = float(input("Enter volume of solvent (liters): "))
    M = moles / volume
    print(f"Molarity = {M:.3f} M")


def normality():
    gram_eq = float(input("Enter gram equivalents: "))
    volume = float(input("Enter volume of solution (liters): "))
    N = gram_eq / volume
    print(f"Normality = {N:.3f} N")


def molality():
    moles = float(input("Enter moles of solute: "))
    kg = float(input("Enter mass of solvent (kg): "))
    m = moles / kg
    print(f"Molality = {m:.3f} m")


def dna_purity():
    A260 = float(input("Enter A260: "))
    A280 = float(input("Enter A280: "))
    purity = A260 / A280
    print(f"DNA Purity Ratio = {purity:.3f}")



def moles_calculation():
    mass = float(input("Enter given mass (g): "))
    molar_mass = float(input("Enter molar mass (g/mol): "))
    moles = mass / molar_mass
    print(f"Moles = {moles:.4f} mol")


def ph_calculator():
    h = float(input("[H+] (in M): "))
    print("pH =", -math.log10(h))

def density():
   print("Density =", float(input("Mass: ")) / float(input("Volume: ")))

def osmotic_pressure():
  print("Osmotic Pressure Calculator")

  i = float(input("Enter van't Hoff factor (i): "))
  M = float(input("Enter molarity (M): "))
  T = float(input("Enter temperature (K): "))

  R = 0.0821   # Gas constant

  pi = i * M * R * T

  print("Osmotic Pressure (π) =", pi, "atm")

def Hardy_Weinberg_Equation():
    print("Hardy–Weinberg Equation Calculator")
    print("Formula: p² + 2pq + q² = 1")

    p = float(input("Enter value of p (allele frequency): "))
    q = 1 - p

    p2 = p ** 2
    two_pq = 2 * p * q
    q2 = q ** 2

    print("p² (Homozygous dominant) =", p2)
    print("2pq (Heterozygous) =", two_pq)
    print("q² (Homozygous recessive) =", q2)
    print("Total =", p2 + two_pq + q2)

def DNA_concentration():

   print("DNA Concentration Calculator")

   A260 = float(input("Enter A260 value: "))
   dilution = float(input("Enter dilution factor: "))

   dna_conc = A260 * 50 * dilution

   print("DNA concentration =", dna_conc, "µg/mL")


def RNA_concentration():

   print("RNA Concentration Calculator")

   A260 = float(input("Enter A260 value: "))
   dilution = float(input("Enter dilution factor: "))
   rna_conc = A260 * 40 * dilution # Assuming a common RNA conversion factor of 40 µg/mL per A260 unit
   print("RNA concentration =", rna_conc, "µg/mL")



def Main():

    print("!!!!!!!!!!!Welcome to the unit converter!!!!!!!!!!!")
    print("1.mass_converter")
    print("2.volume_converter")
    print("3.concentration_converter")
    print("4.molarity by dilusion (M1*V1 = M2*V2)")
    print("5.molarity CALCULATION IN GRAMS")
    print("6.Molarity to normality ")
    print("7.percentage to grams")
    print("8.molarity to normality")
    print("9.molality")
    print("10.normality by dilusion (N 1V1=N2 V2)")
    print("11.temperature_converter")
    print("12.protein_concentration")
    print("13. calculate molarity by moles")
    print("14. calculate normality")
    print("15. calculate molality")
    print("16. calculate dna purity")
    print("17. calculate moles")
    print("18. calculate ph")
    print("19. calculate density")
    print("20. calculate the osmotic pressur")
    print("21.Hardy–Weinberg Equation")
    print("22.DNA concentration")
    print("23.RNA concentration")
    print("24. calculate protein concentration")
    print("25. I like to Exit")

    choice=input("what do want to do?")

    if choice=="1":
        mass_converter()
    elif choice=="2":
        volume_converter()
    elif choice=="3":
        concentration_converter()
    elif choice=="4":
        molarity_by_dilusion()
    elif choice=="5":
        calculate_Grams_of_substance_to_add()
    elif choice=="6":
       molarity_to_normality() # Assuming `normality()` is intended here, as `Normality()` is not defined
    elif choice=="7":
       percentage_to_grams()
    elif choice=="8":
       molarity_to_normality()
    elif choice=="9":
       calculate_molality()
    elif choice=="10":
       Normality_dilusion()
    elif choice=="11":
      temperature_converter()
    elif choice=="12":
      protein_concentration()
    elif choice=="13":
      molarity()
    elif choice=="14":
      normality()
    elif choice=="15":
      molality()
    elif choice=="16":
      dna_purity()
    elif choice=="17":
      moles_calculation()
    elif choice=="18":
      ph_calculator()
    elif choice=="19":
      density()
    elif choice=="20":
      osmotic_pressure()
    elif choice=="21":
      Hardy_Weinberg_Equation()
    elif choice=="22":
      DNA_concentration()
    elif choice=="23":
      RNA_concentration()
    elif choice=="24":
      protein_concentration()
    elif choice=="25":
      print("thanks visit again, have a good day")
    else:
        print("plese enter valid choice, your enter choice is in invalid")
# Run the program
Main()

print(Main())

