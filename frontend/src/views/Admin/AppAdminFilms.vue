<template>
  <AdminMenu v-if="films">
    <b-table
      :data="films"
      :columns="columns"
      checkable
      :checked-rows="checkedRows"
      @update:checked-rows="(value: MovieResponse[]) => checkedRows = value"
    ></b-table>

    <div class="buttons">
      <b-button
        :label="$t('form.add')"
        type="is-success"
        @click="openModal()"
      />
      <b-button
        :label="$t('form.delete')"
        type="is-danger"
        @click="deleteFilms()"
      />
    </div>
  </AdminMenu>

  <b-modal
      v-model="isComponentModalActive"

      has-modal-card
      trap-focus
      :destroy-on-hide="false"
  >
      <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">{{ $t('pages.admin.films.add') }}</p>
            <button
                type="button"
                class="delete"
                @click="isComponentModalActive=false"
            />
        </header>
        <section class="modal-card-body">
            <b-field label="Title">
                <b-input
                    v-model="movie.title"
                    placeholder="Title"
                    required>
                </b-input>
            </b-field>

            <b-field label="Description">
                <b-input
                  v-model="movie.description"
                  placeholder="Description"
                  required>
                </b-input>
            </b-field>

          <b-field label="Image">
                <b-input
                    v-model="movie.image"
                    placeholder="Image"
                    required>
                </b-input>
            </b-field>

          <b-field label="Afisha image">
                <b-input
                  v-model="movie.afisha_image"
                    placeholder="Afisha image"
                    required>
                </b-input>
            </b-field>

          <b-field label="Lang">
                <b-input
                    v-model="movie.lang"
                    placeholder="lang"
                    required>
                </b-input>
            </b-field>

          <b-field label="Genre">
                <b-input
                    v-model="movie.genre"
                    placeholder="Genre"
                    required>
                </b-input>
            </b-field>

          <b-field label="Time">
                <b-input
                    v-model="movie.time"
                    placeholder="Time"
                    required>
                </b-input>
            </b-field>

          <b-field label="Trailer">
                <b-input
                    v-model="movie.trailer"
                    placeholder="Trailer"
                    required>
                </b-input>
            </b-field>

          <b-field label="Price">
                <b-input
                    v-model="movie.price"
                    type="number"
                    placeholder="Price"
                    required>
                </b-input>
            </b-field>

        </section>
        <footer class="modal-card-foot">
            <b-button
                :label="$t('form.close')"
                @click="isComponentModalActive=false" />
            <b-button
                :label="$t('form.add')"
                type="is-primary"
                @click="addFilm()"
            />
        </footer>
    </div>
  </b-modal>
</template>

<script lang="ts">
import AdminMenu from '@/components/Admin/AdminMenu.vue'
import { useUserStore } from '@/stores/user'
import { addMovieAdmin, deleteMovieAdmin, getMovies, type MovieAddRequest, type MovieResponse } from '@/client'

export default {
  components: {
    AdminMenu
  },
  data() {
    return {
      user: useUserStore(),
      isComponentModalActive: false,
      films: [] as MovieResponse[],
      checkedRows: [] as MovieResponse[],
      columns: [
          {
              field: 'id',
              label: 'ID',
              width: '40',
              numeric: true
          },
          {
              field: 'title',
              label: 'Title',
          },
          {
              field: 'lang',
              label: 'Lang',
          },
          {
              field: 'genre',
              label: 'Genre',
          },
          {
              field: 'time',
              label: 'Time',
          },
          {
              field: 'price',
              label: 'Price',
          }
      ],
      movie: {
        title: '',
        description: '',
        image: '',
        afisha_image: '',
        lang: '',
        genre: '',
        time: '',
        trailer: '',
        price: 0
      } as MovieAddRequest
    };
  },
  methods: {
    deleteFilms() {
      for (const film of this.checkedRows) {
        deleteMovieAdmin({body: {id: film.id}})
      }

      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.$buefy.notification.open({
          message: this.$t('form.successful'),
          type: 'is-success'
      })
    },
    openModal() {
      this.movie = {} as MovieAddRequest
      this.isComponentModalActive = true
    },
    addFilm() {
      if (this.movie.title && this.movie.description && this.movie.image && this.movie.afisha_image &&
        this.movie.lang && this.movie.genre && this.movie.time && this.movie.trailer && this.movie.price) {
        addMovieAdmin({body: this.movie})

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-expect-error
        this.$buefy.notification.open({
          message: this.$t('form.successful'),
          type: 'is-success'
        })
      } else {
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-expect-error
        this.$buefy.notification.open({
          message: this.$t('form.noinput'),
          type: 'is-danger'
        })
      }
    }
  },
  async created() {
    const response = await getMovies({body:{limit: 1000, offset: 0}})

    if (response.status === 200) {
      this.films = response.data as MovieResponse[]
    }
  }
};
</script>
