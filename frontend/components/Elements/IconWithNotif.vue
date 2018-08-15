<template lang="html">
  <span class="icon-with-notification">
    <span v-show="numOfNotif">{{ numOfNotif }}</span>
    <i :class="`icon-${icon}`"></i>
  </span>
</template>

<script>
export default {
  props: [
    'numOfNotif',
    'icon'
  ]
}
</script>

<style lang="scss" scoped>
@import '~/assets/sass/helpers/_variables.scss';

i {
  font-size: 14px;
  color: $color-font-gray-heavy;
}
.icon-with-notification {
  position: relative;
  span {
    font-size: 10px;
    color: $color-red;
    font-family: $gotham-rounded-medium;
    position: absolute;
    top: -8px;
    right: -5px;
  }
}
</style>
