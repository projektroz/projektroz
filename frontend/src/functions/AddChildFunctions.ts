function getChildData(formData: any) {
	return {
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
		},
		address: {
			country: formData.addressCurrentCountry || "",
			city: formData.addressCurrentCity || "",
			street: formData.addressCurrentStreet || "",
			postal_code: formData.addressCurrentPostalCode || "",
			apartment_number: formData.addressCurrentHouseNumber || "",
		},
		mother: {
			name: formData.motherName || "",
			surname: formData.motherSurname || "",
		},
		father: {
			name: formData.fatherName || "",
			surname: formData.fatherSurname || "",
		},
	}
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
        name: childData.name || "",
        surname: childData.surname || "",
        birthDate: childData.birth_date || Date.now(),
        birthPlace: childData.birth_place || "",
        pesel: childData.pesel || 0,
        admissionDate: childData.date_of_admission || Date.now(),
        courtDecision: childData.court_decision || "",
        addressRegisteredCountry: childData.address_registered?.country || "",
        addressRegisteredCity: childData.address_registered?.city || "",
        addressRegisteredStreet: childData.address_registered?.street || "",
        addressRegisteredPostalCode: childData.address_registered?.postal_code || "",
        addressRegisteredHouseNumber: childData.address_registered?.apartment_number || 0,
        addressCurrentCountry: childData.address?.country || "",
        addressCurrentCity: childData.address?.city || "",
        addressCurrentStreet: childData.address?.street || "", 
        addressCurrentPostalCode: childData.address?.postal_code || "",
        addressCurrentHouseNumber: childData.address?.apartment_number || 0,
        motherName: childData.mother?.name || "",
        motherSurname: childData.mother?.surname || "",
        fatherName: childData.father?.name || "",
        fatherSurname: childData.father?.surname || "",
    };
}

function getDefaultFormData() {
    return {
        name: "",
        surname: "",
        birthDate: Date.now(),
        birthPlace: "",
        pesel: 0,
        admissionDate: Date.now(),
        courtDecision: "",
        addressRegisteredCountry: "",
        addressRegisteredCity: "",
        addressRegisteredStreet: "",
        addressRegisteredPostalCode: "",
        addressRegisteredHouseNumber: 0,
        addressCurrentCountry: "",
        addressCurrentCity: "",
        addressCurrentStreet: "", 
        addressCurrentPostalCode: "",
        addressCurrentHouseNumber: 0,
        motherName: "",
        motherSurname: "",
        fatherName: "",
        fatherSurname: "",
    };
}
export { getChildData, parseBackToFormData };