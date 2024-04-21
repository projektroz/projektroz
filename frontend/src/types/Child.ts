type Child= {
	id: number;
	name: string;
	surname: string;
	birth_date: Date;
	birth_place: string;
	pesel: string;
	date_of_admission: Date;
	court_decision: string;
	address: {
        id: number;
        countty: string;
        city: string;
        street: string;
        postal_code: string;
        apartment_number: number;
    };
	address_registered: {
        id: number;
        countty: string;
        city: string;
        street: string;
        postal_code: string;
        apartment_number: number;
    };
	mother: {
        id: number;
        name: string;
        surname: string;
    };
	father: {
        id: number;
        name: string;
        surname: string;
    };
	foster_carer: number; //coś jest nie tak z tym polem, powinno być zwracane jako obiekt a nie id
	note: number;
}

export default Child;