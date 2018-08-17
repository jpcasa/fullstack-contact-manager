<template lang="html">
  <div class="">
    <label id="search-contacts">
      <i class="icon-search"></i>
      <input type="search" placeholder="Search Contacts..." v-model="query" />
    </label>
    <div class="info-section">
      <div class="info-section-left">
        <p>{{ contacts.length }} Contacts</p>
      </div>
      <div class="info-section-right">
        <button><i class="icon-filter"></i>Filter</button>
        <nuxt-link class="desktop" to="/contacts/create"><i class="icon-user-plus"></i> Add Contact</nuxt-link>
      </div>
    </div>
    <section id="contacts-container">

      <!-- Compacted Version -->
      <div class="contacts mobile">
        <div v-for="(contact, index) in contact_list" :key="index" class="contact-row">
          <div class="contact-img">
            <div class="img-circle">
              <img :src="`img/user${contact.id}.jpg`" :alt="contact.first_name">
            </div>
          </div>
          <div class="contact-info">
            <nuxt-link :to="`/contacts/${contact.id}`">
              {{ `${contact.first_name} ${contact.last_name}` }}
            </nuxt-link>
            <span>November 7, 1991</span>
          </div>
          <div class="contact-more">
            <IconWithNotif class="margin-right-small" :numOfNotif="contact.addresses.length" icon="map" />
            <IconWithNotif class="margin-right-small" :numOfNotif="contact.phone_numbers.length" icon="phone" />
            <IconWithNotif :numOfNotif="contact.emails.length" icon="mail" />
          </div>
        </div>
      </div>

      <!-- Full Contact Version -->
      <div class="contacts-expanded desktop">
        <table>
          <tr class="contacts-table-headline">
            <th></th>
            <th class="larger">First Name</th>
            <th class="larger">Last Name</th>
            <th class="larger">Date of Birth</th>
            <th>Addresses</th>
            <th>Emails</th>
            <th>Phone Numbers</th>
            <th class="larger">Created</th>
            <th class="larger">More</th>
          </tr>
          <tr v-for="(contact, index) in contact_list" :key="index" class="contacts-table-row">
            <td><div class="img-circle">
              <img :src="`img/user${contact.id}.jpg`" :alt="contact.first_name">
            </div></td>
            <td class="larger"><span class="normal-title">{{ contact.first_name }}</span></td>
            <td class="larger"><span class="normal-title">{{ contact.last_name }}</span></td>
            <td class="larger"><span class="normal-title">{{ nice_date(contact.date_of_birth) }}</span></td>
            <td><IconWithNotif :numOfNotif="contact.addresses.length" icon="map" /></td>
            <td><IconWithNotif :numOfNotif="contact.emails.length" icon="mail" /></td>
            <td><IconWithNotif :numOfNotif="contact.phone_numbers.length" icon="phone" /></td>
            <td class="larger"><span class="normal-title">{{ nice_date(contact.created_at) }}</span></td>
            <td class="larger"><nuxt-link :to="`/contacts/${contact.id}`">See Contact</nuxt-link></td>
          </tr>
        </table>
      </div>

    </section>
  </div>
</template>

<script>
import IconWithNotif from '~/components/Elements/IconWithNotif.vue';

export default {
  props: ['contacts'],
  data() {
    return {
      query: null
    }
  },
  components: {
    IconWithNotif
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

.contacts {
  .contact-row {
    display: flex;
    align-items: center;
    background-color: #fff;
    border: 1px solid #fff;
    padding: 12px 15px 5px 15px;
    @include border-radius($border-radius);
    margin-bottom: 8px;
    .contact-img {
      flex: 2;
    }
    .contact-info {
      flex: 7;
      a, span {
        display: block;
        font-size: 13px;
        margin: 0;
        padding: 0;
      }
      a {
        color: $color-font-gray-dark;
        font-family: $gotham-rounded-medium;
        margin-bottom: 3px;
        text-decoration: none;
        &:hover {
          color: $color-red;
        }
      }
      span {
        color: $color-font-gray;
      }
    }
    .contact-more {
      flex: 2;
      text-align: right;
    }
  }
}

.img-circle {
  @extend %img-circle;
}

.contacts-expanded {
  margin-top: 25px;
  table {
    display: block;
    width: 100%;
    tr {
      width: 100%;
      display: flex;
      align-items: center;
      th {
        flex: 1;
        font-size: 12px;
        color: $color-font-gray-dark;
        text-align: center;
      }
      td {
        flex: 1;
        text-align: center;
      }
      .larger {
        flex: 2;
      }
    }
    tr.contacts-table-row {
      background-color: #fff;
      margin-bottom: 10px;
      padding: 5px 0;
      @include border-radius($border-radius);
      .normal-title {
        font-size: 12px;
        color: $color-font-gray-heavy;
      }
      .img-circle {
        position: relative;
        top: 3px;
      }
      a {
        font-size: 13px;
        text-decoration: none;
        color: $color-font-gray-heavy;
        &:hover {
          color: $color-red;
          text-decoration: underline;
        }
      }
    }
    tr.contacts-table-headline {
      margin-bottom: 10px;
    }
  }
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
