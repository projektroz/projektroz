import React from "react";
import { Link } from "react-router-dom";
import "./Navmenu.scss";
import logo from "../../assets/images/logo.png"; // Import logo image

interface Link {
  name: string;
  url: string;
  icon: string;
}

interface Links {
  links: Link[];
}

const Navmenu: React.FC<Links> = ({ links }) => {
  return (
    <div className="nav-menu">
      <div className="logo">
        <img src={logo} alt="Logo" height="60px" /> {/* Add logo */}
      </div>
      <ul>
        {links.map((link, index) => (
          <li key={index}>
            <div className="menu-link">
              <img src={link.icon} alt="icon" height="40px" />
              <Link to={link.url}>{link.name}</Link>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Navmenu;
