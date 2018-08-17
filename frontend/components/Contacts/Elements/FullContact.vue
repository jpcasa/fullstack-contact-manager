<template lang="html">
  <div class="contacts-expanded">
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
      <tr v-for="(contact, index) in contacts" :key="index" class="contacts-table-row">
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
</template>

<script>
import IconWithNotif from '~/components/Elements/IconWithNotif.vue'

export default {
  props: ['contacts'],
  components: {
    IconWithNotif
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
</style>
