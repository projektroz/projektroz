import axios from 'axios';

const login = axios.create({
    baseURL: 'http://localhost:8000/login',
    headers: {
        'Content-Type': 'application/json',
    } 
});

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    } 
});

const refresh = axios.create({
    baseURL: 'http://localhost:8000/refresh',
    headers: {
        'Content-Type': 'application/json',
    }
});


api.interceptors.request.use(
    (config: any) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config
    },
    (error: any) => Promise.reject(error)
);

api.interceptors.response.use(
    (response: any) => response,
    async (error: any) => {
        const originalRequest = error.config;
        
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
               
            try {
                const refreshToken = localStorage.getItem('refresh_token');
                const response = await refresh.post('/', { 'refresh': refreshToken });
                const { access } = response.data;

                originalRequest.headers.Authorization = `Bearer ${access}`;
                return api(originalRequest); 
            } catch (refreshError: any) {
                
                if (refreshError.response && (refreshError.response.status === 401 || refreshError.response.status === 403 || refreshError.response.status === 406)) {
                    window.location.href = '/login'; 
                } else {
                    
                    console.error("Nie udało się odświeżyć tokena z innego powodu", refreshError);
                }
            }
        }

        return Promise.reject(error);
    }
);

export { api, login, refresh };