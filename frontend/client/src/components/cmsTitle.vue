<template>
  <div id="cmsTitle">
    <input
      class="borderlesInput"
      v-bind:pageTitle="pageTitle"
      v-on:input="$emit('input', $event.target.value)"
      placeholder="put your title here"
      v-bind:style="{ color: titleColor }">
  </div>
</template>
<script>
  export default {
    name: 'cmsTitle',
    data () {
      return{
      }
    },
    props: {
      titleColor: String,
      pageTitle: String,
    },
    components: {
    }
  };
</script>
<style>
  .borderlesInput {
    border: none;
    font-size: 24px;
    text-align: center;
  }
</style>
