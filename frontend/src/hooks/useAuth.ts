import { useState, useEffect, useCallback } from 'react';
import { loginRequest, registerRequest } from '../api/auth';

const useAuth = () => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);

    useEffect(() => {
        const access_token = localStorage.getItem('access_token');
        if (access_token) {
            console.log("Token znaleziony, ustawiam isLoggedIn na true");
            setIsLoggedIn(true);
        } else {
            console.log("Token nie znaleziony, ustawiam isLoggedIn na false");
            setIsLoggedIn(false);
        }
    }, []);

    const loginUser = async (username: string, password: string) => {
        try {
            const { access, refresh } = await loginRequest(username, password);
            localStorage.setItem('access_token', access);
            localStorage.setItem('refresh_token', refresh);
            console.log("Logowanie udane, ustawiam isLoggedIn na true");
            setIsLoggedIn(true);
        } catch (error) {
            console.error('Nie udało się zalogować:', error);
            throw new Error('Nie udało się zalogować. Spróbuj ponownie.');
        }
    };

    const registerUser = async (username: string, password: string, passwordRepeat: string, email: string, name: string, surname: string) => {
        try {
            const response = await registerRequest(username, password, passwordRepeat, email, name, surname);
            console.log(response);
            window.location.href = '/dashboard';
        } catch (error) {
            console.error('Nie udało się zarejestrować:', error);
            throw new Error('Nie udało się zarejestrować. Spróbuj ponownie.');
        }
    };

    const logout = useCallback(() => {
        console.log("Wylogowywanie...");
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        console.log("Tokeny usunięte, ustawiam isLoggedIn na false");
        setIsLoggedIn(false);
    }, []);

    return { isLoggedIn, loginUser, logout, registerUser };
};

export default useAuth;
