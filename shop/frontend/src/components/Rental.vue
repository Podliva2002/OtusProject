// В вашем компоненте RentalPage.vue
<template>
    <div>
        <h1>{{rental.rentals}}</h1>
        <div class="image">
            <div v-if="rental.rentals === 'Прокат сноубордов'">
                <img src="https://gravity-shop.ru/wp-content/uploads/2024/02/prokat_snowborda_2024-300x300.jpg" alt="Snoubord rental">
                <img src="https://gravity-shop.ru/wp-content/uploads/2024/02/prokat_snowborda_s_krepleniem_2024-300x300.jpg" alt="Snoubord rental">
                <img src="https://gravity-shop.ru/wp-content/uploads/2024/02/prokat_botinok_2024-300x300.jpg" alt="Snoubord rental">
                <div class="descript">
                    <p>
                        В прокат можно взять горнолыжную мааску (очки) - 200 руб.за сутки
                        <br>
                        * стоимость проката в праздничные дни аналогична прокату в выходные
                        <br>
                        * для получения в аренду инвентаря необходим паспорт или другое удостоверение личности.
                        <br>
                        Документ можно заменить денежным залогом.
                    </p>
                </div>
            </div>
            <div v-if="rental.rentals === 'Прокат тюбингов'">
                <img src="https://gravity-shop.ru/wp-content/uploads/2024/02/prokat_tubinga_2024-300x131.jpg">
                <div class="descript">
                    <p>
                        Для получения в аренду тюбинга необходим паспорт или другое удостоверение личности.
                        <br>
                        Документ можно заменить денежным залогом.
                    </p>
                </div>
            </div>
            <div v-if="rental.rentals === 'Прокат велосипедов'">
                <img src="https://gravity-shop.ru/wp-content/uploads/2024/07/prokat_velo_24-300x300.jpg">
                <div class="descript">
                    <p>
                        Для получения в аренду велосипеда необходим паспорт или другое удостоверение личности.
                        <br>
                        Документ можно заменить денежным залогом.
                    </p>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
import { userRental } from '../stores/rental';
export default {
    name: 'RentalPage',
    setup() {
        const rental = userRental()
        return {
            rental,
        };
    },
};
</script>

<style scoped>
h1 {
    font-size: 40px;
}
.image {
    display: flex;
    justify-content: center;
}
.descript {

    
    text-align: left;
    
    
}
</style>