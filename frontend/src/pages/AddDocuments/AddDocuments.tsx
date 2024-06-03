import React, { useEffect, useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import DocumentDataForm from "../../components/DocumentDataForm/DocumentDataForm";
import { addDocument } from "../../api/addDocument";
import "./AddDocuments.scss";

function AddDocuments({ title, method }: { title: string; method: string }) {
    const [formData, setFormData] = useState({
        documentType: "",
        documentNumber: "",
        issueDate: "",
        expirationDate: "",
        issuingAuthority: "",
        additionalInformation: "",
    });

    // useEffect(() => {
    //     const dataFromStorage = localStorage.getItem("documentData");
    //     if (dataFromStorage) {
    //         setFormData(parseBackToFormData(JSON.parse(dataFromStorage)));
    //         localStorage.removeItem("documentData");
    //     }
    // }, []);

    const [error, setError] = useState("");

    const handleInputChange = (id: string, value: string) => {
        setFormData((prevFormData) => ({
            ...prevFormData,
            [id]: value,
        }));
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            const data = getDocumentData(formData);
            console.log("Sending data:", data); // Logowanie danych
            await addDocument(data, method);
            setError("");

            window.location.href = "/dashboard";
        } catch (error: any) {
            console.error("Error:", error); // Logowanie błędu
            setError(error.message);
        }
    };

    const links = [
        {
            name: "Panel sterowania",
            url: "/dashboard",
            icon: "../src/assets/icons/manage.png",
        },
        {
            name: "Wyloguj",
            url: "/logout",
            icon: "../src/assets/icons/logout.png",
        },
    ];

    interface DocumentInput {
        id: string;
        inputLabel: string;
        type: "file" | "text";
    }

    const dataSets: DocumentInput[][] = [
        [
            {
                id: "filename",
                inputLabel: "Nazwa pliku",
                type: "file",
            },
        ],
    ];

    return (
        <div className="app-page add-documents-page">
            <Rectangle links={links}>
                <div className="document-content">
                    <h2>{title}</h2>
                    <form onSubmit={handleSubmit}>
                        <DocumentDataForm
                            dataSets={dataSets}
                            formData={formData}
                            handleInputChange={handleInputChange}
                        />
                    </form>
                    {error && <div className="error">{error}</div>}
                </div>
            </Rectangle>
        </div>
    );
}

export default AddDocuments;

