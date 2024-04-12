// api/auth.ts
import { login, register } from './axios';
type LoginResponse = {
    access: string;
    refresh: string;
  }

  type RegisterResponse = {
    id: Number,
    username: String,
    first_name: String,
    last_name: String,
  }
  
  export async function loginRequest(username: string, password: string): Promise<LoginResponse> {
      const response = await login.post('/', {"username": username, "password": password});
      
      return response.data; 
  }

  export async function registerRequest(username: string, name: string, surname: string, email: string, password: string, passwordRepeat: string): Promise<RegisterResponse> {
    const response = await register.post('/', {"username": username, "first_name": name, "last_name": surname, "email": email, "password": password, "passwordRepeat": passwordRepeat});
    console.log(response);

    return response.data;
}
  