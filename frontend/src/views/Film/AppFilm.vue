<template>
  <div class="section" v-if="film">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-one-third">
          <figure class="image is-4by6">
            <img :src="film.image as string" alt="Movie Poster" />
          </figure>
        </div>

        <div class="column is-two-thirds">
          <h1 class="title is-2">{{ film.title }}</h1>
          <h1 class="subtitle is-3 is-bold">{{ film.price }} {{ $t('pages.film.buy.price') }}</h1>
          <p class="subtitle is-5">{{ film.genre }} | {{ film.time }}</p>
          <p class="content">{{ film.description }}</p>

          <div class="box">
            <iframe
              :src="film.trailer as string"
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
              width="100%"
              height="500"
            ></iframe>
          </div>

          <div class="box">
            <div class="column">
              <h1 class="title is-2">{{ $t('pages.film.sessions') }}</h1>
              <div v-if="userStorage.isAuthenticated">
                <h1 class="subtitle is-4" v-if="sessions.length == 0">{{ $t('pages.film.notsessions') }}</h1>


                <div
                  v-for="session in sessions"
                  :key="session.id"
                  class="buttons"
                >
                  <b-button type="is-primary" outlined @click="openModal(session)">{{ format(session.date, "dd.MM.yy HH:mm") }}</b-button>
                </div>
              </div>

              <div v-else>
                <h1 class="subtitle is-4">Потрібна авторизація</h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <b-modal
      v-model="isComponentModalActive"
      has-modal-card
      full-screen
  >
        <div class="modal-card" style="width: auto">
            <header class="modal-card-head">
                <p class="modal-card-title">{{ film?.title }}</p>
            </header>

            <section class="modal-card-body">
              <b-steps
                  v-model="activeStep"
                  animated
                  rounded
                  label-position="bottom"
                  mobile-mode="minimalist"
                  :has-navigation="false"
              >
                  <b-step-item step="1" :label="$t('pages.film.buy.seat.title')" clickable>
                    <h1 class="title has-text-centered">{{ $t('pages.film.buy.seat.subtitle') }}</h1>

                    <div class="columns is-centered is-multiline">
                      <div v-for="index in current_session?.seats" :key="index" class="column is-2 has-text-centered">
                        <b-checkbox-button
                          v-model="selectedSeats"
                          :native-value="index"
                          :disabled="JSON.parse(current_session?.seats_busy as string).includes(index)"
                        >{{ index }}</b-checkbox-button>
                      </div>
                    </div>

                    <div class="has-text-right">
                      <b-button
                        outlined
                        size="is-medium"
                        type="is-success"
                        icon-pack="mdi"
                        icon-right="chevron-right"
                        :disabled="selectedSeats.length == 0"
                        @click="activeStep = 2"
                      >{{ $t('pages.film.buy.next') }}</b-button>
                    </div>
                  </b-step-item>

                  <b-step-item step="2" :label="$t('pages.film.buy.oplata.title')" :clickable="selectedSeats.length > 0">
                      <h1 class="title has-text-centered">{{ $t('pages.film.buy.oplata.subtitle') }}</h1>

                      <b-field
                        :label="$t('pages.film.buy.oplata.cardNumber.title')"
                        :message="$t('pages.film.buy.oplata.cardNumber.subtitle')"
                        :type="isValidCardNumber() ? 'is-success' : 'is-danger'"
                      >
                        <b-input
                          v-model="paymentData.cardNumber"
                          placeholder="1234567890123456"
                          maxlength="16"
                          type="text"
                          required
                        ></b-input>
                      </b-field>

                      <b-field
                        :label="$t('pages.film.buy.oplata.cardName.title')"
                        :message="$t('pages.film.buy.oplata.cardName.subtitle')"
                        :type="isValidCardName() ? 'is-success' : 'is-danger'"
                      >
                        <b-input
                          v-model="paymentData.cardName"
                          :placeholder="$t('pages.film.buy.oplata.cardName.placeholder')"
                          type="text"
                          required
                        ></b-input>
                      </b-field>

                      <div class="columns">
                        <div class="column">
                          <b-field
                            :label="$t('pages.film.buy.oplata.expiryDate.title')"
                            message="MM/YY"
                            :type="isValidCardExpiryDate() ? 'is-success' : 'is-danger'"
                          >
                            <b-datepicker
                                v-model="paymentData.expiryDate"
                                type="month"
                                icon="calendar-today"
                                trap-focus>
                            </b-datepicker>
                          </b-field>
                        </div>

                        <div class="column">
                          <b-field
                            :label="$t('pages.film.buy.oplata.cvv.title')"
                            :message="$t('pages.film.buy.oplata.cvv.subtitle')"
                            :type="isValidCardCvv() ? 'is-success' : 'is-danger'"
                          >
                            <b-input
                              v-model="paymentData.cvv"
                              :placeholder="$t('pages.film.buy.oplata.cvv.placeholder')"
                              maxlength="3"
                              type="password"
                              required
                            ></b-input>
                          </b-field>
                        </div>
                      </div>

                      <div class="has-text-right">
                        <b-button
                          outlined
                          size="is-medium"
                          type="is-success"
                          icon-pack="mdi"
                          icon-right="chevron-right"
                          :disabled="!(isValidCardNumber() && isValidCardName() && isValidCardExpiryDate() && isValidCardCvv())"
                          @click="processPayment()"
                        >{{ $t('pages.film.buy.buy') }}</b-button>
                      </div>
                  </b-step-item>
              </b-steps>
            </section>
        </div>
  </b-modal>
