<template lang="html">
  <section class="list-with-add">
    <div class="add">
      <form class="" method="post" @submit.prevent="createItem">
        <div class="input">
          <input type="text" name="value" :placeholder="'Add ' + title" required>
        </div>
        <div class="submit">
          <button type="submit"><i :class="'icon-' + icon"></i> +</button>
        </div>
      </form>
    </div>
    <div class="list">
      <div class="list-row" v-for="(item, index) in listItems" :key="index">
        <div class="identifier">
          <i :class="'icon-' + icon"></i>
        </div>
        <div class="name">
          <p>{{ item[value] }}</p>
        </div>
        <div class="options">
          <i class="icon-trash-2" @click="deleteItem(item.id)"></i>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ["owner", "icon", "items", "value", "title", "url", "type"],
  computed: {
    listItems() {
      return this.items
    }
  },
  methods: {
    createItem(submitEvent) {
      const value = submitEvent.target.elements.value.value
      if (value.length) {
        if (this.type == "address") {
          this.createAddress(value, this.owner)
        } else if (this.type == "phone") {
          this.createPhone(value, this.owner)
        } else {
          this.createEmail(value, this.owner)
        }
      }
    },
    deleteItem(id) {
      if (this.type == "address") {
        this.deleteAddress(id)
      } else if (this.type == "phone") {
        this.deletePhone(id)
      } else {
        this.deleteEmail(id)
      }
    },
    async createAddress(title, id) {
      await this.$axios
        .post("addresses/", {
          title: title,
          owner: 1,
          contact_id: id
        })
        .then(response => {
          if (response.status == "201") {
            this.listItems.push({
              id: response.data.id,
              title: title,
              owner: 1
            })
          }
        })
    },
    async deleteAddress(id) {
      await this.$axios.delete(`addresses/${id}/`).then(response => {
        if (response.status == "204") {
          this.listItems = this.listItems.filter(item => item.id !== id)
        }
      })
    },
    async createPhone(number, id) {
      await this.$axios
        .post("phone-numbers/", {
          number: number,
          owner: 1,
          contact_id: id
        })
        .then(response => {
          if (response.status == "201") {
            this.listItems.push({
              id: response.data.id,
              number: number,
              owner: 1
            })
          }
        })
    },
    async deletePhone(id) {
      await this.$axios.delete(`phone-numbers/${id}/`).then(response => {
        if (response.status == "204") {
          this.listItems = this.listItems.filter(item => item.id !== id)
        }
      })
    },
    async createEmail(address, id) {
      await this.$axios
        .post("emails/", {
          address: address,
          owner: 1,
          contact_id: id
        })
        .then(response => {
          if (response.status == "201") {
            this.listItems.push({
              id: response.data.id,
              address: address,
              owner: 1
            })
          }
        })
    },
    async deleteEmail(id) {
      await this.$axios.delete(`emails/${id}/`).then(response => {
        if (response.status == "204") {
          this.listItems = this.listItems.filter(item => item.id !== id)
        }
      })
    }
  }
}
</script>

<style lang="scss">
@import "~/assets/sass/helpers/_variables.scss";
@import "~/assets/sass/helpers/_extensions.scss";

.list-with-add {
  .add {
    form {
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
        cursor: pointer;
        &:hover {
          color: $color-red;
        }
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
