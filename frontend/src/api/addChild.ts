// api/addChild.ts
import { api } from './axios';
import { remapFormData } from '../functions/FormDataRemap';

type AddChildResponse = {
  id: Number;
  name: String;
  surname: String;
  birth_date: Date;
  birth_place: String;
  pesel: String;
  date_of_admission: Date;
  court_decision: String;
  address: Number;
  address_registered: Number;
  mother: Number;
  father: Number;
  foster_carer: Number;
  note: String;
}

export async function addChild(formData: any): Promise<AddChildResponse> {
  console.log(formData);  
  formData = remapFormData(formData);

    console.log(formData);
    const response = await api.post('children/', formData);
    console.log(response.data[0].name);
    
    return response.data;
}



