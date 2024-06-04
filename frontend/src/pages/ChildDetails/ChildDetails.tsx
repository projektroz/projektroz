import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Child from "types/Child";
import "./ChildDetails.scss";
import Rectangle from "../../components/Rectangle/Rectangle";
import { api } from "../../api/axios";
import BackButton from "../../components/BackButton/BackButton";
import "bootstrap/dist/js/bootstrap.bundle.min";

interface Note {
    id: number;
    create_date: string;
    modification_date: string;
    note_text: string;
}

interface Document {
    documentId: number;
    name: string;
    filePath: string;
}

const ChildDetails: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [child, setChild] = useState<Child | null>(null);
    const [notes, setNotes] = useState<Note[]>([]);
    const [documents, setDocuments] = useState<Document[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchChildData = async () => {
            try {
                const response = await api.get(`/children/${id}`);
                setChild(response.data[0]); // Assuming the API returns an array with one child
                setLoading(false);
            } catch (err: any) {
                setError("Nie udało się pobrać danych dziecka.");
                setLoading(false);
            }
        };

        fetchChildData();
    }, [id]);

    useEffect(() => {
        const fetchChildNotes = async () => {
            try {
                const response = await api.get<Note[]>(`/notes/`);
                if (response.status === 404) {
                    throw new Error("No notes found");
                }

                const fetchedNotes = response.data;
                console.log("fetchedNotes", fetchedNotes.length);

                setNotes(fetchedNotes);

                // Use a separate useEffect or a callback to log notes after the state has updated
            } catch (err: any) {
                setError("Nie udało się pobrać notatek dziecka.");
            }
        };

        const fetchChildDoccuments = async () => {
            try {
                const response = await api.get(`/documents/page=0`);
                if (response.status === 404) {
                    console.log("No documents found");
                } else {
                    setDocuments(response.data);
                }
            } catch (err: any) {
                setError("Nie udało się pobrać dokumentów dziecka.");
            }
        };

        fetchChildNotes();
        // fetchChildDoccuments();
    }, [child]);

    // Separate useEffect to log updated notes
    useEffect(() => {
        console.log("noteslength", notes.length);
        console.log(notes);
    }, [notes]);

    useEffect(() => {
        // Set active tab from link
        const url = window.location.href;
        const tab = url.split("#")[1];
        const tabPane = document.getElementById(`${tab}-tab-pane`);
        const tabButton = document.getElementById(`${tab}-tab`);
        if (tab) {
            if (tabPane && tabButton) {
                tabPane.classList.add("show", "active");
                tabButton.classList.add("active");
            }
        } else {
            // set data-tab as default active tab if not tab set
            const dataTabPane = document.getElementById("data-tab-pane");
            const dataTabButton = document.getElementById("data-tab");
            if (dataTabPane && dataTabButton) {
                dataTabPane.classList.add("show", "active");
                dataTabButton.classList.add("active");
            }
        }
    }, [child]);

    if (loading) {
        return <div>Ładowanie...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!child) {
        return <div>Dziecko nie zostało znalezione</div>;
    }

    const handleAddDocument = () => {
        navigate(`/dashboard/add-document/${id}`);
    };

    const handleAddNote = () => {
        navigate(`/dashboard/add-note/${id}`);
    };

    const handleNoteView = (note_id: number) => {
        navigate(`/dashboard/note/${note_id}`);
    };

    const handleNoteEdit = (note_id: number) => {
        navigate(`/dashboard/note/${note_id}/edit`);
    };

    return (
        <div className="app-page child-details">
            <Rectangle>
                <BackButton />
                <h1>Szczegóły dziecka</h1>
                {/* <div className="details-grid"></div> */}
                <ul className="nav nav-tabs" id="myTab" role="tablist">
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="data-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#data-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="data-tab-pane"
                            aria-selected="true">
                            Dane dziecka
                        </button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="address-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#address-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="address-tab-pane"
                            aria-selected="false">
                            Adres zameldowania
                        </button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="parents-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#parents-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="parents-tab-pane"
                            aria-selected="false">
                            Rodzice
                        </button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="living-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#living-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="living-tab-pane"
                            aria-selected="false">
                            Adres zamieszkania
                        </button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="notes-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#notes-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="notes-tab-pane"
                            aria-selected="false">
                            Notatki
                        </button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button
                            className="nav-link"
                            id="documents-tab"
                            data-bs-toggle="tab"
                            data-bs-target="#documents-tab-pane"
                            type="button"
                            role="tab"
                            aria-controls="documents-tab-pane"
                            aria-selected="false">
                            Dokumenty
                        </button>
                    </li>
                </ul>
                <div className="tab-content mt-3" id="myTabContent">
                    <div
                        className="tab-pane fade"
                        id="data-tab-pane"
                        role="tabpanel"
                        aria-labelledby="data-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Dane dziecka</h2>
                            <div className="details-item">
                                <span className="label">Imię:</span>
                                <span className="value">{child.name}</span>
                            </div>
                            <div className="details-item">
                                <span className="label">Nazwisko:</span>
                                <span className="value">{child.surname}</span>
                            </div>
                            <div className="details-item">
                                <span className="label">Data urodzenia:</span>
                                <span className="value">
                                    {new Date(
                                        child.birth_date
                                    ).toLocaleDateString()}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">
                                    Miejsce urodzenia:
                                </span>
                                <span className="value">
                                    {child.birth_place}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">PESEL:</span>
                                <span className="value">{child.pesel}</span>
                            </div>
                            <div className="details-item">
                                <span className="label">Data przyjęcia:</span>
                                <span className="value">
                                    {new Date(
                                        child.date_of_admission
                                    ).toLocaleDateString()}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Decyzja sądu:</span>
                                <span className="value">
                                    {child.court_decision}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Notatka:</span>
                                <span className="value">{child.note}</span>
                            </div>
                        </div>
                    </div>
                    <div
                        className="tab-pane fade"
                        id="address-tab-pane"
                        role="tabpanel"
                        aria-labelledby="address-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Adres zameldowania</h2>
                            <div className="details-item">
                                <span className="label">Kraj:</span>
                                <span className="value">
                                    {child.address_registered.country}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Miasto:</span>
                                <span className="value">
                                    {child.address_registered.city}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Ulica:</span>
                                <span className="value">
                                    {child.address_registered.street}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Kod pocztowy:</span>
                                <span className="value">
                                    {child.address_registered.postal_code}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Numer domu:</span>
                                <span className="value">
                                    {child.address_registered.apartment_number}
                                </span>
                            </div>
                        </div>
                    </div>
                    <div
                        className="tab-pane fade"
                        id="parents-tab-pane"
                        role="tabpanel"
                        aria-labelledby="parents-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Rodzice</h2>
                            <div className="details-item">
                                <span className="label">Imię matki:</span>
                                <span className="value">
                                    {child.mother.name}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Nazwisko matki:</span>
                                <span className="value">
                                    {child.mother.surname}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Imię ojca:</span>
                                <span className="value">
                                    {child.father.name}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Nazwisko ojca:</span>
                                <span className="value">
                                    {child.father.surname}
                                </span>
                            </div>
                        </div>
                    </div>
                    <div
                        className="tab-pane fade"
                        id="living-tab-pane"
                        role="tabpanel"
                        aria-labelledby="living-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Adres zamieszkania</h2>
                            <div className="details-item">
                                <span className="label">Kraj:</span>
                                <span className="value">
                                    {child.address.country}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Miasto:</span>
                                <span className="value">
                                    {child.address.city}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Ulica:</span>
                                <span className="value">
                                    {child.address.street}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Kod pocztowy:</span>
                                <span className="value">
                                    {child.address.postal_code}
                                </span>
                            </div>
                            <div className="details-item">
                                <span className="label">Numer domu:</span>
                                <span className="value">
                                    {child.address.apartment_number}
                                </span>
                            </div>
                        </div>
                    </div>
                    <div
                        className="tab-pane fade"
                        id="notes-tab-pane"
                        role="tabpanel"
                        aria-labelledby="notes-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Notatki</h2>
                            <button
                                className="btn btn-primary mb-3"
                                onClick={handleAddNote}>
                                Dodaj notatkę
                            </button>
                            <div>
                                <span className="label">Notatki:</span>
                                {notes.length > 0 ? (
                                    <span className="value">
                                        {notes.map((note) => (
                                            <div
                                                className="note mb-3"
                                                key={note.id}>
                                                <div className="note-content">
                                                    <h2 className="note-date">
                                                        {new Date(
                                                            note.create_date
                                                        ).toLocaleDateString()}
                                                    </h2>
                                                    <p className="note-text">
                                                        {note.note_text}
                                                    </p>
                                                </div>
                                                <div className="note-actions">
                                                    <button
                                                        className="btn btn-primary"
                                                        onClick={() =>
                                                            handleNoteView(
                                                                note.id
                                                            )
                                                        }>
                                                        Wyświetl
                                                    </button>
                                                    <button
                                                        className="btn btn-primary"
                                                        onClick={() =>
                                                            handleNoteEdit(
                                                                note.id
                                                            )
                                                        }>
                                                        Edytuj
                                                    </button>
                                                </div>
                                            </div>
                                        ))}
                                    </span>
                                ) : (
                                    <span className="value">Brak notatek</span>
                                )}
                            </div>
                        </div>
                    </div>
                    <div
                        className="tab-pane fade"
                        id="documents-tab-pane"
                        role="tabpanel"
                        aria-labelledby="documents-tab"
                        tabIndex={0}>
                        <div className="details-section">
                            <h2>Dokumenty</h2>
                            <button
                                className="btn btn-primary mb-3"
                                onClick={handleAddDocument}>
                                Dodaj dokument
                            </button>
                            <div className="details-item">
                                <span className="label">Dokumenty:</span>
                                {documents.length > 0 ? (
                                    <span className="value">
                                        {documents.map((document) => (
                                            <a
                                                href={document.filePath}
                                                target="_blank"
                                                rel="noreferrer">
                                                {document.name}
                                            </a>
                                        ))}
                                    </span>
                                ) : (
                                    <span className="value">
                                        Brak dokumentów
                                    </span>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </Rectangle>
        </div>
    );
};

export default ChildDetails;
