import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import Child from "types/Child";
import "./ChildDetails.scss";
import Rectangle from "../../components/Rectangle/Rectangle.tsx";

const mockChildren: Child[] = [
    { id: 1, name: "Jan", surname: "Kowalski", birth_date: new Date('2010-01-01'), birth_place: "Warszawa", pesel: "12345678901", date_of_admission: new Date('2020-01-01'), court_decision: "Decyzja Sądu", address: { id: 1, country: "Polska", city: "Warszawa", street: "Ulica", postal_code: "00-001", apartment_number: 1, is_registered: true }, address_registered: { id: 2, country: "Polska", city: "Warszawa", street: "Inna Ulica", postal_code: "00-002", apartment_number: 2, is_registered: true }, mother: { id: 1, name: "Anna", surname: "Kowalska", role: "Matka" }, father: { id: 2, name: "Piotr", surname: "Kowalski", role: "Ojciec" }, foster_carer: 2, note: 5 }
    // Dodaj pozostałe dzieci
];

const ChildDetails: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const child = mockChildren.find(child => child.id === parseInt(id!));

    if (!child) {
        return <div>Dziecko nie zostało znalezione</div>;
    }

    return (
        <div className="app-page child-details">
            <Rectangle>
                <h1>Szczegóły dziecka</h1>
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
                    <span className="value">{child.birth_date.toLocaleDateString()}</span>
                </div>
                <div className="details-item">
                    <span className="label">Miejsce urodzenia:</span>
                    <span className="value">{child.birth_place}</span>
                </div>
                <div className="details-item">
                    <span className="label">PESEL:</span>
                    <span className="value">{child.pesel}</span>
                </div>
                <div className="details-item">
                    <span className="label">Opiekun:</span>
                    {/*<span className="value">{child.foster_carer.name} {child.foster_carer.surname}</span>*/}
                </div>
                {/* Dodaj pozostałe szczegóły */}
                <button className="back-button" onClick={() => navigate(-1)}>Powrót</button>
            </Rectangle>
        </div>
    );
};

export default ChildDetails;
