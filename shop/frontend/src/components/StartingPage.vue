<template>
    <div class="slider">
        <div class="slides" ref="slides">
            <div class="slide active">
                <img src="@/assets/velo-prokat1.jpg" alt="Image 1">
            </div>
            <div class="slide">
                <img src="@/assets/velomoika-2048x878.jpg" alt="Image 2">
            </div>
            <div class="slide">
                <img src="@/assets/velozapchasti-768x288.jpg" alt="Image 3">
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const slides = ref(null);
let currentSlide = 0;

function showSlide(index) {
    const slideElements = slides.value.children;
    if (index >= slideElements.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slideElements.length - 1;
    } else {
        currentSlide = index;
    }

    const offset = -currentSlide * 100;
    slides.value.style.transform = `translateX(${offset}%)`;
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

onMounted(() => {
    setInterval(() => {
        changeSlide(1);
    }, 5000);
});
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
    width: 100%;
    height: 532px;
    object-fit: fill;
    display: block;
}
</style>
