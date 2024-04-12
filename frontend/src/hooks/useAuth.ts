// hooks/useAuth.tsx
import { useState } from 'react';
import { loginRequest, registerRequest } from '../api/auth'

const useAuth = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const loginUser = async (username: string, password: string) => {
        try {
            const { access, refresh } = await loginRequest(username, password);
            
            localStorage.setItem('access_token', access);
            localStorage.setItem('refresh_token', refresh);
            
            setIsLoggedIn(true);
        } catch (error) {
            throw new Error('Nie udało się zalogować. Spróbuj ponownie.');
        }
    };

    const registerUser = async(username: string, name: string, surname: string, email: string, password: string, passwordRepeat: string) => {
        try {
            const response = await registerRequest(username, name, surname, email, password, passwordRepeat);
            console.log(response);

            window.location.href = '/login';
        } catch (error) {
            throw new Error('Nie udało się zarejestrować. Spróbuj ponownie.');
        }
    };

    // Funkcja wylogowywania
    const logout = () => {
        // Usuwamy tokeny z localStorage
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        
        // Ustawiamy stan isLoggedIn na false
        setIsLoggedIn(false);
        window.location.reload();
    };

    // Zwracamy stan autoryzacji (czy użytkownik jest zalogowany), oraz funkcje logowania i wylogowywania
    return { isLoggedIn, loginUser, logout, registerUser };
};

export default useAuth;
