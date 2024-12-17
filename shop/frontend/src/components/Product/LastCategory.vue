<template>
    <div class="product-grid">
    <div class="product-card" v-for="a in product.category.filter(item => item.parent_name == category)" :key="a.id">
        <img :src="a.image" class="product-image" alt="Изображение товара">
        <div class="category-title">
            <router-link :to="{ name: 'NewCatalog', params: { idCategory: a.id } }">{{ a.name }}</router-link>  
        </div>
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
      const category = route.params.lastId;
      localStorage.setItem('currentPage', 1)
      product.currentPage = 1;
  
      onMounted(async () => {
        product.fetchCategories();
        console.log(category);
      });
  
      return {
        product,
        category,
      };
    },
  };
  </script>

<style scoped>
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    margin: 20px;
    background-color: #f0f0f0;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

.product-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* Распределяет пространство между элементами */
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s;
    position: relative;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.product-image {
    width: auto;
    height: auto;
    object-fit: cover;
}

.product-title {
    font-size: 1.1em;
    font-weight: 600;
    margin: 15px;
    color: #333;
}
</style>