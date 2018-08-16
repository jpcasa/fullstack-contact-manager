<template lang="html">
  <nav class="navigation-simple">
    <button
      v-for="(item, index) in items"
      :key="index"
      :class="item.status">
      {{ item.title }}
    </button>
  </nav>
</template>

<script>
export default {
  props: ['items']
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';

  .navigation-simple {
    display: flex;
    button {
      flex: 1;
      border: none;
      padding: 0;
      font-size: 14px;
      background: none;
      cursor: pointer;
      font-family: $gotham-rounded-medium;
      color: $color-font-gray-dark;
      &:hover {
        color: $color-red;
      }
    }
    .active {
      color: $color-red;
    }
  }
</style>
