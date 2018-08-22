<template lang="html">
  <div class="container">
    <section class="top">
      <span class="current-path">
        <span>Dashboard / </span>
        <nuxt-link to="/">Contacts</nuxt-link>
        <span> / </span>
        <span class="active" to="/"> Create Contact</span>
        <span class="active"> /</span>
      </span>
      <h2>Contacts</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
    </section>
    <section id="create-contact-container">
      <CreateContact :formData="formData" action="create" edit="" />
    </section>
  </div>
</template>

<script>
import CreateContact from '~/components/Contacts/CreateContact.vue'

export default {
  data() {
    return {
      formData: {
        "redirect_url": "/",
        "method": "POST",
        "fields": [
          {
            "label": "First Name",
            "type": "text",
            "name": "first_name",
            "placeholder": "Enter First Name Here...",
            "value": "",
            "required": true
          },
          {
            "label": "Last Name",
            "type": "text",
            "name": "last_name",
            "placeholder": "Enter Last Name Here...",
            "value": "",
            "required": true
          },
          {
            "label": "Date of Birth",
            "type": "date",
            "name": "date_of_birth",
            "placeholder": "__ / __ / ____",
            "value": "",
            "required": true
          },
          {
            "label": "Avatar",
            "type": "text",
            "name": "avatar",
            "placeholder": "Enter Image Absolute URL",
            "value": "",
            "required": false
          },
          {
            "label": "Notes",
            "type": "textarea",
            "name": "notes",
            "placeholder": "Enter optional notes...",
            "value": "",
            "required": false
          }
        ]
      }
    }
  },
  components: {
    CreateContact
  }
}
</script>

<style lang="scss">
  #create-contact-container {
      padding-bottom: 50px;
  }
</style>
