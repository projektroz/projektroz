


import React, { useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import ChildDataCard from "../../components/ChildDataCard/ChildDataCard";
import { addChild } from "../../api/addChild";
import "./AddChild.scss";

function AddChild() {
  const [formData, setFormData] = useState({
    name: "",
    surname: "",
    birthDate: "",
    birthPlace: "",
    pesel: "",
    admissionDate: "",
    courtDecision: "",
    addressRegisteredCountry: "",
    addressRegisteredCity: "",
    addressRegisteredStreet: "",
    addressRegisteredPostalCode: "",
    addressRegisteredHouseNumber: "",
    addressCurrentCountry: "",
    addressCurrentCity: "",
    addressCurrentStreet: "",
    addressCurrentPostalCode: "",
    addressCurrentHouseNumber: "",
    motherName: "",
    motherSurname: "",
    fatherName: "",
    fatherSurname: ""
  });

  const [error, setError] = useState("");

  const handleInputChange = (name: string, value: string | Date) => {
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      // await addChild(formData);
      console.log(formData);
      setError("");
    } catch (error: any) {
      setError(error.message);
    }
  };

  const links = [
    { name: "Strona główna", url: "/home", icon: "src/assets/icons/home.png" },
    { name: "Panel sterowania", url: "/dashboard", icon: "src/assets/icons/manage.png" },
    { name: "Wyloguj", url: "/logout", icon: "src/assets/icons/logout.png" }
  ];

  interface DataInput {
    inputLabel: string;
    placeholder: string;
    type: 'date' | 'text';
    regex?: string;
  }
  
  const dataSets: DataInput[][] = [
    [
      { inputLabel: "Imie", placeholder: "Wpisz imię", type: "text" },
      { inputLabel: "Nazwisko", placeholder: "Wpisz nazwisko", type: "text" },
      { inputLabel: "Data Urodzenia", placeholder: "Wpisz datę urodzenia", type: "date" },
      { inputLabel: "Miejsce Urodzenia", placeholder: "Wpisz miejsce urodzenia", type: "text" },
      { inputLabel: "PESEL", placeholder: "Wpisz PESEL", type: "text", regex: "[0-9]{11}$" },
      { inputLabel: "Data Przyjęcia", placeholder: "Wpisz datę przyjęcia", type: "date" },
      { inputLabel: "Decyzja Sadu", placeholder: "Wpisz decyzję sądu", type: "text" },
    ],
    [
      {inputLabel: "Kraj Stalego Zameldowania", placeholder: "Wpisz kraj", type: "text"},
      {inputLabel: "Miasto Stalego Zameldowania", placeholder: "Wpisz miasto", type: "text"},
      {inputLabel: "Ulica Stalego Zameldowania", placeholder: "Wpisz ulicę", type: "text"},
      {inputLabel: "Kod Pocztowy Stalego Zameldowania", placeholder: "Wpisz kod pocztowy", type: "text"},
      {inputLabel: "Numer Domu Stalego Zameldowania", placeholder: "Wpisz numer domu", type: "text"},
    ],
    [
      {inputLabel: "Kraj Zamieszkania", placeholder: "Wpisz kraj", type: "text"},
      {inputLabel: "Miasto Zamieszkania", placeholder: "Wpisz miasto", type: "text"},
      {inputLabel: "Ulica Zamieszkania", placeholder: "Wpisz ulicę", type: "text"},
      {inputLabel: "Kod pocztowy Zamieszkania", placeholder: "Wpisz kod pocztowy", type: "text"},
      {inputLabel: "Numer domu Zamieszkania", placeholder: "Wpisz numer domu", type: "text"},
    ],
    [
      {inputLabel: "Imie Matki", placeholder: "Wpisz imię matki", type: "text"},
      {inputLabel: "Nazwisko Matki", placeholder: "Wpisz nazwisko matki", type: "text"},
    ],
    [
      {inputLabel: "Imie Ojca", placeholder: "Wpisz imię ojca", type: "text"},
      {inputLabel: "Nazwisko Ojca", placeholder: "Wpisz nazwisko ojca", type: "text"},
    ]
  ];

  return (
    <div className="add-child-page">
      <Rectangle links={links}>
        <div className="child-content">
          <h2>Dodaj dziecko</h2>
          <form onSubmit={handleSubmit}>
            <ChildDataCard
              dataSets={dataSets}
              formData={formData}
              handleInputChange={handleInputChange}
            />
            <button type="submit">Dodaj dziecko</button>
          </form>
          {error && <div className="error">{error}</div>}
        </div>
      </Rectangle>
    </div>
  );
}

export default AddChild;