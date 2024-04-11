// hooks/useAuth.tsx
import { useState } from 'react';
import { loginRequest } from '../api/auth'

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
    return { isLoggedIn, loginUser, logout };
};

export default useAuth;
