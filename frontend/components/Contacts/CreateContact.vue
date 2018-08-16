<template lang="html">
  <form
    class="form"
    :action="formData.redirect_url"
    :method="formData.method">
    <label
      v-for="(field, index) in formData.fields"
      v-html="displayField(field)"
      :key="index"
      for=""></label>
    <input type="submit" value="Create Contact" />
  </form>
</template>

<script>
export default {
  props: ['formData'],
  methods: {
    displayField(field) {
      // Checks if Field is required
      let required = ''
      let requiredTitle = '(Optional)'
      if (field.required) {
        required = 'required';
        requiredTitle = ''
      }

      // Display Field Depending on type and options
      if (field.type=='file') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <input type="file" ${required} />
        `
      } else if (field.type=='text') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <input type="text" name="${field.name}" placeholder="${field.placeholder}" ${required}>
        `
      } else if (field.type=='date') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <input v-validate="'date_format:DD/MM/YYYY'" type="date" name="${field.name}" ${required}>
        `
      } else if (field.type=='textarea') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <textarea name="${field.name}" rows="8" placeholder="${field.placeholder}"></textarea>
        `
      }
    }
  }
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_mixins.scss';
  @import '~/assets/sass/helpers/_extensions.scss';

  .form {
    label {
      display: block;
      margin-bottom: 25px;
      p {
        color: $color-font-gray-dark;
        font-family: $gotham-rounded-medium;
        font-size: 14px;
        margin-bottom: 10px;
      }
      input[type="text"], input[type="date"] {
        width: 100%;
        height: 40px;
        border: none;
        font-size: 13px;
        text-indent: 15px;
        font-family: $gotham-rounded-book;
        @include border-radius($border-radius);
      }
      textarea {
        width: 100%;
        border: none;
        font-size: 13px;
        text-indent: 15px;
        padding-top: 10px;
        font-family: $gotham-rounded-book;
        @include border-radius($border-radius);
      }
    }
    input[type="submit"] {
      width: 100%;
      background-color: $color-red;
      color: #fff;
      height: 45px;
      border: none;
      cursor: pointer;
      font-family: $gotham-rounded-medium;
      @include border-radius($border-radius);
      &:hover {
        background-color: $color-red-dark;
      }
    }
  }
</style>
