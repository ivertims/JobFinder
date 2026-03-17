import { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import { Bookmark, Briefcase, Calendar, CheckCircle, Search, Trash2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import '../styles/Dashboard.css';

export default function Dashboard() {
  const navigate = useNavigate();
  const [stats, setStats] = useState({
    saved: 12,
    applied: 5,
    interviewing: 2,
    rejected: 1
  });

  const [recentSearches, setRecentSearches] = useState([
    "Frontend Developer", "UX Designer", "Software Engineer - Internship", "React Developer"
  ]);

  const [savedJobs, setSavedJobs] = useState([
    { id: 1, title: "Junior React Developer", company: "TechCorp", location: "London, UK", salary: "£35k - £45k", savedDate: "2 days ago" },
    { id: 2, title: "UX/UI Designer Intern", company: "Designly", location: "Remote", salary: "Competitive", savedDate: "3 days ago" },
    { id: 3, title: "Software Engineer", company: "DataSync", location: "Manchester, UK", salary: "£40k - £50k", savedDate: "1 week ago" }
  ]);

  const [applications, setApplications] = useState([
    { id: 1, title: "Junior React Developer", company: "TechCorp", status: "applied", date: "Applied on Mar 15" },
    { id: 2, title: "UX/UI Designer Intern", company: "Designly", status: "interviewing", date: "Interview on Mar 20" }
  ]);

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="dashboard-main">
        <header className="dashboard-header">
          <div className="header-title">
            <h1>Welcome back, student!</h1>
            <p>Here's what's happening with your job search today.</p>
          </div>
          <button onClick={() => navigate('/search')} className="gradient-btn">
            <Search size={18} />
            <span>Search Jobs</span>
          </button>
        </header>

        {/* Stats Grid */}
        <section className="stats-grid">
          <div className="glass-card stat-card">
            <div className="stat-icon" style={{ background: 'rgba(59, 130, 246, 0.1)', color: '#3b82f6' }}>
              <Bookmark />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.saved}</div>
              <div className="stat-label">Saved Jobs</div>
            </div>
          </div>

          <div className="glass-card stat-card">
            <div className="stat-icon" style={{ background: 'rgba(16, 185, 129, 0.1)', color: '#10b981' }}>
              <Briefcase />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.applied}</div>
              <div className="stat-label">Applications</div>
            </div>
          </div>

          <div className="glass-card stat-card">
            <div className="stat-icon" style={{ background: 'rgba(245, 158, 11, 0.1)', color: '#f59e0b' }}>
              <Calendar />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.interviewing}</div>
              <div className="stat-label">Interviews</div>
            </div>
          </div>

          <div className="glass-card stat-card">
            <div className="stat-icon" style={{ background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444' }}>
              <CheckCircle />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.rejected}</div>
              <div className="stat-label">Archived</div>
            </div>
          </div>
        </section>

        {/* Content Section */}
        <div className="content-grid">
          {/* Recent saved jobs */}
          <section className="glass-card section-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h2 style={{ fontSize: '18px' }}>Saved Jobs</h2>
              <button onClick={() => navigate('/saved')} style={{ background: 'none', border: 'none', color: 'var(--accent-secondary)', cursor: 'pointer', fontSize: '14px' }}>View All</button>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {savedJobs.map(job => (
                <div key={job.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px', background: 'rgba(255,255,255,0.02)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.03)' }}>
                  <div>
                    <h3 style={{ fontSize: '15px', fontWeight: 600 }}>{job.title}</h3>
                    <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}>{job.company} • {job.location}</p>
                  </div>
                  <div style={{ textAlign: 'right', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{job.savedDate}</span>
                    <button style={{ background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', opacity: 0.7 }}><Trash2 size={16} /></button>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* Recent Searches */}
          <section className="glass-card section-card">
            <h2 style={{ fontSize: '18px' }}>Recent Searches</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
              {recentSearches.map((search, idx) => (
                <div key={idx} style={{ background: 'rgba(67, 97, 238, 0.1)', color: 'var(--accent-secondary)', padding: '6px 12px', borderRadius: '20px', fontSize: '13px', display: 'flex', alignItems: 'center', gap: '6px', border: '1px solid rgba(67, 97, 238, 0.2)', cursor: 'pointer' }}>
                  <Search size={14} />
                  <span>{search}</span>
                </div>
              ))}
            </div>
          </section>
        </div>
      </main>
    </div>
  );
}
