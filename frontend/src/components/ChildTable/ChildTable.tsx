import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Child from "../../types/Child";
import "./ChildTable.scss";

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
    };

    return (
        <div>
            <div className="form-floating mb-3">
                <input
                    type="text"
                    placeholder="Szukaj..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="search-input form-control"
                    id="floatingSearch"
                />
                <label htmlFor="floatingSearch">Szukaj...</label>
            </div>
            <table className="child-table">
                <thead>
                    <tr>
                        <th onClick={() => requestSort("name")}>Imię</th>
                        <th onClick={() => requestSort("surname")}>Nazwisko</th>
                        <th onClick={() => requestSort("birth_date")}>
                            Data urodzenia
                        </th>
                        <th onClick={() => requestSort("birth_place")}>
                            Miejsce urodzenia
                        </th>
                        <th onClick={() => requestSort("pesel")}>PESEL</th>
                        <th>Akcje</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredChildren.map((child) => (
                        <tr key={child.id}>
                            <td>{child.name}</td>
                            <td>{child.surname}</td>
                            <td>
                                {new Date(
                                    child.birth_date
                                ).toLocaleDateString()}
                            </td>
                            <td>{child.birth_place}</td>
                            <td>{child.pesel}</td>
                            <td>
                                <div className="button-container">
                                    <button
                                        onClick={() => handleView(child.id)}>
                                        Wyświetl
                                    </button>
                                    <button
                                        onClick={() => handleEdit(child.id)}>
                                        Edytuj
                                    </button>
                                </div>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ChildTable;

