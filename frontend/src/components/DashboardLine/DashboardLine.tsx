import React from "react";
import DashboardCard from "../DashboardCard/DashboardCard";
import "./DashboardLine.scss";

interface Card {
  title: string;
  image: string;
}

interface Props {
  title: string;
  cards: Card[];
}

const DashboardLine: React.FC<Props> = ({ title, cards }) => {
  return (
    <div className="dashboard-line">
      <h2>{title}</h2>
      <div className="dashboard-line__cards">
        {cards.map((card, index) => (
          <DashboardCard key={index} title={card.title} image={card.image} />
        ))}
      </div>
    </div>
  );
};

export default DashboardLine;
