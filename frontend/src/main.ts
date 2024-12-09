import './assets/scss/main.scss'

import { createApp } from 'vue'

import App from './App.vue'

import Buefy from 'buefy'

import i18n from './i18n'

import { createPinia } from 'pinia'
import router from './router'
import { client, getMovie } from '@/client'

const app = createApp(App)

client.setConfig({
  baseURL: 'http://127.0.0.1:8000',
})

console.log(getMovie())

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-expect-error
app.use(Buefy)

app.use(createPinia())
app.use(router)

app.use(i18n)

app.mount('#app')
