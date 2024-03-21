// pages/Login/Login.tsx
import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom";

import useNavigation from "../../hooks/useNavigation";
import useAuth from "../../hooks/useAuth";

import Rectangle from "../../components/Rectangle/Rectangle";
import Navmenu from "../../components/Navmenu/Navmenu";

import "./Login.scss";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
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
  return (
    <div className="login-page">
      <Rectangle>
        <div className="content">
          <h2>Zaloguj się</h2>
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
            {error && <p className="text-danger">{error}</p>}
            <button type="submit" className="btn btn-primary">
              <span>Zaloguj się</span>
            </button>
          </form>
          <p>
            Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link>
          </p>
          <hr className="line"></hr>
          <button>
            <img
              src="src/assets/images/google_logo.png"
              alt="google"
              width="40px"
            />
            Zaloguj z Google
          </button>
          <label htmlFor=""></label>
        </div>
      </Rectangle>
      {/* <ScrollAction /> */}
    </div>
  );
}

export default Login;
