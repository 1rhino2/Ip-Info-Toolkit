from utils import get_ip_info, is_valid_ip, export_json
import sys

def main():
    print("=== 🌐 IP Info Toolkit ===\n")
    ip = input("Enter a valid IPv4 address: ").strip()

    if not is_valid_ip(ip):
        print("[!] Invalid IPv4 address format.")
        sys.exit(1)

    print("\n[+] Retrieving IP information...\n")
    info = get_ip_info(ip)

    if "Error" in info:
        print(f"[!] Lookup failed: {info['Error']}")
        sys.exit(1)

    for k, v in info.items():
        print(f"{k:<12}: {v}")

    save = input("\nExport as JSON file? (y/N): ").lower()
    if save == 'y':
        if export_json(ip, info):
            print("[+] JSON exported successfully.")
        else:
            print("[!] Failed to export JSON.")

if __name__ == "__main__":
    main()
