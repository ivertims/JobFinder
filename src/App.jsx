import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Dashboard from './pages/Dashboard';
import Search from './pages/Search';
import Applications from './pages/Applications';
import MapView from './pages/MapView';
import Login from './pages/Login';
import './styles/variables.css';
import './index.css';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  
  if (loading) return <div style={{ color: 'white', padding: '20px' }}>Loading application...</div>;
  if (!user) return <Navigate to="/login" replace />;
  
  return children;
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          {/* Public Routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Login />} />

          {/* Protected Routes */}
          <Route path="/" element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } />

          <Route path="/search" element={
            <ProtectedRoute>
              <Search />
            </ProtectedRoute>
          } />

          <Route path="/applications" element={
            <ProtectedRoute>
              <Applications />
            </ProtectedRoute>
          } />

          <Route path="/map" element={
            <ProtectedRoute>
              <MapView />
            </ProtectedRoute>
          } />

          {/* Fallback mock saved view redirects */}
          <Route path="/saved" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
