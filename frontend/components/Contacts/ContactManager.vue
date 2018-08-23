<template lang="html">
  <div class="contact-manager">
    <div class="top-contact-manager">
      <label id="search-contacts">
        <i class="icon-search"></i>
        <input type="search" placeholder="Search Contacts..." v-model="query" />
      </label>
      <div class="info-section">
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
import ShortContact from "~/components/Contacts/Elements/ShortContact.vue"
import FullContact from "~/components/Contacts/Elements/FullContact.vue"

export default {
  props: ["contacts"],
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
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      ]
      const date = new Date(date_to_improve)
      const monthName = monthNames[date.getMonth()]
      return `${monthName} ${date.getDay()}, ${date.getFullYear()}`
    }
  }
}
</script>

<style lang="scss">
@import "~/assets/sass/helpers/_variables.scss";
@import "~/assets/sass/helpers/_mixins.scss";
@import "~/assets/sass/helpers/_extensions.scss";

.contact-manager {
  .top-contact-manager {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    .info-section {
      flex: 1;
      text-align: center;
      display: none;
      a {
        display: block;
        font-size: 12px;
        background-color: $color-red;
        text-decoration: none;
        color: #fff;
        padding: 12px 0;
        @include border-radius($border-radius);
        &:hover {
          background-color: $color-red-dark;
        }
      }
    }
    #search-contacts {
      flex: 4;
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
  .contact-manager {
    .top-contact-manager {
      flex-direction: row;
      .info-section {
        display: block;
        margin-left: 20px;
      }
    }
  }
}
</style>
