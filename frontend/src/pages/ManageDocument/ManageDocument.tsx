import React from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import { useDocumentData } from "../../hooks/useDocumentData.ts";
import "./ManageDocument.scss";
import DocumentTable from "../../components/DocumentTable/DocumentTable";

function ManageDocument() {
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

    const fosterCarerId = 4;
    const document = useDocumentData(fosterCarerId);

    return (
        <div className="app-page manage-child-page">
            <Rectangle links={links}>
                <div className="manageChild">
                    <DocumentTable document={document} />
                </div>
            </Rectangle>
        </div>
    );
}

export default ManageDocument;

