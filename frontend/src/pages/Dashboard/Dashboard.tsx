import React from "react";
import useAuth from "../../hooks/useAuth";
import DashboardLine from "../../components/DashboardLine/DashboardLine";
import Rectangle from "../../components/Rectangle/Rectangle";

import homeIcon from "../../assets/icons/home.png";
import logoutIcon from "../../assets/icons/logout.png";
import addChildIcon from "../../assets/icons/add.png";
import manageChildIcon from "../../assets/icons/manage.png";

import "./Dashboard.scss";

function Dashboard() {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout(); 
  };

  const links = [
    { name: "Strona główna", url: "/home", icon: homeIcon },
    { name: "Wyloguj", url: "/logout", icon: logoutIcon },
  ];

  const childCards = [
    { title: "Dodaj dziecko", url: "/dashboard/add-child", image: addChildIcon },
    { title: "Zarządzaj dziećmi", url: "/dashboard/manage-child", image: manageChildIcon },
  ];

  const documentsCards = [
    { title: "Dodaj dokument", url: "/dashboard", image: addChildIcon },
    { title: "Zarządzaj dokumentami", url: "/dashboard", image: manageChildIcon },
  ];

  const templateCards = [
    { title: "Dodaj szablon", url: "/dashboard", image: addChildIcon },
    { title: "Zarządzaj szablonami", url: "/dashboard", image: manageChildIcon },
  ];

  return (
    <div className="app-page dashboard-page">
      <Rectangle links={links}>
        <DashboardLine title="Dzieci" cards={childCards} />
        {/*<DashboardLine title="Dokumenty" cards={documentsCards} />*/}
        <DashboardLine title="Szablony" cards={templateCards} />
      </Rectangle>
    </div>
  );
}

export default Dashboard;
