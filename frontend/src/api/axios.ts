import axios, { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios';

interface CustomAxiosRequestConfig extends AxiosRequestConfig {
    _retry?: boolean;  // Optional boolean property
}

const login = axios.create({
    baseURL: 'http://localhost:8000/login',
    headers: {
        'Content-Type': 'application/json',
    } 
});

const register = axios.create({
    baseURL: 'http://localhost:8000/register',
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
const upload = axios.create({
    baseURL: 'http://localhost:8000/upload',
    headers: {
        'Content-Type': 'multipart/form-data',
    }
});


const addInterceptors = (instance: any) => {
    instance.interceptors.request.use(
        (config: any) => {
            const token = localStorage.getItem('access_token');
            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`;
            }
            return config;
        },
        (error: AxiosError): Promise<AxiosError> => Promise.reject(error)
    );

    instance.interceptors.response.use(
        (response: AxiosResponse) => response,
        async (error: AxiosError) => {
            const originalRequest = error.config as CustomAxiosRequestConfig;
        
            if (originalRequest == undefined) return Promise.reject(error);
            
            if (error.response && error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                
                try {
                    const refreshToken = localStorage.getItem('refresh_token');
                    
                    const response = await refresh.post('/', { 'refresh': refreshToken });
                    
                    const { access } = response.data;
        
                    localStorage.setItem('access_token', access);
                    originalRequest.headers = originalRequest.headers || {};
                    originalRequest.headers['Authorization'] = `Bearer ${access}`;
                    
                    return instance(originalRequest); 
                } catch (refreshError: unknown) {
                    
                    if (refreshError instanceof AxiosError && refreshError.response) {
                        
                        if ([401, 403, 406].includes(refreshError.response.status)) {
                            window.location.href = '/login';
                        } else {
                            console.error("Nie udało się odświeżyć tokena z innego powodu", refreshError);
                        }
                    } else {
                        console.error("Unhandled error type during token refresh", refreshError);
                    }
                }
            }

            return Promise.reject(error);
        }
    );
};

addInterceptors(api);
addInterceptors(upload);


export { api, login, refresh, register, upload };