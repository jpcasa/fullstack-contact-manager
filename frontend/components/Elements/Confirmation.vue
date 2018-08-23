<template lang="html">
  <div class="confirmation">
    <div class="confirm">
      <p>{{ message }}</p>
      <h1>{{ title }}</h1>
      <button @click="deleteContactApi(contact_id)" class="delete">Delete</button>
      <nuxt-link :to="cancel_url" class="cancel">Cancel</nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  props: ["contact_id", "message", "title", "cancel_url"],
  methods: {
    async deleteContactApi(id) {
      await this.$axios.delete(`contacts/${id}/`).then(response => {
        if (response.status == "204") {
          this.$nuxt.$router.replace({ path: "/" })
        }
      })
    }
  }
}
</script>

<style lang="scss">
@import "~/assets/sass/helpers/_extensions.scss";

.confirmation {
  display: flex;
  min-height: 650px;
  align-items: center;
  justify-content: center;
  width: 100%;
  .confirm {
    text-align: center;
    margin-bottom: 20px;
    p,
    h1 {
      margin: 0;
      padding: 0;
    }
    h1 {
      margin: 10px 0 20px 0;
    }
    button,
    a {
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

@media (min-width: 992px) {
  .confirmation {
    min-height: 750px;
  }
}
</style>
