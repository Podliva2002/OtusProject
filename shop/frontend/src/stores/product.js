import { defineStore } from "pinia";
import axios from 'axios';

export const userProduct = defineStore("product", {
    state: () => ({
        products: [],
        productDetails: [],
        error: null,
        category: [],
        currentPage: 1,
        itemsPerPage: 4,
        totalPages: 0,
        filters: {},
    }),
    actions: {
        async fetchData(page = 1, filters = {}) {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/products/products/`, {
                    params: {
                        page: page,
                        limit: this.itemsPerPage,
                        ...this.filters,
                    }
                });
                this.products = response.data.results;
                this.totalPages = Math.ceil(response.data.count / this.itemsPerPage);
                console.log("Успех в получении данных");
                const count = this.querysetCount; // Получаем значение геттера
                console.log('Текущий счетчик выборки:', count);
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении данных:", err);
            }
        },
        async fetchDetailProduct(productId) {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/products/products/${productId}/`);
                this.productDetails = response.data;
                console.log("Успех в получении детальной информации о товаре");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении детальной информации о товаре:", err);
            }   
        },
        async fetchCategories() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/products/categories/');
                this.category = response.data;
                console.log("Успех в получении категорий");
                const a = this.querysetCount;
                console.log(a);           
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении категорий:", err);
            }
        },
        setPage(page) {
            if (page < 1 || page > this.totalPages) return;
            
            this.currentPage = page;
            this.fetchData(page);
        },
        setFilters(filters) {
            this.filters = {
                ...this.filters,
                ...Object.fromEntries(Object.entries(filters).filter(([_, v]) => v != null && v !== ''))
            };
            this.currentPage = 1;
            this.fetchData(this.currentPage);
        },
        clearFilters() {
            this.filters = {};
            this.currentPage = 1;
            this.fetchData(this.currentPage);
            window.location.reload();
        }
    },
    getters: {
        querysetCount(state) {
            const count = state.products.length;
            return count
        },
    },
});
