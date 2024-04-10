// api/addChild.ts
type AddChildResponse = {
  id: number;
  name: string;
  surname: string;
}

export async function addChild(name: string, surname: string, birthDate?: Date): Promise<AddChildResponse> {
    const response = await fetch('http://localhost:8000/children/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'authorization': `Bearer ${localStorage.getItem('access_token')}`,
        },
        body: JSON.stringify({ name, surname }),
    });

    if(!response.ok) {
        throw new Error("Nie udało się dodać dziecka");
    }

    return response.json();
}
