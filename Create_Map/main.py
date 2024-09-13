from flask import Flask, render_template_string, request
import folium
import geocoder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place = request.form.get('place')
        location = geocoder.osm(place)
        if location.ok:
            lat, lng = location.latlng
        else:
            lat, lng = 0, 0  # Default to (0, 0) if location not found
    else:
        # Get my location
        my_location = geocoder.ip("me")
        lat = my_location.latlng[0]
        lng = my_location.latlng[1]

    # Define map
    m = folium.Map(location=[lat, lng], zoom_start=15)
    
    # Create a FeatureGroup
    feature_group = folium.FeatureGroup(name="My Feature Group").add_to(m)
    
    # Add circle to the FeatureGroup
    folium.Circle(location=[lat, lng], radius=1000, color="blue", fill=True, fill_color="red").add_to(feature_group)
    
    # Add marker to the FeatureGroup
    folium.Marker(location=[lat, lng], popup="My Location").add_to(feature_group)
    
    # Render the map as HTML
    map_html = m._repr_html_()
    
    # Return the map HTML in a simple template
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Location Map</title>
        </head>
        <body>
            <form method="post">
                <input type="text" name="place" placeholder="Enter a place name">
                <input type="submit" value="Search">
            </form>
            {{ map_html|safe }}
        </body>
        </html>
    """, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
