import React, { useEffect, useState } from "react";
import "./DocumentDataForm.scss";

// Interfejsy definiujące dane wejściowe i właściwości komponentów
interface DocumentInput {
    id: string;
    inputLabel: string;
    type: string;
    category?: string;
}

interface DocumentDataFormProps {
    dataSets: DocumentInput[];
    formData: {
        file_path: string;
        file_id: number;
        file: File;
        file_type: string;
        child_id: number;
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

    console.log(dataSets);
    console.log(formData);

    useEffect(() => {
        if (formData.file_type) {
            console.log("Document type:", formData.file_type);
            setDocumentType(formData.file_type);
        }
    }, [formData.file_type]);

    const handleDropdownChange = (type: string) => {
        setDocumentType(type);
        switch (type) {
            case DocumentType.SZKOLA:
                handleInputChange("file_type", "Szkola");
                break;
            case DocumentType.SAD:
                handleInputChange("file_type", "Sad");
                break;
            case DocumentType.ZDROWIE:
                handleInputChange("file_type", "Zdrowie");
                break;
            case DocumentType.INNE:
                handleInputChange("file_type", "Inne");
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
