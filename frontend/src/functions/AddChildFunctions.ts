function getChildData(formData: any) {
    return {
        id: formData.id || "",
        name: formData.name || "",
        surname: formData.surname || "",
        birth_date: formData.birthDate || "",
        birth_place: formData.birthPlace || "",
        pesel: formData.pesel || "",
        date_of_admission: formData.admissionDate || "",
        court_decision: formData.courtDecision || "",
        address_registered: {
            country: formData.addressRegisteredCountry || "",
            city: formData.addressRegisteredCity || "",
            street: formData.addressRegisteredStreet || "",
            postal_code: formData.addressRegisteredPostalCode || "",
            apartment_number: formData.addressRegisteredHouseNumber || "",
            is_registered: true,
        },
        address: {
            country: formData.addressCurrentCountry || "",
            city: formData.addressCurrentCity || "",
            street: formData.addressCurrentStreet || "",
            postal_code: formData.addressCurrentPostalCode || "",
            apartment_number: formData.addressCurrentHouseNumber || "",
            is_registered: false,
        },
        mother: {
            name: formData.motherName || "",
            surname: formData.motherSurname || "",
            role: "M",
        },
        father: {
            name: formData.fatherName || "",
            surname: formData.fatherSurname || "",
            role: "F",
        },
        note: formData.note || 1  // Assuming a default note ID, adjust as necessary
    };
};

function parseBackToFormData(childDataString: string) {
    let childData = null;
    try {
        childData = JSON.parse(childDataString);
    } catch (error) {
        console.error('Error parsing childData:', error);
        return getDefaultFormData(); 
    }

    if (!childData) {
        console.error('No valid child data available');
        return getDefaultFormData();
    }

    return {
        id: childData.id || "",
        name: childData.name || "",
        surname: childData.surname || "",
        birthDate: childData.birth_date || "",
        birthPlace: childData.birth_place || "",
        pesel: childData.pesel || "",
        admissionDate: childData.date_of_admission || "",
        courtDecision: childData.court_decision || "",
        addressRegisteredCountry: childData.address_registered?.country || "",
        addressRegisteredCity: childData.address_registered?.city || "",
        addressRegisteredStreet: childData.address_registered?.street || "",
        addressRegisteredPostalCode: childData.address_registered?.postal_code || "",
        addressRegisteredHouseNumber: childData.address_registered?.apartment_number || "",
        addressCurrentCountry: childData.address?.country || "",
        addressCurrentCity: childData.address?.city || "",
        addressCurrentStreet: childData.address?.street || "", 
        addressCurrentPostalCode: childData.address?.postal_code || "",
        addressCurrentHouseNumber: childData.address?.apartment_number || "",
        motherName: childData.mother?.name || "",
        motherSurname: childData.mother?.surname || "",
        fatherName: childData.father?.name || "",
        fatherSurname: childData.father?.surname || "",
        note: childData.note || 1  // Assuming a default note ID, adjust as necessary
    };
}

function getDefaultFormData() {
    return {
        id: "",
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
        note: 1  // Assuming a default note ID, adjust as necessary
    };
}

export { getChildData, parseBackToFormData };
