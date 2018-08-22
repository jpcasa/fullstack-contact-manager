<template lang="html">
  <div class="confirmation">
    <div class="confirm">
      <p>{{ message }}</p>
      <h1>{{ title }}</h1>
      <button class="delete">Delete</button>
      <nuxt-link :to="cancel_url" class="cancel">Cancel</nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  props: ['message', 'title', 'cancel_url']
}
</script>

<style lang="scss">
@import '~/assets/sass/helpers/_extensions.scss';

.confirmation {
  display: flex;
  min-height: 550px;
  align-items: center;
  justify-content: center;
  .confirm {
    text-align: center;
    margin-bottom: 20px;
    p, h1 {
      margin: 0;
      padding: 0;
    }
    h1 {
      margin: 10px 0 20px 0;
    }
    button, a {
      @extend %button;
      text-decoration: none;
    }
    .delete {
      @extend %button-red;
      margin-right: 10px;
    }
    .cancel {
      @extend %button-white;
    }
  }
}
</style>
