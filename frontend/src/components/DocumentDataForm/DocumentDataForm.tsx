import React, { useState } from "react";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import "./DocumentDataForm.scss";

// Interfejsy definiujące dane wejściowe i właściwości komponentów
interface DocumentInput {
    id: string;
    inputLabel: string;
    type: "file" | "text";
}

interface DocumentDataFormProps {
    dataSets: DocumentInput[][];
    formData: { [key: string]: string };
    handleInputChange: (name: string, value: string) => void;
}

// Komponent nawigacyjnego przycisku (lewo/prawo)
const NavigationButton: React.FC<{
    direction: "left" | "right";
    onClick: () => void;
    isVisible: boolean;
}> = ({ direction, onClick, isVisible }) => (
    <button
        onClick={onClick}
        type="button"
        className="btn-half"
        style={{
            visibility: isVisible ? "visible" : "hidden",
            opacity: isVisible ? 1 : 0,
            transition: "all 0.25s ease-out",
        }}>
        <img
            src={`../src/assets/icons/${
                direction === "left" ? "previous" : "next"
            }-light.png`}
            alt={`${direction === "left" ? "Poprzedni" : "Następny"} zestaw`}
            className="btn-icon"
        />
    </button>
);

// Komponent pojedynczego pola danych
const DocumentInputField: React.FC<{
    data: DocumentInput;
    index: number;
    value: string;
    handleInputChange: (name: string, value: string) => void;
}> = ({ data, index, value, handleInputChange }) => (
    <div className="document-input content-center">
        <h3>{data.inputLabel}</h3>
        <div className="form-floating" style={{ width: "100%" }}>
            <input
                className="form-control"
                id={`floatingInput-${data.id}-${index}`}
                type={data.type}
                name={data.id}
                value={value}
                onChange={(e) => handleInputChange(data.id, e.target.value)}
                required
                style={{ width: "100%", padding: "1.2rem .75rem" }}
            />
            {data.type !== "file" && (
                <label htmlFor={`floatingInput-${data.id}-${index}`}>
                    {data.id}
                </label>
            )}
        </div>
    </div>
);

// Komponent reprezentujący pojedynczy zestaw danych
const DocumentDataSet: React.FC<{
    dataSet: DocumentInput[];
    index: number;
    currentSetIndex: number;
    formData: { [key: string]: string };
    handleInputChange: (name: string, value: string) => void;
}> = ({ dataSet, index, currentSetIndex, formData, handleInputChange }) => (
    <CSSTransition
        key={index}
        classNames={`slide-${currentSetIndex > index ? "left" : "right"}`}
        timeout={300}>
        <div
            style={{
                visibility: currentSetIndex === index ? "visible" : "hidden",
                opacity: currentSetIndex === index ? 1 : 0,
                height: currentSetIndex === index ? "auto" : 0,
                overflow: currentSetIndex === index ? "visible" : "hidden",
                transition: "all 0.25s ease-out",
            }}
            className="content-center">
            {dataSet.map((data, dataIndex) => (
                <DocumentInputField
                    key={dataIndex}
                    data={data}
                    index={index}
                    value={formData[data.id]}
                    handleInputChange={handleInputChange}
                />
            ))}
        </div>
    </CSSTransition>
);

// Główny komponent zarządzający zestawami danych
const DocumentDataForm: React.FC<DocumentDataFormProps> = ({
    dataSets,
    formData,
    handleInputChange,
}) => {
    const [currentSetIndex, setCurrentSetIndex] = useState(0);

    const nextSet = () =>
        setCurrentSetIndex((prevIndex) =>
            Math.min(prevIndex + 1, dataSets.length - 1)
        );
    const prevSet = () =>
        setCurrentSetIndex((prevIndex) => Math.max(prevIndex - 1, 0));

    return (
        <div className="document-data-form-wrapper">
            <div className="document-data-form content-between">
                <NavigationButton
                    direction="left"
                    onClick={prevSet}
                    isVisible={currentSetIndex > 0}
                />
                <TransitionGroup>
                    {dataSets.map((dataSet, index) => (
                        <DocumentDataSet
                            key={index}
                            dataSet={dataSet}
                            index={index}
                            currentSetIndex={currentSetIndex}
                            formData={formData}
                            handleInputChange={handleInputChange}
                        />
                    ))}
                </TransitionGroup>
                <NavigationButton
                    direction="right"
                    onClick={nextSet}
                    isVisible={currentSetIndex < dataSets.length - 1}
                />
            </div>
            <div className="scroll-progress-container">
                <div
                    className="progress-bar"
                    style={{
                        width: `${
                            ((currentSetIndex + 1) / dataSets.length) * 100
                        }%`,
                        transition: "width 0.3s ease-in-out",
                    }}></div>
            </div>
            <button
                type="submit"
                style={{
                    opacity: currentSetIndex === dataSets.length - 1 ? 1 : 0.3,
                    transition: "all 0.25s ease-out",
                }}
                className="btn"
                disabled={currentSetIndex !== dataSets.length - 1}>
                Dodaj dokument
            </button>
        </div>
    );
};

export default DocumentDataForm;

