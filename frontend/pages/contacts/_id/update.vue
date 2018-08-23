<template lang="html">
  <div class="container">
    <section class="top">
      <span class="current-path">
        <span>Dashboard / </span>
        <nuxt-link to="/">Contacts</nuxt-link>
        <span> / </span>
        <span> Update Contact</span>
        <span> /</span>
        <span class="active" to="/"> {{ profile.first_name }}</span>
        <span class="active"> /</span>
      </span>
      <h2>Update: {{ profile.first_name + " " + profile.last_name }}</h2>
    </section>
    <section id="create-contact-container">
      <CreateUpdateContact :formData="formData" action="edit" :edit="profile.id" />
    </section>
  </div>
</template>

<script>
import CreateUpdateContact from "~/components/Contacts/CreateUpdateContact.vue"

export default {
  data() {
    return {
      profile: {}
    }
  },
  computed: {
    formData() {
      return {
        redirect_url: "/",
        method: "POST",
        fields: [
          {
            label: "First Name",
            type: "text",
            name: "first_name",
            placeholder: "Enter First Name Here...",
            value: this.profile.first_name,
            required: true
          },
          {
            label: "Last Name",
            type: "text",
            name: "last_name",
            placeholder: "Enter Last Name Here...",
            value: this.profile.last_name,
            required: true
          },
          {
            label: "Date of Birth",
            type: "date",
            name: "date_of_birth",
            placeholder: "__ / __ / ____",
            value: this.profile.date_of_birth,
            required: true
          },
          {
            label: "Avatar",
            type: "text",
            name: "avatar",
            placeholder: "Enter Image Absolute URL",
            value: this.profile.avatar,
            required: false
          },
          {
            label: "Notes",
            type: "textarea",
            name: "notes",
            placeholder: "Enter optional notes...",
            value: this.profile.notes,
            required: false
          }
        ]
      }
    }
  },
  components: {
    CreateUpdateContact
  },
  methods: {
    async fetchProfile() {
      const profile = await this.$axios.$get(
        `contacts/${this.$route.params.id}/?format=json`
      )
      this.profile = profile
    }
  },
  created() {
    this.fetchProfile()
  }
}
</script>

<style lang="scss">
#create-contact-container {
  margin-bottom: 30px;
}
</style>
