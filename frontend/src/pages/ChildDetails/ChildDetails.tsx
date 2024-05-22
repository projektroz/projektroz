import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Child from "types/Child";
import "./ChildDetails.scss";
import Rectangle from "../../components/Rectangle/Rectangle";
import { api } from "../../api/axios";
import BackButton from "../../components/BackButton/BackButton";

const ChildDetails: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [child, setChild] = useState<Child | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchChildData = async () => {
            try {
                const response = await api.get(`/children/${id}`);
                setChild(response.data[0]);  // Assuming the API returns an array with one child
                setLoading(false);
            } catch (err: any) {
                setError('Nie udało się pobrać danych dziecka.');
                setLoading(false);
            }
        };

        fetchChildData();
    }, [id]);

    if (loading) {
        return <div>Ładowanie...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!child) {
        return <div>Dziecko nie zostało znalezione</div>;
    }

    return (
        <div className="app-page child-details">
            <Rectangle>
                
                <BackButton />
                <h1>Szczegóły dziecka</h1>
                <div className="details-grid">
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
                            <span className="value">{new Date(child.birth_date).toLocaleDateString()}</span>
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
                            <span className="label">Data przyjęcia:</span>
                            <span className="value">{new Date(child.date_of_admission).toLocaleDateString()}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Decyzja sądu:</span>
                            <span className="value">{child.court_decision}</span>
                        </div>
                        {/* <div className="details-item">
                            <span className="label">Notatka:</span>
                            <span className="value">{child.note}</span>
                        </div> */}
                    </div>
                    <div className="details-section">
                        <h2>Adres zameldowania</h2>
                        <div className="details-item">
                            <span className="label">Kraj:</span>
                            <span className="value">{child.address_registered.country}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Miasto:</span>
                            <span className="value">{child.address_registered.city}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Ulica:</span>
                            <span className="value">{child.address_registered.street}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Kod pocztowy:</span>
                            <span className="value">{child.address_registered.postal_code}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Numer domu:</span>
                            <span className="value">{child.address_registered.apartment_number}</span>
                        </div>
                    </div>
                    <div className="details-section">
                        <h2>Rodzice</h2>
                        <div className="details-item">
                            <span className="label">Imię matki:</span>
                            <span className="value">{child.mother.name}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Nazwisko matki:</span>
                            <span className="value">{child.mother.surname}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Imię ojca:</span>
                            <span className="value">{child.father.name}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Nazwisko ojca:</span>
                            <span className="value">{child.father.surname}</span>
                        </div>
                    </div>
                    <div className="details-section">
                        <h2>Adres zamieszkania</h2>
                        <div className="details-item">
                            <span className="label">Kraj:</span>
                            <span className="value">{child.address.country}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Miasto:</span>
                            <span className="value">{child.address.city}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Ulica:</span>
                            <span className="value">{child.address.street}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Kod pocztowy:</span>
                            <span className="value">{child.address.postal_code}</span>
                        </div>
                        <div className="details-item">
                            <span className="label">Numer domu:</span>
                            <span className="value">{child.address.apartment_number}</span>
                        </div>
                    </div>
                </div>
           </Rectangle>
        </div>
    );
};

export default ChildDetails;
