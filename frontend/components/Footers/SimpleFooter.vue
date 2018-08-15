<template lang="html">
  <div id="simple-footer">
    <p v-html="message" />
  </div>
</template>

<script>
export default {
  props: ['message']
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';

  #simple-footer {
    display: block;
    background-color: $color-red;
    text-align: center;
    padding: 25px;
    p {
      color: #fff;
      font-size: 14px;
      padding: 0;
      margin: 0;
      a {
        color: $color-red-dark;
        text-decoration: none;
        font-family: $gotham-rounded-medium;
        &:hover {
          text-decoration: underline;
        }
      }
    }
  }
</style>
