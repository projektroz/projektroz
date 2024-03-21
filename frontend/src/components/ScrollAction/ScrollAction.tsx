import React from "react";
import "./ScrollAction.scss";

const ScrollAction: React.FC = () => {
  return (
    <div id="scroll-action">
      <div className="scroll-box">
        <div className="scroll-element"></div>
      </div>
      <p>scroll</p>
    </div>
  );
};

export default ScrollAction;
