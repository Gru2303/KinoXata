<template>
    <b-carousel
      icon-prev="arrow-left"
      icon-next="arrow-right"
      icon-size="is-large"
      autoplay
      repeat
      interval="5000"
    >
        <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
          <div class="hero carousel-image is-large has-text-centered"
          style="background-image: url('https://planetakino.ua/res/get-poster/00000000000000000000000000004726/moana-2-afisha3.jpg');"
          >
            <div class="overlay"></div>
            <div class="hero-body">
              <div class="container">
                <h1 class="title is-1">{{carousel.text}}</h1>
                <b-button type="is-primary" size="is-medium">Детальніше</b-button>
              </div>
            </div>
          </div>
        </b-carousel-item>
    </b-carousel>
</template>

<style lang="scss" scoped>
.title {
  color: white;
}

.carousel-image {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 0;
}
</style>

<script lang="ts">
export default {
    data(){
        return {
            carousels: [
                { text: 'Slide - вцвфцвыфв', color: 'primary' },
                { text: 'Slide 2', color: 'info' },
                { text: 'Slide 3', color: 'success' },
                { text: 'Slide 4', color: 'warning' },
                { text: 'Slide 5', color: 'danger' }
            ]
        }
    }
}
</script>
