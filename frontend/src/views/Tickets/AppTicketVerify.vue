<template>
  <section class="section" v-if="ticket">
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-full">
          <div class="box">
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image">
                    <img :src="ticket.film.image as string" alt="Ticket Image" />
                  </figure>
                </div>

                <div class="media-content">
                  <p class="title is-1">{{ ticket.film.title }}</p>
                  <p class="subtitle is-4">{{ $t('pages.tickets.ticket.session') }} {{ format(ticket.date, "dd.MM.yy HH:mm") }}</p>
                  <p class="subtitle is-4">{{ $t('pages.tickets.ticket.seats') }} {{ ticket.seats }}</p>
                </div>

                <div class="media-right" style="display: flex; flex-direction: column; align-items: center;">
                  <b-icon
                    icon="check-circle"
                    type="is-success"
                    custom-size=" "
                    style="font-size: 100px;"
                  >
                  </b-icon>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section is-flex is-justify-content-center is-align-items-center" v-else>
    <div class="box is-flex is-justify-content-center is-align-items-center custom-box">
      <b-icon
        icon="close-octagon"
        type="is-danger"
        custom-size=" "
        style="font-size: 256px;"
      >
      </b-icon>
    </div>
  </section>
</template>

<style scoped>
.custom-box {
  width: 50vw;
  height: 50vh;
  border: 2px solid #dbdbdb;
}
</style>

<script lang="ts">
import { getTicketBySign, type UserTicketResponse } from '@/client'
import { format } from 'date-fns';

export default {
  data() {
    return {
      ticket: null as UserTicketResponse | null,
      format: format
    };
  },
  methods: {

  },
  async created() {
    const sign = this.$route.params.ticket as string;
    const response = await getTicketBySign({body:{sign: sign}})

    if (response.status === 200) {
      this.ticket = response.data as UserTicketResponse
    }
  }
};
</script>
