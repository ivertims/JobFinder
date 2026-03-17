import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Search, Bookmark, Briefcase, MapPin, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function Sidebar() {
  const { logout, user } = useAuth();

  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <Briefcase size={28} />
        <span>JobHub</span>
      </div>
      
      <nav className="sidebar-nav">
        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </NavLink>
        
        <NavLink to="/search" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Search size={20} />
          <span>Search Jobs</span>
        </NavLink>
        
        <NavLink to="/saved" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Bookmark size={20} />
          <span>Saved Jobs</span>
        </NavLink>

        <NavLink to="/applications" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Briefcase size={20} />
          <span>Applications</span>
        </NavLink>

        <NavLink to="/map" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <MapPin size={20} />
          <span>Map View</span>
        </NavLink>
      </nav>

      <div style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {user && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px' }}>
            <img 
              src={user.photoURL || 'https://via.placeholder.com/40'} 
              alt="Profile" 
              style={{ width: '40px', height: '40px', borderRadius: '50%' }}
            />
            <div style={{ overflow: 'hidden' }}>
              <p style={{ fontWeight: 600, fontSize: '14px', whiteSpace: 'nowrap', textOverflow: 'ellipsis' }}>{user.displayName || 'User'}</p>
              <p style={{ color: 'var(--text-muted)', fontSize: '12px' }}>Student</p>
            </div>
          </div>
        )}
        <button onClick={logout} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          <LogOut size={20} />
          <span>Logout</span>
        </button>
      </div>
    </div>
  );
}
