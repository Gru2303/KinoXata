<template>
    <b-carousel
      icon-prev="arrow-left"
      icon-next="arrow-right"
      icon-size="is-large"
      autoplay
      repeat
      interval="5000"
    >
        <b-carousel-item v-for="(film, i) in afishaFilms" :key="i">
          <div class="hero carousel-image is-large has-text-centered"
          :style="`background-image: url('${film.afisha_image}');`"
          >
            <div class="overlay"></div>
            <div class="hero-body">
              <div class="container">
                <h1 class="title is-1">{{ film.title }} - {{ (film.description as string).slice(0, 100) }}...</h1>
                <b-button
                  tag="router-link"
                  :to="{ name: 'film', params: { id: film.id } }"
                  type="is-primary"
                  size="is-medium"
                >Детальніше</b-button>
              </div>
            </div>
          </div>
        </b-carousel-item>
    </b-carousel>

  <AppFilms />
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
import AppFilms from '@/views/Films/AppFilms.vue'
import { getMovies, type MovieResponse } from '@/client'

export default {
  components: { AppFilms },
  data() {
      return {
          afishaFilms: [] as MovieResponse[]
      }
  },
  async created() {
    const response = await getMovies({ body: { limit: 5 } })

    if (response.status == 200) {
      this.afishaFilms = response.data as MovieResponse[]
    }
  }
}
</script>
