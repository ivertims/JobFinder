import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Search, Bookmark, Briefcase, MapPin, LogOut, Sun, Moon } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';
import { useAuth } from '../context/AuthContext';

export default function Sidebar() {
  const { logout, user } = useAuth();
  const { isDarkMode, toggleTheme } = useTheme();

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
        {user && (
          <div className="nav-item sidebar-profile-nav">
             <img 
               src={user.photoURL || 'https://via.placeholder.com/40'} 
               alt="Profile" 
               style={{ width: '24px', height: '24px', borderRadius: '50%' }}
             />
             <span>{user.displayName ? (user.displayName.split(' ')[0]) : 'User'}</span>
          </div>
        )}
        
        <NavLink to="/search" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''} nav-search`}>
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

      <div className="sidebar-footer" style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {user && (
          <div className="sidebar-profile" style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px' }}>
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
        <button onClick={toggleTheme} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          {isDarkMode ? <Sun size={20} /> : <Moon size={20} />}
          <span>{isDarkMode ? 'Light Mode' : 'Dark Mode'}</span>
        </button>
        <button onClick={logout} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          <LogOut size={20} />
          <span>Logout</span>
        </button>
      </div>
    </div>
  );
}
