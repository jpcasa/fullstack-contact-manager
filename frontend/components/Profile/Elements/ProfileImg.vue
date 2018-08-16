<template lang="html">
  <div class="profile-img" :style="`background-image: url(${img})`">
    <div id="profile-container">
      <div class="name">
        <p>{{ first_name }}</p>
        <span id="username">@jpcasabianca</span>
      </div>
      <div class="options">
        <button id="edit-contact"><i class="icon-edit-2"></i></button>
        <button id="delete-contact"><i class="icon-trash"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'user_id',
    'img',
    'first_name',
    'last_name',
    'username'
  ]
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_extensions.scss';

  .profile-img {
    display: block;
    height: 300px;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    position: relative;
    #profile-container {
      display: flex;
      align-items: flex-end;
      height: 100%;
      z-index: 50;
      background-color: rgba(0, 0, 0, 0.3);
      width: 100%;
      .name {
        flex: 4;
        margin-bottom: 20px;
        margin-left: 5%;
        p {
          color: #fff;
          font-family: $gotham-rounded-medium;
          margin: 0 0 4px 0;
          font-size: 18px;
        }
        #username {
          color: #fff;
        }
      }
      .options {
        flex: 2;
        text-align: right;
        margin-bottom: 20px;
        margin-right: 5%;
        button {
          @extend %button-circle;
        }
        #edit-contact {
          @extend %button-white;
          margin-right: 8px;
        }
        #delete-contact {
          @extend %button-red;
        }
      }
    }
  }
</style>
