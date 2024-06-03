import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Child from "../../types/Child";
import "./ChildTable.scss";
import "bootstrap/dist/css/bootstrap.min.css";

interface ChildTableProps {
    children: Child[];
}

const ChildTable: React.FC<ChildTableProps> = ({ children }) => {
    const [sortConfig, setSortConfig] = useState<{
        key: keyof Child;
        direction: "ascending" | "descending";
    } | null>(null);
    const [searchTerm, setSearchTerm] = useState("");
    const navigate = useNavigate();

    console.log("Children passed to table:", children); // Log the children data

    const sortedChildren = React.useMemo(() => {
        const sortableChildren = [...children];
        if (sortConfig !== null) {
            sortableChildren.sort((a, b) => {
                const key = sortConfig.key;
                if (typeof a[key] === "string" && typeof b[key] === "string") {
                    return sortConfig.direction === "ascending"
                        ? (a[key] as string).localeCompare(b[key] as string)
                        : (b[key] as string).localeCompare(a[key] as string);
                } else if (
                    new Date(a[key] as string) instanceof Date &&
                    new Date(b[key] as string) instanceof Date
                ) {
                    return sortConfig.direction === "ascending"
                        ? new Date(a[key] as string).getTime() -
                              new Date(b[key] as string).getTime()
                        : new Date(b[key] as string).getTime() -
                              new Date(a[key] as string).getTime();
                } else if (
                    typeof a[key] === "number" &&
                    typeof b[key] === "number"
                ) {
                    return sortConfig.direction === "ascending"
                        ? (a[key] as number) - (b[key] as number)
                        : (b[key] as number) - (a[key] as number);
                }
                return 0;
            });
        }
        return sortableChildren;
    }, [children, sortConfig]);

    const filteredChildren = sortedChildren.filter(
        (child) =>
            child.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            child.surname.toLowerCase().includes(searchTerm.toLowerCase()) ||
            child.birth_place
                .toLowerCase()
                .includes(searchTerm.toLowerCase()) ||
            child.pesel.includes(searchTerm)
    );

    const requestSort = (key: keyof Child) => {
        let direction: "ascending" | "descending" = "ascending";
        if (
            sortConfig &&
            sortConfig.key === key &&
            sortConfig.direction === "ascending"
        ) {
            direction = "descending";
        }
        setSortConfig({ key, direction });
    };

    const handleView = (id: number) => {
        navigate(`/dashboard/manage-child/${id}`);
    };

    const handleEdit = (id: number) => {
        console.log(`Edytuj dziecko o ID: ${id}`);
        navigate(`/dashboard/edit-child/${id}`);
    };

    const handleNotes = (id: number) => {
        console.log(`Notatki dla dziecka o ID: ${id}`);
        navigate(`/dashboard/manage-child/${id}#notes`);
    };

    const handleDocuments = (id: number) => {
        console.log(`Dokumenty dla dziecka o ID: ${id}`);
        navigate(`/dashboard/manage-child/${id}#documents`);
    };

    return (
        <div style={{ maxHeight: "100%" }}>
            <div className="top-bar">
                <div className="form-floating" style={{ width: "60%" }}>
                    <input
                        type="text"
                        placeholder="Szukaj..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="form-control search-input"
                        id="floatingSearch"
                    />
                    <label htmlFor="floatingSearch">Szukaj...</label>
                </div>
                <div className="btn-group">
                    <button
                        className="btn btn-secondary btn-lg dropdown-toggle"
                        type="button"
                        data-bs-toggle="dropdown"
                        aria-expanded="false">
                        Sortowanie
                    </button>
                    <ul className="dropdown-menu">
                        <li>
                            <a
                                className="dropdown-item"
                                onClick={() => requestSort("name")}>
                                Sortuj po imieniu
                            </a>
                        </li>
                        <li>
                            <a
                                className="dropdown-item"
                                onClick={() => requestSort("surname")}>
                                Sortuj po nazwisku
                            </a>
                        </li>
                        <li>
                            <a
                                className="dropdown-item"
                                onClick={() => requestSort("birth_date")}>
                                Sortuj po dacie urodzenia
                            </a>
                        </li>
                        <li>
                            <a
                                className="dropdown-item"
                                onClick={() => requestSort("birth_place")}>
                                Sortuj po miejscu urodzenia
                            </a>
                        </li>
                        <li>
                            <a
                                className="dropdown-item"
                                onClick={() => requestSort("pesel")}>
                                Sortuj po peselu
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div className="content-scroll">
                {filteredChildren.map((child) => (
                    <div className="child-card" key={child.id}>
                        <div className="child-card-header">
                            <h2 className="mb-3">
                                {child.name} {child.surname}
                            </h2>
                            <div className="child-card-content">
                                <p>
                                    <strong>Data urodzenia: </strong>
                                    {new Date(
                                        child.birth_date
                                    ).toLocaleDateString()}
                                </p>
                                <p>
                                    <strong>Miejsce urodzenia: </strong>
                                    {child.birth_place}
                                </p>
                                <p>
                                    <strong>PESEL: </strong> {child.pesel}
                                </p>
                            </div>
                        </div>
                        <div className="button-container">
                            <button onClick={() => handleView(child.id)}>
                                Wyświetl
                            </button>
                            <button onClick={() => handleEdit(child.id)}>
                                Edytuj
                            </button>
                            <button onClick={() => handleDocuments(child.id)}>
                                Dokumenty
                            </button>
                            <button onClick={() => handleNotes(child.id)}>
                                Notatki
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ChildTable;
