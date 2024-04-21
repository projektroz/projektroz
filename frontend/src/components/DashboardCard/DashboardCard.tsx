import React from "react";
import "./DashboardCard.scss";
import Child from "types/Child";

interface Props {
	title: string;
	image: string;
	url: string;
	childData: Child;
}

const DashboardCard: React.FC<Props> = ({ title, image, url, childData }) => {
	const handleClick = () => {
		if (childData !== undefined) {
			localStorage.setItem("childData", JSON.stringify(childData));
		}

		if (url !== "") {
			window.location.href = url;
		}
	};

	return (
		<div className="card" onClick={handleClick}>
			<img src={image} alt={title} className="icon" />
			<p className="iconName">{title}</p>
			<div className="blur"></div>
		</div>
	);
};

export default DashboardCard;
