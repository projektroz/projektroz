import React, { useState } from "react";
import { CSSTransition, TransitionGroup } from "react-transition-group";

import "./ChildDataForm.scss";

interface DataInput {
	id: string;
	inputLabel: string;
	placeholder: string;
	type: "date" | "text";
	regex?: string;
}

interface DataCardProps {
	dataSets: DataInput[][];
	formData: { [key: string]: string };
	handleInputChange: (name: string, value: string) => void;
}

const DataCard: React.FC<DataCardProps> = ({
	dataSets,
	formData,
	handleInputChange,
}) => {
	const [currentSetIndex, setCurrentSetIndex] = useState(0);
	const [animationDirection, setAnimationDirection] = useState<
		"left" | "right"
	>("left");

	const nextSet = () => {
		setAnimationDirection("right");
		setCurrentSetIndex((prevIndex) =>
			Math.min(prevIndex + 1, dataSets.length - 1)
		);
	};

	const prevSet = () => {
		setAnimationDirection("left");
		setCurrentSetIndex((prevIndex) => Math.max(prevIndex - 1, 0));
	};

	const visibilityStyle = (index: number): React.CSSProperties => ({
		visibility: currentSetIndex === index ? "visible" : "hidden",
		opacity: currentSetIndex === index ? 1 : 0,
		height: currentSetIndex === index ? "auto" : 0,
		overflow: currentSetIndex === index ? "visible" : "hidden",
		transition: "all 0.25s ease-out",
	});

	return (
		<div className="data-card-wrapper">
			<div className="childData-card content-between">
				<button
					onClick={prevSet}
					type="button"
					className="btn-half"
					style={{
						visibility: currentSetIndex === 0 ? "hidden" : "visible",
						opacity: currentSetIndex === 0 ? 0 : 1,
						userSelect: currentSetIndex === 4 ? "none" : "auto",
						transition: "all 0.25s ease-out",
					}}>
					<img
						src="../src/assets/icons/previous-light.png"
						alt="Poprzedni zestaw"
						className="btn-icon"
					/>
				</button>
				<TransitionGroup>
					{dataSets.map((dataSet, index) => (
						<CSSTransition
							key={index}
							classNames={`slide-${animationDirection}`}
							timeout={300}
						>
							<div style={visibilityStyle(index)} className="content-center">
								{dataSet.map((data, dataIndex) => (
									<div
										className="childData-input content-center"
										key={dataIndex}
									>
										<h3>{data.inputLabel}</h3>
										<input
											type={data.type}
											name={data.id}
											value={formData[data.id] || ""}
											onChange={(e) =>
												handleInputChange(data.id, e.target.value)
											}
											placeholder={data.placeholder}
										/>
									</div>
								))}
							</div>
						</CSSTransition>
					))}
				</TransitionGroup>
				<button
					onClick={nextSet}
					type="button"
					className="btn-half"
					style={{
						visibility: currentSetIndex === 4 ? "hidden" : "visible",
						opacity: currentSetIndex === 4 ? 0 : 1,
						userSelect: currentSetIndex === 4 ? "none" : "auto",
						transition: "all 0.25s ease-out",
					}}>
					<img
						src="../src/assets/icons/next-light.png"
						alt="Następny zestaw"
						className="btn-icon"
					/>
				</button>
			</div>
			<div className="scroll-progress-container">
				<div
					className="progress-bar"
					style={{
						width: `${((currentSetIndex + 1) / dataSets.length) * 100}%`,
						transition: `width 0.3s ease-in-out`,
					}}
				></div>
			</div>
			<button
				type="submit"
				style={{
					opacity: currentSetIndex === 4 ? 1 : 0.3,
					transition: "all 0.25s ease-out",
				}}
				className="btn"
				disabled={currentSetIndex !== 4}
			>
				Dodaj dziecko
			</button>
		</div>
	);
};

export default DataCard;
