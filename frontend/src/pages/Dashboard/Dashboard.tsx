// DashboardPage.tsx
// import React from "react";
import useAuth from "../../hooks/useAuth";
import DashboardLine from "../../components/DashboardLine/DashboardLine";

import "./Dashboard.scss";
import Rectangle from "../../components/Rectangle/Rectangle";

function Dashboard() {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout(); // Wywołujemy funkcję logout, aby wylogować użytkownika
  };

  const links = [
    { name: "Strona główna", url: "/home", icon: "src/assets/icons/home.png" },
    { name: "Wyloguj", url: "/logout", icon: "src/assets/icons/logout.png" },
  ];

  const childCards = [
    { title: "Dodaj dziecko", image: "src/assets/icons/add.png" },
    { title: "Zarządzaj dziećmi", image: "src/assets/icons/manage.png" },
    // { title: "Tytuł 3", image: "url_do_zdjecia_3" },
  ];

  const documentsCards = [
    { title: "Dodaj dokument", image: "src/assets/icons/add.png" },
    { title: "Zarządzaj dokumentami", image: "src/assets/icons/manage.png" },
    // { title: "Tytuł 3", image: "url_do_zdjecia_3" },
  ];

  const templateCards = [
    { title: "Dodaj szablon", image: "src/assets/icons/add.png" },
    { title: "Zarządzaj szablonami", image: "src/assets/icons/manage.png" },
    // { title: "Tytuł 3", image: "url_do_zdjecia_3" },
  ];

  return (
    <div className="dashboard-page">
      <Rectangle links={links}>
        <DashboardLine title="Dzieci" cards={childCards} />
        <DashboardLine title="Dokumenty" cards={documentsCards} />
        <DashboardLine title="Szablony" cards={templateCards} />
        {/* <button onClick={handleLogout}>Wyloguj</button> */}
      </Rectangle>
    </div>
  );
}

export default Dashboard;
