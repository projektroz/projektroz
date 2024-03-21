// api/auth.ts
type LoginResponse = {
    access: string;
    refresh: string;
  }
  
  export async function login(username: string, password: string): Promise<LoginResponse> {
    const response = await fetch('http://localhost:8000/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
  
    if (!response.ok) {
      throw new Error('Nieprawidłowa nazwa użytkownika lub hasło');
    }
  
    return response.json();
  }
  