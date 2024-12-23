import { createI18n } from 'vue-i18n'

import en from './locales/en'
import uk from './locales/uk'

export default createI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en: en,
    uk: uk,
  },
})
