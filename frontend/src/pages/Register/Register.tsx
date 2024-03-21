// pages/Register/Register.tsx
import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom";

// import useNavigation from "../../hooks/useNavigation";
import useAuth from "../../hooks/useAuth";

import Rectangle from "../../components/Rectangle/Rectangle";
// import Navmenu from "../../components/Navmenu/Navmenu";

import "./Register.scss";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [reapeatPassword, setRepeatPassword] = useState("");
  const [error, setError] = useState<string>("");
  const { isLoggedIn, loginUser } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await loginUser(username, password);
      setError("");
    } catch (error: any) {
      setError(error.message);
    }
  };
  if (isLoggedIn) {
    return <Navigate to="/dashboard" />;
  }
  const links = [
    {
      name: "Strona główna",
      url: "/home",
      icon: "src/assets/icons/home.png",
    },
  ];

  return (
    <div className="register-page">
      <Rectangle links={links}>
        <div className="content">
          <h2>Rejestracja</h2>
          <form onSubmit={handleSubmit} className="login-form">
            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Nazwa użytkownika
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                placeholder="Wprowadź nazwę użytkownika"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Hasło
              </label>
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
            <div className="mb-3">
              <label htmlFor="repeatPassword" className="form-label">
                Powtórz Hasło
              </label>
              <input
                type="repeatPassword"
                className="form-control"
                id="repeatPassword"
                placeholder="Wprowadź hasło ponownie"
                value={reapeatPassword}
                onChange={(e) => setRepeatPassword(e.target.value)}
                required
              />
            </div>
            {error && <p className="text-danger">{error}</p>}
            <button type="submit" className="btn btn-primary">
              <span>Zarejestruj się</span>
            </button>
          </form>
        </div>
      </Rectangle>
      {/* <ScrollAction /> */}
    </div>
  );
}

export default Register;
