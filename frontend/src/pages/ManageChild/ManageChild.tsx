// import React, { useState } from "react";
import Rectangle from "../../components/Rectangle/Rectangle";
// import { addChild, addFather, addMother } from "../../api/addChild";
// import { getChildData } from '../../functions/AddChildFunctions';
// import {useChildData} from "../../components/ChildData/ChildData";
import "./ManageChild.scss";
import Child from "types/Child";
import ChildTable from "../../components/ChildTable/ChildTable.tsx";


function ManageChild() {
    const links = [
        {
            name: "Strona główna",
            url: "/home",
            icon: "../src/assets/icons/home.png",
        },
        {
            name: "Panel sterowania",
            url: "/dashboard",
            icon: "../src/assets/icons/manage.png",
        },
        { name: "Wyloguj", url: "/logout", icon: "../src/assets/icons/logout.png" },
    ];

    // const fosterCarerId = 1;
    // const children = useChildData(fosterCarerId);

    // Statyczna lista dzieci dla testow
    const children: Child[] = [
        { id: 1, name: "Jan", surname: "Kowalski", birth_date: new Date('2010-01-01'), birth_place: "Warszawa", pesel: "12345678901", date_of_admission: new Date('2020-01-01'), court_decision: "Decyzja Sądu", address: { id: 1, country: "Polska", city: "Warszawa", street: "Ulica", postal_code: "00-001", apartment_number: 1, is_registered: true }, address_registered: { id: 2, country: "Polska", city: "Warszawa", street: "Inna Ulica", postal_code: "00-002", apartment_number: 2, is_registered: true }, mother: { id: 1, name: "Anna", surname: "Kowalska", role: "Matka" }, father: { id: 2, name: "Piotr", surname: "Kowalski", role: "Ojciec" }, foster_carer: 1, note: 5 },
        { id: 2, name: "Anna", surname: "Nowak", birth_date: new Date('2012-02-02'), birth_place: "Kraków", pesel: "23456789012", date_of_admission: new Date('2021-02-02'), court_decision: "Decyzja Sądu", address: { id: 3, country: "Polska", city: "Kraków", street: "Ulica", postal_code: "30-001", apartment_number: 3, is_registered: true }, address_registered: { id: 4, country: "Polska", city: "Kraków", street: "Inna Ulica", postal_code: "30-002", apartment_number: 4, is_registered: true }, mother: { id: 3, name: "Ewa", surname: "Nowak", role: "Matka" }, father: { id: 4, name: "Jan", surname: "Nowak", role: "Ojciec" }, foster_carer: 2, note: 4 },
        { id: 3, name: "sss", surname: "Wiśniewski", birth_date: new Date('2014-03-03'), birth_place: "Gdańsk", pesel: "34567890123", date_of_admission: new Date('2022-03-03'), court_decision: "Decyzja Sądu", address: { id: 5, country: "Polska", city: "Gdańsk", street: "Ulica", postal_code: "80-001", apartment_number: 5, is_registered: true }, address_registered: { id: 6, country: "Polska", city: "Gdańsk", street: "Inna Ulica", postal_code: "80-002", apartment_number: 6, is_registered: true }, mother: { id: 5, name: "Magdalena", surname: "Wiśniewska", role: "Matka" }, father: { id: 6, name: "Tomasz", surname: "Wiśniewski", role: "Ojciec" }, foster_carer: 3, note: 3 },
        { id: 4, name: "Marcin", surname: "Lewandowski", birth_date: new Date('2011-04-04'), birth_place: "Poznań", pesel: "45678901234", date_of_admission: new Date('2019-04-04'), court_decision: "Decyzja Sądu", address: { id: 7, country: "Polska", city: "Poznań", street: "Główna", postal_code: "61-001", apartment_number: 7, is_registered: true }, address_registered: { id: 8, country: "Polska", city: "Poznań", street: "Pomocnicza", postal_code: "61-002", apartment_number: 8, is_registered: true }, mother: { id: 7, name: "Monika", surname: "Lewandowska", role: "Matka" }, father: { id: 8, name: "Robert", surname: "Lewandowski", role: "Ojciec" }, foster_carer: 4, note: 2 },
        { id: 5, name: "Zofia", surname: "Kwiatkowska", birth_date: new Date('2013-05-05'), birth_place: "Łódź", pesel: "56789012345", date_of_admission: new Date('2020-05-05'), court_decision: "Decyzja Sądu", address: { id: 9, country: "Polska", city: "Łódź", street: "Słoneczna", postal_code: "90-001", apartment_number: 9, is_registered: true }, address_registered: { id: 10, country: "Polska", city: "Łódź", street: "Księżycowa", postal_code: "90-002", apartment_number: 10, is_registered: true }, mother: { id: 9, name: "Karolina", surname: "Kwiatkowska", role: "Matka" }, father: { id: 10, name: "Marek", surname: "Kwiatkowski", role: "Ojciec" }, foster_carer: 5, note: 4 },
        { id: 6, name: "Kamil", surname: "Zieliński", birth_date: new Date('2015-06-06'), birth_place: "Wrocław", pesel: "67890123456", date_of_admission: new Date('2021-06-06'), court_decision: "Decyzja Sądu", address: { id: 11, country: "Polska", city: "Wrocław", street: "Długa", postal_code: "50-001", apartment_number: 11, is_registered: true }, address_registered: { id: 12, country: "Polska", city: "Wrocław", street: "Krótka", postal_code: "50-002", apartment_number: 12, is_registered: true }, mother: { id: 11, name: "Ewa", surname: "Zielińska", role: "Matka" }, father: { id: 12, name: "Paweł", surname: "Zieliński", role: "Ojciec" }, foster_carer: 6, note: 5 },
        { id: 7, name: "Katarzyna", surname: "Piotrowska", birth_date: new Date('2009-07-07'), birth_place: "Gdynia", pesel: "78901234567", date_of_admission: new Date('2018-07-07'), court_decision: "Decyzja Sądu", address: { id: 13, country: "Polska", city: "Gdynia", street: "Morawska", postal_code: "81-001", apartment_number: 13, is_registered: true }, address_registered: { id: 14, country: "Polska", city: "Gdynia", street: "Bałtycka", postal_code: "81-002", apartment_number: 14, is_registered: true }, mother: { id: 13, name: "Alicja", surname: "Piotrowska", role: "Matka" }, father: { id: 14, name: "Grzegorz", surname: "Piotrowski", role: "Ojciec" }, foster_carer: 7, note: 3 },
        { id: 8, name: "Kamil", surname: "Zieliński", birth_date: new Date('2015-06-06'), birth_place: "Wrocław", pesel: "67890123456", date_of_admission: new Date('2021-06-06'), court_decision: "Decyzja Sądu", address: { id: 11, country: "Polska", city: "Wrocław", street: "Długa", postal_code: "50-001", apartment_number: 11, is_registered: true }, address_registered: { id: 12, country: "Polska", city: "Wrocław", street: "Krótka", postal_code: "50-002", apartment_number: 12, is_registered: true }, mother: { id: 11, name: "Ewa", surname: "Zielińska", role: "Matka" }, father: { id: 12, name: "Paweł", surname: "Zieliński", role: "Ojciec" }, foster_carer: 8, note: 5 },
        { id: 9, name: "Katarzyna", surname: "Piotrowska", birth_date: new Date('2009-07-07'), birth_place: "Gdynia", pesel: "78901234567", date_of_admission: new Date('2018-07-07'), court_decision: "Decyzja Sądu", address: { id: 13, country: "Polska", city: "Gdynia", street: "Morawska", postal_code: "81-001", apartment_number: 13, is_registered: true }, address_registered: { id: 14, country: "Polska", city: "Gdynia", street: "Bałtycka", postal_code: "81-002", apartment_number: 14, is_registered: true }, mother: { id: 13, name: "Alicja", surname: "Piotrowska", role: "Matka" }, father: { id: 14, name: "Grzegorz", surname: "Piotrowski", role: "Ojciec" }, foster_carer: 9, note: 3 },
        { id: 10, name: "Kamil", surname: "Zieliński", birth_date: new Date('2015-06-06'), birth_place: "Wrocław", pesel: "67890123456", date_of_admission: new Date('2021-06-06'), court_decision: "Decyzja Sądu", address: { id: 11, country: "Polska", city: "Wrocław", street: "Długa", postal_code: "50-001", apartment_number: 11, is_registered: true }, address_registered: { id: 12, country: "Polska", city: "Wrocław", street: "Krótka", postal_code: "50-002", apartment_number: 12, is_registered: true }, mother: { id: 11, name: "Ewa", surname: "Zielińska", role: "Matka" }, father: { id: 12, name: "Paweł", surname: "Zieliński", role: "Ojciec" }, foster_carer: 10, note: 5 },
        { id: 11, name: "Katarzyna", surname: "Piotrowska", birth_date: new Date('2009-07-07'), birth_place: "Gdynia", pesel: "78901234567", date_of_admission: new Date('2018-07-07'), court_decision: "Decyzja Sądu", address: { id: 13, country: "Polska", city: "Gdynia", street: "Morawska", postal_code: "81-001", apartment_number: 13, is_registered: true }, address_registered: { id: 14, country: "Polska", city: "Gdynia", street: "Bałtycka", postal_code: "81-002", apartment_number: 14, is_registered: true }, mother: { id: 13, name: "Alicja", surname: "Piotrowska", role: "Matka" }, father: { id: 14, name: "Grzegorz", surname: "Piotrowski", role: "Ojciec" }, foster_carer: 11, note: 3 },
        { id: 12, name: "Michał", surname: "Nowakowski", birth_date: new Date('2008-08-08'), birth_place: "Szczecin", pesel: "89012345678", date_of_admission: new Date('2017-08-08'), court_decision: "Decyzja Sądu", address: { id: 15, country: "Polska", city: "Szczecin", street: "Wiejska", postal_code: "70-001", apartment_number: 15, is_registered: true }, address_registered: { id: 16, country: "Polska", city: "Szczecin", street: "Miejska", postal_code: "70-002", apartment_number: 16, is_registered: true }, mother: { id: 15, name: "Magdalena", surname: "Nowakowska", role: "Matka" }, father: { id: 16, name: "Mariusz", surname: "Nowakowski", role: "Ojciec" }, foster_carer: 12, note: 4 }
    ];



    return (
        <div className="app-page manage-child-page">
            <Rectangle links={links}>
                <div className='manageChild'>
                    <ChildTable children={children} />
                </div>
            </Rectangle>
        </div>
    );
} 
export default ManageChild;