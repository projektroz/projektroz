import React from "react";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import "./NoteDataForm.scss";

// Interfejsy definiujące dane wejściowe i właściwości komponentów
interface NoteInput {
    id: string;
    inputLabel: string;
    type: string;
}

interface NoteDataFormProps {
    dataSets: NoteInput[][];
    formData: {
        create_date: string;
        modification_date: string;
        note_text: string;
    };
    handleInputChange: (name: string, value: string) => void;
}

interface NoteInputFieldProps {
    data: NoteInput;
    index: number;
    value: string;
    handleInputChange: (name: string, value: string) => void;
}

const NoteInputField: React.FC<NoteInputFieldProps> = ({
    data,
    index,
    value,
    handleInputChange,
}) => {
    return (
        <div className="Note-input content-center">
            {data.type === "date" ? (
                <div className="form-floating mb-3" style={{ width: "100%" }}>
                    <input
                        className="form-control"
                        id={`floatingInput-${data.id}-${index}`}
                        type={data.type}
                        name={data.id}
                        value={
                            data.type === "date"
                                ? new Date().toISOString().slice(0, 10)
                                : value
                        }
                        disabled={data.type === "date"}
                        onChange={(e) =>
                            handleInputChange(data.id, e.target.value)
                        }
                        required
                        style={{ width: "100%" }}
                    />
                    <label htmlFor={`floatingInput-${data.id}-${index}`}>
                        {data.inputLabel}
                    </label>
                </div>
            ) : (
                <div className="form-floating mb-3" style={{ width: "100%" }}>
                    <textarea
                        className="form-control"
                        id={`floatingInput-${data.id}-${index}`}
                        name={data.id}
                        value={value}
                        onChange={(e) =>
                            handleInputChange(data.id, e.target.value)
                        }
                        required
                        style={{
                            width: "100%",
                            height: "300px",
                            resize: "none",
                        }}
                    />
                    <label htmlFor={`floatingInput-${data.id}-${index}`}>
                        {data.inputLabel}
                    </label>
                </div>
            )}
        </div>
    );
};

// Komponent reprezentujący pojedynczy zestaw danych
const NoteDataSet: React.FC<{
    dataSet: NoteInput[];
    index: number;
    formData: {
        create_date: string;
        modification_date: string;
        note_text: string;
    };
    handleInputChange: (name: string, value: string) => void;
}> = ({ dataSet, index, formData, handleInputChange }) => (
    <div className="content-center">
        {dataSet.map((data, dataIndex) => (
            <NoteInputField
                key={dataIndex}
                data={data}
                index={index}
                value={formData[data.id as keyof typeof formData]}
                handleInputChange={handleInputChange}
            />
        ))}
    </div>
);

// Główny komponent zarządzający zestawami danych
const NoteDataForm: React.FC<NoteDataFormProps> = ({
    dataSets,
    formData,
    handleInputChange,
}) => {
    return (
        <div className="Note-data-form-wrapper">
            <div className="Note-data-form">
                <TransitionGroup>
                    {dataSets.map((dataSet, index) => (
                        <CSSTransition
                            key={index}
                            timeout={500}
                            classNames="fade">
                            <NoteDataSet
                                dataSet={dataSet}
                                index={index}
                                formData={formData}
                                handleInputChange={handleInputChange}
                            />
                        </CSSTransition>
                    ))}
                </TransitionGroup>
            </div>
            <button
                type="submit"
                style={{
                    opacity: "1",
                    transition: "all 0.25s ease-out",
                    width: "100%",
                }}
                className="btn btn-primary">
                Dodaj notatkę
            </button>
        </div>
    );
};

export default NoteDataForm;
