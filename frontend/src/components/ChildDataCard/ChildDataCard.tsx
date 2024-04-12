import React, { useState } from "react";
import { CSSTransition, TransitionGroup } from "react-transition-group";

import "./ChildDataCard.scss";

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

  return (
    <div className="data-card-wrapper">
      <div className="childData-card content-between">
        <button onClick={prevSet} type="button" className="btn-half">
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
              <div
                style={{
                  visibility: currentSetIndex === index ? "visible" : "hidden",
                  opacity: currentSetIndex === index ? 1 : 0,
                  height: currentSetIndex === index ? "auto" : 0,
                  overflow: currentSetIndex === index ? "visible" : "hidden",
                  transition: "all 0.25s ease-out",
                }}
                className="content-center"
              >
                {dataSet.map((data, dataIndex) => {
                  return (
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
                  );
                })}
              </div>
            </CSSTransition>
          ))}
        </TransitionGroup>
        <button onClick={nextSet} type="button" className="btn-half">
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
    </div>
  );
};

export default DataCard;
