<template lang="html">
  <div class="contacts mobile">
    <div v-for="(contact, index) in contacts" :key="index" class="contact-row">
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
</template>

<script>
import IconWithNotif from '~/components/Elements/IconWithNotif.vue'

export default {
  props: ['contacts'],
  components: {
    IconWithNotif
  }
}
</script>

<style lang="scss">
@import '~/assets/sass/helpers/_variables.scss';
@import '~/assets/sass/helpers/_mixins.scss';

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
</style>
