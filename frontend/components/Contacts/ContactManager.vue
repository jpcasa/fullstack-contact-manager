<template lang="html">
  <div class="">
    <label id="search-contacts">
      <i class="icon-search"></i>
      <input type="search" placeholder="Search Contacts..." v-model="query" />
    </label>
    <div class="info-section">
      <div class="info-section-left">
        <p>Contacts</p>
      </div>
      <div class="info-section-right">
        <button><i class="icon-filter"></i>Filter</button>
        <nuxt-link class="desktop" to="/contacts/create"><i class="icon-user-plus"></i> Add Contact</nuxt-link>
      </div>
    </div>
    <section id="contacts-container">

      <!-- Compacted Version -->
      <ShortContact class="mobile" :contacts="contact_list" />

      <!-- Full Contact Version -->
      <FullContact class="desktop" :contacts="contact_list" />

    </section>
  </div>
</template>

<script>
import ShortContact from '~/components/Contacts/Elements/ShortContact.vue';
import FullContact from '~/components/Contacts/Elements/FullContact.vue';

export default {
  props: ['contacts'],
  data() {
    return {
      query: null
    }
  },
  components: {
    ShortContact,
    FullContact
  },
  computed: {
    contact_list() {
      if (this.query && this.query.length > 2) {
        return this.contacts.filter(item => {
          const query = this.query.toLowerCase()
          if (item.first_name.toLowerCase().indexOf(query) !== -1) {
            return true
          } else if (item.last_name.toLowerCase().indexOf(query) !== -1) {
            return true
          }
        })
      } else {
        return this.contacts
      }
      // return this.previousVisitors.filter(v => v.firstName === this.visitor.firstName)
    }
  },
  methods: {
    nice_date(date_to_improve) {
      const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ];
      const date = new Date(date_to_improve)
      const monthName = monthNames[date.getMonth()]
      return `${monthName} ${date.getDay()}, ${date.getFullYear()}`
    }
  }
}
</script>

<style lang="scss">
@import '~/assets/sass/helpers/_variables.scss';
@import '~/assets/sass/helpers/_mixins.scss';
@import '~/assets/sass/helpers/_extensions.scss';

#search-contacts {
  width: 100%;
  display: block;
  position: relative;
  input[type="search"] {
    width: 100%;
    display: block;
    background-color: $color-gray;
    border: none;
    @include border-radius($border-radius);
    height: 40px;
    text-indent: 40px;
    font-family: $gotham-rounded-book;
    font-size: 14px;
  }
  i {
    position: absolute;
    left: 14px;
    top: 11px;
  }
}

.info-section {
  display: flex;
  margin: 15px 0;
  align-items: center;
  .info-section-left {
    text-align: left;
    flex: 2;
    p {
      color: $color-font-gray-dark;
      font-family: $gotham-rounded-medium;
      font-weight: normal;
      font-size: 14px;
    }
  }
  .info-section-right {
    text-align: right;
    flex: 3;
    button, a {
      @extend %button;
      font-size: 14px;
    }
    button {
      @extend %button-white;
    }
    a {
      @extend %button-red;
      text-decoration: none;
      margin-left: 15px;
      display: none;
    }
  }
}

#contacts-container {
  display: block;
  padding-bottom: 100px;
}

.img-circle {
  @extend %img-circle;
}

@media (min-width: 992px) {
  .info-section {
    .info-section-right {
      a {
        display: inline-block;
      }
    }
  }
}
</style>
