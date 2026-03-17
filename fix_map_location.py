import os

map_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\pages\MapView.jsx"

with open(map_path, 'r', encoding='utf-8') as f:
    content = f.read()

geolocation_snippet = """  const [userLocation, setUserLocation] = useState(null);

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setCenter([latitude, longitude]);
          setUserLocation([latitude, longitude]);
        },
        (error) => {
          console.error("Error getting location:", error);
        }
      );
    }
  }, []);"""

# Place it inside MapView above the loadJobs Effect
if 'useEffect(() => {\n    const loadJobs' in content:
    content = content.replace('useEffect(() => {\n    const loadJobs', geolocation_snippet + '\n\n  useEffect(() => {\n    const loadJobs')

user_marker = """            {userLocation && (
              <Marker position={userLocation} icon={L.divIcon({ 
                className: 'user-location-marker',
                html: '<div style="background-color: #4361ee; width: 14px; height: 14px; border: 2px solid white; border-radius: 50%; box-shadow: 0 0 10px rgba(67, 97, 238, 0.5); animation: pulse 1.5s infinite;"></div>',
                iconSize: [14, 14]
              })}>
                <Popup>You are here</Popup>
              </Marker>
            )}"""

# Place userMarker inside MapContainer
if '<ChangeView center={center} />' in content:
    content = content.replace('<ChangeView center={center} />', '<ChangeView center={center} />\n' + user_marker)

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("MapView user location injected")
