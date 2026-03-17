import { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import { Briefcase, Calendar, CheckSquare, Clock, Plus, Trash2 } from 'lucide-react';
import '../styles/Applications.css';

export default function Applications() {
  const [applications, setApplications] = useState([
    { id: 1, title: "Junior React Developer", company: "TechCorp", status: "applied", date: "Applied Mar 15", salary: "£35k" },
    { id: 2, title: "UX/UI Designer Intern", company: "Designly", status: "interviewing", date: "Interview Mar 20", salary: "Competitive" },
    { id: 3, title: "Software Engineer", company: "DataSync", status: "rejected", date: "Applied Mar 10", salary: "£40k" }
  ]);

  const updateStatus = (id, newStatus) => {
    setApplications(apps => apps.map(app => app.id === id ? { ...app, status: newStatus } : app));
  };

  const removeApp = (id) => {
    setApplications(apps => apps.filter(app => app.id !== id));
  };

  const columns = [
    { id: 'applied', label: 'Applied', color: '#14b8a6', icon: <Briefcase size={16} /> },
    { id: 'interviewing', label: 'Interviewing', color: '#f59e0b', icon: <Calendar size={16} /> },
    { id: 'offer', label: 'Offer', color: '#10b981', icon: <CheckSquare size={16} /> },
    { id: 'rejected', label: 'Archived', color: '#ef4444', icon: <Clock size={16} /> }
  ];

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="applications-main">
        <header className="applications-header">
          <div className="header-title">
            <h1>Application Tracker</h1>
            <p>Track your job applications and stay organized.</p>
          </div>
          <button className="gradient-btn"><Plus size={18} /> Add Application</button>
        </header>

        <section className="kanban-container">
          {columns.map(column => (
            <div key={column.id} className="kanban-column">
              <div className="column-header" style={{ borderBottom: `2px solid ${column.color}` }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ color: column.color }}>{column.icon}</span>
                  <h3>{column.label}</h3>
                </div>
                <span className="column-count">{applications.filter(app => app.status === column.id).length}</span>
              </div>

              <div className="column-cards">
                {applications.filter(app => app.status === column.id).map(app => (
                  <div key={app.id} className="glass-card kanban-card">
                    <div className="card-header">
                      <h4>{app.title}</h4>
                      <button onClick={() => removeApp(app.id)} className="delete-btn"><Trash2 size={16} /></button>
                    </div>
                    <p className="card-company">{app.company}</p>
                    <p className="card-salary">{app.salary}</p>
                    
                    <div className="card-actions">
                      {column.id !== 'applied' && (
                        <button onClick={() => updateStatus(app.id, 'applied')} className="status-btn">Apply</button>
                      )}
                      {column.id !== 'interviewing' && (
                        <button onClick={() => updateStatus(app.id, 'interviewing')} className="status-btn">Interview</button>
                      )}
                      {column.id !== 'offer' && (
                        <button onClick={() => updateStatus(app.id, 'offer')} className="status-btn">Offer</button>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
}
