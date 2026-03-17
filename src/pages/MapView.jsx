import { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import { fetchJobs } from '../services/adzuna';
import { MapPin, Search } from 'lucide-react';
import '../styles/MapView.css';

export default function MapView() {
  const [jobs, setJobs] = useState([]);
  const [center, setCenter] = useState({ lat: 51.5074, lng: -0.1278 }); // Default London
  const [selectedJob, setSelectedJob] = useState(null);

  useEffect(() => {
    const loadJobs = async () => {
      const data = await fetchJobs('', '');
      setJobs(data.results);
      if (data.results.length > 0) {
        setSelectedJob(data.results[0]);
        setCenter({ lat: data.results[0].latitude || 51.5074, lng: data.results[0].longitude || -0.1278 });
      }
    };
    loadJobs();
  }, []);

  const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;
  const isMockMap = !apiKey || apiKey === 'your-google-maps-api-key';

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="map-main">
        <div className="map-view-container">
          {isMockMap ? (
            <div className="mock-map glass-card">
              <div className="mock-map-overlay">
                <MapPin size={48} className="map-pin-icon" style={{ color: 'var(--accent-secondary)' }} />
                <h3>Google Maps View</h3>
                <p>Add <code>VITE_GOOGLE_MAPS_API_KEY</code> to `.env` to load live map.</p>
                {selectedJob && (
                  <div className="mock-marker" style={{ position: 'absolute', top: '40%', left: '50%', transform: 'translate(-50%, -50%)' }}>
                    <div className="marker-pin"></div>
                    <div className="marker-label">{selectedJob.title}</div>
                  </div>
                )}
              </div>
            </div>
          ) : (
            <iframe
              width="100%"
              height="100%"
              style={{ border: 0, borderRadius: '16px' }}
              loading="lazy"
              allowFullScreen
              src={`https://www.google.com/maps/embed/v1/search?key=${apiKey}&q=jobs+in+london`}
            ></iframe>
          )}
        </div>

        {/* Floating details section for selected side-by-side job listing */}
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
}
