import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../../api/axios";
import Rectangle from "../../components/Rectangle/Rectangle";
import BackButton from "../../components/BackButton/BackButton";

import "./Notes.scss";

interface Note {
    id: number;
    create_date: string;
    modification_date: string;
    note_text: string;
}

const Notes = () => {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [data, setData] = useState<Note>({
        id: -1,
        create_date: "",
        modification_date: "",
        note_text: "",
    });
    const [edit, setEdit] = useState(false);
    const [saveActive, setSaveActive] = useState(false);

    const { noteId, action } = useParams<{ noteId: string; action: string }>();

    useEffect(() => {
        if (noteId) {
            setEdit(action === "edit");
            fetchNotes(parseInt(noteId));
        }
    }, [noteId, action]);

    const fetchNotes = async (id: number) => {
        try {
            const response = await api.get(`/notes/${id}`);
            console.log("Notes:", response.data);
            if (response.status === 200) {
                console.log("Notes loaded successfully");
                setData(response.data);
            }
        } catch (error: any) {
            setError(error.message || "Nie udało się pobrać notatek dziecka.");
        } finally {
            setLoading(false);
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error! {error}</div>;

    const handleTextChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const text = e.target.value;
        setData((prev) => ({ ...prev, note_text: text }));
        console.log("Text changed:", text);
        setSaveActive(true);
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const noteText = (e.target as HTMLFormElement).querySelector(
            "textarea"
        )?.value;
        if (!noteText) return;

        const fetchData = async () => {
            try {
                data.modification_date = new Date().toISOString().split("T")[0];

                const response = await api.put(`/notes/${data.id}`, data);
                console.log("Note updated:", response.data);
                if (response.status === 200) {
                    console.log("Note updated successfully");
                    setEdit(false);
                    fetchNotes(data.id);
                }
            } catch (error: any) {
                setError(
                    error.message || "Nie udało się zaktualizować notatki."
                );
            }
        };

        fetchData();
    };

    return (
        <div className="app-page note-container">
            <Rectangle>
                <BackButton />
                <h1>Notatka</h1>
                <form
                    className="content-center"
                    onSubmit={(e) => handleSubmit(e)}>
                    <textarea
                        defaultValue={data.note_text}
                        disabled={!edit}
                        onChange={(e) => handleTextChange(e)}
                    />
                    {edit && (
                        <button
                            className="btn btn-primary"
                            type="submit"
                            disabled={!saveActive}>
                            Zapisz
                        </button>
                    )}
                </form>
            </Rectangle>
        </div>
    );
};

export default Notes;
