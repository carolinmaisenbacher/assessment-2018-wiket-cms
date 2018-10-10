<template>
  <div id="previewStyle">
    <previewTitle>
      <p slot="content"> {{ title }} </p>
    </previewTitle>
  </div>
</template>
<script>
  import previewTitle from './previewTitle'

  export default {
    name: 'preview',
    data () {
      return{

      }
    },
    props: ['title'],
    components: {
      previewTitle,
    },
  };
</script>
<style>
  #previewStyle {
    width: 80%;
    height: 100%;
    float: left;
  }
</style>
