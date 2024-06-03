// pages/Login/Login.tsx
import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom";

import Rectangle from "../../components/Rectangle/Rectangle";
import Button from "../../components/Button/Button";
import BackButton from "../../components/BackButton/BackButton";
import useAuth from "../../hooks/useAuth";

import "./Login.scss";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState<string>("");
    const [loading, setLoading] = useState(false);
    const { isLoggedIn, loginUser } = useAuth();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);

        try {
            await loginUser(username, password);
            setError("");
        } catch (error: any) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    if (isLoggedIn) {
        return <Navigate to="/dashboard" />;
    }

    return (
        <div className="app-page login-page">
            <Rectangle width="50%">
                <div className="content">
                    <div className="header">
                        <BackButton />
                        <h2>Zaloguj się</h2>
                    </div>

                    <form onSubmit={handleSubmit} className="login-form">
                        <div className="form-floating mb-3">
                            <input
                                type="text"
                                className="form-control"
                                id="username"
                                placeholder="Wprowadź nazwę użytkownika"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                            />
                            <label htmlFor="username" className="form-label">
                                Nazwa użytkownika
                            </label>
                        </div>
                        <div className="form-floating mb-3">
                            <input
                                type="password"
                                className="form-control"
                                id="password"
                                placeholder="Wprowadź hasło"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                            <label htmlFor="password" className="form-label">
                                Hasło
                            </label>
                        </div>
                        {error && <p className="text-danger">{error}</p>}
                        <Button
                            width="100%"
                            label={loading ? "Logowanie..." : "Zaloguj się"}
                            type="submit"
                            className="btn-login"
                            disabled={loading}
                        />
                    </form>
                    <p>
                        Nie masz jeszcze konta?{" "}
                        <Link to="/register" className="link">
                            Zarejestruj się
                        </Link>
                    </p>
                    <hr className="line" />
                    <Button
                        backgroundColor="var(--disabled)"
                        color="var(--primary)"
                        label="Zaloguj z Google"
                        onClick={() => (window.location.href = "/login")}
                    />
                </div>
            </Rectangle>
        </div>
    );
}

export default Login;
