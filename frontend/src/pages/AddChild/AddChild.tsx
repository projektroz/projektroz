import React, { useEffect, useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
import ChildDataCard from "../../components/ChildDataForm/ChildDataForm";
import { addChild } from "../../api/addChild";
import { getChildData, parseBackToFormData } from '../../functions/AddChildFunctions';
import "./AddChild.scss";
import Child from "types/Child";

function AddChild({title, method}: {title: string, method: string}) {
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
		fatherSurname: "",
	});

	useEffect(() => {
        const dataFromStorage = localStorage.getItem("childData");
        if (dataFromStorage) {
            setFormData(parseBackToFormData(dataFromStorage));
			localStorage.removeItem("childData");
        }
    }, []);

	const [error, setError] = useState("");

	const handleInputChange = (id: string, value: string | Date) => {
		setFormData((prevFormData) => ({
			...prevFormData,
			[id]: value,
		}));
	};

	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		try {
			await addChild(getChildData(formData), method);

			setError("");

      window.location.href = "/dashboard";
		} catch (error: any) {
			setError(error.message);
		}
	};

	const links = [
		{
			name: "Strona główna",
			url: "/home",
			icon: "src/assets/icons/home.png",
		},
		{
			name: "Panel sterowania",
			url: "/dashboard",
			icon: "../src/assets/icons/manage.png",
		},
		{ name: "Wyloguj", url: "/logout", icon: "../src/assets/icons/logout.png" },
	];

	interface DataInput {
		id: string;
		inputLabel: string;
		placeholder: string;
		type: "date" | "text";
		regex?: string;
	}

	const dataSets: DataInput[][] = [
		[
			{
				id: "name",
				inputLabel: "Imie",
				placeholder: "Wpisz imię",
				type: "text"
			},
			{
				id: "surname",
				inputLabel: "Nazwisko",
				placeholder: "Wpisz nazwisko",
				type: "text"
			},
			{
				id: "birthDate",
				inputLabel: "Data Urodzenia",
				placeholder: "Wpisz datę urodzenia",
				type: "date",
			},
			{
				id: "birthPlace",
				inputLabel: "Miejsce Urodzenia",
				placeholder: "Wpisz miejsce urodzenia",
				type: "text",
			},
			{
				id: "pesel",
				inputLabel: "PESEL",
				placeholder: "Wpisz PESEL",
				type: "text",
				regex: "[0-9]{11}$",
			},
			{
				id: "admissionDate",
				inputLabel: "Data Przyjęcia",
				placeholder: "Wpisz datę przyjęcia",
				type: "date",
			},
			{
				id: "courtDecision",
				inputLabel: "Decyzja Sadu",
				placeholder: "Wpisz decyzję sądu",
				type: "text",
			},
		],
		[
			{
				id: "addressRegisteredCountry",
				inputLabel: "Kraj Zameldowania",
				placeholder: "Wpisz kraj",
				type: "text",
			},
			{
				id: "addressRegisteredCity",
				inputLabel: "Miasto Zameldowania",
				placeholder: "Wpisz miasto",
				type: "text",
			},
			{
				id: "addressRegisteredStreet",
				inputLabel: "Ulica Zameldowania",
				placeholder: "Wpisz ulicę",
				type: "text",
			},
			{
				id: "addressRegisteredPostalCode",
				inputLabel: "Kod Pocztowy Zameldowania",
				placeholder: "Wpisz kod pocztowy",
				type: "text",
			},
			{
				id: "addressRegisteredHouseNumber",
				inputLabel: "Numer Domu Zameldowania",
				placeholder: "Wpisz numer domu",
				type: "text",
			},
		],
		[
			{
				id: "addressCurrentCountry",
				inputLabel: "Kraj Zamieszkania",
				placeholder: "Wpisz kraj",
				type: "text",
			},
			{
				id: "addressCurrentCity",
				inputLabel: "Miasto Zamieszkania",
				placeholder: "Wpisz miasto",
				type: "text",
			},
			{
				id: "addressCurrentStreet",
				inputLabel: "Ulica Zamieszkania",
				placeholder: "Wpisz ulicę",
				type: "text",
			},
			{
				id: "addressCurrentPostalCode",
				inputLabel: "Kod pocztowy Zamieszkania",
				placeholder: "Wpisz kod pocztowy",
				type: "text",
			},
			{
				id: "addressCurrentHouseNumber",
				inputLabel: "Numer domu Zamieszkania",
				placeholder: "Wpisz numer domu",
				type: "text",
			},
		],
		[
			{
				id: "motherName",
				inputLabel: "Imie Matki",
				placeholder: "Wpisz imię matki",
				type: "text",
			},
			{
				id: "motherSurname",
				inputLabel: "Nazwisko Matki",
				placeholder: "Wpisz nazwisko matki",
				type: "text",
			},
		],
		[
			{
				id: "fatherName",
				inputLabel: "Imie Ojca",
				placeholder: "Wpisz imię ojca",
				type: "text"
			},
			{
				id: "fatherSurname",
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
					<h2>{title}</h2>
					<form onSubmit={handleSubmit}>
						<ChildDataCard
							dataSets={dataSets}
							formData={formData}
							handleInputChange={handleInputChange}
						/>
						{/* <button type="submit">Dodaj dziecko</button> */}
					</form>
					{error && <div className="error">{error}</div>}
				</div>
			</Rectangle>
		</div>
	);
}

export default AddChild;
