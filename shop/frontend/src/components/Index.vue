cd <template>
<header>
        <div class="top-header">
            <div class="site-header">
                <router-link to="/">
                    <img class="logo" src="C:\MyFolder\Shop\shop\frontend\src\assets\GRAVITY_shop_logo-2048x164-1.jpg" alt="Logo">
                </router-link>
            </div>
            
            <div class="login">
                <a href="#">Login/Register</a>
            </div>
        </div>
        <div class="navigation">
            <nav class="navigate">
                <div class="menu">
                    <ul>
                        <li><router-link to="/catalog">Каталог</router-link></li>
                        <li><a href="#">Мастерская</a></li>
                        <div class="dropMenu">
                            <li class="addContent">
                                Прокат
                                <div class="subMenu">
                                    <router-link v-for="(a, index) in rental.listRentals" :key="index" :to="'/rental/' + a" @click="rental.changeRental(a)">
                                        {{ a }}
                                    </router-link>

                                </div>
                            </li>
                        </div>
                        <li>
                            <router-link to="/washing" active-class="active">Веломойка</router-link>
                        </li>
                        <li><a href="#">Контакты</a></li>
                    </ul>
                </div>
            </nav>
    </div>
    </header>    
<body>
    <router-view />
</body>

</template>

<script>
import { ref } from 'vue';
import { userRental } from '../stores/rental';

export default {
    name: 'Header',

    setup() {
        const rental = userRental()

        return {
            rental,
        }
    }
    

}

</script>

<style scoped>

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: left;
    width: 100%; /* Убедитесь, что это значение подходит для вашего дизайна */
    margin-bottom: 30px;
}

.logo {
    height: 24px; 
    margin-bottom: 0;
}

.login a {
    text-decoration: none;
    color: #000;
}

.navigate {
    margin-top: 10px; /* Отступ сверху для навигации */
    background-color: black; /* Устанавливаем черный фон */
    padding: 1px; /* Уменьшаем отступы сверху и снизу для навигации */
}

.navigate ul {
    list-style-type: none; /* Убираем маркеры списка */
    padding: 0; /* Убираем отступы */
    display: flex; /* Используем Flexbox для горизонтального расположения */
}

.navigate li {
    margin-right: 20px; /* Уменьшаем отступ между элементами навигации */
    text-decoration: none; /* Убираем подчеркивание у ссылок */
    color: #fff; /* Устанавливаем белый цвет текста для контраста с черным фоном */
}

.navigate a {
    text-decoration: none; /* Убираем подчеркивание у ссылок */
    color: #fff; /* Устанавливаем белый цвет текста для контраста с черным фоном */
    padding: 5px 10px; /* Добавляем отступы внутри ссылок для улучшения кликабельности */
}

.active {
    font-weight: bold;
    font-weight: 2000;
    text-decoration: underline;
}

.dropMenu {
    position: relative; /* Устанавливаем относительное позиционирование для родительского элемента */
}

.subMenu {
    display: none; /* Скрываем подменю по умолчанию */
    position: absolute; /* Устанавливаем абсолютное позиционирование для подменю */
    top: 100%; /* Размещаем подменю под родительским элементом */
    left: 0; /* Выравниваем по левому краю */
    background-color: white; /* Устанавливаем белый фон для подменю */
    border: 1px solid #ccc; /* Добавляем границу */
    z-index: 1000; /* Устанавливаем z-index, чтобы подменю было поверх других элементов */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Добавляем тень для подменю */
}

.dropMenu:hover .subMenu {
    display: block; /* Показываем подменю при наведении на родительский элемент */
}

.subMenu a {
    display: block; /* Делаем ссылки блочными для удобства клика */
    padding: 10px; /* Добавляем отступы для ссылок */
    color: #000; /* Устанавливаем черный цвет текста */
    text-decoration: none; /* Убираем подчеркивание */
}

.subMenu a:hover {
    background-color: #f0f0f0; /* Меняем фон ссылки при наведении */
}

.addContent::after {
    content: "▼";
    margin-right: 0.5em;
}

 
</style>