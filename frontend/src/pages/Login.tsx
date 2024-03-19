// src/pages/Login.tsx

import React, { useState } from 'react';
import Navbar from '../components/Navbar/Navbar.tsx';

const Login: React.FC = () => {
  // Stan dla przechowywania danych logowania
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // Obsługa zmiany wartości pól formularza
  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  // Obsługa przesłania formularza logowania
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // Tutaj można dodać logikę uwierzytelniania użytkownika
    console.log('Zaloguj:', { username, password });
  };

  return (
    <div>
      <Navbar />
      <h1>Logowanie</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Użytkownik:</label>
          <input type="text" value={username} onChange={handleUsernameChange} />
        </div>
        <div>
          <label>Hasło:</label>
          <input type="password" value={password} onChange={handlePasswordChange} />
        </div>
        <button type="submit">Zaloguj</button>
      </form>
    </div>
  );
}

export default Login;
