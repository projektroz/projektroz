import React from "react";
import "./DashboardCard.scss";

interface Props {
  title: string;
  image: string;
}

const Card: React.FC<Props> = ({ title, image }) => {
  return (
    <div className="card">
      <img src={image} alt={title} className="icon" />
      <p className="iconName">{title}</p>
      <div className="blur"></div>
    </div>
  );
};

export default Card;
