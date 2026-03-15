import subprocess 
import os

def main():
    os.chdir(r"C:\Users\ihsan\Desktop\0. PROJECT\CSV TO KML")
    
    scripts = {
        "1": "convert_fat_to_kml.py", 
        "2": "convert_pole_to_kml.py", 
        "3": "convert_ch_to_kml.py",
        "4": "convert_hp_to_kml.py"
    }
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== CSV TO KML CONVERTER ===\n")
        
        # Tampilkan menu
        for num, script in scripts.items():
            print(f"  {num}. {script}")
        print("  0. KELUAR")
        
        choice = input("\nPilih skrip (angka): ").strip()
        
        if choice == '0':
            print("\nTerima kasih! Program ditutup.")
            break
        elif choice in scripts:
            selected_script = scripts[choice]
            print(f"\n--- Menjalankan {selected_script} ---")
            try:
                result = subprocess.run(["python", selected_script], check=True)
                if result.returncode == 0:
                    print(f"✓ {selected_script} selesai dengan sukses")
                else:
                    print(f"✗ {selected_script} mengalami error")
            except Exception as e:
                print(f"✗ Error: {e}")
            
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("Pilihan tidak valid! Masukkan angka 0-5")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()