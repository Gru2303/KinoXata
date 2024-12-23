<template>
  <section class="section">
    <div class="container">

      <img src="@/assets/img/logo_big.svg" alt="About" class="image" />

      <h1 class="title has-text-centered">{{ $t('pages.info.cinemas.title') }}</h1>

     <div class="content">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2792.2809241555237!2d30.46247276361536!3d50.45146746769026!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40d4ce83b06d9ee7%3A0x1d170c10bb79676c!2z0J_QvtC70ZbRgtC10YXQvdGW0YfQvdC40Lkg0ZbQvdGB0YLQuNGC0YPRgg!5e0!3m2!1suk!2sua!4v1734885102038!5m2!1suk!2sua"
          class="google-map"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
          allowfullscreen
        />

      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.google-map {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>

<script setup lang="ts">

</script>
