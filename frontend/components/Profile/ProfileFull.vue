<template lang="html">
  <div class="profile-full">
    <div class="profile-full-left">
      <ProfileImg
        :user_id="profile.user_id"
        :img="profile.avatar"
        :first_name="profile.first_name"
        :last_name="profile.last_name"
        username="" />

        <ProfileInfo :profile_info="profile_info"/>

    </div>
    <div class="profile-full-right" />
  </div>
</template>

<script>
import ProfileImg from '~/components/Profile/Elements/ProfileImg.vue'
import ProfileInfo from '~/components/Profile/Elements/ProfileInfo.vue'

export default {
  props: ['profile'],
  components: {
    ProfileImg,
    ProfileInfo
  },
  computed: {
    profile_info() {
      return [
        {
          "title": "First Name",
          "value": this.profile.first_name,
          "type": "text"
        },
        {
          "title": "Last Name",
          "value": this.profile.last_name,
          "type": "text"
        },
        {
          "title": "Birth Date",
          "value": this.profile.date_of_birth,
          "type": "date"
        },
        {
          "title": "Created",
          "value": this.profile.created_at,
          "type": "date"
        },
        {
          "title": "Notes",
          "value": this.profile.notes,
          "type": "text"
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.profile-full {
  display: flex;
  width: 100%;
  .profile-full-left,
  .profile-full-right {
    flex: 1;
  }
}
</style>
