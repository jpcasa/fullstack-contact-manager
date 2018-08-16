<template lang="html">
  <div id="main-header">
    <div class="header-left mobile">
      <i @click="showMenu = !showMenu" :class="toggleMenuIcon()" id="icon-menu" />
    </div>
    <div class="header-center">
      <nuxt-link to="/"><img src="~/static/img/logo.png" id="main-logo" alt="Logo Service Fusion"></nuxt-link>
    </div>
    <div class="header-right mobile">
      <i class="icon-bell" />
      <i class="icon-user" />
    </div>
    <div class="header-desktop">
      <nav class="links">
        <nuxt-link
        v-for="(item, index) in menuItems"
        :key="index"
        :to="item.url"
        v-show="item.action == 'push'">
          <i v-show="item.icon != ''" :class="`icon-${item.icon}`"></i>{{ item.title }}
        </nuxt-link>
      </nav>
    </div>
    <transition name="fade">
      <div v-show="showMenu" id="dropdown-menu">
        <span @click="showMenu = !showMenu">
          <nuxt-link
          v-for="(item, index) in menuItems"
          :key="index"
          :to="item.url"
          v-show="item.action == 'push'">{{ item.title }}</nuxt-link>
        </span>
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
  top: 73px;
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

.header-desktop {
  flex-direction: column;
  display: none;
  .links {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    a {
      flex: 1;
      padding: 15px 0;
      color: $color-font-gray-heavy;
      font-family: $gotham-rounded-medium;
      padding-left: 30px;
      text-decoration: none;
      border-right: 5px solid #fff;
      @include transition(all 0.3s ease-in-out);
      &:hover {
        color: $color-red;
        border-right: 5px solid $color-red;
      }
      i {
        position: relative;
        top: 3px;
        display: inline-block;
        margin-right: 15px;
      }
    }
    .nuxt-link-exact-active {
      color: $color-red;
      border-right: 5px solid $color-red;
    }
  }
}

@media (min-width: 992px) {
  #main-header {
    left: 0;
    top: 0;
    width: $sidebar-width;
    height: 100%;
    display: block;
  }
  .header-desktop {
    display: flex;
  }
}
</style>
