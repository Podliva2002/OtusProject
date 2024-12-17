<template>
    <div class="login" v-if="!user.isLoggedIn">
    <h2 v-if="!user.isLoggedIn">Вход в систему</h2>
    <form v-if="!user.isLoggedIn" @submit.prevent="login" class="login-form">
      <div class="form-group">
        <input
          id="username"
          type="text"
          v-model="username"
          required
          class="form-input"
          placeholder="Логин"
        />
      </div>
      <div class="form-group">
        <input
          id="password"
          type="password"
          v-model="password"
          required
          class="form-input"
          placeholder="Пароль"
        />
      </div>
      <p v-if="user.message" class="error-message">{{ user.message }}</p>
      <button type="submit" class="submit-button">Войти</button>
      <div class="create-account">
        <RouterLink to="/register">Нет аккаунта? Зарегистрируйтесь</RouterLink>
      </div>
    </form>
  </div>
  <div v-else>Вы уже вошли</div>
</template>

<script>
import { userAccount } from '../../stores/user';
import { ref } from 'vue';

export default {
    setup () {
        const user = userAccount();
        const username = ref('')
        const password = ref('')

        const login = async () => {
            await user.login(username.value, password.value);
        };
        

        return {
            user,
            username,
            password,
            login,
        }
    }
}
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.form-group {
    display: block;
    
}
input {
  font-family: inherit; /* 1 */
  font-size: inherit; /* 1 */
  line-height: inherit; /* 1 */
  margin-bottom: 20px;
  padding: 10px; /* 2 */
  border: 1; /* 3 */
  border-radius: 4px; /* 3 */
  outline: none; /* 4 */
}
h2 {
    margin-bottom: 30px;
    color: rgb(0, 0, 0);
}

.submit-button {background-image: linear-gradient(to right, #FF512F 0%, #F09819  51%, #FF512F  100%)}
    .submit-button {
    margin: 10px;

    text-transform: uppercase;
    transition: 0.5s;
    background-size: 200% auto;
    color: white;            
    box-shadow: 0 0 20px #eee;
    border-radius: 10px;

    }

    .submit-button:hover {
    background-position: right center;
    color: #fff;
    text-decoration: none;
    }

.error-message {

    margin-top: 10px;
    font-size: 20px;
}
         
</style>