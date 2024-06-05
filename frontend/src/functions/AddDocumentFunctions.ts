function getDocumentData(formData: any) {
    console.log("Document data:", formData);
    return {
        document_path: formData.file_path,
        document_google_id: formData.file_id,
        category: formData.file_type,
        child: formData.child_id,
    };
}

function getDocumentFile(formData: any) {
    return {
        file: formData.file,
        name: formData.file.name,
        file_type: formData.file_type,
        child_id: formData.child_id,
    };
}

function parseBackToFormData(documentDataString: string) {
    let documentData = null;
    try {
        documentData = JSON.parse(documentDataString);
    } catch (error) {
        console.error("Error parsing childData:", error);
        return getDefaultFormData();
    }

    if (!documentData) {
        console.error("No valid child data available");
        return getDefaultFormData();
    }

    return {
        document_path: documentData.document_path,
        document_id: documentData.document_id,
        file: new File([""], ""),
        name: "",
        file_type: "",
        child_id: 1,
    };
}

function getDefaultFormData() {
    return {
        document_path: "",
        document_id: 1,
        file: new File([""], ""),
        name: "",
        file_type: "",
        child_id: 1,
    };
}

export { getDocumentData, getDocumentFile, parseBackToFormData };
