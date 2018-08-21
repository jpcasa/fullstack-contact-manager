<template lang="html">
  <section id="profile">
    <!-- <div class="container" style="display:block;margin-bottom:100px;">
      <ProfileFull :profile="profile" />
    </div> -->
    <ProfileSimple :profile="profile" />
  </section>
</template>

<script>
import ProfileSimple from '~/components/Profile/ProfileSimple.vue'
import ProfileFull from '~/components/Profile/ProfileFull.vue'
import dataJSON from '~/api/data.json'

export default {
  data() {
    return {
      contact_list: dataJSON.contacts
    }
  },
  validate ({ params }) {
    // Must be a number
    return /^\d+$/.test(params.id)
  },
  components: {
    ProfileSimple,
    ProfileFull
  },
  computed: {
    profile() {
      return this.contact_list.find(x => x.id == this.$route.params.id)
    }
  }
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_extensions.scss';

  #profile {
    padding-bottom: 50px;
  }
</style>
