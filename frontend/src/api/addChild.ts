// api/addChild.ts
import { api } from './axios';
type AddChildResponse = {
  id: number;
  name: string;
  surname: string;
}
// name: string, surname: string, birthDate?: Date
export async function addChild(): Promise<AddChildResponse> {
    
    const response = api.post('children/');

    return response.data;
}
// id: Number;
//     name: String;
//     surname: String;
//     birth_date: Date;
//     birth_place: String;
//     pesel: String;
//     date_of_admission: Date;
//     court_decision: String;
//     address: Number;
//     address_registered: Number;
//     mother: Number;
//     father: Number;
//     foster_carer: Number;
//     note: String;