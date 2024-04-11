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

        if(error.response.status == 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = localStorage.getItem('refresh_token');
                const response = await refresh.post('/', {'refresh': refreshToken});
                const { token } = response.data;

                localStorage.setItem('access_token', token);

                originalRequest.headers.Authorization = `Bearer ${token}`;
                return axios(originalRequest);
            } catch (error) {
                window.location.href = '/login';
            }
        }

        return Promise.reject(error);
    }
);

export { api, login, refresh };