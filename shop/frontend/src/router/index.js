import { createRouter, createWebHistory } from 'vue-router';
import FirstPage from '../components/StartingPage.vue';
import Washing from '../components/Washing.vue';
import Rental from '../components/Rental.vue';
import ProductDetail from '../components/Product/ProductDetail.vue';
import Category from '../components/Product/Category.vue';
import CategorySub from '../components/Product/CategorySub.vue';
import newCatalog from '../components/Product/newCatalog.vue';
import LastCategory from '../components/Product/LastCategory.vue';
import LoginForm from '../components/UserProfile/LoginForm.vue';
import Register from '../components/UserProfile/Register.vue';
import Profile from '../components/UserProfile/Profile.vue';
import Basket from '../components/UserProfile/Basket.vue';

const routes = [
    { path: '/', component: FirstPage},
    { path: '/washing', component: Washing},
    {    
        path: '/rental/:rentalType',
        name: 'Rental',
        component: Rental
    },
    { path: '/category', component: Category},
    { path: '/category/:id', name: 'CategorySub', component: CategorySub },
    { path: '/category/:id/:lastId', name: 'CategorySubLastId', component: LastCategory},
    { 
        path: '/productDetail/:id', 
        name: 'ProductDetail',
        component: ProductDetail 
    },
    { 
        path: '/newCatalog/:idCategory',
        name: 'NewCatalog',
        component: newCatalog,
    },
    { path: '/login', component: LoginForm },
    { path: '/register', component: Register },
    { 
        path: '/profile',
        component: Profile,
        children: [
            { path: '/', component: Profile},
            { path: '/basket', component: Basket }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;