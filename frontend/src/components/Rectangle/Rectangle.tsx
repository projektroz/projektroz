// components/Rectangle/Rectangle.tsx
import React from 'react';
import './Rectangle.scss';

interface RectangleProps {
  children: React.ReactNode;
}

const Rectangle: React.FC<RectangleProps> = ({ children }) => {
  return (
    <div className="rectangle">
      {children}
    </div>
  );
};

export default Rectangle;
