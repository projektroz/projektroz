import { api, upload } from "./axios";

type AddDocumentResponse = {
    id: number;
    document_type: string;
    document_number: string;
    issue_date: Date;
    expiration_date: Date;
    issuing_authority: string;
    additional_information: string;
};

export async function addDocument(
    documentData: any,
    method: string
): Promise<AddDocumentResponse> {
    const documentId = documentData.id;
    console.log("Sending data:", documentData); // Logowanie danych do wysyłki
    try {
        const response =
            method === "POST"
                ? await api.post("documents/", documentData)
                : await api.put(`documents/${documentId}/`, documentData);

        return response.data;
    } catch (error: any) {
        console.error("Error:", error.response.data); // Logowanie błędu
        throw new Error(
            error.response.data.detail ||
                "An error occurred while processing your request."
        );
    }
}

export async function addDocumentFile(data: any): Promise<any> {
    console.log("Sending file:", JSON.stringify(data));
    try {
        // const formData = new FormData();
        // formData.append("file", file);
        // formData.append("name", name);
        const response = await upload.post("/", data);

        return response.data;
    } catch (error: any) {
        console.error("Error:", error.response.data); // Logowanie błędu
        throw new Error(
            error.response.data.detail ||
                "An error occurred while processing your request."
        );
    }
}
