// components/Rectangle/Rectangle.tsx
import React from "react";
import "./Rectangle.scss";
import Navmenu from "../Navmenu/Navmenu";

interface RectangleProps {
  children: React.ReactNode;
  links?: { name: string; url: string; icon: string }[];
  width?: string; 
  height?: string;
}

const Rectangle: React.FC<RectangleProps> = ({ 
  children, 
  links = [], 
  width = '',  // Domyślna szerokość
  height = '' // Domyślna wysokość
  }) => {
  return (
    <div className="rectangle" style={{ width, height }}>
      <div className="rectangle-content">
        {children}
      </div>
      {links.length > 0 && (  // Renderuj Navmenu tylko jeśli 'links' zawiera elementy
        <div className="rectangle-nav">
          <Navmenu links={links} />
        </div>
      )}
    </div>
  );
};

export default Rectangle;
