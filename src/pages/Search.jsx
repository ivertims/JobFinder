import { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import { fetchJobs } from '../services/adzuna';
import { Search as SearchIcon, MapPin, DollarSign, Bookmark, Briefcase } from 'lucide-react';
import '../styles/Search.css';

export default function Search() {
  const [keyword, setKeyword] = useState('');
  const [location, setLocation] = useState('');
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedJob, setSelectedJob] = useState(null);

  useEffect(() => {
    handleSearch();
  }, []);

  const handleSearch = async (e) => {
    if (e) e.preventDefault();
    setLoading(true);
    try {
      const data = await fetchJobs(keyword, location);
      setJobs(data.results);
      if (data.results.length > 0) {
        setSelectedJob(data.results[0]);
      }
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="search-main">
        <header className="search-header">
          <form className="search-bar glass-card" onSubmit={handleSearch}>
            <div className="search-input-group">
              <SearchIcon size={20} className="input-icon" />
              <input 
                type="text" 
                placeholder="Job title, skills, or company"
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
              />
            </div>
            <div className="search-divider"></div>
            <div className="search-input-group">
              <MapPin size={20} className="input-icon" />
              <input 
                type="text" 
                placeholder="City or remote"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
              />
            </div>
            <button type="submit" className="gradient-btn"><SearchIcon size={18} /> Search</button>
          </form>
        </header>

        <div className="search-results-container">
          {/* Results List */}
          <section className="results-list">
            {loading ? (
              <p>Loading jobs...</p>
            ) : jobs.length === 0 ? (
              <p>No jobs found. Try searching for "Developer".</p>
            ) : (
              jobs.map(job => (
                <div 
                  key={job.id} 
                  className={`glass-card job-card ${selectedJob && selectedJob.id === job.id ? 'selected' : ''}`}
                  onClick={() => setSelectedJob(job)}
                >
                  <div className="job-card-header">
                    <h3>{job.title}</h3>
                    <button className="save-btn"><Bookmark size={18} /></button>
                  </div>
                  <p className="job-company">{job.company?.display_name}</p>
                  <div className="job-meta">
                    <div className="meta-item"><MapPin size={14} /> {job.location?.display_name}</div>
                    <div className="meta-item"><DollarSign size={14} /> {job.salary_min ? `${job.salary_min.toLocaleString()} - ${job.salary_max ? job.salary_max.toLocaleString() : "Competitive"}` : "Competitive"}</div>
                  </div>
                </div>
              ))
            )}
          </section>

          {/* Job Details Panel */}
          {selectedJob && (
            <section className="glass-card details-panel">
              <div className="details-header">
                <h2>{selectedJob.title}</h2>
                <p className="details-company">{selectedJob.company?.display_name}</p>
                <p className="details-location"><MapPin size={16} /> {selectedJob.location?.display_name}</p>
                
                <div className="details-actions">
                  <button className="gradient-btn" style={{ flex: 1 }}>Apply Now <Briefcase size={16} /></button>
                  <button className="secondary-btn"><Bookmark size={18} /></button>
                </div>
              </div>

              <div className="details-content">
                <h3>Job Description</h3>
                <p className="description-text">{selectedJob.description}</p>
              </div>
            </section>
          )}
        </div>
      </main>
    </div>
  );
}
