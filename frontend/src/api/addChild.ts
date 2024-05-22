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

export async function addChild(childData: any, method: string): Promise<AddChildResponse> {
    const childId = childData.id;
    console.log("Sending data:", childData); // Logowanie danych do wysyłki
    try {
        const response = (method === 'POST' ? 
            await api.post('children/', childData) : 
            await api.put(`children/${childId}/`, childData));

        return response.data;
    } catch (error: any) {
        console.error("Error:", error.response.data); // Logowanie błędu
        throw new Error(error.response.data.detail || "An error occurred while processing your request.");
    }
}
