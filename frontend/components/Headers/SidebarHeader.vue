<template lang="html">
  <div id="main-header">
    <div class="header-left">
      <i @click="showMenu = !showMenu" :class="toggleMenuIcon()" id="icon-menu" />
    </div>
    <div class="header-center">
      <img src="img/logo.png" id="main-logo" alt="Logo Service Fusion">
    </div>
    <div class="header-right">
      <i class="icon-bell" />
      <i class="icon-user" />
    </div>
    <transition name="fade">
      <div v-show="showMenu" id="dropdown-menu">
        <nuxt-link
          v-for="(item, index) in menuItems"
          :key="index"
          :to="item.url"
          v-show="item.action == 'push'">{{ item.title }}</nuxt-link>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props: ['menuItems'],
  data() {
    return {
      showMenu: false
    }
  },
  methods: {
    toggleMenuIcon() {
      if (!this.showMenu) {
        return 'icon-menu'
      } else {
        return 'icon-x'
      }
    }
  }
}
</script>

<style lang="scss">
@import '../../assets/sass/helpers/_variables.scss';
@import '../../assets/sass/helpers/_mixins.scss';

#main-header {
  z-index: 999;
  display: flex;
  align-items: center;
  position: fixed;
  background-color: $header-background;
  width: 100%;
  left: 0;
  top: 0;
  padding: 8px 0;
  border-bottom: 1px solid #e6e6e6;
  i {
    font-size: 22px;
    cursor: pointer;
    @include transition(all 0.3s ease-in-out);
  }
  .header-left {
    flex: 2;
    text-align: left;
    margin-left: 15px;
    i {
      &:hover {
        color: $color-red;
      }
    }
  }
  .header-right {
    flex: 2;
    text-align: right;
    margin-right: 15px;
    i {
      &:last-child {
        margin-left: 8px;
      }
    }
  }
  .header-center {
    flex: 12;
    text-align: center;
    img {
      width: 180px;
      height: auto;
    }
  }
}

#dropdown-menu {
  position: absolute;
  left: 0;
  top: 75px;
  background-color: $header-background;
  width: 100%;
  text-align: center;
  a {
    text-decoration: none;
    color: $color-font-gray-dark;
    font-family: $gotham-rounded-medium;
    font-weight: normal;
    display: block;
    padding: 15px 0;
    &:hover {
      background-color: $color-red;
      color: #fff;
    }
  }
  .nuxt-link-exact-active {
    background-color: $color-red;
    color: #fff;
  }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
