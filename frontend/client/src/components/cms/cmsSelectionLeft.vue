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
    padding: 5px 10px;
    margin: 0;

  }
  p {
    padding: 0 10px 10px;
    margin: 0;
  }
  button {
    margin: 0;
    padding: 0;
    border-radius: 5px;
    width: inherit;
  }

  #cmsSelectionLeft {
    box-sizing: border-box;
    background-color: inherit;
    text-align: left;
    float: left;
    margin: 10px;

  }
  #text {
    width: 300px;
  }
</style>
