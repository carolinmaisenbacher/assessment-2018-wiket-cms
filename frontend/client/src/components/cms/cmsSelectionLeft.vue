<template>
  <div id="cmsSelectionLeft">
    <div id="text">
      <h4>
        {{ data.title }}
      </h4>
      <p>
        {{ data.subtext }}
      </p>
    </div>
  </div>
</template>
<script>
  export default {

    name: 'cmsSelectionLeft',
    data () {
      return{
      }
    },
    props: {
      data: {
        type: Object,
      },
    },
    components: {
    }
  };
</script>
<style>
  h4 {
    margin: 5px 10px;

  }
  p {
    margin: 0 10px 10px;
  }
  #cmsSelectionLeft {
    border: 2px none black;
    border-radius: 5px;
    width: 100%;
    text-align: left;
    float: left;
    margin: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
</style>
