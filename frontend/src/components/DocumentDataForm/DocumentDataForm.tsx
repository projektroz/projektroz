import React, { useState } from "react";
import "./DocumentDataForm.scss";

// Interfejsy definiujące dane wejściowe i właściwości komponentów
interface DocumentInput {
    id: string;
    inputLabel: string;
    type: string;
}

interface DocumentDataFormProps {
    dataSets: DocumentInput[];
    formData: {
        file: File;
        document_path: string;
        child: number;
        category: number;
    };
    handleInputChange: (name: string, value: any) => void;
}

// make enum
enum DocumentType {
    SZKOLA = "Szkoła",
    SAD = "Sąd",
    ZDROWIE = "Zdrowie",
    INNE = "Inne",
}

const DocumentDataForm: React.FC<DocumentDataFormProps> = ({
    dataSets,
    formData,
    handleInputChange,
}) => {
    const [documentType, setDocumentType] = useState<string>("Typ dokumentu");

    const handleDropdownChange = (type: string) => {
        setDocumentType(type);
        switch (type) {
            case DocumentType.SZKOLA:
                handleInputChange("category", 1);
                break;
            case DocumentType.SAD:
                handleInputChange("category", 2);
                break;
            case DocumentType.ZDROWIE:
                handleInputChange("category", 3);
                break;
            case DocumentType.INNE:
                handleInputChange("category", 4);
                break;
        }
    };

    return (
        <div className="document-data-form-wrapper">
            <div className="document-data-form content-center">
                {dataSets.map((data, index) => (
                    <div className="document-input" key={index}>
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
                                            e.target.files
                                                ? e.target.files[0]
                                                : null
                                        )
                                    }
                                    required
                                />
                            </div>
                        ) : null}
                    </div>
                ))}
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
        </div>
    );
};

export default DocumentDataForm;
