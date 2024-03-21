// components/Button/Button.tsx
import React from 'react';
import './Button.scss';

interface ButtonProps {
  onClick: () => void;
  children?: React.ReactNode;
}

const Button: React.FC<ButtonProps> = ({ children, onClick }) => {
  return (
    <button className="btn" onClick={onClick}>
      {children}
    </button>
  );
};

export default Button;
