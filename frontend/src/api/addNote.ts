import { api } from "./axios";

export async function addNote(data: any) {
    console.log(JSON.stringify(data));
    const response = await api.post("/api/notes/", data);
    return response;
}
