<template>
  <div class="container">
    <section id="top">
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
#top {
  h2 {
    margin-bottom: 0;
  }
  p {
    font-size: 14px;
  }
  margin-bottom: 30px;
}
</style>
