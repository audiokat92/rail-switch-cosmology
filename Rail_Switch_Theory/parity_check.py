import pandas as pd
import scipy.stats as stats

# ==========================================
# FILE: parity_check.py
# PROJECT: Rail-Switch Cosmology
# AUTHOR: William M. Holden
# DESC: Statistical analysis of Galaxy Chirality (Spin Direction).
#       Tests the hypothesis of a "Left-Handed" Universe.
# ==========================================

def analyze_galaxy_parity(csv_file_path):
    print(f"--- Loading Galaxy Data from {csv_file_path} ---")
    
    # MOCK DATA GENERATION (For demonstration if no CSV exists)
    # In a real run, you would load: df = pd.read_csv(csv_file_path)
    # Here we simulate the Lior Shamir (2023) findings:
    total_galaxies = 1000000
    # Observed excess of Left-Handed (Z-spirals) vs Right-Handed (S-spirals)
    left_handed = 510000  # 51%
    right_handed = 490000 # 49%
    
    print(f"Total Sample Size: {total_galaxies}")
    print(f"Left-Handed (CCW): {left_handed}")
    print(f"Right-Handed (CW): {right_handed}")
    
    # --- The Binomial Test ---
    # Null Hypothesis: The universe is random (p=0.5)
    # Alternative: The universe has a spin bias (p != 0.5)
    
    p_value = stats.binomtest(left_handed, n=total_galaxies, p=0.5, alternative='two-sided').pvalue
    
    print("\n--- Statistical Results ---")
    print(f"P-Value: {p_value}")
    
    if p_value < 0.05:
        print("RESULT: SIGNIFICANT. The universe shows Parity Violation.")
        print("CONCLUSION: Supports Torsion-Induced Bounce Hypothesis.")
    else:
        print("RESULT: Insignificant. Universe appears isotropic.")

if __name__ == "__main__":
    # To run with real data, uncomment below:
    # analyze_galaxy_parity("galaxy_zoo_data.csv")
    
    # Run demo mode
    analyze_galaxy_parity("demo")