import Rectangle from "../../components/Rectangle/Rectangle";
import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api, upload } from "../../api/axios";
import { addDocument, addDocumentFile } from "../../api/addDocument";
import {
    getDocumentData,
    getDocumentFile,
} from "../../functions/AddDocumentFunctions";
import DocumentDataForm from "../../components/DocumentDataForm/DocumentDataForm";

import "./Documents.scss";

interface File {
    file_name: string;
    file_data: string;
    mime_type: string;
}

interface FileData {
    id: number;
    document_path: string;
    category: string;
    child_id: number;
    document_google_id: string;
    name: string;
}

const Documents = () => {
    const { child_id, action, document_id } = useParams<{
        child_id: string;
        action: string;
        document_id: string;
    }>();
    const [loading, setLoading] = useState(true);
    const [file, setFile] = useState<File | null>(null);
    const [fileData, setFileData] = useState<FileData | null>(null);
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        file_path: "",
        file_id: 1,
        file: new File([""], ""),
        name: "",
        file_type: "",
        child_id: 1,
    });

    useEffect(() => {
        const fetchDocument = async () => {
            setLoading(true);
            try {
                const response = await api.get(`/documents/${document_id}`);
                console.log("Pobranie dokumentu z bazy: ", response.data);
                setFileData(response.data);
                setFormData((prevFormData) => ({
                    ...prevFormData,
                    child_id: response.data.child_id,
                    file_id: response.data.id,
                    file_path: response.data.document_path,
                    file_type: response.data.category,
                    name: response.data.name,
                }));
                if (action === "download") {
                    const fileResponse = await upload.get(
                        `/${response.data.document_google_id}`
                    );
                    console.log(
                        "Pobranie dokumentu z google'a: ",
                        fileResponse.data
                    );
                    setFile(fileResponse.data);
                }
            } catch (error: any) {
                console.error("Error:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchDocument();
    }, [document_id, action]);

    useEffect(() => {
        if (action === "download" && file) {
            const downloadFile = () => {
                const { file_name, file_data, mime_type } = file;

                // Create a new link element
                const link = document.createElement("a");
                link.href = `data:${mime_type};base64,${file_data}`;
                link.download = file_name;

                // Append the link to the body (required for Firefox)
                document.body.appendChild(link);

                // Programmatically click the link
                link.click();

                // Remove the link from the document
                document.body.removeChild(link);

                // Cleanup
                URL.revokeObjectURL(link.href);
                navigate(-1);
            };

            downloadFile();
        }
    }, [file, action, navigate]);

    const handleInputChange = (id: string, value: any) => {
        setFormData((prevFormData) => ({
            ...prevFormData,
            [id]: value,
        }));
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);

        if (!child_id) {
            console.error("Child ID not found");
            return;
        }
        const updatedFormData = {
            ...formData,
            child_id: parseInt(child_id),
            name: fileData?.name || formData.name || file?.file_name,
            file_type: fileData?.category || formData.file_type,
        };

        // console.log("Updated form data:", updatedFormData);
        // return;

        try {
            const data = getDocumentFile(updatedFormData);
            console.log("Sending file: ", updatedFormData);
            // return;

            const response = await addDocumentFile(data);
            console.log("Google response: ", response);
            if (response) {
                console.log("File uploaded successfully");
                updatedFormData.file_path = response.file_path;
                updatedFormData.file_id = response.file_id;
            }
        } catch (error: any) {
            console.error("Error:", error);
            setLoading(false);
            return;
        }
        try {
            const data = getDocumentData(updatedFormData);
            console.log("Prepared data:", data, updatedFormData);
            if (!document_id) {
                console.error("Document ID not found");
                return;
            }
            const id = parseInt(document_id);
            console.log(JSON.stringify(data));
            // return;
            const response = await addDocument(data, "PUT", id);

            console.log("Document updated successfully:", response);
            // return;

            navigate(-1);
        } catch (error: any) {
            console.error("Error:", error);
            setLoading(false);
            return;
        }
        setLoading(false);
    };

    const dataSets = [
        {
            id: "file",
            inputLabel: "Nazwa pliku",
            type: "file",
        },
    ];

    return (
        <div className="app-page">
            <Rectangle>
                <h1>Documents</h1>
                {loading && <p>Ładowanie...</p>}
                {!loading && action === "download" && (
                    <p>Pobieranie dokumentu...</p>
                )}
                {!loading && action === "upload" && (
                    <form onSubmit={handleSubmit} className="form">
                        <DocumentDataForm
                            dataSets={dataSets}
                            formData={formData}
                            handleInputChange={handleInputChange}
                        />
                        <button
                            type="submit"
                            style={{
                                opacity: "1",
                                transition: "all 0.25s ease-out",
                            }}
                            className="btn btn-primary mt-3">
                            Aktualizuj dokument
                        </button>
                    </form>
                )}
            </Rectangle>
        </div>
    );
};

export default Documents;
