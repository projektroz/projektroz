function remapFormData(formData: any) {
  return {
    name: formData.name || "",
    surname: formData.surname || "",
    birth_date: formData.birthDate || "",
    birth_place: formData.birthPlace || "",
    pesel: formData.pesel || "",
    date_of_admission: formData.admissionDate || "",
    court_decision: formData.courtDecision || "",
    AddressRegistered: {
      country: formData.addressRegisteredCountry || "",
      city: formData.addressRegisteredCity || "",
      street: formData.addressRegisteredStreet || "",
      postal_code: formData.addressRegisteredPostalCode || "",
      apartment_number: formData.addressRegisteredHouseNumber || "",
    },
    Address: {
      country: formData.addressCurrentCountry || "",
      city: formData.addressCurrentCity || "",
      street: formData.addressCurrentStreet || "",
      postal_code: formData.addressCurrentPostalCode || "",
      apartment_number: formData.addressCurrentHouseNumber || "",
    },
    Mother: {
      name: formData.motherName || "",
      surname: formData.motherSurname || "",
    },
    Father: {
      name: formData.fatherName || "",
      surname: formData.fatherSurname || "",
    },
  };
}

export { remapFormData };