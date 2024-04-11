// api/auth.ts
import { login } from './axios';
type LoginResponse = {
    access: string;
    refresh: string;
  }
  
  export async function loginRequest(username: string, password: string): Promise<LoginResponse> {
      const response = await login.post('/', {"username": username, "password": password});
      
      return response.data; 
  }
  