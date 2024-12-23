<template>
  <AdminMenu v-if="users">
    <b-table
      :data="users"
      :columns="columns"
      checkable
      :checked-rows="checkedRows"
      @update:checked-rows="(value: UserMeResponse[]) => checkedRows = value"
    ></b-table>

    <div class="buttons">
      <b-button
        :label="$t('pages.admin.users.take')"
        type="is-success"
        @click="take()"
      />
      <b-button
        :label="$t('pages.admin.users.give')"
        type="is-danger"
        @click="console.log(checkedRows);give()"
      />
    </div>
  </AdminMenu>
</template>

<script lang="ts">
import AdminMenu from '@/components/Admin/AdminMenu.vue'
import { useUserStore } from '@/stores/user'
import { getUsersAdmin, setUserAdmin, type UserMeResponse } from '@/client'

export default {
  components: {
    AdminMenu
  },
  data() {
    return {
      user: useUserStore(),
      users: [] as UserMeResponse[],
      checkedRows: [] as UserMeResponse[],
      columns: [
          {
              field: 'id',
              label: 'ID',
              width: '40',
              numeric: true
          },
          {
              field: 'email',
              label: 'Email',
          },
          {
              field: 'name',
              label: 'Name',
          },
          {
              field: 'register_time',
              label: 'Register Time',
              centered: true
          }
      ]
    };
  },
  methods: {
    give() {
      for (const user of this.checkedRows) {
        setUserAdmin({body: {id: user.id, admin: true}})
      }

      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.$buefy.notification.open({
          message: this.$t('form.successful'),
          type: 'is-success'
      })
    },
    take() {
      for (const user of this.checkedRows) {
        setUserAdmin({body: {id: user.id, admin: false}})
      }

      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.$buefy.notification.open({
          message: this.$t('form.successful'),
          type: 'is-success'
      })
    }
  },
  async created() {
    const response = await getUsersAdmin({body:{limit: 1000, offset: 0}})

    if (response.status === 200) {
      this.users = response.data as UserMeResponse[]
    }
  }
};
</script>
