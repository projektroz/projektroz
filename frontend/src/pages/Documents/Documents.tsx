import Rectangle from "../../components/Rectangle/Rectangle";
// import { useEffect, useState } from "react";
// import { useParams } from "react-router-dom";
// import { api } from "../../api/axios";

const Documents = () => {
    // const { document_google_id, action } = useParams<{
    //     document_google_id: string;
    //     action: string;
    // }>();
    // const [loading, setLoading] = useState(true);

    // useEffect(() => {
    //     // Pobieranie danych dokumentu
    //     const fetchDocument = async () => {
    //         try {
    //             const response = await api.get(
    //                 `/documents/${document_google_id}`
    //             );
    //             console.log(response.data); // Logowanie danych
    //         } catch (error: any) {
    //             console.error("Error:", error); // Logowanie błędu
    //         }
    //     };
    //     fetchDocument();
    // }, [document_google_id]);

    // if (loading) return <p>Loading...</p>;

    return (
        <div className="app-page">
            <Rectangle>
                <h1>Documents</h1>
            </Rectangle>
        </div>
    );
};

export default Documents;
