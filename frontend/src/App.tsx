import React, { useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/global.scss";
import useAuth from "./hooks/useAuth";
import PrivateRoutes from "./components/PrivateRoute/PrivateRoute";

import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import Logout from "./pages/Logout/Logout";
import Register from "./pages/Register/Register";
import Dashboard from "./pages/Dashboard/Dashboard";
import AddChild from "./pages/AddChild/AddChild";
import ManageChild from "./pages/ManageChild/ManageChild";
import ChildDetails from "./pages/ChildDetails/ChildDetails";

const App = () => {
    const { isLoggedIn, logout } = useAuth();

    useEffect(() => {
        const access_token = localStorage.getItem('access_token');
        if (!access_token) {
            console.log("Token nie znaleziony, wywołuję logout");
            logout();
        } else {
            console.log("Token znaleziony, użytkownik jest zalogowany");
        }
    }, [logout]);

    return (
        <>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/home" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/logout" element={<Logout />} />
                <Route path="/register" element={<Register />} />
                
                <Route element={<PrivateRoutes />}>
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/dashboard/add-child" element={<AddChild title="Dodaj dziecko" method="POST"/>} />
                    <Route path="/dashboard/manage-child" element={<ManageChild />} />
                    <Route path="/dashboard/manage-child/:id" element={<ChildDetails />} />
                    <Route path="/dashboard/manage-child/edit-child" element={<AddChild title="Edytuj dziecko" method="PUT"/>} />
                </Route>
            </Routes>
        </>
    );
};

export default App;
