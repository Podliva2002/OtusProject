<template>
    <div class="product-container">
      <h1 class="product-title">{{ product.productDetails.name }}</h1>
      <img :src="product.productDetails.image" alt="Product Image" class="product-image">
      <p class="product-price">Цена: {{ product.productDetails.price }} руб</p>
      <div class="category">
        <h2>Категории:</h2>
        <ul>
          <li v-for="a in product.productDetails.category" :key="a.id" class="category-item">
            {{ a.name }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import { userProduct } from '../../stores/product';
  
  export default {
    setup() {
      const product = userProduct();
      const route = useRoute();
      const productId = route.params.id;
  
      onMounted(async () => {
        product.fetchDetailProduct(productId);
      });
  
      return {
        product,
      };
    },
  };
  </script>
  
  <style scoped>
  .product-container {
    max-width: 600px; /* Максимальная ширина контейнера */
    margin: 20px auto; /* Центрирование контейнера */
    padding: 20px; /* Отступы внутри контейнера */
    border: 1px solid #ddd; /* Рамка вокруг контейнера */
    border-radius: 10px; /* Закругленные углы */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Тень для контейнера */
    background-color: #fff; /* Цвет фона контейнера */
  }
  
  .product-title {
    font-size: 24px; /* Размер шрифта заголовка */
    margin-bottom: 10px; /* Отступ снизу */
    color: #333; /* Цвет текста заголовка */
  }
  
  .product-image {
    max-width: 50%; /* Максимальная ширина изображения */
    height: auto; /* Автоматическая высота */
    display: block; /* Блочный элемент */
    margin: 0 auto; /* Центрирование изображения */
    padding: 10px; /* Отступы вокруг изображения */
    border: 1px solid #ccc; /* Рамка вокруг изображения */
    border-radius: 5px; /* Закругленные углы */
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); /* Тень для изображения */
  }
  
  .product-price {
    font-size: 20px; /* Размер шрифта для цены */
    color: black; /* Цвет текста для цены */
    margin: 10px 0; /* Отступы сверху и снизу */
  }
  
  .category {
    margin-top: 20px; /* Отступ сверху для категории */
  }
  
  .category ul {
    list-style-type: none; /* Убираем маркеры списка */
    padding: 0; /* Убираем отступы */
  }
  
  .category-item {
    background-color: #f0f0f0; /* Цвет фона для элементов списка */
    border: 1px solid #ccc; /* Рамка вокруг элементов */
    border-radius: 5px; /* Закругленные углы */
    padding: 10px; /* Отступы внутри элементов */
    margin: 5px 0; /* Отступы между элементами */
    transition: background-color 0.3s; /* Плавный переход цвета фона */
    font-size: 16px; /* Размер шрифта для категорий */
  }
  
  .category-item:hover {
    background-color: #e0e0e0; /* Цвет фона при наведении */
  }
  </style>
  