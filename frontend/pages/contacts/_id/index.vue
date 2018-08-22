<template lang="html">
  <section id="profile">
    <!-- <div class="container" style="display:block;margin-bottom:100px;">
      <ProfileFull :profile="profile" />
    </div> -->
    <section class="top desktop">
      <div class="container">
        <span class="current-path">
          <span>Dashboard / </span>
          <nuxt-link to="/">Contacts</nuxt-link>
          <span> / </span>
          <span class="active" to="/"> {{ profile.first_name + ' ' + profile.last_name }}</span>
          <span class="active"> /</span>
        </span>
      </div>
    </section>
    <ProfileSimple :profile="profile" />
  </section>
</template>

<script>
import ProfileSimple from '~/components/Profile/ProfileSimple.vue'
import dataJSON from '~/api/data.json'

export default {
  data() {
    return {
      contact_list: dataJSON.contacts,
      profile: {}
    }
  },
  validate ({ params }) {
    // Must be a number
    return /^\d+$/.test(params.id)
  },
  components: {
    ProfileSimple
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
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_extensions.scss';

  #profile {
    padding-bottom: 50px;
    width: 100%;
  }

  .top {
    margin-bottom: 0;
  }
</style>
