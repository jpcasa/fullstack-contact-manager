<template lang="html">
  <form
    class="form"
    :action="formData.redirect_url"
    :method="formData.method"
    @submit.prevent="getFormValues">
    <p class="error-message" v-if="error">{{ error }}</p>
    <label
      v-for="(field, index) in formData.fields"
      v-html="displayField(field)"
      :key="index"
      for=""></label>
    <input type="submit" :value="buttonText" />
  </form>
</template>

<script>
export default {
  props: ['formData', 'action', 'edit'],
  data() {
    return {
      error: null
    }
  },
  computed: {
    buttonText() {
      if (this.action == 'create') {
        return 'Create Contact'
      } else {
        return 'Update Contact'
      }
    }
  },
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
          <input type="text" name="${field.name}" placeholder="${field.placeholder}" value="${field.value}" ${required}>
        `
      } else if (field.type=='date') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <input v-validate="'date_format:DD/MM/YYYY'" type="date" name="${field.name}" value="${field.value}" ${required}>
        `
      } else if (field.type=='textarea') {
        return `
          <p>${field.label} ${requiredTitle}</p>
          <textarea name="${field.name}" rows="8" placeholder="${field.placeholder}">${field.value}</textarea>
        `
      }
    },
    getFormValues (submitEvent) {
      const first_name = submitEvent.target.elements.first_name.value
      const last_name = submitEvent.target.elements.last_name.value
      const date_of_birth = submitEvent.target.elements.date_of_birth.value + 'T11:11:00Z'
      const avatar = submitEvent.target.elements.avatar.value
      const notes = submitEvent.target.elements.notes.value
      if (this.action == 'create') {
        this.createProfile(first_name, last_name, date_of_birth, avatar, notes)
      } else {
        this.updateProfile(first_name, last_name, date_of_birth, avatar, notes)
      }
    },
    async createProfile(first_name, last_name, date_of_birth, avatar, notes) {
      await this.$axios.post('contacts/', {
        first_name: first_name,
        last_name: last_name,
        date_of_birth: date_of_birth,
        avatar: avatar,
        notes: notes
      })
      .then(response => {
        if (response.status == '201') {
          this.$nuxt.$router.replace({ path: '/' })
        }
      })
      .catch((error) => {
        this.error = "Problem submitting New Contact. Try again later."
      })
    },
    async updateProfile(first_name, last_name, date_of_birth, avatar, notes) {
      await this.$axios.put(`contacts/${this.edit}/`, {
        first_name: first_name,
        last_name: last_name,
        date_of_birth: date_of_birth,
        avatar: avatar,
        notes: notes
      })
      .then(response => {
        if (response.status == '200') {
          this.$nuxt.$router.replace({ path: `/contacts/${this.edit}/` })
        }
      })
      .catch((error) => {
        this.error = "Problem Editing the contact. Try again later."
        console.error(error);
      })
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
      font-size: 14px;
      font-family: $gotham-rounded-medium;
      @include border-radius($border-radius);
      &:hover {
        background-color: $color-red-dark;
      }
    }
  }

  .error-message {
    display: block;
    background-color: $color-red;
    color: #fff;
    font-size: 14px;
    @include border-radius($border-radius);
    padding: 8px 0;
    text-align: center;
  }
</style>
