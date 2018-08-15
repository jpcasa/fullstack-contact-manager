<template>
  <div>

    <!-- MAIN HEADER -->
    <header>
      <SidebarHeader :menuItems="menuItems" />
    </header>

    <!-- MAIN CONTENT -->
    <main id="main-content">
      <div class="container">
        <nuxt/>
      </div>
    </main>

    <!-- MAIN FOOTER -->
    <footer>
      <SimpleFooter :message="footerMessage" />
    </footer>

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
            "title": "Dashboard",
            "action": "push",
            "url": "/"
          },
          {
            "title": "Contacts",
            "action": "push",
            "url": "/contacts"
          }
        ]
      }
    },
    components: {
      SidebarHeader,
      SimpleFooter
    }
  }
</script>

<style lang="scss">
  @import '../assets/sass/helpers/_variables.scss';

  #main-content {
    background-color: $color-gray-light;
    padding-top: $margin-top-main-content;
    display: block;
    margin: 0;
    .container {
      width: 92%;
      margin: auto;
    }
  }

</style>
