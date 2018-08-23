<template lang="html">
  <Confirmation :contact_id="$route.params.id" message="Are you sure you want to delete" :title="profile.first_name" :cancel_url="cancelUrl" />
</template>

<script>
import Confirmation from "~/components/Elements/Confirmation.vue"

export default {
  data() {
    return {
      profile: {}
    }
  },
  computed: {
    cancelUrl() {
      return "/contacts/" + this.profile.id
    }
  },
  components: {
    Confirmation
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

<style lang="css">
</style>
