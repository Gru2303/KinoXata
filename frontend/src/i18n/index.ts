import i18next from 'i18next';

import uk from './locales/uk'

// Define your translations
const resources = {
  en: {
    translation: uk
  }
};

// Initialize i18next
i18next.init({
  resources,
  lng: 'en', // Default language
  interpolation: {
    escapeValue: false, // Not needed for Vue.js
  },
});

export default i18next;
