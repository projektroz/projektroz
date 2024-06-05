import React, { useEffect, useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import DocumentDataForm from "../../components/DocumentDataForm/DocumentDataForm";
import { addDocument, addDocumentFile } from "../../api/addDocument";
import {
    getDocumentData,
    getDocumentFile,
} from "../../functions/AddDocumentFunctions";
import "./AddDocuments.scss";

function AddDocuments({ title, method }: { title: string; method: string }) {
    const [loading, setLoading] = useState(false);
    const [childId, setChildId] = useState<number | null>(null);
    const [formData, setFormData] = useState({
        file_path: "",
        file_id: 1,
        file: new File([""], ""),
        name: "",
        file_type: "",
        child_id: 1,
    });
    const [error, setError] = useState("");

    useEffect(() => {
        const id = window.location.pathname.split("/").pop();
        if (id) setChildId(parseInt(id, 10));
    }, []);

    useEffect(() => {
        if (childId) {
            setFormData((prevFormData) => ({
                ...prevFormData,
                child_id: childId,
            }));
        }
    }, [childId]);
    
    const handleInputChange = (id: string, value: any) => {
        setFormData((prevFormData) => ({
            ...prevFormData,
            [id]: value,
        }));
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);
        try {
            const data = getDocumentFile(formData);
            console.log("Sending file: ", formData); // Logowanie pliku
            const response = await addDocumentFile(data);
            console.log("Google response: ", response); // Logowanie odpowiedzi z Google
            if (response) {
                console.log("File uploaded successfully");
                formData.file_path = response.file_path;
                formData.file_id = response.file_id;
            }
        } catch (error: any) {
            console.error("Error:", error); // Logowanie błędu
            setError(error.message);
            return;
        }
        try {
            const data = getDocumentData(formData);
            console.log("Sending data:", data); // Logowanie danych
            await addDocument(data, method);

            window.location.href = `/dashboard/manage-child/${childId}`;
        } catch (error: any) {
            console.error("Error:", error); // Logowanie błędu
            setError(error.message);
            return;
        }
        setLoading(false);
    };

    const links = [
        {
            name: "Panel sterowania",
            url: "/dashboard",
            icon: "../../src/assets/icons/manage.png",
        },
        {
            name: "Wyloguj",
            url: "/logout",
            icon: "../../src/assets/icons/logout.png",
        },
    ];

    const dataSets = [
        {
            id: "file",
            inputLabel: "Nazwa pliku",
            type: "file",
        },
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
                        {loading && <div className="loading">Loading...</div>}
                        <button
                            type="submit"
                            style={{
                                opacity: "1",
                                transition: "all 0.25s ease-out",
                            }}
                            className="btn btn-primary">
                            Dodaj dokument
                        </button>
                    </form>
                    {error && <div className="error">{error}</div>}
                </div>
            </Rectangle>
        </div>
    );
}

export default AddDocuments;
