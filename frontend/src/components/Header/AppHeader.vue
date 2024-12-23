<template>
  <b-navbar type="is-dark">
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img src="@/assets/img/logo_big.svg"  alt="KinoXata"/>
      </b-navbar-item>
    </template>

    <template #start>
      <b-navbar-item tag="router-link" :to="{ path: '/' }"> {{ $t('navbar.home') }} </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ path: '/films' }"> {{ $t('navbar.films') }} </b-navbar-item>
      <b-navbar-dropdown :label="$t('navbar.info.info')">
        <b-navbar-item tag="router-link" :to="{ path: '/info/cinemas' }">
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
        <b-navbar-dropdown>
          <template #label>
            <img :src="currentFlagPath" class="lang-img" loading="lazy" alt="Avatar" />
          </template>

          <b-navbar-item @click="langStore.setLang('uk')">
            <img src="@/assets/img/flags/uk.svg" class="lang-img" loading="lazy" alt="Avatar" />

            {{ $t('navbar.lang.uk') }}
          </b-navbar-item>
          <b-navbar-item @click="langStore.setLang('en')">
            <img src="@/assets/img/flags/en.svg" class="lang-img" loading="lazy" alt="Avatar" />

            {{ $t('navbar.lang.en') }}
          </b-navbar-item>
        </b-navbar-dropdown>
      </b-navbar-item>

      <b-navbar-item tag="div" v-if="!userStore.isAuthenticated">
        <b-button type="is-primary" @click="isComponentModalActive = true">
          <strong>{{ $t('navbar.signin') }}</strong>
        </b-button>
      </b-navbar-item>

      <b-navbar-item tag="div" v-if="userStore.isAuthenticated">
        <b-navbar-dropdown>
          <template #label>
            <img src="@/assets/cdn/avatar.jpg" class="profile-img" loading="lazy" alt="Avatar" />

            {{ userStore.user?.name }}
          </template>

          <b-navbar-item tag="router-link" :to="{ path: '/tickets' }">
            {{ $t('navbar.profile.tickets') }}
          </b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/admin' }">
            {{ $t('navbar.profile.admin') }}
          </b-navbar-item>
          <b-navbar-item @click="logout">
            {{ $t('navbar.profile.logout') }}
          </b-navbar-item>
        </b-navbar-dropdown>
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
              <b-button @click="googleClick" type="is-primary" size="is-large" icon-left="google" outlined expanded>{{ $t('navbar.login.google') }}</b-button>
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

.navbar-item .profile-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

.navbar-item .lang-img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}
</style>

<script lang="ts">
import { getGoogleLoginUrl, unauthorized } from '@/client'
import { useUserStore } from '@/stores/user'
import { useLangStore } from '@/stores/lang'

import en from "@/assets/img/flags/en.svg"
import uk from "@/assets/img/flags/uk.svg"

export default {
  methods: {
    googleClick() {
      getGoogleLoginUrl().then(url => {
        if (url.status == 200 && url.data) {
          window.location.href = url.data.url;
        }
      });
    },
    logout() {
      unauthorized()
      window.location.reload();
    }
  },
  data() {
    return {
      isComponentModalActive: false,
      userStore: useUserStore(),
      langStore: useLangStore()
    }
  },
  computed: {
    currentFlagPath() {
      const flags = {
        en: en,
        uk: uk,
      };

      return flags[this.langStore.getLang()];
    },
  },
}
</script>
