import { useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import "./AddChild.scss";
import { addChild } from "../../api/addChild";


function AddChild() {
    const [name, setName] = useState("");
    const [surname, setSurname] = useState("");
    const [error, setError] = useState<string>("");
    // const {}
    // const [birthDate, setBirthDate] = useState("");
    // const [birthPlace, setBirthPlace] = useState("");
    // const [pesel, setPesel] = useState("");
    // const [address, setAddress] = useState("");
    // const [registeredAddreess, setRegisteredAddress] = useState("");
    // const [dateOfAdmission, setDateOfAdmission] = useState("");
    // const [courtDecision, setCourtDecision] = useState("");
    // const [motherName, setMotherName] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            await addChild(name, surname);
            setError("");
        } catch (error: any) {
            setError(error.message);
        }
    };
    

    const links = [
        { name: "Strona główna", url: "/home", icon: "src/assets/icons/home.png" },
        { name: "Panel sterowania", url: "/dashboard", icon: "src/assets/icons/manage.png"},
        { name: "Wyloguj", url: "/logout", icon: "src/assets/icons/logout.png" },
      ];

    return (
        <div className="AddChild-page">
            <Rectangle links={links}>
                <div className="content">
                    <h2>Dodaj dziecko</h2>
                    <form onSubmit={handleSubmit} className="add-child-form">
                        <div className="mb-3">
                            <label htmlFor="name" className="form-label">
                                Imię
                            </label>
                            <input
                                type="text"
                                className="form-control"
                                id="name"
                                placeholder="Wprowadź imię"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                required
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="surname" className="form-label">
                                Nazwisko
                            </label>
                            <input
                                type="text"
                                className="form-control"
                                id="surname"
                                placeholder="Wprowadź nazwisko"
                                value={surname}
                                onChange={(e) => setSurname(e.target.value)}
                                required
                            />
                        </div>
                        <button type="submit" className="btn btn-primary">Dodaj</button>
                    </form>
                    <div className="error">{error}</div>
                </div>
            </Rectangle>
        </div>
    );
}

export default AddChild;