// src/components/Navbar.jsx
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <Link className="navbar-brand fw-bold" to="/">
          🍽️ Food5 Restaurant
        </Link>
        
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
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">🏠 Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/bread">🍞 Bread</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/menu">📋 Menu</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/orders">📝 Orders</Link>
            </li>
          </ul>
          
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/login">🔐 Login</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/register">📝 Register</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;