<template>
    <div v-if="user.isLoggedIn">
        <h2>Корзина</h2>
        <div class="basket">
            <table>
                <thead>
                    <tr>
                        <th> </th>
                        <th> </th>
                        <th>Товар</th>
                        <th>Цена</th>
                        <th>Количество</th>
                        <th>Сумма</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(b, index) in product.addbasket" :key="b.id">
                        <td><button @click="product.deleteNoteBasket(b.id, user.user.id)" class="delete-button" aria-label="Закрыть">×</button></td>
                        <td>
                            <img :src="b.image" alt="Product Image" width="100" height="100" />
                        </td>
                        <td><router-link :to="{ name: 'ProductDetail', params: { id: b.product } }">{{ b.product_name }}</router-link></td>
                        <td>{{ b.cost }} ₽</td>
                        <td>
                            <button @click="product.decrement(b.id, user.user.id)" :disabled="b.quantity <= 1" :class="{ 'disabled-button': b.quantity <= 1 }">-</button>
                                {{ b.quantity }}
                            <button @click="product.increment(b.id, user.user.id)">+</button></td>
                        <td>{{ b.total_sum }} ₽</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="5"></td>
                        <td><strong>Итого: {{ product.getBasketSum }}</strong></td>
                    </tr>
                </tfoot>
            </table>
            <button class="order-button">Создать заказ</button>
            
        </div>
        
    </div>
    <div v-else>
        <h2>Войдите или зарегистрируйтесь, чтобы оформить заказ</h2>
    </div>
</template>

<script>
import { onMounted } from 'vue';
import { userProduct } from '../../stores/product';
import { userAccount } from '../../stores/user';

export default {
    setup() {
        const product = userProduct();
        const user = userAccount();

        onMounted(async () => {
            try {
                await user.fetchCurrentUser();
                await product.getMyBasket(user.user.id);
            } catch (error) {
                console.error("Error fetching user or basket data:", error);
            }
        });

        return {
            product,
            user,
        };
    }
}
</script>

<style scoped>
table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 5px;
    text-align: center;
}

th {
    background-color: #f2f2f2;
}
img {
    max-width: 50%;
    height: auto;
}

button {
    padding: 3px 5px;
    border-width: 1px;
    background-color: #f1f1f5;
    color: black;
    width: 35px;
    height: 30px;
    cursor: pointer;
}

.disabled-button {
    background-color: #ccc;
    color: #666;
    cursor: not-allowed;
    opacity: 0.6;
}
.delete-button {
    background-color: white;
}
.order-button {
    margin: 15px;
    background-color: black;
    color: white;
    border-radius: 10px;
    height: 60px;
    width: 150px;
    float: right;  
}
h2 {  
    margin-top: 0px;
}
</style>
