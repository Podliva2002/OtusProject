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
        addbasket: [],
        message: '',
    }),
    actions: {
        async fetchData(page=1) {
            try {
                const response = await axios.get(`http://localhost:8000/api/products/products/`, {
                    params: {
                        page,
                        limit: this.itemsPerPage,
                        ...this.filters,
                    }
                });
                this.products = response.data.results;
                this.totalPages = Math.ceil(response.data.count / this.itemsPerPage);
                console.log("Успех в получении данных");
                const count = this.querysetCount;
                console.log('Текущий счетчик выборки:', count);
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении данных:", err);
            }
        },
        async fetchDetailProduct(productId) {
            try {
                const response = await axios.get(`http://localhost:8000/api/products/products/${productId}/`);
                this.productDetails = response.data;
                console.log("Успех в получении детальной информации о товаре");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении детальной информации о товаре:", err);
            }   
        },
        async fetchCategories() {
            try {
                const response = await axios.get('http://localhost:8000/api/products/categories/');
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
            this.fetchData(this.currentPage);
        },
        setFilters(filters) {
            this.filters = {
                ...this.filters,
                ...Object.fromEntries(Object.entries(filters).filter(([_, v]) => v != null && v !== ''))
            };
            if (this.querysetCount > 0 && this.totalPages >= this.currentPage) {
                this.fetchData(this.currentPage);
            } else {
                this.currentPage = 1
                this.fetchData(this.currentPage);
            }
        },
        clearFilters() {
            this.filters = {};
            this.currentPage = 1;
            this.fetchData(this.currentPage);
            window.location.reload();
        },
        async fetchAddBasket(user, product) {
            try {
                const response = await axios.post(`http://localhost:8000/api/products/baskets/`, {
                    user,
                    product,
                    quantity : 1,
                });    
                console.log("Успех добавления товара в корзину");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при добавлении товара в корзину:", err);
                this.message = 'Авторизирутесь для возможности добавления товара в корзину'
            }
        },
        async getMyBasket(userId){
            try {
                const response = await axios.get(`http://localhost:8000/api/products/basket/${userId}`);
                this.addbasket = response.data;
                console.log("Успех получения списка товаров в корзине");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при получении списка товаров в корзине:", err);
            }
        },
        async changeQuantity(productId, quantity) {
            try {
                const response = await axios.patch(`http://localhost:8000/api/products/baskets/${productId}/`, {
                    quantity,
                });
                console.log("Успех изменения количества товара в корзине");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при изменении количества товара в корзине:", err);
            }
        },
        async deleteNoteBasket(productId, userId) {
            try {
                const response = await axios.delete(`http://localhost:8000/api/products/baskets/${productId}/`);
                await this.getMyBasket(userId);
                console.log("Успех удаления товара из корзины");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при удалении товара из корзины:", err);
            }
        },
        async increment(productId, userId) {
            const product = this.addbasket.find(item => item.id === productId);
            if (product) {
                product.quantity++;
                await this.changeQuantity(productId, product.quantity);
                await this.getMyBasket(userId);
            }
        },
        
        async decrement(productId, userId) {
            const product = this.addbasket.find(item => item.id === productId);
            if (product && product.quantity > 1) {
                product.quantity--;
                await this.changeQuantity(productId, product.quantity)
                await this.getMyBasket(userId);
            }
        },
        async addOrder(first_name, last_name, email, addres, basket, userId) {
            try {
                const response = await axios.post(`http://localhost:8000/api/products/orders/`, {
                    first_name,
                    last_name,
                    email,
                    addres,
                    basket,
                    userId,
                });
                console.log("Успех оформления заказа");
            } catch (err) {
                this.error = err;
                console.error("Ошибка при оформлении заказа:", err);
            }

        }

    },
    getters: {
        querysetCount(state) {
            const count = state.products.length;
            return count
        },
        getBasketSum(state) {
            return state.addbasket.reduce((total, item) => {
                return total + (item.total_sum || 0); // Add total_sum of each item
            }, 0);
        },
    },
});
