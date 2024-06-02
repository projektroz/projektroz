import React, { useState } from "react";
import { Navigate } from "react-router-dom";
import Rectangle from "../../components/Rectangle/Rectangle";
import Button from "../../components/Button/Button";
import BackButton from "../../components/BackButton/BackButton";
import useAuth from "../../hooks/useAuth";

import "./Register.scss";
 
function Register() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [repeatPassword, setRepeatPassword] = useState("");
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [error, setError] = useState<string>("");
    const registerUser = useAuth().registerUser;

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (password !== repeatPassword) {
            setError("Hasła nie są identyczne.");
            return;
        }
        try {
            await registerUser(username,  password, repeatPassword, email, firstName, lastName);
            setError("");
        } catch (error: any) {
            setError(error.message);
        }
    };

    return (
        <div className="app-page register-page">
            <Rectangle width="40%">
                <div className="content">
                    <div className="header">
                        <BackButton />
                        <h2>Rejestracja</h2>
                    </div>
                    <form onSubmit={handleSubmit} className="register-form">
                        <div className="form-group">
                            <label htmlFor="username" className="form-label">Nazwa użytkownika:</label>
                            <input
                                type="text"
                                className="form-control"
                                id="username"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="email" className="form-label">Email:</label>
                            <input
                                type="email"
                                className="form-control"
                                id="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="firstName" className="form-label">Imię:</label>
                            <input
                                type="text"
                                className="form-control"
                                id="firstName"
                                value={firstName}
                                onChange={(e) => setFirstName(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="lastName" className="form-label">Nazwisko:</label>
                            <input
                                type="text"
                                className="form-control"
                                id="lastName"
                                value={lastName}
                                onChange={(e) => setLastName(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password" className="form-label">Hasło:</label>
                            <input
                                type="password"
                                className="form-control"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="repeatPassword" className="form-label">Powtórz hasło:</label>
                            <input
                                type="password"
                                className="form-control"
                                id="repeatPassword"
                                value={repeatPassword}
                                onChange={(e) => setRepeatPassword(e.target.value)}
                                required
                            />
                        </div>
                        {error && <p className="text-danger">{error}</p>}
                        <Button type="submit" label="Zarejestruj się" className="btn-register" />
                    </form>
                </div>
            </Rectangle>
        </div>
    );
}

export default Register;
