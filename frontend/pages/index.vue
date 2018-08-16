<template>
  <div class="container">
    <section class="top">
      <span class="current-path">
        <span>Dashboard / </span>
        <nuxt-link class="active" to="/">Contacts</nuxt-link>
        <span class="active"> /</span>
      </span>
      <h2>Contacts</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
    </section>
    <section id="contacts">
      <ContactManager :contacts="contacts" />
    </section>
  </div>
</template>

<script>
import ContactManager from '~/components/Contacts/ContactManager.vue'
import dataJSON from '~/api/data.json'

export default {
  data() {
    return {
      contacts: dataJSON.contacts
    }
  },
  components: {
    ContactManager
  }
}
</script>

<style lang="scss">
</style>
