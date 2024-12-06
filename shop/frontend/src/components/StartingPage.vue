<template>
    <div class="slider">
        <div class="slides">
            <div class="slide active">
                <img src="C:\MyFolder\Shop\shop\frontend\src\assets\velo-prokat1.jpg" alt="Image 1">
            </div>
            <div class="slide">
                <img src="C:\MyFolder\Shop\shop\frontend\src\assets\velomoika-2048x878.jpg" alt="Image 2">
            </div>
            <div class="slide">
                <img src="C:\MyFolder\Shop\shop\frontend\src\assets\velozapchasti-768x288.jpg" alt="Image 3">
            </div>
        </div>
    </div>
</template>

<script setup>
let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }

    const offset = -currentSlide * 100;
    document.querySelector('.slides').style.transform = `translateX(${offset}%)`;
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

setInterval(() => {
    changeSlide(1);
}, 5000);
</script>

<style scoped>
.slider {
    position: relative;
    max-width: 1230px;
    margin: auto;
    overflow: hidden;
}

.slides {
    display: flex;
    transition: transform 0.5s ease;
}

.slide {
    min-width: 100%;
}

img {
    width: 100%; /* Изображение занимает всю ширину слайда */
    display: block; /* Убираем пробелы под изображением */
}
</style>