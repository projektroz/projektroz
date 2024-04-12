// api/addChild.ts
import { api } from './axios';


type AddChildResponse = {
	id: number;
	name: string;
	surname: string;
	birth_date: Date;
	birth_place: string;
	pesel: string;
	date_of_admission: Date;
	court_decision: string;
	address: number;
	address_registered: number;
	mother: number;
	father: number;
	foster_carer: number;
	note: string;
}

type AddParentResponse = {
	id: number;
	name: string;
	surname: string;
	child_id: number;
}

export async function addChild(childData: any): Promise<AddChildResponse> {
	try {
		const response = await api.post('children/', childData);
		return response.data;
	} catch (error: any) {
		throw new Error(error.response.data.detail);
	}
}

export async function addMother(motherData: any): Promise<AddParentResponse> {
	try {
		const response = await api.post('mother/', motherData);
		return response.data;
	
	} catch (error: any) {
		throw new Error(error.response.data.detail);
	}
}

export async function addFather(fatherData: any): Promise<AddParentResponse> {
	try{
		const response = await api.post('father/', fatherData);
		return response.data;
	} catch (error: any) {
		throw new Error(error.response.data.detail);
	}
}



