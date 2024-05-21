import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Child from "types/Child";
import "./ChildTable.scss";

interface ChildTableProps {
    children: Child[];
}

const ChildTable: React.FC<ChildTableProps> = ({ children }) => {
    const [sortConfig, setSortConfig] = useState<{ key: keyof Child; direction: 'ascending' | 'descending' } | null>(null);
    const [searchTerm, setSearchTerm] = useState("");
    const navigate = useNavigate();

    const sortedChildren = React.useMemo(() => {
        const sortableChildren = [...children];
        if (sortConfig !== null) {
            sortableChildren.sort((a, b) => {
                const key = sortConfig.key;
                if (typeof a[key] === 'string' && typeof b[key] === 'string') {
                    return sortConfig.direction === 'ascending'
                        ? (a[key] as string).localeCompare(b[key] as string)
                        : (b[key] as string).localeCompare(a[key] as string);
                } else if (a[key] instanceof Date && b[key] instanceof Date) {
                    return sortConfig.direction === 'ascending'
                        ? (a[key] as Date).getTime() - (b[key] as Date).getTime()
                        : (b[key] as Date).getTime() - (a[key] as Date).getTime();
                } else if (typeof a[key] === 'number' && typeof b[key] === 'number') {
                    return sortConfig.direction === 'ascending'
                        ? (a[key] as number) - (b[key] as number)
                        : (b[key] as number) - (a[key] as number);
                }
                return 0;
            });
        }
        return sortableChildren;
    }, [children, sortConfig]);

    const filteredChildren = sortedChildren.filter((child) =>
        child.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        child.surname.toLowerCase().includes(searchTerm.toLowerCase()) ||
        child.birth_place.toLowerCase().includes(searchTerm.toLowerCase()) ||
        child.pesel.includes(searchTerm)
    );

    const requestSort = (key: keyof Child) => {
        let direction: 'ascending' | 'descending' = 'ascending';
        if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
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
            <input
                type="text"
                placeholder="Szukaj..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="search-input"
            />
            <table className="child-table">
                <thead>
                <tr>
                    <th onClick={() => requestSort('name')}>Imię</th>
                    <th onClick={() => requestSort('surname')}>Nazwisko</th>
                    <th onClick={() => requestSort('birth_date')}>Data urodzenia</th>
                    <th onClick={() => requestSort('birth_place')}>Miejsce urodzenia</th>
                    <th onClick={() => requestSort('pesel')}>PESEL</th>
                    <th>Akcje</th>
                </tr>
                </thead>
                <tbody>
                {filteredChildren.map((child) => (
                    <tr key={child.id}>
                        <td>{child.name}</td>
                        <td>{child.surname}</td>
                        <td>{child.birth_date.toLocaleDateString()}</td>
                        <td>{child.birth_place}</td>
                        <td>{child.pesel}</td>
                        <td>
                            <div className="button-container">
                                <button onClick={() => handleView(child.id)}>Wyświetl</button>
                                <button onClick={() => handleEdit(child.id)}>Edytuj</button>
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
