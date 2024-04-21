import React from "react";
import DashboardCard from "../DashboardCard/DashboardCard";
import "./DashboardLine.scss";
import Child from "types/Child";

interface Card {
  title: string;
  image: string;
  url: string;
  childData?: any;
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
          <DashboardCard key={index} title={card.title} image={card.image} url={card.url} childData={card.childData} />
        ))}
      </div>
    </div>
  );
};

export default DashboardLine;
