// components/Navmenu/Navmenu.tsx
import React from "react";
import { Link } from "react-router-dom";
import "./Navmenu.scss";

const Navmenu: React.FC = () => {
  return (
    <div className="nav-menu">
      <Link to="/home" className="link">
        Strona główna
      </Link>
      <Link to="/home/#info" className="link">
        Informacje
      </Link>
      <Link to="/login" className="link">
        Logowanie
      </Link>
    </div>
  );
};

export default Navmenu;
