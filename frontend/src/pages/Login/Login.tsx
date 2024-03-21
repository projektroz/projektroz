// pages/Login/Login.tsx
import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Login.scss";
import Rectangle from "../../components/Rectangle/Rectangle";
import Navmenu from "../../components/Navmenu/Navmenu";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        throw new Error("Niepoprawne dane logowania.");
      }

      const { access, refresh } = await response.json();
      localStorage.setItem("access_token", access);
      localStorage.setItem("refresh_token", refresh);
      setError("");
      // Przekierowanie do innej strony po poprawnym zalogowaniu
    } catch (error: any) {
      setError(error.message);
    }
  };

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
              Zaloguj się
            </button>
          </form>
          <p>
            Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link>
          </p>
          <hr className="line"></hr>
          <button>Zaloguj z Google</button>
        </div>
      </Rectangle>
    </div>
  );
}

export default Login;
