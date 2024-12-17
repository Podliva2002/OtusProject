<template>
    <div class="container">
        <div class="profile" v-if="user.isLoggedIn">
            <RouterLink to="/profile">Профиль</RouterLink>
            <RouterLink to="/basket">Корзина</RouterLink>
            <a href="#" @click="user.logout()">Выйти</a>
        </div>
        <div class="content">
            <RouterView></RouterView>
            <div v-if="$route.path === '/profile'" class="my-profile">
                <form @submit.prevent="user.updateUserInfo(user.user.last_name, user.user.first_name, user.user.email, user.user.id, password)">
                <div class="common-info">
                    <div class="full-name">
                        <p>
                            <label for="last_name">Фамилия: </label>
                            <input type="text" id="last_name" v-model="user.user.last_name">
                        </p>
                        <p>
                            <label for="first_name">Имя: </label>
                            <input type="text" id="first_name" v-model="user.user.first_name">
                        </p>
                        <p>
                            <label for="email">Email: </label>
                            <input type="email" id="email" v-model="user.user.email">
                        </p>
                    </div>
                    <div class="form-group">
                        <label for="password">Новый пароль:  </label>
                        <input
                        id="password"
                        type="password"
                        v-model="password"
                        class="form-input"
                        placeholder="Пароль"
                        />
                    </div>
                </div>
                <p v-if="user.message" class="error-message">{{ user.message }}</p>
                <div class="buttons">
                    <button type="submit">Сохранить</button>
                </div>
                </form>
            </div>
        </div>
    </div>
    
</template>

<script>
import { ref } from 'vue';
import { userAccount } from '../../stores/user';
import { RouterView } from 'vue-router';
export default {
    setup () {
        const user = userAccount();
        const password = ref('')
        

        return {
            user,
            password
        }
    }
}
</script>

<style scoped>
.container {
    display: flex; /* Используем Flexbox для расположения элементов */
}

.profile {
    width: 200px; /* Ширина меню */
    height: 132px;
    padding: 10px;
    background-color: #f0f0f0; /* Цвет фона для меню */
    border-right: 1px solid #ccc; /* Разделительная линия */
}

.profile a {
    display: block; /* Делаем ссылки блочными элементами */
    padding: 10px; /* Отступы для ссылок */
    text-decoration: none; /* Убираем подчеркивание */
    color: #333; /* Цвет текста */
}

.profile a:hover {
    background-color: #e0e0e0; /* Цвет фона при наведении */
}

.content {
    flex: 1; /* Занимает оставшееся пространство */
    margin-left: 20px;
}
.full-name {
    display: flex; /* Включаем Flexbox */
    justify-content: center; /* Центрируем элементы по горизонтали */
}
p {
    margin: 5px;
}
.buttons {
    display: flex;
    justify-content: right;
}
.form-group {
    display: flex;
    justify-content: center;
}
</style>