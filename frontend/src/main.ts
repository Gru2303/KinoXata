import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import I18NextVue from 'i18next-vue';
import i18next from './i18n';

import { createPinia } from 'pinia'
import router from './router'

const app = createApp(App)

app.use(I18NextVue, { i18next });

app.use(createPinia())
app.use(router)

app.mount('#app')