</template>

<script lang="ts">
import { format } from 'date-fns';
import {
  getMovie,
  getMovieSessions,
  type MovieResponse,
  type MovieSessionsResponse,
  processPayment,
} from '@/client'
import router from '@/router'
import { useUserStore } from '@/stores/user'

export default {
  data() {
    return {
      userStorage: useUserStore(),
      film: null as MovieResponse | null,
      sessions: [] as MovieSessionsResponse[],
      isComponentModalActive: false,
      current_session: null as MovieSessionsResponse | null,
      activeStep: 0,
      selectedSeats: [],
      paymentData: {
        cardNumber: '',
        cardName: '',
        expiryDate: '',
        cvv: ''
      },
      format: format
    };
  },
  methods: {
    openModal(session: MovieSessionsResponse) {
      this.current_session = session;
      this.isComponentModalActive = true
      this.activeStep = 0;
      this.selectedSeats = [];
    },
    isValidCardNumber() {
      return this.paymentData.cardNumber.length == 16 && /^[0-9]+$/.test(this.paymentData.cardNumber)
    },
    isValidCardName() {
      return this.paymentData.cardName.length > 5 && /^[a-zA-Z\s]+$/.test(this.paymentData.cardName)
    },
    isValidCardExpiryDate() {
      return this.paymentData.expiryDate
    },
    isValidCardCvv() {
      return this.paymentData.cvv.length == 3 && /^[0-9]+$/.test(this.paymentData.cvv)
    },
    async processPayment() {
      if (this.isValidCardNumber() && this.isValidCardName() && this.isValidCardExpiryDate() && this.isValidCardCvv()) {
        const payment = await processPayment({body: {
          session_id: this.current_session?.id as number,
          seats: this.selectedSeats,
          card_number: this.paymentData.cardNumber,
          card_name: this.paymentData.cardName,
          card_exp: this.paymentData.expiryDate,
          card_cvv: this.paymentData.cvv,
         }});

        if (payment.status == 200) {
          if (payment.data?.success) {
            await router.push({ name: 'tickets' })
            window.location.reload();
          } else {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-expect-error
            this.$buefy.notification.open({
                message: this.$t(payment.data?.message as string),
                type: 'is-danger'
            })
          }
        }
      }
    }
  },
  async created() {
    const response = await getMovie({body: {id: parseInt(this.$route.params.id as string)}})
    const responseSessions = await getMovieSessions({body: {id: parseInt(this.$route.params.id as string) }})

    if (response.status == 200) {
      this.film = response.data as MovieResponse
    }

    if (responseSessions.status == 200) {
      this.sessions = responseSessions.data as MovieSessionsResponse[]
    }
  }
};
</script>
