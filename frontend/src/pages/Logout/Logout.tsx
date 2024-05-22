import React, { useEffect } from "react";
import { Navigate } from "react-router-dom";
import useAuth from "../../hooks/useAuth";

function Logout() {
    const { logout } = useAuth();

    useEffect(() => {
        console.log("Komponent Logout zamontowany, wywołuję logout");
        logout();
    }, [logout]);

    return <Navigate to="/home" />;
}

export default Logout;
