import socket
from ipwhois import IPWhois

def url_to_ip(url):
    if not url:
        return {"error": "URL is required"}, 400
    try:
        ip_address = socket.gethostbyname(url)
        return {"url": url, "ip": ip_address}, 200
    except Exception as e:
        return {"error": str(e)}, 500

def ip_to_location(ip):
    if not ip:
        return {"error": "IP address is required"}, 400

    try:
        # IPWhois-Abfrage
        obj = IPWhois(ip)
        results = obj.lookup_rdap()

        location_data = {
            "city": results.get("network", {}).get("name", "Unknown"),
            "country": results.get("asn_country_code", "Unknown"),
            "latitude": None,  # Nicht verfügbar in ipwhois
            "longitude": None  # Nicht verfügbar in ipwhois
        }
        return {"ip": ip, "location": location_data}, 200

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500