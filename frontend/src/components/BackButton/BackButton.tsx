// components/BackButton/BackButton.tsx
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './BackButton.scss';

const BackButton = () => {
    const navigate = useNavigate();

    return (
        <button className="back-button" onClick={() => navigate(-1)}>
            <img src="../../src/assets/icons/back-button.svg" alt="Powrót" />
        </button>
    );
};

export default BackButton;
