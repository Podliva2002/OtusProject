<template>
    <div class="filters">
        <input type="number" v-model="filter.min_price" placeholder="Минимальная цена" class="search-input">
        <input type="number" v-model="filter.max_price" placeholder="Максимальная цена" class="search-input">

        <div>
            <button @click="applyFilters">Применить</button>
            <button @click="product.clearFilters">Сбросить фильтры</button>
        </div>
    </div>
    <div class="product-grid">
        <div class="product-card" v-for="a in product.products" :key="a.id">
            <img :src="a.image" class="product-image" alt="Изображение товара">
            <div class="product-title"><router-link :to="{ name: 'ProductDetail', params: { id: a.id } }">{{ a.name }}</router-link></div>
            <div class="product-price">Цена: {{ a.price }} руб.</div>
            <button class="add-to-cart">Добавить в корзину</button>
        </div>
    </div>
    <div class="pagination">
            <button @click="changePage(product.currentPage - 1)" :disabled="product.currentPage === 1">Назад</button>
            <span>Страница {{ product.currentPage }}</span>
            <button @click="changePage(product.currentPage + 1)" :disabled="product.currentPage === product.totalPages">Вперед</button>
    </div>

    <!-- ----------------------------------------------------------------
    <div class="list-group" v-for="cat in product.category">
        {{ cat.name }}
    </div> -->

    

</template>

<script>
import { userProduct } from '../../stores/product';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';

export default {
    setup() {
        
        const product = userProduct();
        const route = useRoute();
        const filter = {
            category: route.params.idCategory,
            min_price: null, //
            max_price: null,
        };
        
        const changePage = (page) => {
            product.setPage(page);
        };
        const applyFilters = () => {
            product.setFilters(filter);
        };

        onMounted(() => {
            product.fetchData(product.currentPage).then(() => {
                applyFilters();
            });
            product.fetchCategories();
            console.log(filter);
        });
        

        return {
            product,
            changePage,
            applyFilters,
            filter,
        }
    }
}
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

.product-price {
    font-size: 1em;
    color: #555;
    margin: 0 15px 15px;
}

.add-to-cart {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 12px;
    margin: 15px; /* Отступы вокруг кнопки */
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s, transform 0.2s;
}

.add-to-cart:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}

.filters {
    display: flex;
    
    align-items: center;
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 5px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    color: #333;
}

.selector {
    padding: 10px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    margin-right: 10px;
    background-color: #ffffff;
    color: #333;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}
.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 5px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);

}
.search-input {
    padding: 10px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    margin-right: 10px;
    background-color: #ffffff;
    color: #333;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
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
</style>



