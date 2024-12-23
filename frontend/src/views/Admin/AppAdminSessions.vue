<template>
  <AdminMenu v-if="sessions">
    <b-table
      :data="sessions"
      :columns="columns"
      checkable
      :checked-rows="checkedRows"
      @update:checked-rows="(value: MovieSessionsResponse[]) => checkedRows = value"
    ></b-table>

    <div class="buttons">
      <b-button
        :label="$t('form.add')"
        type="is-success"
        @click="openModal()"
      />
      <b-button
        :label="$t('form.edit')"
        type="is-warning"
        @click="openModal()"
      />
      <b-button
        :label="$t('form.delete')"
        type="is-danger"
        @click="deleteSessions()"
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
            <p class="modal-card-title">{{ $t('pages.admin.sessions.add') }}</p>
            <button
                type="button"
                class="delete"
                @click="isComponentModalActive=false"
            />
        </header>
        <section class="modal-card-body">
            <b-field label="Film">
              <b-select v-model="session.film_id" placeholder="Film" expanded>
                <option
                    v-for="film in films"
                    :value="film.id"
                    :key="film.id">
                    {{ film.title }}
                </option>
            </b-select>
            </b-field>

            <b-field label="Seats">
                <b-input
                  type="number"
                  v-model="session.seats"
                  placeholder="Seats"
                  required>
                </b-input>
            </b-field>

          <b-field label="Date">
            <b-datetimepicker
              v-model="session.date"
              placeholder="Date"
              icon="calendar-today"
              editable>
            </b-datetimepicker>
          </b-field>



        </section>
        <footer class="modal-card-foot">
            <b-button
                :label="$t('form.close')"
                @click="isComponentModalActive=false" />
            <b-button
                :label="$t('form.add')"
                type="is-primary"
                @click="addSession()"
            />
        </footer>
    </div>
  </b-modal>
</template>

<script lang="ts">
import AdminMenu from '@/components/Admin/AdminMenu.vue'
import { useUserStore } from '@/stores/user'
import {
  addSessionAdmin,
  deleteSessionAdmin,
  getMovies, getSessionAdmin,
  type MovieResponse, type MovieSessionsAddRequest,
  type MovieSessionsResponse,
} from '@/client'

export default {
  components: {
    AdminMenu
  },
  data() {
    return {
      user: useUserStore(),
      isComponentModalActive: false,
      films: [] as MovieResponse[],
      sessions: [] as MovieSessionsResponse[],
      checkedRows: [] as MovieSessionsResponse[],
      columns: [
          {
              field: 'id',
              label: 'ID',
              width: '40',
              numeric: true
          },
          {
              field: 'film_id',
              label: 'Film id',
          },
          {
              field: 'seats',
              label: 'Seats',
          },
          {
              field: 'date',
              label: 'Date',
          }
      ],
      session: {
        film_id: 0,
        seats: 0,
        date: null as Date | null,
      } as MovieSessionsAddRequest
    };
  },
  methods: {
    deleteSessions() {
      for (const session of this.checkedRows) {
        deleteSessionAdmin({body: {id: session.id}})
      }

      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.$buefy.notification.open({
          message: this.$t('form.successful'),
          type: 'is-success'
      })
    },
    openModal() {
      this.session = {} as MovieSessionsAddRequest
      this.isComponentModalActive = true
    },
    addSession() {
      if (this.session.film_id && this.session.seats && this.session.date) {
        addSessionAdmin({body: this.session})

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
    const response2 = await getSessionAdmin({body:{limit: 1000, offset: 0}})

    if (response.status === 200) {
      this.films = response.data as MovieResponse[]
    }

    if (response2.status === 200) {
      this.sessions = response2.data as MovieSessionsResponse[]
    }
  }
};
</script>
