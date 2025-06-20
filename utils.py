import requests
import json
import re

def is_valid_ip(ip):
    return re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip) is not None

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,proxy,mobile,hosting,query"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if data['status'] != 'success':
            return {"Error": data.get("message", "Unknown error")}

        return {
            "IP": data["query"],
            "Country": data["country"],
            "Region": data["regionName"],
            "City": data["city"],
            "ZIP": data["zip"],
            "Latitude": data["lat"],
            "Longitude": data["lon"],
            "ISP": data["isp"],
            "Organization": data["org"],
            "AS": data["as"],
            "Proxy/VPN": "Yes" if data["proxy"] else "No",
            "Mobile Network": "Yes" if data["mobile"] else "No",
            "Hosting Provider": "Yes" if data["hosting"] else "No"
        }

    except requests.exceptions.Timeout:
        return {"Error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"Error": "Connection error. Check your internet."}
    except Exception as e:
        return {"Error": str(e)}

def export_json(ip, info):
    try:
        filename = f"{ip.replace('.', '_')}_lookup.json"
        with open(filename, 'w') as f:
            json.dump(info, f, indent=4)
        return True
    except Exception:
        return False
