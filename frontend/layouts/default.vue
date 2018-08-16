<template>
  <div class="relative">

    <!-- MAIN HEADER -->
    <header>
      <SidebarHeader :menuItems="menuItems" />
    </header>

    <!-- MAIN CONTENT -->
    <main id="main-content">
      <nuxt/>
    </main>

    <!-- MAIN FOOTER -->
    <footer>
      <SimpleFooter :message="footerMessage" />
    </footer>

    <span v-show="showAdd()" id="add-contact">
      <nuxt-link to="/contacts/create">
        <i class="icon-user-plus"></i>
      </nuxt-link>
    </span>

  </div>
</template>

<script>
  import SidebarHeader from '~/components/Headers/SidebarHeader.vue'
  import SimpleFooter from '~/components/Footers/SimpleFooter.vue'

  export default {
    data() {
      return {
        footerMessage: `
          Made with by
          <a href="http://jpcasabianca.com" target="_blank">
            JP Casabianca.
          </a>
        `,
        menuItems: [
          {
            "title": "Contacts",
            "action": "push",
            "icon": "circle",
            "url": "/"
          },
          {
            "title": "Create Contact",
            "action": "push",
            "icon": "user-plus",
            "url": "/contacts/create"
          }
        ]
      }
    },
    components: {
      SidebarHeader,
      SimpleFooter
    },
    methods: {
      showAdd() {
        if (this.$nuxt.$route.path != '/contacts/create') {
          return true
        } else {
          return false
        }
      }
    }
  }
</script>

<style lang="scss">
  @import '../assets/sass/helpers/_variables.scss';
  @import '../assets/sass/helpers/_mixins.scss';

  #main-content {
    background-color: $color-gray-light;
    padding-top: $margin-top-main-content;
    display: block;
    margin: 0;
    .container {
      width: 90%;
      margin: auto;
    }
  }

  #add-contact {
    position: fixed;
    bottom: 30px;
    left: 30px;
    background-color: $color-red;
    -webkit-box-shadow: 0px 0px 5px -1px rgba(239,63,66,1);
    -moz-box-shadow: 0px 0px 5px -1px rgba(239,63,66,1);
    box-shadow: 0px 0px 5px -1px rgba(239,63,66,1);
    font-size: 22px;
    padding: 12px 14px;
    cursor: pointer;
    @include border-radius(50%);
    &:hover {
      background-color: $color-red-dark;
    }
    a {
      text-decoration: none;
      color: #fff;
    }
  }

  .top {
    margin-top: 25px;
    h2 {
      margin-bottom: 0;
    }
    p {
      font-size: 14px;
    }
    margin-bottom: 30px;
  }

  .current-path {
    font-size: 14px;
    color: $color-font-gray-heavy;
    a {
      text-decoration: none;
      color: $color-font-gray-heavy;
      &:hover {
        color: $color-red;
        text-decoration: underline;
      }
    }
    .active {
      color: $color-red;
      font-family: $gotham-rounded-medium;
    }
  }

  @media (min-width: 992px) {
    #main-content {
      display: flex;
      margin-left: $sidebar-width;
      padding-top: $margin-top-main-content-desktop;
    }
  }
</style>
