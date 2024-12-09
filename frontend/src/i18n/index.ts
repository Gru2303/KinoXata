import { createI18n } from 'vue-i18n'

import uk from './locales/uk'

export default createI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en: uk,
    uk: uk,
  },
})
