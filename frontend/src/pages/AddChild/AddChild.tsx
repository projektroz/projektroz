import { useState } from "react";
import { addChild } from "../../api/addChild";

import "./AddChild.scss";
import Rectangle from "../../components/Rectangle/Rectangle";

function AddChild() {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [error, setError] = useState<string>("");
  const [birthDate, setBirthDate] = useState("");
  const [birthPlace, setBirthPlace] = useState("");
  const [pesel, setPesel] = useState("");
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
    {
      name: "Panel sterowania",
      url: "/dashboard",
      icon: "src/assets/icons/manage.png",
    },
    { name: "Wyloguj", url: "/logout", icon: "src/assets/icons/logout.png" },
  ];

  return (
    <div className="app-page add-child-page">
      <Rectangle links={links}>
        <div className="child-content">
          <h2>Dodaj dziecko</h2>
          <form onSubmit={handleSubmit} className="add-child-form">
            <div className="mb-3">
              <label htmlFor="name" className="form-label">
                *Imię
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
                *Nazwisko
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
            <div className="mb-3">
              <label htmlFor="birthDate" className="form-label">
                Data urodzenia
              </label>
              <input
                type="date"
                className="form-control"
                id="birthDate"
                placeholder="Wprowadź datę urodzenia"
                value={birthDate}
                onChange={(e) => setBirthDate(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="birthPlace" className="form-label">
                Miejsce urodzenia
              </label>
              <input
                type="text"
                className="form-control"
                id="birthPlace"
                placeholder="Wprowadź miejsce urodzenia"
                value={birthPlace}
                onChange={(e) => setBirthPlace(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="pesel" className="form-label">
                PESEL
              </label>
              <input
                type="text"
                className="form-control"
                id="pesel"
                placeholder="Wprowadź PESEL"
                value={pesel}
                onChange={(e) => setPesel(e.target.value)}
                required
              />
            </div>
            <div>
              <p> * pole wymagane </p>
            </div>
            <button type="submit" className="btn btn-primary">
              Dalej
            </button>
            <h4>1 z 3</h4>
          </form>
          <div className="error">{error}</div>
        </div>
      </Rectangle>
    </div>
  );
}

export default AddChild;
