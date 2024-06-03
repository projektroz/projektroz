function getDocumentData(formData: any) {
    return {
        document_path: formData.document_path,
        child: formData.child,
        category: formData.category,
    };
}

function getDocumentFile(formData: any) {
    return {
        file: formData.file,
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
        child: documentData.child,
        category: documentData.category,
    };
}

function getDefaultFormData() {
    return {
        file: "",
        document_path: "",
        child: 1,
        category: 1,
    };
}

export { getDocumentData, getDocumentFile, parseBackToFormData };
