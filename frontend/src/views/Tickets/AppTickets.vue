<template>
  <section class="section" v-if="tickets">
    <div class="container">
      <h1 class="title">{{ $t('pages.tickets.title') }}</h1>

      <div class="columns is-multiline">
        <div
          class="column is-full"
          v-for="ticket in tickets"
          :key="ticket.id"
          :ref="`content-` + ticket.id"
        >
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
                  <QrcodeVue
                    class="qr-code"
                    :size="400"
                    :value="generateTicketQRCode(ticket.secret)"
                  />

                  <b-button
                    type="is-primary is-large"
                    class="mt-3"
                    @click="downloadTicket(ticket.id)"
                  >{{ $t('pages.tickets.ticket.download') }}</b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script lang="ts">
import QrcodeVue from 'qrcode.vue'

import html2canvas from 'html2canvas'

import { format } from 'date-fns';
import { getTickets, type UserTicketResponse } from '@/client'

export default {
  components: {
    QrcodeVue
  },
  data() {
    return {
      tickets: [] as UserTicketResponse[],
      format: format
    }
  },
  methods: {
    generateTicketQRCode(ticket: string): string {
      return window.location.origin + this.$router.resolve({ name: 'verify', params: { ticket: ticket} }).href;
    },
    downloadTicket(id: number) {
      const content = (this.$refs['content-' + id] as HTMLElement[])[0];

      html2canvas(content).then((canvas) => {
        const link = document.createElement('a');

        link.href = canvas.toDataURL('image/png');
        link.download = `ticket-${id}.png`;

        link.click();
      });
    }
  },
  async created() {
    const response = await getTickets()

    if (response.status === 200) {
      this.tickets = response.data as UserTicketResponse[]
    }
  }
}
</script>
