<template>
  <div id="preferences">
    <div>
      color of title
      <input
        type="text"
        v-bind:titleColor="titleColor"
        v-on:input="$emit('input', $event.target.value)"
        placeholder="Hex-Color" />
    </div>
    <div>
      <button id="submitButton" @click="submit">
        submit
      </button>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'preferences',
    data () {
      return{
      }
    },
    props: {
      titleColor: String,
    },
    methods: {
      submit(){
        this.$parent.postSubmitToServer(this.titleColor);
      }
    }
  };
</script>
<style>
  #preferences {
    background-color: yellow;
  }
</style>
