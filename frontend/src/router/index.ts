import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/Admin/AppAdminStatistic.vue'),
    },
    {
      path: '/admin/users',
      name: 'admin/users',
      component: () => import('../views/Admin/AppAdminUsers.vue'),
    },
    {
      path: '/admin/films',
      name: 'admin/films',
      component: () => import('../views/Admin/AppAdminFilms.vue'),
    },
    {
      path: '/admin/sessions',
      name: 'admin/sessions',
      component: () => import('../views/Admin/AppAdminSessions.vue'),
    },
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home/AppHome.vue'),
    },
    {
      path: '/tickets',
      name: 'tickets',
      component: () => import('../views/Tickets/AppTickets.vue'),
    },
    {
      path: '/tickets/verify/:ticket',
      name: 'verify',
      component: () => import('../views/Tickets/AppTicketVerify.vue'),
    },
    {
      path: '/films',
      name: 'films',
      component: () => import('../views/Films/AppFilms.vue'),
    },
    {
      path: '/film/:id',
      name: 'film',
      component: () => import('../views/Film/AppFilm.vue'),
    },
    {
      path: '/info/about',
      name: 'about',
      component: () => import('../views/info/About/ViewAbout.vue'),
    },
    {
      path: '/info/contacts',
      name: 'contacts',
      component: () => import('../views/info/Contacts/ViewContacts.vue'),
    },
    {
      path: '/info/cinemas',
      name: 'cinemas',
      component: () => import('../views/info/Cinemas/ViewCinemas.vue'),
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/'
    }
  ],
})

export default router
