import React, { useEffect, useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import NotesDataForm from "../../components/NotesDataForm/NotesDataForm";
import { addNote } from "../../api/addNote";
import { getNoteData } from "../../functions/AddNoteFunctions";
import "./AddNotes.scss";
import { useParams } from "react-router-dom";

function AddNotes({ title }: { title: string }) {
    const [formData, setFormData] = useState({
        create_date: "",
        modification_date: "",
        note_text: "",
        child: -1,
    });
    const [error, setError] = useState("");

    const childId = useParams<{ childId: string }>().childId;

    const handleInputChange = (id: string, value: string) => {
        setFormData((prevFormData) => ({
            ...prevFormData,
            [id]: value,
        }));
    };

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            const data = getNoteData(formData);
            console.log("Sending data:", data); // Logowanie danych
            data.create_date = new Date().toISOString().slice(0, 10);
            data.modification_date = new Date().toISOString().slice(0, 10);
            if (childId === undefined) {
                throw new Error("Nie znaleziono id dziecka");
            }
            data.child = parseInt(childId);
            await addNote(data);

            window.location.href = `/dashboard/manage-child/${childId}`;
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

    interface NoteInput {
        id: string;
        inputLabel: string;
        type: "text" | "date";
    }

    const dataSets: NoteInput[][] = [
        [
            { id: "create_date", inputLabel: "Data utworzenia", type: "date" },
            {
                id: "modification_date",
                inputLabel: "Data modyfikacji",
                type: "date",
            },
            { id: "note_text", inputLabel: "Treść notatki", type: "text" },
        ],
    ];

    return (
        <div className="app-page add-notes-page">
            <Rectangle links={links}>
                <div className="note-content">
                    <h2>{title}</h2>
                    <form onSubmit={handleSubmit}>
                        <NotesDataForm
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

export default AddNotes;
