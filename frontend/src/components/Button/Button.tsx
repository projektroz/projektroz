// components/Button/Button.tsx
import React from 'react';
import './Button.scss';

interface ButtonProps {
  label: string;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
  disabled?: boolean;
  backgroundColor?: string;  
  color?: string;            
  fontSize?: string;         
  width?: string;
}

const Button: React.FC<ButtonProps> = ({
  label,
  onClick = () => {},
  type = 'button',
  className = '',
  disabled = false,
  backgroundColor = '', 
  color = '',           
  fontSize = '16px',   
  width = '',
}) => {
  return (
    <button
      className={`button ${className}`}
      onClick={onClick}
      type={type}
      disabled={disabled}
      style={{ backgroundColor, color, fontSize, width }}
    >
      {label}
    </button>
  );
};

export default Button;