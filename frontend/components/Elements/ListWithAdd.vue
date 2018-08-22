<template lang="html">
  <section class="list-with-add">
    <div class="add">
      <div class="input">
        <input type="text" name="address" :placeholder="'Add ' + title">
      </div>
      <div class="submit">
        <button type="submit"><i :class="'icon-' + icon"></i> +</button>
      </div>
    </div>
    <div class="list">
      <div class="list-row" v-for="(item, index) in items" :key="index">
        <div class="identifier">
          <i :class="'icon-' + icon"></i>
        </div>
        <div class="name">
          <p>{{ item[value] }}</p>
        </div>
        <div class="options">
          <i class="icon-edit-2"></i>
          <i class="icon-trash-2"></i>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ['icon', 'items', 'value', 'title']
}
</script>

<style lang="scss">
  @import '~/assets/sass/helpers/_variables.scss';
  @import '~/assets/sass/helpers/_extensions.scss';

  .list-with-add {
    .add {
      display: flex;
      align-items: center;
      margin-bottom: 15px;
      .input {
        flex: 3;
        margin-right: 20px;
        input {
          width: 100%;
          height: 40px;
          border: none;
          font-size: 13px;
          font-family: $gotham-rounded-book;
          text-indent: 15px;
          @include border-radius($border-radius);
        }
      }
      .submit {
        flex: 1;
        button {
          background-color: $color-red;
          color: #fff;
          border: none;
          height: 40px;
          width: 100%;
          font-size: 16px;
          cursor: pointer;
          font-family: $gotham-rounded-medium;
          @include border-radius($border-radius);
          &:hover {
            background-color: $color-red-dark;
          }
          i {
            font-size: 16px;
          }
        }
      }
    }
    .list-row {
      display: flex;
      width: 100%;
      background-color: #fff;
      margin-bottom: 15px;
      align-items: center;
      .options {
        flex: 1.5;
        text-align: right;
        margin-right: 12px;
        i {
          color: $color-font-gray-heavy;
        }
        .icon-trash-2 {
          margin-left: 5px;
        }
      }
      .identifier {
        flex: 1.5;
        border-right: 1px solid #e6e6e6;
        text-align: center;
        i {
          display: inline-block;
          padding: 15px 0;
          color: $color-font-gray-heavy;
        }
      }
      .name {
        flex: 7;
        p {
          margin: 0 0 0 15px;
          font-size: 13px;
          font-family: $gotham-rounded-medium;
          color: $color-font-gray-dark;
        }
      }
    }
  }
</style>
