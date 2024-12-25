<template>
  <section class="section">
    <div class="container">
      <h1 class="title is-3">{{ $t('pages.films.title') }}</h1>

      <div class="columns is-mobile is-vcentered">
        <div class="column is-6">
          <div class="field">
            <label class="label">{{ $t('pages.films.search.title') }}</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="$t('pages.films.search.placeholder')"
                v-model="searchQuery"
              />
            </div>
          </div>
        </div>

        <div class="column is-6 has-text-right">
          <div class="field">
            <label class="label">{{ $t('pages.films.sort.title') }}</label>
            <div class="control">
              <b-select v-model="sortOption">
                <option value="date">{{ $t('pages.films.sort.date') }}</option>
                <option value="name">{{ $t('pages.films.sort.name') }}</option>
                <option value="price">{{ $t('pages.films.sort.price') }}</option>
              </b-select>
            </div>
          </div>
        </div>
      </div>

      <div class="columns is-multiline">
        <div
          v-for="film in filteredMovies()"
          :key="film.id"
          class="column is-4"
        >
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by5">
                <img :src="film.image as string" :alt="film.title" loading="lazy" />
              </figure>
            </div>
            <div class="card-content">
              <p class="title is-5">{{ film.title }}</p>
              <p class="subtitle is-6" style="height: 80px;">{{ (film.description as string).slice(0, 150) }}...</p>
              <p class="is-size-5 has-text-weight-bold">{{ film.price }} {{ $t('pages.films.price') }}</p>
            </div>
            <footer class="card-footer">
                <b-button
                  tag="router-link"
                  :to="{ name: 'film', params: { id: film.id } }"
                  type="is-primary"
                  class="card-footer-item"
                >
                  {{ $t('pages.films.buy') }}
                </b-button>
            </footer>
          </div>
        </div>
      </div>

      <div class="has-text-centered">
        <b-button
          type="is-primary"
          outlined
          @click="loadMoreMovies"
        >
          {{ $t('pages.films.more') }}
        </b-button>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.card {
  margin-bottom: 20px;
}
</style>

<script lang="ts">
import { getMovies, type MovieResponse } from '@/client'

export default {
  data() {
      return {
          searchQuery: "",
          sortOption: "date",
          films: [] as MovieResponse[]
      }
  },
  methods: {
    filteredMovies(): MovieResponse[] {
      const lowerCaseSearchQuery = this.searchQuery.toLowerCase()

      let sortedMovies = this.films;

      if (this.sortOption == "date") {
        sortedMovies = sortedMovies.sort((a, b) => {
          return new Date(b.create_time).getTime() - new Date(a.create_time).getTime()
        })
      } else if (this.sortOption == "name") {
        sortedMovies = sortedMovies.sort((a, b) => {
          return a.title.toLowerCase().localeCompare(b.title.toLowerCase())
        })
      } else if (this.sortOption == "price") {
        sortedMovies = sortedMovies.sort((a, b) => {
          return a.price - b.price
        })
      }

      return sortedMovies.filter(film => {
        return film.title.toLowerCase().includes(lowerCaseSearchQuery) ||
          (film.description as string).toLowerCase().includes(lowerCaseSearchQuery)
      })
    },
    loadMoreMovies() {
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.$buefy.notification.open({
          message: this.$t('pages.films.nomore'),
          type: 'is-success'
      })
    }
  },
  async created() {
    const response = await getMovies({ body: { limit: 5 } })

    if (response.status == 200) {
      this.films = response.data as MovieResponse[]
    }
  }
}
</script>
