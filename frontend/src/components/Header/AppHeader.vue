<template>
  <b-navbar type="is-dark">
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img src="@/assets/img/logo_big.svg" />
      </b-navbar-item>
    </template>

    <template #start>
      <b-navbar-item tag="router-link" :to="{ path: '/' }"> {{ $t('navbar.home') }} </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ path: '/films' }"> {{ $t('navbar.films') }} </b-navbar-item>
      <b-navbar-dropdown :label="$t('navbar.info.info')">
        <b-navbar-item tag="router-link" :to="{ path: '/info/locations' }">
          {{ $t('navbar.info.locations') }}
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/info/contacts' }">
          {{ $t('navbar.info.contacts') }}
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/info/about' }">
          {{ $t('navbar.info.about') }}
        </b-navbar-item>
      </b-navbar-dropdown>
    </template>

    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<style lang="scss" scoped>
.navbar-item img {
  max-height: 4rem;
}
</style>

<script setup lang="ts">
</script>
