import { defineStore } from 'pinia';
import i18n from '@/i18n'
import type { GeneratedLocale } from '@intlify/core-base'


export type Lang = 'en' | 'uk';

export const useLangStore = defineStore('lang', {
  state: (): {lang: Lang} => ({
    lang: localStorage.getItem('lang') as Lang || 'en',
  }),
  actions: {
    setLang(lang: Lang) {
      this.lang = lang;
      i18n.global.locale = lang as GeneratedLocale;
      localStorage.setItem('lang', lang);
    },
    getLang(): Lang {
      return this.lang;
    }
  },
});
