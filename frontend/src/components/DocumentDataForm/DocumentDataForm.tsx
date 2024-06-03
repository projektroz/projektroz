import React, { useState } from "react";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import "./DocumentDataForm.scss";

// Interfejsy definiujące dane wejściowe i właściwości komponentów
interface DocumentInput {
    id: string;
    inputLabel: string;
    type: string;
}

interface DocumentDataFormProps {
    dataSets: DocumentInput[][];
    formData: { document_path: string; child: number; category: number };
    handleInputChange: (name: string, value: string) => void;
}

interface DocumentInputFieldProps {
    data: DocumentInput;
    index: number;
    value: string;
    handleInputChange: (name: string, value: string) => void;
}

// make enum
enum DocumentType {
    SZKOLA = "Szkoła",
    SAD = "Sąd",
    ZDROWIE = "Zdrowie",
    INNE = "Inne",
}

const DocumentInputField: React.FC<DocumentInputFieldProps> = ({
    data,
    index,
    value,
    handleInputChange,
}) => {
    const [documentType, setDocumentType] = useState<string>("Typ dokumentu");

    const handleDropdownChange = (type: string) => {
        setDocumentType(type);
        // Przypisz wartość do odpowiadających z enuma
        switch (type) {
            case DocumentType.SZKOLA:
                handleInputChange(data.id, DocumentType.SZKOLA);
                break;
            case DocumentType.SAD:
                handleInputChange(data.id, DocumentType.SAD);
                break;
            case DocumentType.ZDROWIE:
                handleInputChange(data.id, DocumentType.ZDROWIE);
                break;
            case DocumentType.INNE:
                handleInputChange(data.id, DocumentType.INNE);
                break;
        }
    };

    return (
        <div className="document-input content-center">
            {data.type === "file" ? (
                <div>
                    <label
                        htmlFor={`formFile-${data.id}`}
                        className="form-label">
                        {data.inputLabel}
                    </label>
                    <input
                        className="form-control"
                        type="file"
                        id={`formFile-${data.id}`}
                        name={data.id}
                        onChange={(e) =>
                            handleInputChange(
                                data.id,
                                e.target.files ? e.target.files[0].name : ""
                            )
                        }
                        required
                    />
                </div>
            ) : (
                <div className="form-floating" style={{ width: "100%" }}>
                    <input
                        className="form-control"
                        id={`floatingInput-${data.id}-${index}`}
                        type={data.type}
                        name={data.id}
                        value={value}
                        onChange={(e) =>
                            handleInputChange(data.id, e.target.value)
                        }
                        required
                        style={{ width: "100%" }}
                    />
                    <label htmlFor={`floatingInput-${data.id}`}>
                        {data.id}
                    </label>
                </div>
            )}
            <div className="dropdown">
                <button
                    className="btn btn-secondary dropdown-toggle"
                    type="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false">
                    {documentType}
                </button>
                <ul className="dropdown-menu">
                    <li>
                        <a
                            className="dropdown-item"
                            href="#"
                            onClick={() => handleDropdownChange("Szkoła")}>
                            Szkoła
                        </a>
                    </li>
                    <li>
                        <a
                            className="dropdown-item"
                            href="#"
                            onClick={() => handleDropdownChange("Sąd")}>
                            Sąd
                        </a>
                    </li>
                    <li>
                        <a
                            className="dropdown-item"
                            href="#"
                            onClick={() => handleDropdownChange("Zdrowie")}>
                            Zdrowie
                        </a>
                    </li>
                    <li>
                        <a
                            className="dropdown-item"
                            href="#"
                            onClick={() => handleDropdownChange("Inne")}>
                            Inne
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    );
};

// Komponent reprezentujący pojedynczy zestaw danych
const DocumentDataSet: React.FC<{
    dataSet: DocumentInput[];
    index: number;
    formData: { document_path: string; child: number; category: number };
    handleInputChange: (name: string, value: string) => void;
}> = ({ dataSet, index, formData, handleInputChange }) => (
    <div className="content-center">
        {dataSet.map((data, dataIndex) => (
            <DocumentInputField
                key={dataIndex}
                data={data}
                index={index}
                value={formData[data.id as keyof typeof formData] as string}
                handleInputChange={handleInputChange}
            />
        ))}
    </div>
);
// Główny komponent zarządzający zestawami danych
const DocumentDataForm: React.FC<DocumentDataFormProps> = ({
    dataSets,
    formData,
    handleInputChange,
}) => {
    return (
        <div className="document-data-form-wrapper">
            <div className="document-data-form">
                <TransitionGroup>
                    {dataSets.map((dataSet, index) => (
                        <CSSTransition
                            key={index}
                            timeout={500}
                            classNames="fade">
                            <DocumentDataSet
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
                }}
                className="btn btn-primary">
                Dodaj dokument
            </button>
        </div>
    );
};

export default DocumentDataForm;
