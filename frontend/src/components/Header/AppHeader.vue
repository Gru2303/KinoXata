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
        <b-button type="is-primary" @click="isComponentModalActive = true">
          <strong>{{ $t('navbar.signin') }}</strong>
        </b-button>
      </b-navbar-item>
    </template>
  </b-navbar>

  <b-modal
      v-model="isComponentModalActive"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-label="Login"
      close-button-aria-label="Close"
      aria-modal
  >
        <div class="modal-card" style="width: auto">
            <header class="modal-card-head">
                <p class="modal-card-title">{{ $t('navbar.login.title') }}</p>

                <button
                    type="button"
                    class="delete"
                    @click="isComponentModalActive = false"
                />
            </header>

            <section class="modal-card-body">
              <div class="buttons">
              <b-button type="is-primary" size="is-large" icon-left="google" outlined expanded>{{ $t('navbar.login.google') }}</b-button>
              <b-button type="is-primary" size="is-large" icon-left="microsoft" outlined expanded disabled>{{ $t('navbar.login.microsoft') }}</b-button>
              <b-button type="is-primary" size="is-large" icon-left="apple" outlined expanded disabled>{{ $t('navbar.login.apple') }}</b-button>
              </div>
            </section>
        </div>
  </b-modal>
</template>

<style lang="scss" scoped>
.navbar-item img {
  max-height: 4rem;
}
</style>

<script lang="ts">
export default {
  data() {
    return {
      isComponentModalActive: false
    }
  }
}
</script>
