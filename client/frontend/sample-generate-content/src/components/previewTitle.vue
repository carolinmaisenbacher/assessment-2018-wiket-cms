<template>
  <div id="previewTitleStyle">
    <slot name="content">
      default title
    </slot>
  </div>
</template>
<script>
  export default {
    name: 'previewTitle',
    data () {
      return{

      }
    },
  };
</script>
<style>
  #previewTitleStyle {
    width: 100%;
    height: 100px;
    background-color: #EEEEEE;
    float: left;
  }
</style>
