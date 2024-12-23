<template>
  <div class="admin-layout" v-if="user.isAdministrator">
    <section class="section menu-section" >
      <b-menu>
        <b-menu-list :label="$t('pages.admin.menu.title')">
          <b-menu-item
            icon="information-outline"
            :label="$t('pages.admin.menu.stats')"
            tag="router-link"
            :to="{ path: '/admin' }"
            :model-value="$route.path === '/admin'"
          ></b-menu-item>
          <b-menu-item
            icon="account"
            :label="$t('pages.admin.menu.users')"
            tag="router-link"
            :to="{ path: '/admin/users' }"
            :model-value="$route.path === '/admin/users'"
          ></b-menu-item>
          <b-menu-item
            icon="movie-open"
            :label="$t('pages.admin.menu.films')"
            tag="router-link"
            :to="{ path: '/admin/films' }"
            :model-value="$route.path === '/admin/films'"
          ></b-menu-item>
          <b-menu-item
            icon="book"
            :label="$t('pages.admin.menu.sessions')"
            tag="router-link"
            :to="{ path: '/admin/sessions' }"
            :model-value="$route.path === '/admin/sessions'"
          ></b-menu-item>
        </b-menu-list>
      </b-menu>
    </section>

    <section class="content">
      <slot />
    </section>
  </div>

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

<style lang="scss" scoped>
.admin-layout {
  display: flex;
  height: 100vh;
}

.menu-section {
  width: 250px;
  background-color: #f5f5f5;
  border-right: 1px solid #ddd;
  padding: 10px;
  overflow-y: auto;
}

.content {
  flex: 1;
  padding: 20px;
}

.custom-box {
  width: 50vw;
  height: 50vh;
  border: 2px solid #dbdbdb;
}
</style>

<script lang="ts">
import { useUserStore } from '@/stores/user'

export default {
  data() {
    return {
      user: useUserStore()
    };
  },
  methods: {

  }
};
</script>
