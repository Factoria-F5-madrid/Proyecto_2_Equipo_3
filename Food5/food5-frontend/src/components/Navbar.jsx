import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';

export default function Navbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    localStorage.getItem('loggedIn') === 'true'
  );

  useEffect(() => {
    const handleStorageChange = () => {
      setIsAuthenticated(localStorage.getItem('loggedIn') === 'true');
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, []);

  const login = () => {
    localStorage.setItem('loggedIn', 'true');
    setIsAuthenticated(true); // Actualiza React también
  };

  const logout = () => {
    localStorage.removeItem('loggedIn');
    setIsAuthenticated(false); // Actualiza React también
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <Link to="/" className="navbar-brand">Food5</Link>
      <button
        className="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>

      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item">
            <Link to="/" className="nav-link">Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/contacto" className="nav-link">Contacto</Link>
          </li>

          {isAuthenticated && (
            <>
              <li className="nav-item">
                <Link to="/productos" className="nav-link">Productos</Link>
              </li>
              <li className="nav-item">
                <Link to="/dashboard" className="nav-link">Dashboard</Link>
              </li>
            </>
          )}
        </ul>
      </div>

      {/* Botones para demo */}
      <div className="ms-3">
        {!isAuthenticated ? (
          <button onClick={login} className="btn btn-success me-2">Login</button>
        ) : (
          <button onClick={logout} className="btn btn-danger">Logout</button>
        )}
      </div>
    </nav>
  );
}