# Ip Info Toolkit

This is a simple toolkit for retrieving IP information using the `ipinfo.io` API.

# Installation

Features

- Gets country, city, and timezone information for a given IP address.
- Shows ISP and organization details.
- Optional export to a json file.

# Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Ip-Info-Toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Ip-Info-Toolkit
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:

   ```bash
   python ip_info_toolkit.py

   ```

5. Follow the prompts to enter an IP address or domain name.
6. View the retrieved information in the console or in the `ip_info.json` file if you choose to export it.

# Example

```bash
$ python ip_info_toolkit.py
Enter an IP address or domain name: 8.8.8.8
IP Address: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ZIP: 94043
Latitude: 37.386
Longitude: -122.0838
ISP: Google LLC
Organization: Google LLC
AS: AS15169 Google LLC
Proxy/VPN: No
Mobile Network: No
Hosting Provider: No
```
