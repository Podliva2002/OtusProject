<template>
    <div class="login">
    <h2>Регистрация</h2>
    <form @submit.prevent="registration" class="login-form">
      <div class="form-group">
        <input
          id="last-name"
          type="text"
          v-model="last_name"
          required
          class="form-input"
          placeholder="Фамилия"
        />
      </div>
      <div class="form-group">
        <input
          id="first-name"
          type="text"
          v-model="first_name"
          required
          class="form-input"
          placeholder="Имя"
        />
      </div>
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
          id="email"
          type="email"
          v-model="email"
          required
          class="form-input"
          placeholder="Email"
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
      <div class="form-group">
        <input
          id="password"
          type="password"
          v-model="password_confirmation"
          required
          class="form-input"
          placeholder="Подтвердите пароль"
        />
      </div>
      <p v-if="register.message" class="error-message">{{ register.message }}</p>
      <button type="submit" class="submit-button">Создать</button>
      <div class="create-account">
        <RouterLink to="/login">Уже есть аккаунт? Войти</RouterLink>
      </div>
    </form>
    <!-- <p v-if="user.message" class="error-message">{{ user.message }}</p> -->
  </div>
</template>

<script>
import { ref } from 'vue';
import { userAccount } from '../../stores/user';

export default {
    setup () {
      const register = userAccount();
      const last_name = ref('')
      const first_name = ref('')
      const username = ref('')
      const email = ref('')
      const password = ref('')
      const password_confirmation = ref('')

      const registration = async () => {
        await register.register(last_name.value, first_name.value, username.value, email.value, password.value, password_confirmation.value)
      };
        

        return {
          register,
          last_name,
          first_name,
          username,
          email,
          password,
          password_confirmation,
          registration,
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