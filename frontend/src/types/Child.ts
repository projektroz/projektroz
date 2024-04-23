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
        country: string;
        city: string;
        street: string;
        postal_code: string;
        apartment_number: number;
        is_registered: boolean;
    };
	address_registered: {
        id: number;
        country: string;
        city: string;
        street: string;
        postal_code: string;
        apartment_number: number;
        is_registered: boolean;
    };
	mother: {
        id: number;
        name: string;
        surname: string;
        role: string;
    };
	father: {
        id: number;
        name: string;
        surname: string;
        role: string;
    };
	foster_carer: number; //coś jest nie tak z tym polem, powinno być zwracane jako obiekt a nie id
	note: number;
}

export default Child;