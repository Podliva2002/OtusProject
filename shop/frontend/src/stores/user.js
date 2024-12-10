import { defineStore } from "pinia";
import axios from 'axios';

export const userAccount = defineStore("user",{
    state: () => ({
        user: localStorage.getItem("user") || {},
        isLoggedIn: !!localStorage.getItem('token'),
        token: localStorage.getItem("token"),
        message: '',
    }),
    actions: {
        async login(username, password) {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api-token-auth/', {
                    username,
                    password
                });
                this.token = response.data.token;
                localStorage.setItem("token", this.token);
                this.isLoggedIn = true;
                await this.fetchCurrentUser();
                this.message = 'Вы вошли!';
            } catch (error) {
                console.error("Ошибка входа:", error.response ? error.response.data : error.message);
                this.message = 'Ошибка входа: ' + (error.response.data.non_field_errors ? error.response.data.non_field_errors[0] : error.message);
            }
        },
        logout() {
            this.clearToken();
            this.message = 'Вы вышли!';
        },
        clearToken() {
            this.token = null;
            this.isLoggedIn = false;
            localStorage.removeItem("token");
            this.user = {};
        },
        async fetchCurrentUser() {
            const headers = {
                'Authorization': `Token ${this.token}`, // Используем токен для авторизации
            };

            try {
                const response = await axios.get('http://127.0.0.1:8000/api/user/current-user/', { headers });
                this.user = response.data;
                localStorage.setItem("user", this.user);
            } catch (error) {
                console.error("Ошибка при получении текущего пользователя:", error.response ? error.response.data : error.message);
            }
        },
        async register(last_name, first_name, username, email, password, password_confirmation) {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/user/register/', {
                    last_name,
                    first_name,
                    username,
                    email,
                    password,
                    password_confirmation
                });
                this.message = 'Вы успешно зарегистрировались!';
            } catch (error) {
                const errors = error.response.data;
                console.error('Registration error:', errors);
                this.message = 'Ошибка регистрации: ' + Object.values(errors).flat().join(', ');
            }
            
        }
    },
})