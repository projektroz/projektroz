import { useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import "./AddChild.scss";
import { addChild } from "../../api/addChild";
import ChildDataCard from "../../components/ChildDataCard/ChildDataCard";

function AddChild() {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [birthPlace, setBirthPlace] = useState("");
  const [pesel, setPesel] = useState("");
  const [admissionDate, setAdmissionDate] = useState("");
  const [courtDecision, setCourtDecision] = useState("");

  const [motherName, setMotherName] = useState("");
  const [motherSurname, setMotherSurname] = useState("");

  const [fatherName, setFatherName] = useState("");
  const [fatherSurname, setFatherSurname] = useState("");

  const [addressRegisteredCountry, setAddressRegisteredCountry] = useState("");
  const [addressRegisteredCity, setAddressRegisteredCity] = useState("");
  const [addressRegisteredStreet, setAddressRegisteredStreet] = useState("");
  const [addressRegisteredPostalCode, setAddressRegisteredPostalCode] =
    useState("");
  const [addressRegisteredHouseNumber, setAddressRegisteredHouseNumber] =
    useState("");

  const [addressCurrentCountry, setAddressCurrentCountry] = useState("");
  const [addressCurrentCity, setAddressCurrentCity] = useState("");
  const [addressCurrentStreet, setAddressCurrentStreet] = useState("");
  const [addressCurrentPostalCode, setAddressCurrentPostalCode] = useState("");
  const [addressCurrentHouseNumber, setAddressCurrentHouseNumber] =
    useState("");

  const [error, setError] = useState<string>("");

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

  interface DataInput {
    inputLabel: string;
    placeholder: string;
    type: "date" | "text";
    regex?: string;
  }

  const dataSets: DataInput[][] = [
    [
      { inputLabel: "Imię", placeholder: "Wpisz imię", type: "text" },
      { inputLabel: "Nazwisko", placeholder: "Wpisz nazwisko", type: "text" },
      {
        inputLabel: "Data urodzenia",
        placeholder: "Wpisz datę urodzenia",
        type: "date",
      },
      {
        inputLabel: "Miejsce urodzenia",
        placeholder: "Wpisz miejsce urodzenia",
        type: "text",
      },
      {
        inputLabel: "PESEL",
        placeholder: "Wpisz PESEL",
        type: "text",
        regex: "[0-9]{11}$",
      },
      {
        inputLabel: "Data przyjęcia",
        placeholder: "Wpisz datę przyjęcia",
        type: "date",
      },
      {
        inputLabel: "Decyzja sądu",
        placeholder: "Wpisz decyzję sądu",
        type: "text",
      },
    ],
    [
      { inputLabel: "Kraj", placeholder: "Wpisz kraj", type: "text" },
      { inputLabel: "Miastio", placeholder: "Wpisz miasto", type: "text" },
      { inputLabel: "Ulica", placeholder: "Wpisz ulicę", type: "text" },
      {
        inputLabel: "Kod pocztowy",
        placeholder: "Wpisz kod pocztowy",
        type: "text",
      },
      {
        inputLabel: "Numer domu",
        placeholder: "Wpisz numer domu",
        type: "text",
      },
    ],
    [
      { inputLabel: "Kraj", placeholder: "Wpisz kraj", type: "text" },
      { inputLabel: "Miastio", placeholder: "Wpisz miasto", type: "text" },
      { inputLabel: "Ulica", placeholder: "Wpisz ulicę", type: "text" },
      {
        inputLabel: "Kod pocztowy",
        placeholder: "Wpisz kod pocztowy",
        type: "text",
      },
      {
        inputLabel: "Numer domu",
        placeholder: "Wpisz numer domu",
        type: "text",
      },
    ],
    [
      {
        inputLabel: "Imie Matki",
        placeholder: "Wpisz imię matki",
        type: "text",
      },
      {
        inputLabel: "Nazwisko Matki",
        placeholder: "Wpisz nazwisko matki",
        type: "text",
      },
    ],
    [
      { inputLabel: "Imie Ojca", placeholder: "Wpisz imię ojca", type: "text" },
      {
        inputLabel: "Nazwisko Ojca",
        placeholder: "Wpisz nazwisko ojca",
        type: "text",
      },
    ],
  ];

  return (
    <div className="app-page add-child-page">
      <Rectangle links={links}>
        <div className="child-content">
          <h2>Dodaj dziecko</h2>
          <form onSubmit={handleSubmit}>
            <ChildDataCard dataSets={dataSets} />
            <button type="submit">Dodaj dziecko</button>
          </form>
          <div className="error">{error}</div>
        </div>
      </Rectangle>
    </div>
  );
}

export default AddChild;
