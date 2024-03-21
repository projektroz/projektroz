import { Outlet, Navigate } from 'react-router-dom'

const PrivateRoutes = () => {
    const isLoggedIn = localStorage.getItem('access_token') !== null; 

    return isLoggedIn ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoutes;