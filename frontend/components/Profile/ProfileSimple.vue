<template lang="html">
  <div class="profile-simple">
    <ProfileImg
      :user_id="profile.user_id"
      :img="profile.avatar"
      :first_name="profile.first_name"
      :last_name="profile.last_name"
      username="" />
    <div class="container">
      <ProfileInfo :profile_info="profile_info"/>
      <NavigationSimple :items="navItems" />
      <ListWithAdd />
    </div>
  </div>
</template>

<script>
import ProfileImg from '~/components/Profile/Elements/ProfileImg.vue'
import ProfileInfo from '~/components/Profile/Elements/ProfileInfo.vue'
import NavigationSimple from '~/components/Elements/NavigationSimple.vue'
import ListWithAdd from '~/components/Elements/ListWithAdd.vue'

export default {
  props: ['profile'],
  data() {
    return {
      navItems: [
        {
          "title": "Adresses",
          "show": "addresses",
          "status": "active"
        },
        {
          "title": "Phone Numbers",
          "show": "phone_numbers",
          "status": ""
        },
        {
          "title": "Emails",
          "show": "emails",
          "status": ""
        }
      ]
    }
  },
  components: {
    ProfileImg,
    ProfileInfo,
    NavigationSimple,
    ListWithAdd
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
 .profile-simple {
   #profile-info-container {
     margin: 15px 0;
   }
   .container {
     .navigation-simple {
       margin: 25px 0;
     }
   }
 }
</style>
