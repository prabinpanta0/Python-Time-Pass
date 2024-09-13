from flask import Flask, render_template_string, request
import folium
import geocoder
import os
import json
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load location data from JSON files
locations = []
locations_folder = os.path.join(os.path.dirname(__file__), 'Locations')
for filename in os.listdir(locations_folder):
    if filename.endswith('.json'):
        with open(os.path.join(locations_folder, filename), 'r') as f:
            locations.extend(json.load(f))

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get latitude and longitude from URL parameters if available
    lat = request.args.get('lat', type=float, default=None)
    lng = request.args.get('lng', type=float, default=None)
    user_marker_color = "green"
    search_marker_color = "red"
    search_lat, search_lng = None, None

    if request.method == 'POST':
        if 'place' in request.form:
            place = request.form.get('place')
            logging.debug(f"Searching for place: {place}")
            # Search for the place in the loaded JSON data
            for location in locations:
                if location['name'].lower() == place.lower():
                    search_lat, search_lng = location['latitude'], location['longitude']
                    logging.debug(f"Found location: {location}")
                    break
            if search_lat is not None and search_lng is not None:
                lat, lng = search_lat, search_lng
            else:
                logging.debug("Place not found in the locations data.")
        elif 'trace' in request.form:
            my_location = geocoder.ip("me")
            if my_location.ok:
                lat, lng = my_location.latlng

    # If no lat/lng from URL or form, use default location
    if lat is None or lng is None:
        my_location = geocoder.ip("me")
        lat, lng = my_location.latlng if my_location.ok else (0, 0)

    # Define map
    m = folium.Map(location=[lat, lng], zoom_start=15)
    
    # Create a FeatureGroup
    feature_group = folium.FeatureGroup(name="My Feature Group").add_to(m)
    
    # Add circle to the FeatureGroup for user's location
    folium.Circle(location=[lat, lng], radius=1000, color=user_marker_color, fill=True, fill_color=user_marker_color).add_to(feature_group)
    
    # Add marker for user's location
    folium.Marker(location=[lat, lng], popup="My Location", icon=folium.Icon(color=user_marker_color)).add_to(feature_group)
    
    # Add marker and circle for searched location if available
    if search_lat is not None and search_lng is not None:
        folium.Marker(location=[search_lat, search_lng], popup="Searched Location", icon=folium.Icon(color=search_marker_color)).add_to(feature_group)
        folium.Circle(location=[search_lat, search_lng], radius=1000, color=search_marker_color, fill=True, fill_color=search_marker_color).add_to(feature_group)
    
    # Render the map as HTML
    map_html = m._repr_html_()
    
    # Return the map HTML in a simple template with CSS
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Location Map</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                nav {
                    width: 100%;
                    background-color: #333;
                    overflow: hidden;
                }
                nav form {
                    display: inline-block;
                    margin: 0;
                }
                nav input[type="text"], nav input[type="submit"] {
                    padding: 10px;
                    margin: 5px;
                    font-size: 16px;
                }
                nav input[type="submit"] {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                nav input[type="submit"]:hover {
                    background-color: #45a049;
                }
                #map {
                    width: 100%;
                    height: 100vh;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <nav>
                <form method="post">
                    <input type="text" name="place" placeholder="Enter a place name">
                    <input type="submit" value="Search">
                </form>
                <form method="post">
                    <input type="hidden" name="trace" value="1">
                    <input type="submit" value="Trace My Location">
                </form>
            </nav>
            <div id="map">{{ map_html|safe }}</div>
        </body>
        </html>
    """, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
