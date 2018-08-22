<template lang="html">
  <div class="profile-simple">
    <div class="profile-simple-left">
      <ProfileImg
        :contact_id="profile.id"
        :img="profile.avatar"
        :first_name="profile.first_name"
        :last_name="profile.last_name"
        username="username" />
      <div class="container">
        <ProfileInfo :profile_info="profile_info"/>
      </div>
    </div>
    <div class="profile-simple-right">
      <div class="container">
        <p class="subtitle">Addresses</p>
        <ListWithAdd
          title="Address"
          icon="map"
          value="title"
          url="/addresses/"
          :items="profile.addresses" />
        <p class="subtitle">Phone Numbers</p>
        <ListWithAdd
          title="Phone Number"
          icon="phone"
          value="number"
          url="/phone_numbers/"
          :items="profile.phone_numbers" />
        <p class="subtitle">Addresses</p>
        <ListWithAdd
          title="Email"
          icon="mail"
          value="address"
          url="/emails/"
          :items="profile.emails" />
      </div>
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
      items: [],
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
  },
  methods: {
    chooseItems(show) {
      this.profItems = 'a'
    }
  },
  mounted() {
    this.items = this.profile.addresses
  }
}
</script>

<style lang="scss">
@import '~/assets/sass/helpers/_extensions.scss';

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

 .subtitle {
   color: $color-red;
   font-family: $gotham-rounded-medium;
   font-size: 15px;
 }

 .navigation-simple {
   display: flex;
   button {
     flex: 1;
     border: none;
     padding: 0;
     font-size: 14px;
     background: none;
     cursor: pointer;
     font-family: $gotham-rounded-medium;
     color: $color-font-gray-dark;
     &:hover {
       color: $color-red;
     }
   }
   .active {
     color: $color-red;
   }
 }

 @media (min-width: 768px) {
   .profile-simple {
     display: flex;
     width: 90%;
     margin: auto;
     max-width: 900px;
     padding: 30px 0;
     .profile-simple-left,
     .profile-simple-right {
       flex: 1;
     }
     .profile-simple-left {
       .container {
         width: 100% !important;
         margin-top: 0 !important;
       }
     }
     .profile-simple-right {
       max-height: 550px;
       overflow-y: scroll;
     }
     .profile-img,
     #profile-container {
       @include border-radius($border-radius);
     }
   }
 }
</style>
