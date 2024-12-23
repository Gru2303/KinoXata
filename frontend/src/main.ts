import './assets/scss/main.scss'

import { createApp } from 'vue'

import App from './App.vue'

import Buefy from 'buefy'

import i18n from './i18n'

import { createPinia } from 'pinia'
import router from './router'
import { client, getUserMe } from '@/client'
import { useUserStore } from '@/stores/user'
import { useLangStore } from '@/stores/lang'
import type { GeneratedLocale } from '@intlify/core-base'

const app = createApp(App)

client.setConfig({
  baseURL: 'http://localhost',
})

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-expect-error
app.use(Buefy)

app.use(createPinia())
app.use(router)

app.use(i18n)

i18n.global.locale = useLangStore().getLang() as GeneratedLocale

getUserMe().then((user) => {
  if (user.status === 200 && user.data) {
    useUserStore().setUser(user.data)
  }

  app.mount('#app')
}).catch(console.error)
