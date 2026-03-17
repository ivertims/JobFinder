import os

map_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\pages\MapView.jsx"

content = """import { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import { fetchJobs } from '../services/adzuna';
import { MapPin } from 'lucide-react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import '../styles/MapView.css';

// Fix Marker icons issue for Leaflet in React
import markerIcon2x from 'leaflet/dist/images/marker-icon-2x.png';
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: markerIcon2x,
    iconUrl: markerIcon,
    shadowUrl: markerShadow,
});

function ChangeView({ center }) {
  const map = useMap();
  useEffect(() => {
    map.setView(center, 13);
  }, [center, map]);
  return null;
}

export default function MapView() {
  const [jobs, setJobs] = useState([]);
  const [center, setCenter] = useState([51.5074, -0.1278]); // Default London
  const [selectedJob, setSelectedJob] = useState(null);

  useEffect(() => {
    const loadJobs = async () => {
      const data = await fetchJobs('', '');
      // Filter items that have latitude/longitude
      const withGeo = data.results.filter(job => job.latitude && job.longitude);
      setJobs(withGeo);
      if (withGeo.length > 0) {
        setSelectedJob(withGeo[0]);
        setCenter([withGeo[0].latitude, withGeo[0].longitude]);
      }
    };
    loadJobs();
  }, []);

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="map-main">
        {/* Leaflet CSS Injection */}
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        
        <div className="map-view-container" style={{ height: '100%', width: '100%' }}>
          <MapContainer center={center} zoom={13} style={{ height: '100%', width: '100%', borderRadius: '16px' }}>
            <ChangeView center={center} />
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {jobs.map(job => (
              <Marker 
                key={job.id} 
                position={[job.latitude, job.longitude]}
                eventHandlers={{
                  click: () => setSelectedJob(job),
                }}
              >
                <Popup>
                  <div style={{ fontSize: '13px', color: '#000' }}>
                    <strong>{job.title}</strong>
                    <p style={{ margin: '2px 0', color: 'var(--accent-secondary)' }}>{job.company?.display_name}</p>
                    <p style={{ margin: 0, fontSize: '12px', color: '#666' }}>{job.location?.display_name}</p>
                  </div>
                </Popup>
              </Marker>
            ))}
          </MapContainer>
        </div>

        {/* Floating details section */}
        {selectedJob && (
          <div className="glass-card map-floating-details">
            <h4 style={{ fontSize: '15px' }}>{selectedJob.title}</h4>
            <p style={{ color: 'var(--accent-secondary)', fontSize: '13px' }}>{selectedJob.company?.display_name}</p>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}><MapPin size={12} /> {selectedJob.location?.display_name}</p>
          </div>
        )}
      </main>
    </div>
  );
}"""

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("MapView updated to Leaflet")
