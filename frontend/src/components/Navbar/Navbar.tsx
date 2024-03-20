// src/components/Navbar/Navbar.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.scss';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Twoja Nazwa</Link>
        <div className="collapse navbar-collapse mx-auto text-center" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/">Strona Główna</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/login">Logowanie</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
