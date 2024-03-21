// DashboardPage.tsx
import React from 'react';
import useAuth from '../../hooks/useAuth';

function Dashboard() {
  const { logout } = useAuth();

  const handleLogout = () => {
      logout(); // Wywołujemy funkcję logout, aby wylogować użytkownika
  };

  return (
    <div className="dashboard-page">
        <h2>Dashboard</h2>
        <p>To jest ekran Dashboardu.</p>
        <button onClick={handleLogout} className="btn btn-danger">Wyloguj się</button>
    </div>
  );
};

export default Dashboard;
