import { createContext, useContext, useState, useEffect } from 'react';
import { auth, isConfigValid } from '../services/firebase';
import { onAuthStateChanged, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut } from 'firebase/auth';

const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isMock, setIsMock] = useState(!isConfigValid);

  useEffect(() => {
    if (!isConfigValid) {
      // Setup mock user for testing if no Firebase setup
      console.log("Setting up MOCK user session");
      setUser({
        uid: 'mock-user-id',
        email: 'student@example.com',
        displayName: 'John Doe',
        photoURL: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&auto=format&fit=crop'
      });
      setLoading(false);
      return;
    }

    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  const login = async (email, password) => {
    if (!isConfigValid) {
      console.log("MOCK Login with:", email);
      setUser({ uid: 'mock-user-id', email, displayName: 'John Doe' });
      return;
    }
    return signInWithEmailAndPassword(auth, email, password);
  };

  const signup = async (email, password) => {
    if (!isConfigValid) {
      console.log("MOCK Signup with:", email);
      return;
    }
    return createUserWithEmailAndPassword(auth, email, password);
  };

  const logout = async () => {
    if (!isConfigValid) {
      setUser(null);
      return;
    }
    return signOut(auth);
  };

  const value = {
    user,
    login,
    signup,
    logout,
    loading,
    isMock
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
