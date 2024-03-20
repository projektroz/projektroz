// src/pages/Login/Login.tsx

import React, { useState } from 'react';
import Navbar from '../../components/Navbar/Navbar';
import { Link } from 'react-router-dom';
import './Login.scss';

function Login() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState<string>('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
        const response = await fetch('http://localhost:8000/api-auth/login', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });

        if (!response.ok) {
            throw new Error('Niepoprawne dane logowania.');
        }

        const data = await response.json();
        localStorage.setItem('token', data.token); // Zapis tokena JWT do local storage
        setError('');
        // Przekierowanie do innej strony po poprawnym zalogowaniu
        } catch (error: any) {
        setError(error.message);
        }
    };

  return (
    <div className="login-page">
      <Navbar />
      <div className="login-form">
        <h2>Zaloguj się</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">Email</label>
            <input 
              type="email" 
              className="form-control" 
              id="email" 
              placeholder="Wprowadź email" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              required 
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">Hasło</label>
            <input 
              type="password" 
              className="form-control" 
              id="password" 
              placeholder="Wprowadź hasło" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              required 
            />
          </div>
          {error && <p className="text-danger">{error}</p>}
          <button type="submit" className="btn btn-primary">Zaloguj się</button>
        </form>
        <p>Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link></p>
      </div>
    </div>
  );
}

export default Login;
