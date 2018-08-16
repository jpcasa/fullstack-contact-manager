<template lang="html">
  <section id="profile-info-container">
    <div class="info-row" v-for="(info, index) in profile_info" :key="index">
      <div class="bold-title">
        <p>{{ info.title }}</p>
      </div>
      <div class="normal-title">
        <p>{{ displayValue(info) }}</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ['profile_info'],
  methods: {
    displayValue(item) {
      if(item.type == 'date') {
        const monthNames = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"
        ];
        const date = new Date(item.value)
        const monthName = monthNames[date.getMonth()]
        return `${monthName} ${date.getDay()}, ${date.getFullYear()}`
      }
      return item.value
    }
  }
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_mixins.scss';

  #profile-info-container {
    background-color: #fff;
    display: flex;
    flex-direction: column;
    padding: 30px;
    @include border-radius($border-radius);
    .info-row {
      display: flex;
      flex: 1;
      padding: 8px 0;
      .bold-title {
        flex: 2;
        p {
          font-family: $gotham-rounded-medium;
          color: $color-font-gray-dark;
          font-size: 14px;
          margin: 0;
        }
      }
      .normal-title {
        flex: 3;
        p {
          font-size: 14px;
          margin: 0;
        }
      }
    }
  }
</style>
