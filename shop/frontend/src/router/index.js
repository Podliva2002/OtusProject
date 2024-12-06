import { createRouter, createWebHistory } from 'vue-router';
import FirstPage from '../components/StartingPage.vue';
import Washing from '../components/Washing.vue';
import Rental from '../components/Rental.vue';
import Catalog from '../components/Catalog.vue';
import ProductDetail from '../components/ProductDetail.vue';

const routes = [
    { path: '/', component: FirstPage},
    { path: '/washing', component: Washing},
    {    
        path: '/rental/:rentalType',
        name: 'Rental',
        component: Rental
    },
    { path: '/catalog', component: Catalog},
    { 
        path: '/productDetail/:id', 
        name: 'ProductDetail',
        component: ProductDetail 
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;