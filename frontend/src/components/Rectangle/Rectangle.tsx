// components/Rectangle/Rectangle.tsx
import React from "react";
import "./Rectangle.scss";
import Navmenu from "../Navmenu/Navmenu";

interface RectangleProps {
  children: React.ReactNode;
}

const Rectangle: React.FC<RectangleProps> = ({ children }) => {
  return (
    <div id="rectangle">
      <div id="rectangleFace">
        <div id="rectangleLeft">{children}</div>
        <div id="rectangleRight">
          <Navmenu />
          <div className="blur"></div>
        </div>
      </div>
      <div className="blur">
        <div id="elipse1"></div>
        <div id="elipse2"></div>
      </div>
    </div>
  );
};

export default Rectangle;
