// src/components/Navbar.jsx
import { Link } from 'react-router-dom';

export default function Navbar() {
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
            <Link to="/login" className="nav-link">Login</Link>
          </li>
          <li className="nav-item">
            {/* 
          {!user?.isAuthenticated && (
                                     // solo mostramos el botón register cuando el usuario no está logueado
            <li className="nav-item">
            <Link to="/register" className="nav-link">Register</Link>
          </li>
            )}
            */}
          </li>
          <li className="nav-item">
            <Link to="/menu" className="nav-link">Menú</Link>
          </li>
          <li className="nav-item">
            <Link to="/orders" className="nav-link">Pedidos</Link>
          </li>
          <li className="nav-item">
            <Link to="/" className="nav-link">Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/dashboard" className="nav-link">Dashboard</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}