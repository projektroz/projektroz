// pages/Register/Register.tsx
import React, { useState } from "react";

// import useNavigation from "../../hooks/useNavigation";
import useAuth from "../../hooks/useAuth";
import Rectangle from "../../components/Rectangle/Rectangle";
// import Navmenu from "../../components/Navmenu/Navmenu";

import "./Register.scss";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [reapeatPassword, setRepeatPassword] = useState("");
  const [email, setEmail] = useState("");
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [error, setError] = useState<string>("");
  const registerUser = useAuth().registerUser;

  const validateData = () => {
    const emailRegex = new RegExp('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$');
    const passwordRegex = new RegExp('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=])(?=\\S+$).{8,}$');
    if (!passwordRegex.test(password)) {
      setError("Hasło musi zawierać co najmniej jedną dużą literę, jedną małą literę, jedną cyfrę i jeden znak specjalny oraz 8 znaków");
      return false;
    }
    if (password !== reapeatPassword) {
      setError("Hasła nie są takie same");
      return false;
    }
    if (!emailRegex.test(email)) {
      setError("Niepoprawny adres email");
      return false;
    }
    return true;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validateData()) {
      return;
    }
    try {
      await registerUser(username, first_name, last_name, email, password, reapeatPassword);
      setError("");
    } catch (error: any) {
      setError(error.message);
    }
  };
  const links = [
    {
      name: "Strona główna",
      url: "/home",
      icon: "src/assets/icons/home.png",
    },
  ];

  return (
    <div className="app-page register-page">
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
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                type="text"
                className="form-control"
                id="email"
                placeholder="Wprowadź email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                Imie
              </label>
              <input
                type="text"
                className="form-control"
                id="name"
                placeholder="Wprowadź imie"
                value={first_name}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="surname" className="form-label">
                Nazwisko
              </label>
              <input
                type="text"
                className="form-control"
                id="surname"
                placeholder="Wprowadź nazwisko"
                value={last_name}
                onChange={(e) => setLastName(e.target.value)}
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
                type="password"
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
