import ipinfo
import requests
import json  # Import the json module
import os


access_token = '9423813a0273d3'

# Create an instance of the ipinfo client
handler = ipinfo.getHandler(access_token)

# Attempt to get the IP address of the user you want to locate
try:
    # Assuming you want to fetch the IP address of the local machine
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']  # Example IP address; replace with actual IP address or remove this line to auto-detect
    
    # Get the location details
    details = handler.getDetails(ip_address)
    
    # Extract the location information
    city = details.city
    region = details.region
    country = details.country
    latitude = details.latitude
    longitude = details.longitude
    timezone = details.timezone
    
    # Prepare the data to be saved
    location_data = {
        "City": city,
        "Region": region,
        "Country": country,
        "Latitude": latitude,
        "Longitude": longitude,
        "Timezone": timezone
    }
    
    # Save the location details to a JSON file
    output_path = os.path.join(os.getcwd(),  'Output', 'location_info.json')
    
    # Save the location details to a JSON file in the output folder
    with open(output_path, 'w') as f:
        json.dump(location_data, f, indent=4)
    
    
    # Print the location details
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timezone: {timezone}")
except Exception as e:
    print(f"An error occurred: {e}")
