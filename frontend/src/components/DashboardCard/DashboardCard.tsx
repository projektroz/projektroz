import React from "react";
import "./DashboardCard.scss";

interface Props {
  title: string;
  image: string;
  url: string;
}

const Card: React.FC<Props> = ({ title, image, url }) => {
  return (
    <div className="card" onClick={() => (window.location.href = url)}>
      <img src={image} alt={title} className="icon" />
      <p className="iconName">{title}</p>
      <div className="blur"></div>
    </div>
  );
};

export default Card;
