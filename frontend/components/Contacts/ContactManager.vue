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
      </div>
    </div>
    <section id="contacts-container">
      <div class="contacts">
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
  div {
    flex: 1;
  }
  .info-section-left {
    text-align: left;
    p {
      color: $color-font-gray-dark;
      font-family: $gotham-rounded-medium;
      font-weight: normal;
      font-size: 14px;
    }
  }
  .info-section-right {
    text-align: right;
    button {
      @extend %button;
      @extend %button-white;
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
      .img-circle {
        @extend %img-circle;
      }
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
</style>
