<template>
  <AdminMenu v-if="stats">
    <div class="columns is-multiline">
      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.users }}</p>
          <p>{{ $t('pages.admin.stats.users') }}</p>
        </div>
      </div>

      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.films }}</p>
          <p>{{ $t('pages.admin.stats.films') }}</p>
        </div>
      </div>

      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.sessions }}</p>
          <p>{{ $t('pages.admin.stats.sessions') }}</p>
        </div>
      </div>

      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.tickets_sell }}</p>
          <p>{{ $t('pages.admin.stats.tickets_sell') }}</p>
        </div>
      </div>

      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.month_money }}</p>
          <p>{{ $t('pages.admin.stats.month_money') }}</p>
        </div>
      </div>

      <div class="column is-one-third">
        <div class="box has-text-centered">
          <p class="title">{{ stats.week_money }}</p>
          <p>{{ $t('pages.admin.stats.week_money') }}</p>
        </div>
      </div>
    </div>
  </AdminMenu>
</template>

<script lang="ts">
import AdminMenu from '@/components/Admin/AdminMenu.vue'
import { useUserStore } from '@/stores/user'
import { type AdminStatsResponse, getAdminStats } from '@/client'

export default {
  components: {
    AdminMenu
  },
  data() {
    return {
      user: useUserStore(),
      stats: null as AdminStatsResponse | null
    };
  },
  methods: {

  },
  async created() {
    const response = await getAdminStats()

    if (response.status === 200) {
      this.stats = response.data as AdminStatsResponse
    }
  }
};
</script>
