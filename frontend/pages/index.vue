<template>
  <div class="container">
    <section class="top">
      <div class="top-bar">
        <div class="top-bar-left">
          <span class="current-path">
            <span>Dashboard / </span>
            <nuxt-link class="active" to="/">Contacts</nuxt-link>
            <span class="active"> /</span>
          </span>
        </div>
        <div class="top-bar-right desktop">
          <i class="icon-bell"></i>
          <i class="icon-user"></i>
          <span>jpcasabianca</span>
        </div>
      </div>
      <h2>Contacts</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
    </section>
    <section id="contacts">
      <ContactManager :contacts="contactData" />
    </section>
  </div>
</template>

<script>
import ContactManager from '~/components/Contacts/ContactManager.vue'
import dataJSON from '~/api/data.json'

export default {
  data() {
    return {
      contacts: dataJSON.contacts,
      contactData: {}
    }
  },
  components: {
    ContactManager
  },
  methods: {
    async fetchContacts() {
      const data = await this.$axios.$get('contacts/?format=json')
      this.contactData = data
    }
  },
  created () {
    this.fetchContacts()
  }
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';

  .top-bar {
    display: flex;
    .top-bar-left {
      flex: 1;
    }
    .top-bar-right {
      flex: 1;
      text-align: right;
      color: $color-font-gray-heavy;
      i {
        display: inline-block;
        margin-right: 6px;
        position: relative;
        top: 3px;
        font-size: 18px;
        color: $color-font-gray-dark;
      }
      span {
        font-size: 14px;
        display: inline-block;
      }
    }
  }
</style>
