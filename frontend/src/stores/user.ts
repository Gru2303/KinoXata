import { defineStore } from 'pinia';
import type { UserMeResponse } from '@/client'

export const useUserStore = defineStore('user', {
  state: (): { user: UserMeResponse | null }  => ({
    user: null,
  }),
  actions: {
    setUser(userData: UserMeResponse) {
      this.user = userData;
    },
    clearUser() {
      this.user = null;
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.user,
    isAdministrator: (state) => state.user?.permission.toLowerCase().includes('ff'),
  },
});
